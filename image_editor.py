#!/usr/bin/env python3
"""
Image Editor & Enhancement Tool

A practical CLI tool for editing, enhancing, and making images more appealing.
Implements the techniques described in image-editing-skill.md.

Usage:
    python image_editor.py <command> <input> [options]

Examples:
    python image_editor.py enhance photo.jpg --style pop
    python image_editor.py resize photo.jpg --platform instagram-post
    python image_editor.py batch ./photos --style golden-hour --format webp
    python image_editor.py auto photo.jpg -o enhanced.jpg

Requirements:
    pip install Pillow numpy
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageStat
except ImportError:
    print("Error: Pillow is required. Install it with: pip install Pillow")
    sys.exit(1)

try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False


# ---------------------------------------------------------------------------
# Enhancement Recipes (from Section 10 of image-editing-skill.md)
# ---------------------------------------------------------------------------

RECIPES = {
    "pop": {
        "description": "Vivid & Punchy — bold colors with punch. Great for landscapes, travel, food.",
        "brightness": 1.05,
        "contrast": 1.20,
        "color": 1.15,
        "sharpness": 1.30,
        "vibrance": 1.20,
        "vignette": 0.15,
    },
    "film": {
        "description": "Warm & Nostalgic — soft, faded, vintage aesthetic. Ideal for portraits, lifestyle.",
        "brightness": 1.08,
        "contrast": 0.90,
        "color": 0.90,
        "sharpness": 0.95,
        "warmth": 15,
        "fade": 15,
        "grain": 8,
    },
    "moody": {
        "description": "Dark & Dramatic — cinematic, brooding. Best for urban, night, editorial.",
        "brightness": 0.85,
        "contrast": 1.25,
        "color": 0.85,
        "sharpness": 1.15,
        "vibrance": 0.90,
        "vignette": 0.30,
        "coolness": 10,
    },
    "bright": {
        "description": "Bright & Airy — light, clean, fresh. Perfect for weddings, lifestyle, product.",
        "brightness": 1.20,
        "contrast": 0.90,
        "color": 1.05,
        "sharpness": 1.05,
        "warmth": 8,
        "vibrance": 1.10,
    },
    "golden-hour": {
        "description": "Golden Hour Glow — warm, sun-drenched. Ideal for portraits, landscapes at sunset.",
        "brightness": 1.10,
        "contrast": 1.10,
        "color": 1.10,
        "sharpness": 1.05,
        "warmth": 25,
        "vibrance": 1.15,
        "vignette": 0.10,
    },
    "bw-dramatic": {
        "description": "High Contrast B&W — bold, dramatic, editorial black and white.",
        "brightness": 1.0,
        "contrast": 1.40,
        "sharpness": 1.20,
        "grayscale": True,
        "vignette": 0.20,
    },
    "soft-portrait": {
        "description": "Soft Portrait — flattering skin, gentle warmth. For portraits and headshots.",
        "brightness": 1.08,
        "contrast": 0.95,
        "color": 1.05,
        "sharpness": 0.85,
        "warmth": 10,
        "vibrance": 1.05,
        "smooth": 1,
    },
}

# Social media platform sizes (from Section 9.2)
PLATFORM_SIZES = {
    "instagram-post": (1080, 1350),
    "instagram-story": (1080, 1920),
    "instagram-square": (1080, 1080),
    "instagram-profile": (320, 320),
    "facebook-post": (1200, 630),
    "facebook-story": (1080, 1920),
    "facebook-profile": (180, 180),
    "twitter-post": (1600, 900),
    "twitter-profile": (400, 400),
    "linkedin-post": (1200, 627),
    "linkedin-profile": (400, 400),
    "youtube-thumbnail": (1280, 720),
    "youtube-shorts": (1080, 1920),
    "youtube-profile": (800, 800),
    "pinterest-pin": (1000, 1500),
    "tiktok-video": (1080, 1920),
    "tiktok-profile": (200, 200),
}


# ---------------------------------------------------------------------------
# Core Image Processing Functions
# ---------------------------------------------------------------------------

def adjust_warmth(image, amount):
    """Shift image color temperature. Positive = warmer, negative = cooler."""
    if amount == 0:
        return image
    r, g, b = image.split()[:3]
    if amount > 0:
        r = r.point(lambda x: min(255, x + amount))
        b = b.point(lambda x: max(0, x - amount // 2))
    else:
        r = r.point(lambda x: max(0, x + amount))
        b = b.point(lambda x: min(255, x - amount // 2))
    if image.mode == "RGBA":
        return Image.merge("RGBA", (r, g, b, image.split()[3]))
    return Image.merge("RGB", (r, g, b))


def adjust_coolness(image, amount):
    """Shift image toward cooler tones."""
    return adjust_warmth(image, -amount)


def apply_vibrance(image, factor):
    """
    Boost less-saturated colors more than already-saturated ones.
    Factor > 1.0 increases vibrance, < 1.0 decreases.
    """
    if not HAS_NUMPY:
        # Fallback: use simple saturation adjustment
        return ImageEnhance.Color(image).enhance(factor)

    arr = np.array(image, dtype=np.float64)
    if arr.shape[2] == 4:
        rgb = arr[:, :, :3]
        alpha = arr[:, :, 3:]
    else:
        rgb = arr
        alpha = None

    gray = np.mean(rgb, axis=2, keepdims=True)
    saturation = np.max(rgb, axis=2, keepdims=True) - np.min(rgb, axis=2, keepdims=True)
    max_sat = saturation.max() if saturation.max() > 0 else 1.0
    # Less saturated pixels get stronger boost
    mask = 1.0 - (saturation / max_sat)
    adjusted_factor = 1.0 + (factor - 1.0) * mask
    result = gray + (rgb - gray) * adjusted_factor
    result = np.clip(result, 0, 255).astype(np.uint8)

    if alpha is not None:
        result = np.concatenate([result, alpha.astype(np.uint8)], axis=2)
        return Image.fromarray(result, "RGBA")
    return Image.fromarray(result, "RGB")


def apply_vignette(image, strength):
    """Apply a vignette effect (darken edges). Strength 0.0-1.0."""
    if strength <= 0:
        return image
    if not HAS_NUMPY:
        # Simple fallback: draw a semi-transparent dark ellipse
        overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        w, h = image.size
        for i in range(20):
            opacity = int(strength * 255 * (i / 20) * 0.5)
            margin = int(w * 0.05 * (20 - i))
            draw.ellipse(
                [-margin, -margin, w + margin, h + margin],
                fill=None,
                outline=(0, 0, 0, opacity),
                width=max(1, margin // 2),
            )
        return Image.alpha_composite(image.convert("RGBA"), overlay).convert(image.mode)

    w, h = image.size
    arr = np.array(image, dtype=np.float64)
    Y, X = np.ogrid[:h, :w]
    cx, cy = w / 2, h / 2
    radius = max(cx, cy)
    dist = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
    dist = dist / radius
    # Smooth falloff from center
    vignette = 1.0 - strength * np.clip(dist - 0.4, 0, 1) ** 1.5 * 2.5
    vignette = np.clip(vignette, 0, 1)

    if len(arr.shape) == 3:
        if arr.shape[2] == 4:
            arr[:, :, :3] = arr[:, :, :3] * vignette[:, :, np.newaxis]
        else:
            arr = arr * vignette[:, :, np.newaxis]
    else:
        arr = arr * vignette

    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), image.mode)


def apply_fade(image, amount):
    """Lift black point to create a faded/matte look. Amount 0-50."""
    if amount <= 0:
        return image
    return image.point(lambda x: int(x + (amount * (255 - x) / 255)))


def apply_grain(image, amount):
    """Add film grain effect. Amount controls intensity (0-50)."""
    if amount <= 0 or not HAS_NUMPY:
        return image
    arr = np.array(image, dtype=np.float64)
    noise = np.random.normal(0, amount, arr.shape[:2])
    if len(arr.shape) == 3:
        if arr.shape[2] == 4:
            arr[:, :, :3] += noise[:, :, np.newaxis]
        else:
            arr += noise[:, :, np.newaxis]
    else:
        arr += noise
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), image.mode)


def apply_smooth(image, passes=1):
    """Gentle skin smoothing. Each pass applies a subtle blur."""
    result = image
    for _ in range(passes):
        result = result.filter(ImageFilter.GaussianBlur(radius=0.8))
    # Blend smoothed with original to preserve some texture
    return Image.blend(image, result, 0.5)


def auto_levels(image):
    """Auto-adjust levels by stretching histogram to full range."""
    if image.mode == "RGBA":
        r, g, b, a = image.split()
        rgb = Image.merge("RGB", (r, g, b))
        rgb = ImageOps.autocontrast(rgb, cutoff=0.5)
        r, g, b = rgb.split()
        return Image.merge("RGBA", (r, g, b, a))
    return ImageOps.autocontrast(image, cutoff=0.5)


# ---------------------------------------------------------------------------
# High-Level Operations
# ---------------------------------------------------------------------------

def apply_recipe(image, recipe_name):
    """Apply a named enhancement recipe to an image."""
    if recipe_name not in RECIPES:
        print(f"Error: Unknown recipe '{recipe_name}'. Available: {', '.join(RECIPES.keys())}")
        sys.exit(1)

    recipe = RECIPES[recipe_name]
    result = image.copy()

    # Convert to RGB if needed for processing
    original_mode = result.mode
    if result.mode == "RGBA":
        alpha = result.split()[3]
    else:
        alpha = None
        result = result.convert("RGB")

    # Grayscale conversion (before other adjustments)
    if recipe.get("grayscale"):
        result = ImageOps.grayscale(result).convert("RGB")

    # Brightness
    if recipe.get("brightness", 1.0) != 1.0:
        result = ImageEnhance.Brightness(result).enhance(recipe["brightness"])

    # Contrast
    if recipe.get("contrast", 1.0) != 1.0:
        result = ImageEnhance.Contrast(result).enhance(recipe["contrast"])

    # Color / Saturation
    if recipe.get("color", 1.0) != 1.0:
        result = ImageEnhance.Color(result).enhance(recipe["color"])

    # Vibrance
    if recipe.get("vibrance", 1.0) != 1.0:
        result = apply_vibrance(result, recipe["vibrance"])

    # Warmth
    if recipe.get("warmth", 0) != 0:
        result = adjust_warmth(result, recipe["warmth"])

    # Coolness
    if recipe.get("coolness", 0) != 0:
        result = adjust_coolness(result, recipe["coolness"])

    # Fade (lifted blacks)
    if recipe.get("fade", 0) > 0:
        result = apply_fade(result, recipe["fade"])

    # Skin smoothing
    if recipe.get("smooth", 0) > 0:
        result = apply_smooth(result, recipe["smooth"])

    # Sharpness
    if recipe.get("sharpness", 1.0) != 1.0:
        result = ImageEnhance.Sharpness(result).enhance(recipe["sharpness"])

    # Grain
    if recipe.get("grain", 0) > 0:
        result = apply_grain(result, recipe["grain"])

    # Vignette
    if recipe.get("vignette", 0) > 0:
        result = apply_vignette(result, recipe["vignette"])

    # Restore alpha if present
    if alpha is not None:
        result = result.convert("RGBA")
        result.putalpha(alpha)
    elif original_mode == "RGBA":
        result = result.convert("RGBA")

    return result


def auto_enhance(image):
    """
    Automatically enhance an image using balanced adjustments.
    Analyzes the image and applies appropriate corrections.
    """
    result = image.copy()
    if result.mode == "RGBA":
        alpha = result.split()[3]
        result = result.convert("RGB")
    else:
        alpha = None

    # Analyze image statistics
    stat = ImageStat.Stat(result)
    mean_brightness = sum(stat.mean[:3]) / 3

    # Step 1: Auto levels
    result = auto_levels(result)

    # Step 2: Brightness correction based on analysis
    if mean_brightness < 100:
        factor = 1.0 + (100 - mean_brightness) / 200
        result = ImageEnhance.Brightness(result).enhance(min(factor, 1.3))
    elif mean_brightness > 170:
        factor = 1.0 - (mean_brightness - 170) / 200
        result = ImageEnhance.Brightness(result).enhance(max(factor, 0.85))

    # Step 3: Moderate contrast boost
    result = ImageEnhance.Contrast(result).enhance(1.10)

    # Step 4: Vibrance boost (subtle)
    result = apply_vibrance(result, 1.12)

    # Step 5: Light sharpening
    result = ImageEnhance.Sharpness(result).enhance(1.15)

    # Step 6: Subtle vignette
    result = apply_vignette(result, 0.08)

    if alpha is not None:
        result = result.convert("RGBA")
        result.putalpha(alpha)

    return result


def resize_for_platform(image, platform, fit="cover"):
    """Resize and crop image for a specific social media platform."""
    if platform not in PLATFORM_SIZES:
        print(f"Error: Unknown platform '{platform}'. Available: {', '.join(sorted(PLATFORM_SIZES.keys()))}")
        sys.exit(1)

    target_w, target_h = PLATFORM_SIZES[platform]

    if fit == "cover":
        # Resize to cover the target area, then center-crop
        img_ratio = image.width / image.height
        target_ratio = target_w / target_h
        if img_ratio > target_ratio:
            new_h = target_h
            new_w = int(new_h * img_ratio)
        else:
            new_w = target_w
            new_h = int(new_w / img_ratio)
        result = image.resize((new_w, new_h), Image.LANCZOS)
        left = (new_w - target_w) // 2
        top = (new_h - target_h) // 2
        result = result.crop((left, top, left + target_w, top + target_h))
    elif fit == "contain":
        # Resize to fit within target, pad with black
        result = ImageOps.pad(image, (target_w, target_h), method=Image.LANCZOS, color=(0, 0, 0))
    elif fit == "stretch":
        result = image.resize((target_w, target_h), Image.LANCZOS)
    else:
        result = ImageOps.fit(image, (target_w, target_h), method=Image.LANCZOS)

    return result


def sharpen_image(image, amount="medium"):
    """Apply sharpening at different intensity levels."""
    factors = {"light": 1.2, "medium": 1.5, "strong": 2.0, "extreme": 3.0}
    factor = factors.get(amount, 1.5)
    return ImageEnhance.Sharpness(image).enhance(factor)


def reduce_noise(image, strength="medium"):
    """Apply noise reduction through selective blurring."""
    radii = {"light": 0.5, "medium": 1.0, "strong": 1.5, "extreme": 2.5}
    radius = radii.get(strength, 1.0)
    blurred = image.filter(ImageFilter.GaussianBlur(radius=radius))
    # Blend to preserve some detail
    blend_factors = {"light": 0.3, "medium": 0.5, "strong": 0.7, "extreme": 0.85}
    blend = blend_factors.get(strength, 0.5)
    return Image.blend(image, blurred, blend)


def adjust_exposure(image, stops):
    """Adjust exposure in stops. +1 = double brightness, -1 = half brightness."""
    factor = 2 ** stops
    return ImageEnhance.Brightness(image).enhance(factor)


def crop_image(image, aspect_ratio=None, region=None):
    """Crop image to aspect ratio (center crop) or specific region."""
    if region:
        left, top, right, bottom = region
        return image.crop((left, top, right, bottom))

    if aspect_ratio:
        target_ratio = aspect_ratio[0] / aspect_ratio[1]
        current_ratio = image.width / image.height
        if current_ratio > target_ratio:
            new_w = int(image.height * target_ratio)
            left = (image.width - new_w) // 2
            return image.crop((left, 0, left + new_w, image.height))
        else:
            new_h = int(image.width / target_ratio)
            top = (image.height - new_h) // 2
            return image.crop((0, top, image.width, top + new_h))

    return image


def convert_format(image, output_path, quality=85):
    """Save image in the format determined by the output path extension."""
    ext = Path(output_path).suffix.lower()
    save_kwargs = {}

    if ext in (".jpg", ".jpeg"):
        if image.mode == "RGBA":
            image = image.convert("RGB")
        save_kwargs["quality"] = quality
        save_kwargs["optimize"] = True
    elif ext == ".png":
        save_kwargs["optimize"] = True
    elif ext == ".webp":
        save_kwargs["quality"] = quality
        save_kwargs["method"] = 4
    elif ext == ".tiff" or ext == ".tif":
        save_kwargs["compression"] = "tiff_lzw"

    image.save(output_path, **save_kwargs)
    return output_path


# ---------------------------------------------------------------------------
# Batch Processing
# ---------------------------------------------------------------------------

def process_batch(input_dir, output_dir, recipe=None, platform=None, fmt=None, quality=85):
    """Process all images in a directory."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    extensions = {".jpg", ".jpeg", ".png", ".webp", ".tiff", ".tif", ".bmp"}
    files = [f for f in input_path.iterdir() if f.suffix.lower() in extensions]

    if not files:
        print(f"No image files found in {input_dir}")
        return

    print(f"Processing {len(files)} images...")

    for i, filepath in enumerate(files, 1):
        try:
            image = Image.open(filepath)
            print(f"  [{i}/{len(files)}] {filepath.name}", end="")

            if recipe:
                if recipe == "auto":
                    image = auto_enhance(image)
                else:
                    image = apply_recipe(image, recipe)

            if platform:
                image = resize_for_platform(image, platform)

            out_ext = f".{fmt}" if fmt else filepath.suffix
            out_name = filepath.stem + out_ext
            out_file = output_path / out_name

            convert_format(image, str(out_file), quality=quality)
            print(f" -> {out_file.name}")

        except Exception as e:
            print(f" [ERROR: {e}]")

    print(f"Done. Output saved to {output_path}")


