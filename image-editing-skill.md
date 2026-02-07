# Image Editing & Enhancement Skill

A comprehensive reference for editing, enhancing, and making images more visually appealing. Use this as a structured knowledge base covering color correction, composition, retouching, effects, and professional workflows across all major editing tools.

**This skill includes a ready-to-use CLI tool** — see [Quick Start](#quick-start) to begin editing images immediately.

---

## Quick Start

### Installation

```bash
# Install dependencies
pip install Pillow numpy

# Verify installation
python image_editor.py --help
```

### Basic Usage

```bash
# Auto-enhance any image (analyzes and applies balanced corrections)
python image_editor.py auto photo.jpg -o enhanced.jpg

# Apply a specific style/recipe
python image_editor.py enhance photo.jpg --style pop
python image_editor.py enhance photo.jpg --style film -o vintage.jpg
python image_editor.py enhance photo.jpg --style moody
python image_editor.py enhance photo.jpg --style bright
python image_editor.py enhance photo.jpg --style golden-hour
python image_editor.py enhance photo.jpg --style bw-dramatic
python image_editor.py enhance photo.jpg --style soft-portrait

# Resize for social media platforms
python image_editor.py resize photo.jpg --platform instagram-post
python image_editor.py resize photo.jpg --platform youtube-thumbnail
python image_editor.py resize photo.jpg --platform twitter-post

# Individual adjustments
python image_editor.py sharpen photo.jpg --amount strong
python image_editor.py denoise photo.jpg --strength medium
python image_editor.py exposure photo.jpg --stops +0.5
python image_editor.py warmth photo.jpg --amount 20
python image_editor.py crop photo.jpg --ratio 16:9

# Convert formats
python image_editor.py convert photo.png --format webp

# Batch process an entire folder
python image_editor.py batch ./photos --style pop --format webp
python image_editor.py batch ./photos --platform instagram-post --output ./resized

# View image info and brightness analysis
python image_editor.py info photo.jpg

# List all available recipes and platforms
python image_editor.py recipes
python image_editor.py platforms
```

### Available Enhancement Styles

| Style | Description | Best For |
|---|---|---|
| `pop` | Vivid & Punchy — bold colors with punch | Landscapes, travel, food |
| `film` | Warm & Nostalgic — soft, faded vintage | Portraits, lifestyle, street |
| `moody` | Dark & Dramatic — cinematic brooding | Urban, night, editorial |
| `bright` | Bright & Airy — light, clean, fresh | Weddings, lifestyle, product |
| `golden-hour` | Golden Hour Glow — warm, sun-drenched | Portraits, sunset landscapes |
| `bw-dramatic` | High Contrast B&W — bold monochrome | Editorial, architecture |
| `soft-portrait` | Soft Portrait — flattering skin tones | Headshots, portraits |

### Supported Platforms for Resizing

| Platform | Output Size |
|---|---|
| `instagram-post` | 1080 x 1350 |
| `instagram-story` | 1080 x 1920 |
| `instagram-square` | 1080 x 1080 |
| `facebook-post` | 1200 x 630 |
| `twitter-post` | 1600 x 900 |
| `linkedin-post` | 1200 x 627 |
| `youtube-thumbnail` | 1280 x 720 |
| `youtube-shorts` | 1080 x 1920 |
| `pinterest-pin` | 1000 x 1500 |
| `tiktok-video` | 1080 x 1920 |

Run `python image_editor.py platforms` for the full list including profile picture sizes.

### Using as a Python Library

You can also import the functions directly in your own scripts:

```python
from image_editor import (
    apply_recipe,
    auto_enhance,
    resize_for_platform,
    apply_vibrance,
    apply_vignette,
    adjust_warmth,
    sharpen_image,
    reduce_noise,
    adjust_exposure,
    crop_image,
)
from PIL import Image

# Load image
img = Image.open("photo.jpg")

# Apply a recipe
result = apply_recipe(img, "golden-hour")
result.save("golden.jpg", quality=90)

# Auto-enhance
result = auto_enhance(img)
result.save("enhanced.jpg", quality=90)

# Chain multiple operations
result = img.copy()
result = adjust_warmth(result, 15)
result = apply_vibrance(result, 1.2)
result = sharpen_image(result, "light")
result = apply_vignette(result, 0.1)
result = resize_for_platform(result, "instagram-post")
result.save("instagram_ready.jpg", quality=90)
```

---

## Table of Contents

1. [Image Editing Fundamentals](#1-image-editing-fundamentals)
2. [Color Correction & Enhancement](#2-color-correction--enhancement)
3. [Exposure & Lighting Adjustments](#3-exposure--lighting-adjustments)
4. [Composition & Cropping](#4-composition--cropping)
5. [Retouching & Cleanup](#5-retouching--cleanup)
6. [Sharpening & Noise Reduction](#6-sharpening--noise-reduction)
7. [Filters, Effects & Styles](#7-filters-effects--styles)
8. [Typography & Overlays](#8-typography--overlays)
9. [Resolution, Resizing & Export](#9-resolution-resizing--export)
10. [Making Images More Appealing](#10-making-images-more-appealing)
11. [Workflow & Best Practices](#11-workflow--best-practices)
12. [Tool-Specific Guides](#12-tool-specific-guides)
13. [Quick Reference & Checklists](#13-quick-reference--checklists)

---

## 1. Image Editing Fundamentals

### 1.1 Core Concepts

Every digital image is composed of pixels, each storing color information. Understanding how these pixels represent color is the foundation of all editing.

| Concept | Description |
|---|---|
| **Pixel** | The smallest unit of a digital image — a single colored dot |
| **Resolution** | The number of pixels in an image (e.g., 3840 x 2160) |
| **DPI / PPI** | Dots/pixels per inch — determines print quality (72 for web, 300 for print) |
| **Bit Depth** | Number of bits per channel — 8-bit (256 levels), 16-bit (65,536 levels) |
| **Color Space** | The range of colors an image can represent (sRGB, Adobe RGB, ProPhoto RGB) |
| **Aspect Ratio** | Width-to-height proportion (16:9, 4:3, 1:1, 3:2) |

### 1.2 Color Models

| Model | Channels | Use Case |
|---|---|---|
| **RGB** | Red, Green, Blue | Digital displays, web, UI design |
| **CMYK** | Cyan, Magenta, Yellow, Key (Black) | Print production |
| **HSL / HSB** | Hue, Saturation, Lightness / Brightness | Intuitive color adjustment |
| **LAB** | Lightness, A (green-red), B (blue-yellow) | Advanced color correction, color-neutral sharpening |

**Key insight:** Edit in RGB for digital output and convert to CMYK only at the final stage for print. Working in LAB mode enables powerful color corrections without introducing color casts.

### 1.3 Non-Destructive Editing

Always preserve the original image data by using non-destructive techniques:

| Technique | Description | Tool Support |
|---|---|---|
| **Adjustment Layers** | Apply changes on separate layers that can be modified or removed | Photoshop, GIMP, Affinity Photo |
| **Smart Objects** | Embed the original data so filters and transforms are re-editable | Photoshop |
| **Masks** | Hide/reveal parts of layers without deleting pixels | All major editors |
| **RAW Processing** | Edit the raw sensor data before converting to a raster format | Lightroom, Camera Raw, Capture One, RawTherapee |
| **Virtual Copies** | Create alternate edits without duplicating files | Lightroom, Capture One |
| **History / Snapshots** | Save editing states to revert to at any point | Photoshop, GIMP |

**Rule:** Never flatten layers or apply destructive edits until the final export. Keep your working file (PSD, XCF, AFPHOTO) with all layers intact.

### 1.4 File Formats Overview

| Format | Compression | Transparency | Best For |
|---|---|---|---|
| **RAW** (CR2, NEF, ARW) | None | N/A | Source files from cameras — maximum editing flexibility |
| **PSD** | Lossless | Yes | Working files with layers (Photoshop) |
| **TIFF** | Lossless | Yes | High-quality archival and print |
| **PNG** | Lossless | Yes | Web graphics, screenshots, images needing transparency |
| **JPEG** | Lossy | No | Photographs for web and sharing (small file size) |
| **WebP** | Lossy/Lossless | Yes | Modern web — smaller than JPEG/PNG at equivalent quality |
| **AVIF** | Lossy/Lossless | Yes | Next-gen web format — superior compression |
| **HEIF/HEIC** | Lossy | Yes | Apple ecosystem — better quality than JPEG at same size |
| **SVG** | N/A (vector) | Yes | Logos, icons, illustrations (scalable without quality loss) |

---

## 2. Color Correction & Enhancement

Color is the single most impactful element in making an image appealing. Proper color correction fixes issues; color grading creates mood and style.

### 2.1 White Balance

White balance ensures neutral whites and accurate colors by compensating for the color temperature of the light source.

| Light Source | Approximate Kelvin | Appearance |
|---|---|---|
| **Candlelight** | 1,800 - 2,000 K | Very warm (orange) |
| **Tungsten / Incandescent** | 2,700 - 3,200 K | Warm (yellow-orange) |
| **Sunrise / Sunset** | 3,000 - 4,000 K | Warm golden |
| **Fluorescent** | 3,500 - 4,500 K | Slightly cool (green tint) |
| **Daylight** | 5,200 - 5,500 K | Neutral |
| **Overcast Sky** | 6,000 - 7,000 K | Cool (blue) |
| **Shade** | 7,000 - 9,000 K | Very cool (blue) |

**How to correct:**
1. Use the eyedropper / white balance picker on a known neutral area (white or gray)
2. Adjust the Temperature slider: move right to warm, left to cool
3. Adjust the Tint slider to correct green-magenta shifts
4. If shooting RAW, white balance is fully adjustable without quality loss

**Creative white balance:** Intentionally warming an image creates a cozy, nostalgic feel. Cooling creates a clinical, modern, or melancholic mood.

### 2.2 Levels & Curves

These are the most powerful tools for tonal and color adjustment.

#### Levels

Controls the input and output tonal range using five points:

```
Input:
  Black Point -------- Midtones -------- White Point
  (shadows)            (gamma)           (highlights)

Output:
  Black Level --------------------------------- White Level
```

| Adjustment | Effect |
|---|---|
| Move black point right | Darken shadows, increase contrast |
| Move white point left | Brighten highlights, increase contrast |
| Move midtone left | Brighten midtones |
| Move midtone right | Darken midtones |

**Quick fix:** Hold Alt/Option while dragging black/white points to see clipping preview — stop just before important detail is lost.

#### Curves

The most versatile tonal adjustment tool. The x-axis represents input tones (shadows left, highlights right), the y-axis represents output.

```
Output
  |         . * (highlight lift)
  |       *
  |     *     <- S-curve adds contrast
  |   *
  | *   (shadow dip)
  +-------------------- Input
  Shadows    Highlights
```

| Curve Shape | Effect |
|---|---|
| **S-curve** | Increases contrast — darkens shadows, brightens highlights |
| **Reverse S-curve** | Decreases contrast — faded/matte look |
| **Linear lift** | Raises all tones — brightens entire image |
| **Linear drop** | Lowers all tones — darkens entire image |
| **Per-channel curves** | Adjust individual R, G, B channels for color grading |

**Pro techniques:**
- Gentle S-curve on the luminosity channel adds contrast without shifting colors
- Lifting the bottom-left point of the curve creates a filmic "faded blacks" look
- Using per-channel curves: boost red in highlights and blue in shadows for a warm cinematic teal-orange grade

### 2.3 Saturation vs. Vibrance

| Adjustment | What It Does | When to Use |
|---|---|---|
| **Saturation** | Increases intensity of ALL colors equally | When the entire image looks washed out |
| **Vibrance** | Boosts less-saturated colors more, protects already-saturated tones and skin tones | Preferred for portraits and natural-looking enhancement |

**Common mistake:** Over-saturating images. Subtle adjustments (+10 to +25) typically look more appealing than extreme boosts. Vibrance is almost always the safer choice.

### 2.4 HSL (Hue, Saturation, Luminance) Adjustments

Targeted per-color adjustments for fine-grained control:

| Channel | Hue Shift | Saturation | Luminance |
|---|---|---|---|
| **Reds** | Shift toward orange/magenta | Control skin tone intensity | Brighten/darken reds |
| **Oranges** | Fine-tune skin tones | Desaturate for natural skin | Brighten skin |
| **Yellows** | Shift greens to yellow/gold | Boost autumn foliage | Control grass brightness |
| **Greens** | Shift toward teal or yellow | Mute or pop foliage | Darken for richness |
| **Blues** | Shift sky color | Intensify or mute sky | Darken sky for drama |
| **Purples** | Shift flower tones | Boost or mute lavender | Control purple brightness |

**Popular color grading moves:**
- Shift greens slightly toward teal + desaturate for a cinematic look
- Shift blues toward teal/aqua for travel photography
- Boost orange luminance + reduce orange saturation for pleasing skin tones
- Shift yellows toward orange for warm autumn tones

### 2.5 Color Grading & Split Toning

Apply different color tints to shadows, midtones, and highlights independently:

| Tonal Range | Common Tint | Effect |
|---|---|---|
| **Shadows** | Blue, teal, deep purple | Adds depth, coolness, cinematic feel |
| **Midtones** | Subtle green or warm neutral | Shifts overall mood without extremes |
| **Highlights** | Orange, warm yellow, peach | Adds warmth, golden glow, sun-kissed feel |

**Classic color grade combinations:**

| Name | Shadows | Highlights | Mood |
|---|---|---|---|
| **Teal & Orange** | Teal / cyan | Orange / amber | Cinematic, blockbuster film |
| **Cool & Warm** | Blue | Warm yellow | Balanced contrast, modern |
| **Vintage / Film** | Green-blue | Peach / faded yellow | Nostalgic, retro |
| **Moody / Dark** | Deep blue-purple | Desaturated warm | Dramatic, editorial |
| **Pastel / Soft** | Soft lavender | Soft pink / peach | Dreamy, feminine, light |

---

## 3. Exposure & Lighting Adjustments

### 3.1 Understanding the Histogram

The histogram shows the distribution of tones in an image from pure black (left) to pure white (right).

```
Pixel
Count
  |
  |    *
  |   * *      *
  |  *   *    * *
  | *     *  *   *
  |*       **     *
  +------------------
  Black  Midtones  White
```

| Histogram Shape | Interpretation |
|---|---|
| **Bunched left** | Underexposed — image is too dark |
| **Bunched right** | Overexposed — image is too bright |
| **Centered / bell** | Well-exposed with full tonal range |
| **Bimodal (two humps)** | High contrast scene — bright and dark areas |
| **Flat / spread out** | Low contrast — image may look flat |
| **Clipping on left** | Crushed blacks — shadow detail lost |
| **Clipping on right** | Blown highlights — highlight detail lost |

**Rule:** A good histogram uses the full tonal range without clipping on either end (unless intentionally artistic).

### 3.2 Exposure Controls

| Slider | Affects | Typical Range |
|---|---|---|
| **Exposure** | Overall brightness (like adjusting aperture) | -2.0 to +2.0 stops |
| **Highlights** | Brightest areas only | -100 to +100 |
| **Shadows** | Darkest areas only | -100 to +100 |
| **Whites** | White clipping point | -100 to +100 |
| **Blacks** | Black clipping point | -100 to +100 |
| **Contrast** | Separation between light and dark tones | -100 to +100 |

**Order of operations for exposure correction:**
1. Set overall Exposure to get the midtones correct
2. Recover Highlights (pull left) to restore blown-out areas
3. Open Shadows (push right) to reveal detail in dark areas
4. Set Whites to establish the brightest point without clipping
5. Set Blacks to establish the deepest shadow without crushing
6. Fine-tune Contrast to taste

### 3.3 Dodge & Burn (Localized Light Control)

Selectively brighten (dodge) or darken (burn) specific areas to direct the viewer's eye and add depth.

| Technique | Method | Use Case |
|---|---|---|
| **Dodge (Lighten)** | Paint with white on a soft-light layer, or use dodge tool | Brighten eyes, highlight cheekbones, draw attention |
| **Burn (Darken)** | Paint with black on a soft-light layer, or use burn tool | Add depth to shadows, darken edges (vignette), sculpt features |
| **Luminosity masking** | Create masks based on tone ranges | Precise adjustments to only highlights, midtones, or shadows |

**Best practice:** Use a soft brush at 5-15% opacity and build up gradually. Multiple gentle passes produce more natural results than one heavy stroke.

### 3.4 HDR & Tone Mapping

High Dynamic Range (HDR) merges multiple exposures to capture detail in both shadows and highlights that a single exposure cannot.

**When to use HDR:**
- High-contrast scenes (bright sky + dark foreground)
- Real estate and architectural photography
- Landscape photography with extreme lighting

**When NOT to use HDR:**
- Scenes with moving subjects (ghosting artifacts)
- Portraits (unnatural skin rendering)
- Situations where contrast is part of the story (silhouettes, low-key)

**Natural-looking HDR tips:**
- Merge at least 3 exposures bracketed 1-2 stops apart
- Use conservative tone mapping — avoid the "crunchy HDR" look
- Reduce clarity/structure in the HDR result for a more natural feel
- Blend with the original middle exposure at 30-50% opacity

---

## 4. Composition & Cropping

### 4.1 Composition Rules

Good composition guides the viewer's eye and creates a sense of balance or intentional tension.

| Rule | Description | When to Use |
|---|---|---|
| **Rule of Thirds** | Place subjects at the intersections of a 3x3 grid | Most photographs — default starting point |
| **Golden Ratio (Phi Grid)** | Similar to thirds but with a tighter center — 1:1.618 | Portraits, fine art, natural scenes |
| **Leading Lines** | Use natural lines (roads, fences, rivers) to draw the eye toward the subject | Landscapes, architecture, street photography |
| **Symmetry** | Center the subject for a balanced, formal composition | Architecture, reflections, product photography |
| **Frame within a Frame** | Use doorways, windows, arches to frame the subject | Architecture, environmental portraits |
| **Negative Space** | Leave empty space around the subject for breathing room | Minimalist design, editorial, social media |
| **Diagonal Lines** | Tilt elements along diagonals for dynamic energy | Action shots, sports, fashion |
| **Fill the Frame** | Get close — let the subject dominate | Macro, portraits, food photography |
| **Odd Numbers** | Groups of 3 or 5 objects are more visually interesting | Still life, product arrangements |

### 4.2 Cropping Best Practices

| Guideline | Details |
|---|---|
| **Crop with purpose** | Every crop should improve composition, not just shrink the image |
| **Maintain aspect ratio** | Match the intended output ratio (16:9 for video, 4:5 for Instagram, 1:1 for profile) |
| **Don't crop joints** | Avoid cropping at wrists, ankles, knees, or elbows in portraits |
| **Leave room for gaze** | If the subject faces left, leave space on the left side |
| **Straighten horizons** | Tilted horizons are immediately noticeable and distracting |
| **Crop in-camera first** | Less cropping in post means more pixels to work with |

### 4.3 Standard Aspect Ratios

| Ratio | Common Use |
|---|---|
| **1:1** | Social media profile pictures, Instagram posts |
| **4:5** | Instagram portrait, mobile-friendly content |
| **3:2** | Standard DSLR/mirrorless output, 4x6 prints |
| **4:3** | Micro four-thirds cameras, older monitors |
| **16:9** | Widescreen displays, YouTube, presentations |
| **2:3** | Pinterest pins (vertical), mobile stories |
| **21:9** | Ultrawide cinematic |

---

## 5. Retouching & Cleanup

### 5.1 Blemish & Object Removal

| Tool | How It Works | Best For |
|---|---|---|
| **Spot Healing Brush** | Automatically samples surrounding texture | Small blemishes, dust spots, minor imperfections |
| **Clone Stamp** | Copies pixels from a source point | Precise removal, pattern-matching areas |
| **Patch Tool** | Drag a selection to blend with a target area | Larger areas on skin or backgrounds |
| **Content-Aware Fill** | Intelligently fills selected area using surrounding context | Removing objects from backgrounds |
| **Frequency Separation** | Separates texture from color on different layers | Advanced skin retouching without losing texture |

### 5.2 Portrait Retouching Guidelines

The goal of portrait retouching is to enhance while preserving the subject's natural appearance.

**DO:**
- Remove temporary blemishes (acne, scratches, stray hairs)
- Even out skin tone using curves or HSL adjustments
- Brighten eyes slightly with dodge tool (iris only)
- Reduce under-eye shadows gently (not eliminate)
- Whiten teeth subtly (reduce yellow saturation, slight luminance boost)
- Add a gentle catch light to eyes if missing
- Use frequency separation to smooth skin while retaining texture

**DON'T:**
- Smooth skin to a plastic, pore-less finish
- Alter facial proportions (unless specifically requested)
- Remove all freckles, moles, or natural features
- Over-whiten eyes or teeth (looks unnatural)
- Over-sharpen eyes (creates an uncanny effect)
- Apply the same retouching to every face — adapt to the subject

### 5.3 Background Cleanup

| Technique | Description |
|---|---|
| **Background blur** | Add gaussian blur to a duplicate layer masked to the background — simulates shallow depth of field |
| **Background replacement** | Select subject, invert, replace background with solid color, gradient, or new scene |
| **Distraction removal** | Clone/heal distracting elements (power lines, trash, signs) |
| **Sky replacement** | Replace a bland sky with a dramatic one — available as an automated feature in Photoshop and Luminar |
| **Edge refinement** | After background work, refine selection edges to avoid halos (use Refine Edge / Select and Mask for hair) |

---

## 6. Sharpening & Noise Reduction

### 6.1 Sharpening

Sharpening increases the contrast along edges to create the perception of greater detail.

| Method | How It Works | When to Use |
|---|---|---|
| **Unsharp Mask (USM)** | Increases contrast at edges using Amount, Radius, Threshold | General-purpose sharpening |
| **Smart Sharpen** | Advanced USM with lens blur correction | Correcting slight softness from lenses |
| **High Pass Sharpening** | Apply High Pass filter on a duplicate layer set to Overlay | Precise control, non-destructive |
| **Capture Sharpening** | Applied during RAW conversion to counteract sensor softness | First stage — always subtle |
| **Output Sharpening** | Applied at the very end, tuned for the output medium | Final stage — different for screen vs. print |

**Recommended settings for Unsharp Mask:**

| Output | Amount | Radius | Threshold |
|---|---|---|---|
| **Web / screen** | 50-100% | 0.5-1.0 px | 0-3 |
| **Print (300 DPI)** | 100-200% | 1.0-2.0 px | 0-5 |
| **High-res detailed** | 80-150% | 0.3-0.8 px | 0-2 |

**High Pass Sharpening steps:**
1. Duplicate the image layer
2. Apply Filter > Other > High Pass (radius 1-3 px)
3. Set blend mode to Overlay (or Soft Light for subtler effect)
4. Adjust layer opacity to taste (typically 40-80%)

**Warning signs of over-sharpening:**
- Visible halos along edges (bright outlines)
- Crunchy, gritty texture in smooth areas
- Amplified noise in shadow areas
- Unnatural edge contrast

### 6.2 Noise Reduction

Noise appears as random grain or color speckles, especially in images shot at high ISO or in low light.

| Noise Type | Appearance | Cause |
|---|---|---|
| **Luminance noise** | Grainy texture (like film grain) | High ISO, small sensors |
| **Chroma noise** | Random colored speckles (red, green, blue) | High ISO, long exposures, underexposure |

| Method | Description | Tool |
|---|---|---|
| **Luminance slider** | Smooths grainy texture — trades detail for smoothness | Lightroom, Camera Raw |
| **Color slider** | Removes chromatic noise — usually safe to apply aggressively | Lightroom, Camera Raw |
| **AI Denoise** | Machine-learning-based noise removal preserving detail | Lightroom AI Denoise, Topaz DeNoise AI, DxO PureRAW |
| **Median filter** | Simple average of surrounding pixels | Photoshop, GIMP |
| **Manual blending** | Stack multiple exposures and average them | Photoshop (Mean stack mode) |

**Noise reduction order of operations:**
1. Apply chromatic noise reduction first (Color slider to ~25-50)
2. Apply luminance noise reduction (start at 20, increase until grain is manageable)
3. Adjust Detail slider to preserve edges (50-75)
4. Apply sharpening AFTER noise reduction, not before

---

## 7. Filters, Effects & Styles

### 7.1 Popular Enhancement Effects

| Effect | How to Achieve | Impact |
|---|---|---|
| **Vignette** | Darken edges, brighten center — Post-Crop Vignette or radial gradient | Draws focus to center, adds depth |
| **Grain / Film Grain** | Add subtle noise with grain controls or overlays | Adds texture, vintage/analog feel |
| **Glow / Soft Focus** | Duplicate layer, apply Gaussian blur, set to Screen at low opacity | Dreamy, romantic, ethereal look |
| **Matte / Faded** | Lift the black point in Curves (raise bottom-left) | Vintage, film-inspired, soft contrast |
| **High Contrast B&W** | Desaturate, then apply strong S-curve + clarity | Bold, dramatic, editorial |
| **Cross-Processing** | Apply opposing curves to individual RGB channels | Unpredictable, retro color shifts |
| **Duotone** | Map two colors to shadows and highlights | Graphic, modern, striking posters |
| **Selective Color Pop** | Desaturate all colors except one | Draws attention to a specific element |
| **Orton Effect** | Blend a sharp copy with a bright, blurred copy | Dreamy glow while retaining detail |
| **Cinemagraph** | Freeze most of image, animate one element | Eye-catching social media content |

### 7.2 Texture & Clarity

| Slider | Effect | Best For |
|---|---|---|
| **Clarity** | Increases midtone contrast — enhances texture and detail | Landscapes, architecture, food, product shots |
| **Texture** | Finer-grained detail enhancement than clarity — better for skin | Portraits (slight negative), nature, close-ups |
| **Dehaze** | Removes atmospheric haze, increases contrast and saturation | Foggy landscapes, misty scenes, underwater |

**Guidelines:**
- Clarity +20 to +40 adds punch to landscapes and cityscapes
- Clarity -10 to -20 softens skin in portraits without blurring
- Texture is safer for skin than Clarity (won't emphasize pores as much)
- Dehaze above +30 can look unnatural — combine with reduced contrast

### 7.3 Black & White Conversion

Good black and white conversion is about far more than removing color.

**Method (best to worst):**
1. Use dedicated B&W conversion panel with per-channel sliders (Lightroom, Photoshop)
2. Channel Mixer: manually blend R, G, B channels for custom tonal mapping
3. Desaturation — simple but lacks control (avoid)

**Tips for compelling B&W:**
- Strong contrast makes B&W images pop — use a pronounced S-curve
- Pay attention to luminance relationships between colors that become the same gray
- Red filter effect (darken blues, brighten reds) for dramatic skies
- Add grain for an analog feel
- Dodge and burn is even more critical in B&W — it defines the image's structure

---

## 8. Typography & Overlays

### 8.1 Adding Text to Images

| Principle | Guideline |
|---|---|
| **Readability first** | Ensure text contrasts with the background — use shadows, outlines, or semi-transparent backing |
| **Font pairing** | Use maximum 2 fonts — one for headlines, one for body text |
| **Hierarchy** | Establish clear size differences between headline, subheadline, and body |
| **Alignment** | Align text to a grid or anchor point — avoid centering everything |
| **Whitespace** | Give text room to breathe — don't crowd edges |

### 8.2 Graphic Overlays

| Overlay Type | Purpose | Implementation |
|---|---|---|
| **Gradient overlay** | Darken areas behind text for readability | Linear or radial gradient on a separate layer, adjust opacity |
| **Light leaks** | Add warm, organic light flares | Use overlay blending mode with a light leak texture |
| **Bokeh overlays** | Add out-of-focus light circles | Screen blending mode with bokeh texture images |
| **Texture overlays** | Add paper, fabric, or concrete textures | Overlay or Soft Light blending mode, reduce opacity |
| **Watermark** | Brand protection | Low-opacity logo on a separate layer, placed consistently |

### 8.3 Blending Modes for Overlays

| Mode | Effect | Common Use |
|---|---|---|
| **Normal** | No blending — covers underlying layer | Base layers, solid elements |
| **Multiply** | Darkens — multiplies base and blend values | Shadows, darkening effects |
| **Screen** | Lightens — inverse of Multiply | Light leaks, brightening effects |
| **Overlay** | Combination of Multiply and Screen — increases contrast | Texture overlays, color grading |
| **Soft Light** | Subtle version of Overlay | Gentle texture and light effects |
| **Hard Light** | Intense version of Overlay | Strong contrast effects |
| **Color Dodge** | Brightens base dramatically using blend layer | Glow effects, light flares |
| **Luminosity** | Applies only the brightness from the blend layer | Sharpening without color shifts |
| **Color** | Applies only the color from the blend layer | Colorizing B&W images, color grading |

---

## 9. Resolution, Resizing & Export

### 9.1 Resolution Guidelines

| Use Case | Resolution | DPI/PPI |
|---|---|---|
| **Web / social media** | 72-150 PPI | 72 PPI standard |
| **Email / messaging** | 72-96 PPI | Keep file size small |
| **Desktop printing** | 240-300 PPI | 300 PPI for photo-quality prints |
| **Large format printing** | 150-200 PPI | Viewed from further away, lower PPI acceptable |
| **Billboard** | 30-72 PPI | Viewed from great distance |

### 9.2 Social Media Image Sizes (2025-2026)

| Platform | Post Size | Story/Reel | Profile |
|---|---|---|---|
| **Instagram** | 1080x1350 (4:5) | 1080x1920 (9:16) | 320x320 |
| **Facebook** | 1200x630 | 1080x1920 | 180x180 |
| **Twitter/X** | 1600x900 (16:9) | N/A | 400x400 |
| **LinkedIn** | 1200x627 | N/A | 400x400 |
| **YouTube** | Thumbnail: 1280x720 | Shorts: 1080x1920 | 800x800 |
| **Pinterest** | 1000x1500 (2:3) | 1080x1920 | 165x165 |
| **TikTok** | N/A | 1080x1920 (9:16) | 200x200 |

### 9.3 Resizing Methods

| Method | Quality | Use When |
|---|---|---|
| **Bicubic (smooth)** | High for downsizing | Reducing image size |
| **Bicubic Sharper** | Best for downsizing | Reducing and maintaining sharpness |
| **Bicubic Smoother** | Best for upsizing | Enlarging images (moderate) |
| **Lanczos** | Highest quality resampling | Available in GIMP, ImageMagick |
| **AI Upscaling** | Best for significant enlargement | Topaz Gigapixel, Photoshop Super Resolution, Real-ESRGAN |
| **Nearest Neighbor** | Preserves hard edges | Pixel art, screenshots with text |

### 9.4 Export Settings

| Format | Quality Setting | Typical File Size | Use Case |
|---|---|---|---|
| **JPEG 60-70%** | Medium | 100-300 KB | Web thumbnails, previews |
| **JPEG 80-85%** | High | 300-800 KB | General web publishing |
| **JPEG 90-95%** | Maximum | 800 KB - 3 MB | High-quality web, client delivery |
| **PNG-8** | 256 colors | 50-200 KB | Simple graphics, icons |
| **PNG-24** | Full color + transparency | 500 KB - 5 MB | Graphics needing transparency |
| **WebP 80%** | High | 30-50% smaller than equivalent JPEG | Modern web optimization |
| **TIFF (uncompressed)** | Lossless | 10-100+ MB | Print production, archival |

---

## 10. Making Images More Appealing

This section brings together specific techniques and recipes to make images visually striking and engaging.

### 10.1 The Five Pillars of Appealing Images

| Pillar | Description | Key Adjustments |
|---|---|---|
| **Light** | Proper exposure and contrast draw the eye | Exposure, Highlights/Shadows, Contrast, Dodge/Burn |
| **Color** | Harmonious, intentional color creates mood | White balance, HSL, Color grading, Vibrance |
| **Clarity** | Sharp detail and clean textures build quality perception | Sharpening, Clarity, Texture, Noise reduction |
| **Composition** | Strong framing and balance keep the viewer engaged | Crop, Straighten, Rule of thirds |
| **Story** | Emotional connection makes images memorable | All of the above working together toward a mood |

### 10.2 Quick Enhancement Recipes

#### Recipe 1: The "Pop" (Vivid & Punchy)
```
Contrast:      +15 to +25
Highlights:    -20
Shadows:       +20
Clarity:       +25
Vibrance:      +20
Saturation:    +5
Vignette:      -15
```
**Result:** Bold, vivid image with punch. Great for landscapes, travel, food.

#### Recipe 2: The "Film Look" (Warm & Nostalgic)
```
Exposure:      +0.2
Contrast:      -10
Highlights:    -30
Shadows:       +25
Blacks:        +15 (lifted / faded)
Tone Curve:    Lift black point to ~10
White Balance:  Warm (+500 K)
Saturation:    -10
Grain:         25, Size 30
Split Tone:    Shadows blue (220°), Highlights orange (40°)
```
**Result:** Soft, faded, vintage aesthetic. Ideal for portraits, lifestyle, street.

#### Recipe 3: The "Moody & Dark" (Dramatic)
```
Exposure:      -0.5
Contrast:      +20
Highlights:    -40
Shadows:       -20
Blacks:        -15
Clarity:       +30
Vibrance:      -10
Saturation:    -15
Vignette:      -30
Color Grade:   Shadows: deep blue (240°), Highlights: muted amber (35°)
```
**Result:** Dark, cinematic, brooding. Best for urban, night, editorial.

#### Recipe 4: The "Bright & Airy" (Light & Clean)
```
Exposure:      +0.5 to +1.0
Contrast:      -15
Highlights:    +10
Shadows:       +40
Whites:        +20
Blacks:        +10
Clarity:       -5
Vibrance:      +10
White Balance:  Slightly warm (+200 K)
Tone Curve:    Gentle lift across midtones
```
**Result:** Light, clean, fresh. Perfect for weddings, lifestyle, product, food.

#### Recipe 5: The "Golden Hour Glow"
```
White Balance:  5800-6500 K (warm)
Tint:          +10 toward magenta
Exposure:      +0.3
Contrast:      +10
Highlights:    -25 (recover sky)
Shadows:       +30 (open shadows)
Vibrance:      +15
Color Grade:   Highlights: peach/gold (30°), Shadows: warm purple (280°)
Radial Filter: Warm exposure boost from light source direction
```
**Result:** Warm, sun-drenched look. Ideal for portraits, landscapes at sunset.

### 10.3 Genre-Specific Enhancement

#### Landscape Photography
- Boost clarity and texture (+20 to +40) for detail
- Darken blues in HSL for dramatic skies
- Use graduated filter to balance sky and foreground
- Increase vibrance rather than saturation for natural color
- Apply local contrast enhancements to foreground elements
- Remove distracting elements (trash, power lines)

#### Portrait Photography
- Reduce clarity slightly (-5 to -15) or use texture slider for skin
- Brighten eyes with radial filter or dodge tool
- Warm white balance slightly for flattering skin tones
- Desaturate oranges/reds slightly if skin looks overly flushed
- Add a subtle vignette to focus attention on the face
- Use frequency separation for detailed skin retouching

#### Food Photography
- Increase clarity and texture for appetizing detail
- Boost warm tones — food looks best slightly warm
- Increase saturation of reds and yellows (appetite-inducing colors)
- Use shallow depth of field (or blur background in post)
- Brighten highlights — food looks fresher when bright
- Use top-down or 45-degree angles for most dishes

#### Product Photography
- Clean, even lighting — minimize harsh shadows
- White or neutral background for e-commerce
- Increase contrast slightly for product definition
- Ensure accurate color representation (important for buyer trust)
- Add subtle shadow/reflection for grounding
- Sharpen at export for crisp detail

#### Architecture & Real Estate
- Correct lens distortion and perspective (vertical lines should be straight)
- Use HDR or exposure blending for interior/exterior balance
- Straighten all horizontal and vertical lines
- Boost clarity for structural detail
- Ensure white balance is neutral and consistent across a set
- Remove temporary clutter and disturbances

### 10.4 Before & After Checklist

Before exporting any enhanced image, verify:

- [ ] White balance looks natural (or intentionally stylized)
- [ ] Exposure is correct — histogram uses full range without unwanted clipping
- [ ] Highlights are not blown, shadows are not crushed (unless intentional)
- [ ] Colors look pleasing and harmonious
- [ ] Skin tones are natural (check against reference if needed)
- [ ] Sharpening is applied without visible halos or artifacts
- [ ] Noise is controlled without losing important texture
- [ ] Composition is strong — horizon straight, distractions removed
- [ ] No visible editing artifacts (clone stamp repeats, selection edges, banding)
- [ ] Image is sized and formatted correctly for the intended output

---

## 11. Workflow & Best Practices

### 11.1 Professional Editing Workflow

Follow this order for best results. Each step builds on the previous.

```
1. Import & Organize
   └─ Cull (select keepers), rate, tag, organize into collections

2. Lens Corrections
   └─ Remove distortion, chromatic aberration, vignetting

3. Crop & Straighten
   └─ Establish composition before adjusting tones

4. White Balance
   └─ Set accurate color foundation

5. Exposure & Tone
   └─ Exposure, Highlights, Shadows, Whites, Blacks, Contrast

6. Color Correction
   └─ HSL adjustments, remove color casts

7. Color Grading
   └─ Split toning, creative color — establish mood

8. Detail
   └─ Noise reduction first, then sharpening

9. Local Adjustments
   └─ Graduated filters, radial filters, brush adjustments
   └─ Dodge and burn

10. Effects
    └─ Vignette, grain, dehaze, special effects

11. Retouching
    └─ Blemish removal, object removal, cleanup

12. Export
    └─ Resize, output sharpen, format, quality settings
```

### 11.2 Batch Editing

For consistent look across a series of images:

1. Edit one "hero" image to perfection
2. Copy/sync settings to similar images
3. Fine-tune individual images (exposure may differ)
4. Use presets to ensure consistent starting points
5. Export all images with identical output settings

### 11.3 Preset / Action Management

| Concept | Description |
|---|---|
| **Presets** (Lightroom, Capture One) | Saved slider positions applied on import or with one click |
| **Actions** (Photoshop) | Recorded sequences of steps that can be replayed |
| **LUTs** (Look-Up Tables) | Color transformation files used for consistent color grading across tools and video |
| **Styles** (Capture One) | Similar to presets — saved adjustment sets |

**Building a preset library:**
- Create presets for your common starting points (daylight portrait, indoor event, landscape sunny, etc.)
- Layer presets: one for base tones, one for color grade, one for effects
- Name presets descriptively: `Moody-Blue-Shadows-v2`, not `Preset 47`
- Periodically audit and remove presets you no longer use

### 11.4 Color Management

| Setting | Recommendation |
|---|---|
| **Working color space** | Adobe RGB (for flexibility) or sRGB (if web-only) |
| **Monitor calibration** | Calibrate monthly with a hardware colorimeter (X-Rite, Datacolor) |
| **Soft proofing** | Preview how colors will look on target output before printing |
| **ICC profiles** | Use paper/printer-specific profiles for accurate prints |
| **Export color space** | sRGB for web (universal compatibility), Adobe RGB for print prepress |

---

## 12. Tool-Specific Guides

### 12.1 Adobe Lightroom (Classic & CC)

**Strengths:** RAW processing, batch editing, catalog organization, non-destructive workflow

| Panel | Key Features |
|---|---|
| **Basic** | White balance, exposure, contrast, highlights, shadows, vibrance |
| **Tone Curve** | Point curve and parametric sliders for fine tonal control |
| **HSL / Color** | Per-color hue, saturation, luminance adjustments |
| **Color Grading** | Three-way color wheels for shadows, midtones, highlights |
| **Detail** | Sharpening and noise reduction |
| **Lens Corrections** | Distortion, chromatic aberration, vignetting removal |
| **Transform** | Perspective correction (guided upright) |
| **Effects** | Post-crop vignette, grain |
| **Calibration** | Camera profile and fine-tuning primary colors |

**Pro tips:**
- Use Auto to get a starting point, then refine manually
- Hold Alt/Option on sliders to see clipping previews
- Create virtual copies for different edit versions
- Use the Target Adjustment Tool (TAT) to drag on the image to adjust curves/HSL
- Sync settings across similar images for batch consistency

### 12.2 Adobe Photoshop

**Strengths:** Compositing, retouching, precise selections, text, effects, advanced manipulation

| Feature | Use Case |
|---|---|
| **Layers & Masks** | Non-destructive compositing and adjustments |
| **Adjustment Layers** | Curves, Levels, Hue/Sat, Color Balance, etc. without altering pixels |
| **Smart Objects** | Re-editable filters and transformations |
| **Content-Aware Fill/Remove** | AI-powered object removal |
| **Select Subject / Sky** | One-click AI selections for subjects and skies |
| **Neural Filters** | AI-powered skin smoothing, colorization, style transfer |
| **Camera Raw Filter** | Apply Lightroom-style adjustments as a filter |
| **Generative Fill / Expand** | AI-powered content generation (Adobe Firefly) |

### 12.3 Free & Open-Source Alternatives

| Tool | Platform | Comparable To | Best For |
|---|---|---|---|
| **GIMP** | Windows, Mac, Linux | Photoshop | Full-featured raster editing, retouching |
| **RawTherapee** | Windows, Mac, Linux | Lightroom (RAW processing) | Non-destructive RAW processing |
| **darktable** | Windows, Mac, Linux | Lightroom | RAW processing with catalog management |
| **Krita** | Windows, Mac, Linux | Photoshop (painting) | Digital painting and illustration |
| **Photopea** | Browser-based | Photoshop | Quick edits without installing software |
| **paint.net** | Windows | Photoshop (simplified) | Simple edits with layer support |

### 12.4 Mobile Editing Apps

| App | Platform | Strengths |
|---|---|---|
| **Lightroom Mobile** | iOS, Android | Full RAW processing, cloud sync with desktop |
| **Snapseed** | iOS, Android | Powerful free editor with selective adjustments |
| **VSCO** | iOS, Android | Excellent film-emulation presets |
| **Darkroom** | iOS | Native Apple RAW support, batch editing |
| **TouchRetouch** | iOS, Android | Object removal specialist |
| **Pixelmator Pro** | iOS, Mac | ML-powered editing, Apple-native |
| **Canva** | iOS, Android, Web | Templates, social media graphics, text overlays |

### 12.5 AI-Powered Tools

| Tool | Capability |
|---|---|
| **Topaz Photo AI** | All-in-one noise reduction, sharpening, upscaling using ML models |
| **Topaz Gigapixel** | AI-based image upscaling (up to 6x) |
| **DxO PureRAW** | RAW file denoising and lens correction before editing |
| **Luminar Neo** | AI-powered sky replacement, skin retouching, relighting, object removal |
| **Remove.bg** | Automatic background removal (web-based) |
| **Runway ML** | AI image generation, inpainting, video effects |
| **Adobe Firefly** | Generative fill, text-to-image, style transfer |

---

## 13. Quick Reference & Checklists

### 13.1 Keyboard Shortcuts (Common Across Tools)

| Action | Photoshop | Lightroom | GIMP |
|---|---|---|---|
| **Undo** | Ctrl/Cmd + Z | Ctrl/Cmd + Z | Ctrl/Cmd + Z |
| **Brush size increase** | ] | ] | ] |
| **Brush size decrease** | [ | [ | [ |
| **Zoom in** | Ctrl/Cmd + + | + / = | + |
| **Zoom to fit** | Ctrl/Cmd + 0 | Ctrl/Cmd + Shift + E | Shift + Ctrl + E |
| **Before/After** | \ (on adjustment) | \ | N/A |
| **Full screen** | F | F | F11 |
| **Clone stamp** | S | N/A | C |
| **Crop** | C | R | Shift + C |

### 13.2 Common Mistakes to Avoid

| Mistake | Why It's Bad | Fix |
|---|---|---|
| **Over-saturation** | Colors look neon and unnatural | Use Vibrance instead; keep adjustments subtle (+10 to +25) |
| **Over-sharpening** | Visible halos and crunchy texture | Sharpen at 100% zoom; use High Pass at low radius |
| **Heavy-handed HDR** | Flat, surreal, "crunchy" look | Use conservative tone mapping; blend with original |
| **Excessive clarity** | Skin looks textured and rough | Use Texture slider instead; reduce clarity on skin |
| **Ignoring white balance** | Unnatural color casts throughout | Always set WB first; use eyedropper on neutral gray |
| **Destructive editing** | Cannot undo or modify later | Use adjustment layers, Smart Objects, work on copies |
| **Crooked horizons** | Immediately noticeable distraction | Use auto-straighten or align to grid |
| **Inconsistent editing** | Series of images look like different photographers | Build and apply presets; sync settings across batch |
| **Editing on uncalibrated display** | Colors and exposure appear different on other screens | Calibrate with hardware colorimeter monthly |
| **Exporting at wrong size/format** | Poor quality or unnecessarily large files | Match resolution and format to intended output |

### 13.3 Enhancement Intensity Guide

| Adjustment | Subtle | Moderate | Strong | Danger Zone |
|---|---|---|---|---|
| **Exposure** | ±0.3 | ±0.7 | ±1.5 | ±2.0+ |
| **Contrast** | ±10 | ±25 | ±40 | ±60+ |
| **Highlights** | ±15 | ±40 | ±70 | ±100 |
| **Shadows** | ±15 | ±40 | ±70 | ±100 |
| **Clarity** | ±10 | ±25 | ±40 | ±60+ |
| **Vibrance** | ±10 | ±25 | ±40 | ±60+ |
| **Saturation** | ±5 | ±15 | ±25 | ±40+ |
| **Sharpening** | 30-50 | 60-90 | 100-150 | 150+ |
| **Noise Reduction** | 10-20 | 25-40 | 45-70 | 80+ |
| **Vignette** | -10 | -20 | -35 | -50+ |
| **Grain** | 10-15 | 20-35 | 40-60 | 70+ |

### 13.4 Image Appeal Diagnostic

If an image doesn't look "right," diagnose using this flowchart:

```
Image looks flat/dull?
├── Check contrast → Apply S-curve
├── Check clarity → Increase clarity +15 to +30
└── Check vibrance → Increase vibrance +15 to +25

Image looks too dark?
├── Increase exposure
├── Open shadows (+30 to +50)
└── Check blacks — lift if needed

Image looks washed out?
├── Increase contrast (+10 to +20)
├── Decrease highlights (-20 to -40)
├── Increase blacks (darken, pull left)
└── Add gentle vignette

Colors look off?
├── Fix white balance first
├── Check for color cast → use Curves per-channel
├── Check HSL — shift problematic hues
└── Ensure display is calibrated

Image looks noisy/grainy?
├── Apply noise reduction (Luminance 25-40)
├── Reduce exposure correction (noise increases with pushed shadows)
└── Consider AI denoise for best quality

Image looks soft/blurry?
├── Apply capture sharpening (Amount 40-80, Radius 1.0)
├── Try High Pass sharpening (radius 1-3, Overlay blend)
├── Check if camera shake — use Smart Sharpen with motion blur removal
└── If severely soft — likely a focus issue, limited recovery possible
```

### 13.5 Output Checklist

Before delivering any final image:

- [ ] Image meets the technical requirements (size, resolution, format, color space)
- [ ] No unwanted artifacts visible at 100% zoom
- [ ] Colors appear correct on a calibrated display
- [ ] Output sharpening applied for the target medium (screen vs. print)
- [ ] File size is appropriate (not unnecessarily large)
- [ ] Metadata is correct (copyright, keywords, description if needed)
- [ ] Working file (PSD/TIFF with layers) is saved separately for future edits
- [ ] Client or project naming convention is followed

---

## Disclaimer

This skill document is for **educational and reference purposes**. Image editing is both a technical craft and a creative art — rules and guidelines serve as starting points, not rigid constraints. Develop your own style through practice and experimentation. Always respect copyright, model releases, and ethical guidelines when editing and publishing images.