# ---------------------------------------------------------------------------
# CLI Interface
# ---------------------------------------------------------------------------

def build_parser():
    parser = argparse.ArgumentParser(
        description="Image Editor & Enhancement Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s enhance photo.jpg --style pop
  %(prog)s enhance photo.jpg --style film -o vintage.jpg
  %(prog)s auto photo.jpg -o enhanced.jpg
  %(prog)s resize photo.jpg --platform instagram-post
  %(prog)s sharpen photo.jpg --amount strong
  %(prog)s crop photo.jpg --ratio 16:9
  %(prog)s batch ./photos --output ./enhanced --style golden-hour
  %(prog)s batch ./photos --platform youtube-thumbnail --format webp
  %(prog)s info photo.jpg
  %(prog)s recipes

Available styles:
  pop           Vivid & Punchy
  film          Warm & Nostalgic
  moody         Dark & Dramatic
  bright        Bright & Airy
  golden-hour   Golden Hour Glow
  bw-dramatic   High Contrast B&W
  soft-portrait Soft Portrait
""",
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # --- enhance ---
    p_enhance = subparsers.add_parser("enhance", help="Apply an enhancement recipe")
    p_enhance.add_argument("input", help="Input image path")
    p_enhance.add_argument("--style", "-s", required=True, choices=list(RECIPES.keys()),
                           help="Enhancement style/recipe to apply")
    p_enhance.add_argument("--output", "-o", help="Output path (default: <input>_<style>.<ext>)")
    p_enhance.add_argument("--quality", "-q", type=int, default=90, help="Output JPEG/WebP quality (default: 90)")

    # --- auto ---
    p_auto = subparsers.add_parser("auto", help="Auto-enhance image with balanced adjustments")
    p_auto.add_argument("input", help="Input image path")
    p_auto.add_argument("--output", "-o", help="Output path")
    p_auto.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- resize ---
    p_resize = subparsers.add_parser("resize", help="Resize for a social media platform")
    p_resize.add_argument("input", help="Input image path")
    p_resize.add_argument("--platform", "-p", required=True, choices=sorted(PLATFORM_SIZES.keys()),
                          help="Target platform")
    p_resize.add_argument("--fit", choices=["cover", "contain", "stretch"], default="cover",
                          help="Fit mode (default: cover)")
    p_resize.add_argument("--output", "-o", help="Output path")
    p_resize.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- sharpen ---
    p_sharpen = subparsers.add_parser("sharpen", help="Sharpen an image")
    p_sharpen.add_argument("input", help="Input image path")
    p_sharpen.add_argument("--amount", "-a", choices=["light", "medium", "strong", "extreme"],
                           default="medium", help="Sharpening intensity (default: medium)")
    p_sharpen.add_argument("--output", "-o", help="Output path")
    p_sharpen.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- denoise ---
    p_denoise = subparsers.add_parser("denoise", help="Reduce noise in an image")
    p_denoise.add_argument("input", help="Input image path")
    p_denoise.add_argument("--strength", "-s", choices=["light", "medium", "strong", "extreme"],
                           default="medium", help="Noise reduction strength (default: medium)")
    p_denoise.add_argument("--output", "-o", help="Output path")
    p_denoise.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- exposure ---
    p_exposure = subparsers.add_parser("exposure", help="Adjust exposure in stops")
    p_exposure.add_argument("input", help="Input image path")
    p_exposure.add_argument("--stops", type=float, required=True,
                            help="Exposure adjustment in stops (+1 = 2x brighter, -1 = 2x darker)")
    p_exposure.add_argument("--output", "-o", help="Output path")
    p_exposure.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- warmth ---
    p_warmth = subparsers.add_parser("warmth", help="Adjust color temperature")
    p_warmth.add_argument("input", help="Input image path")
    p_warmth.add_argument("--amount", "-a", type=int, required=True,
                          help="Warmth adjustment (-50 to +50, positive = warmer)")
    p_warmth.add_argument("--output", "-o", help="Output path")
    p_warmth.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- crop ---
    p_crop = subparsers.add_parser("crop", help="Crop image to aspect ratio")
    p_crop.add_argument("input", help="Input image path")
    p_crop.add_argument("--ratio", "-r", help="Aspect ratio (e.g., 16:9, 4:5, 1:1)")
    p_crop.add_argument("--region", help="Crop region as left,top,right,bottom")
    p_crop.add_argument("--output", "-o", help="Output path")
    p_crop.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- convert ---
    p_convert = subparsers.add_parser("convert", help="Convert image format")
    p_convert.add_argument("input", help="Input image path")
    p_convert.add_argument("--format", "-f", required=True,
                           choices=["jpg", "png", "webp", "tiff", "bmp"],
                           help="Output format")
    p_convert.add_argument("--output", "-o", help="Output path")
    p_convert.add_argument("--quality", "-q", type=int, default=90, help="Output quality (default: 90)")

    # --- batch ---
    p_batch = subparsers.add_parser("batch", help="Batch process a directory of images")
    p_batch.add_argument("input", help="Input directory path")
    p_batch.add_argument("--output", "-o", help="Output directory (default: <input>/enhanced)")
    p_batch.add_argument("--style", "-s", choices=list(RECIPES.keys()) + ["auto"],
                         help="Enhancement style (or 'auto')")
    p_batch.add_argument("--platform", "-p", choices=sorted(PLATFORM_SIZES.keys()),
                         help="Resize for platform")
    p_batch.add_argument("--format", "-f", choices=["jpg", "png", "webp", "tiff"],
                         help="Output format (default: same as input)")
    p_batch.add_argument("--quality", "-q", type=int, default=85, help="Output quality (default: 85)")

    # --- info ---
    p_info = subparsers.add_parser("info", help="Show image information")
    p_info.add_argument("input", help="Input image path")

    # --- recipes ---
    subparsers.add_parser("recipes", help="List all available enhancement recipes")

    # --- platforms ---
    subparsers.add_parser("platforms", help="List all supported social media platform sizes")

    return parser


def get_output_path(input_path, output_path, suffix="", new_ext=None):
    """Generate output path if not specified."""
    if output_path:
        return output_path
    p = Path(input_path)
    ext = new_ext if new_ext else p.suffix
    return str(p.parent / f"{p.stem}_{suffix}{ext}")


def main():
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # --- recipes ---
    if args.command == "recipes":
        print("\nAvailable Enhancement Recipes:\n")
        for name, recipe in RECIPES.items():
            print(f"  {name:16s} {recipe['description']}")
        print(f"\nUsage: {sys.argv[0]} enhance <image> --style <recipe-name>")
        return

    # --- platforms ---
    if args.command == "platforms":
        print("\nSupported Social Media Platform Sizes:\n")
        for name, (w, h) in sorted(PLATFORM_SIZES.items()):
            print(f"  {name:24s} {w}x{h}")
        print(f"\nUsage: {sys.argv[0]} resize <image> --platform <name>")
        return

    # --- info ---
    if args.command == "info":
        try:
            img = Image.open(args.input)
            print(f"\nImage Information: {args.input}\n")
            print(f"  Format:      {img.format}")
            print(f"  Mode:        {img.mode}")
            print(f"  Size:        {img.width} x {img.height}")
            print(f"  Aspect:      {img.width / img.height:.2f}:1")
            file_size = os.path.getsize(args.input)
            if file_size > 1024 * 1024:
                print(f"  File size:   {file_size / (1024 * 1024):.2f} MB")
            else:
                print(f"  File size:   {file_size / 1024:.1f} KB")
            if img.info.get("dpi"):
                print(f"  DPI:         {img.info['dpi']}")
            stat = ImageStat.Stat(img.convert("RGB"))
            print(f"  Mean RGB:    ({stat.mean[0]:.0f}, {stat.mean[1]:.0f}, {stat.mean[2]:.0f})")
            brightness = sum(stat.mean[:3]) / 3
            if brightness < 80:
                assessment = "dark (consider increasing exposure)"
            elif brightness < 120:
                assessment = "slightly dark"
            elif brightness < 160:
                assessment = "well-exposed"
            elif brightness < 200:
                assessment = "slightly bright"
            else:
                assessment = "bright (consider reducing exposure)"
            print(f"  Brightness:  {brightness:.0f}/255 — {assessment}")
        except Exception as e:
            print(f"Error: {e}")
        return

    # --- Commands that process an image ---
    if args.command == "batch":
        output_dir = args.output or str(Path(args.input) / "enhanced")
        process_batch(args.input, output_dir, recipe=args.style,
                      platform=args.platform, fmt=args.format, quality=args.quality)
        return

    # Load input image
    try:
        image = Image.open(args.input)
    except Exception as e:
        print(f"Error opening image: {e}")
        sys.exit(1)

    # Process based on command
    if args.command == "enhance":
        result = apply_recipe(image, args.style)
        output = args.output or get_output_path(args.input, None, args.style)
        convert_format(result, output, quality=args.quality)
        print(f"Enhanced with '{args.style}' recipe -> {output}")

    elif args.command == "auto":
        result = auto_enhance(image)
        output = args.output or get_output_path(args.input, None, "enhanced")
        convert_format(result, output, quality=args.quality)
        print(f"Auto-enhanced -> {output}")

    elif args.command == "resize":
        result = resize_for_platform(image, args.platform, fit=args.fit)
        output = args.output or get_output_path(args.input, None, args.platform)
        convert_format(result, output, quality=args.quality)
        w, h = PLATFORM_SIZES[args.platform]
        print(f"Resized to {w}x{h} ({args.platform}) -> {output}")

    elif args.command == "sharpen":
        result = sharpen_image(image, args.amount)
        output = args.output or get_output_path(args.input, None, f"sharp-{args.amount}")
        convert_format(result, output, quality=args.quality)
        print(f"Sharpened ({args.amount}) -> {output}")

    elif args.command == "denoise":
        result = reduce_noise(image, args.strength)
        output = args.output or get_output_path(args.input, None, f"denoised-{args.strength}")
        convert_format(result, output, quality=args.quality)
        print(f"Denoised ({args.strength}) -> {output}")

    elif args.command == "exposure":
        result = adjust_exposure(image, args.stops)
        sign = "+" if args.stops >= 0 else ""
        output = args.output or get_output_path(args.input, None, f"exp{sign}{args.stops}")
        convert_format(result, output, quality=args.quality)
        print(f"Exposure adjusted ({sign}{args.stops} stops) -> {output}")

    elif args.command == "warmth":
        result = adjust_warmth(image, args.amount)
        sign = "+" if args.amount >= 0 else ""
        label = "warmer" if args.amount > 0 else "cooler"
        output = args.output or get_output_path(args.input, None, label)
        convert_format(result, output, quality=args.quality)
        print(f"Color temperature adjusted ({sign}{args.amount}) -> {output}")

    elif args.command == "crop":
        if args.ratio:
            parts = args.ratio.split(":")
            ratio = (int(parts[0]), int(parts[1]))
            result = crop_image(image, aspect_ratio=ratio)
            output = args.output or get_output_path(args.input, None, f"crop-{args.ratio.replace(':', 'x')}")
        elif args.region:
            region = tuple(int(x) for x in args.region.split(","))
            result = crop_image(image, region=region)
            output = args.output or get_output_path(args.input, None, "cropped")
        else:
            print("Error: Provide --ratio or --region")
            sys.exit(1)
        convert_format(result, output, quality=args.quality)
        print(f"Cropped ({result.width}x{result.height}) -> {output}")

    elif args.command == "convert":
        output = args.output or get_output_path(args.input, None, "converted", f".{args.format}")
        convert_format(image, output, quality=args.quality)
        print(f"Converted to {args.format} -> {output}")


if __name__ == "__main__":
    main()
