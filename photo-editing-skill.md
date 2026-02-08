# Photo Editing Skill

A comprehensive, automated photo editing skill. Upload your photos and this skill handles all the image processing — sharpening, toning, color grading, and bokeh (background blur) — so the subject stands out with professional-quality results.

---

## Table of Contents

1. [Overview & Philosophy](#1-overview--philosophy)
2. [Upload & Input Requirements](#2-upload--input-requirements)
3. [Auto-Detection & Scene Analysis](#3-auto-detection--scene-analysis)
4. [Sharpening](#4-sharpening)
5. [Toning & Color Grading](#5-toning--color-grading)
6. [Bokeh & Background Blur](#6-bokeh--background-blur)
7. [Exposure & Lighting Correction](#7-exposure--lighting-correction)
8. [Noise Reduction](#8-noise-reduction)
9. [Final Compositing & Output](#9-final-compositing--output)
10. [Processing Pipeline](#10-processing-pipeline)
11. [Presets & Styles](#11-presets--styles)
12. [Troubleshooting & Edge Cases](#12-troubleshooting--edge-cases)
13. [Technical Reference](#13-technical-reference)
14. [Tools & Libraries](#14-tools--libraries)

---

## 1. Overview & Philosophy

This skill is designed around one principle: **you upload, it edits**. No sliders, no manual adjustments, no learning curve. The system analyzes each photo, detects the subject, and applies a professional editing pipeline automatically.

### What It Does

| Step | Action | Goal |
|---|---|---|
| **1. Analyze** | Detect subject, scene type, lighting conditions | Understand the photo context |
| **2. Separate** | Isolate foreground subject from background | Prepare for selective editing |
| **3. Sharpen** | Apply intelligent sharpening to the subject | Crisp, detailed subject |
| **4. Tone** | Adjust color balance, grading, and mood | Professional color palette |
| **5. Bokeh** | Blur background with natural depth falloff | Subject pops, distractions fade |
| **6. Correct** | Fix exposure, white balance, noise | Clean, balanced final image |
| **7. Export** | Output in the desired format and resolution | Ready-to-use result |

### Design Principles

- **Non-destructive:** Original photo is never modified; all edits produce a new output
- **Subject-first:** Every adjustment prioritizes making the subject look its best
- **Natural results:** Effects are calibrated to look realistic, not over-processed
- **Batch-friendly:** Upload one photo or a hundred — the pipeline handles both

---

## 2. Upload & Input Requirements

### Supported Formats

| Format | Extension | Notes |
|---|---|---|
| JPEG | `.jpg`, `.jpeg` | Most common; lossy compression |
| PNG | `.png` | Lossless; supports transparency |
| TIFF | `.tif`, `.tiff` | High quality; large file size |
| WebP | `.webp` | Modern web format; good compression |
| HEIC/HEIF | `.heic`, `.heif` | Apple device default format |
| RAW Formats | `.cr2`, `.nef`, `.arw`, `.dng`, `.orf`, `.rw2` | Camera raw files; maximum editing flexibility |

### Input Guidelines

| Parameter | Recommendation |
|---|---|
| **Minimum resolution** | 800 x 600 pixels |
| **Maximum resolution** | 100 megapixels |
| **Color space** | sRGB, Adobe RGB, or ProPhoto RGB (auto-detected) |
| **Bit depth** | 8-bit or 16-bit per channel |
| **File size limit** | Up to 200 MB per image |

### RAW File Handling

When a RAW file is uploaded, the pipeline applies these pre-processing steps before the main edit:

1. **Demosaicing** — Convert Bayer pattern sensor data to full-color pixels
2. **White balance** — Apply camera-embedded or auto-detected white balance
3. **Lens correction** — Fix distortion, vignetting, and chromatic aberration using lens profiles
4. **Base tone curve** — Apply a standard tone curve to convert linear RAW data to a viewable image

---

## 3. Auto-Detection & Scene Analysis

Before any edits are applied, the system analyzes the uploaded photo to determine optimal settings.

### Subject Detection

The system identifies the primary subject using a combination of techniques:

| Method | What It Detects | Used For |
|---|---|---|
| **Semantic segmentation** | People, animals, objects, vehicles | Classifying subject type |
| **Saliency mapping** | Most visually prominent region | Finding the focal point |
| **Face detection** | Human faces, facial landmarks | Portrait-specific adjustments |
| **Depth estimation** | Relative depth of each pixel | Natural bokeh falloff |
| **Edge detection** | Sharp boundaries between subject and background | Precise masking |

### Scene Classification

| Scene Type | Characteristics | Editing Approach |
|---|---|---|
| **Portrait** | Face detected, person is primary subject | Skin-aware sharpening, warm toning, strong bokeh |
| **Group photo** | Multiple faces detected | Moderate bokeh, balanced sharpening across faces |
| **Pet/Animal** | Animal detected as primary subject | Fur-detail sharpening, natural toning, medium bokeh |
| **Street/Urban** | Architecture, vehicles, urban elements | Contrast-focused toning, selective bokeh |
| **Nature/Landscape** | Outdoor scene, no clear single subject | Vibrance toning, minimal bokeh, broad sharpening |
| **Product/Object** | Single object, clean background | Maximum sharpness, neutral toning, gradient bokeh |
| **Food** | Food items detected | Warm toning, texture sharpening, shallow bokeh |
| **Low light** | Dark scene, high ISO noise visible | Aggressive noise reduction before sharpening |

### Lighting Analysis

| Condition | Detection Method | Pipeline Adjustment |
|---|---|---|
| **Well-lit** | Histogram centered, low noise | Standard pipeline |
| **Overexposed** | Histogram clipped at highlights | Highlight recovery before toning |
| **Underexposed** | Histogram skewed left | Shadow lift, noise reduction first |
| **Backlit** | Subject darker than background | Local exposure compensation on subject |
| **Harsh shadows** | Bimodal histogram, strong edges in shadows | Shadow fill, reduced contrast |
| **Golden hour** | Warm color temperature, long shadows | Preserve warm tones, gentle enhancement |
| **Indoor/Artificial** | Mixed or non-daylight white balance | White balance correction, color cast removal |

---

## 4. Sharpening

Sharpening enhances fine detail and makes the subject appear crisp and well-defined. The skill applies sharpening selectively — strong on the subject, minimal or none on the background (which will be blurred anyway).

### Sharpening Methods

#### Unsharp Mask (USM)

The classic sharpening method. Despite the name, it sharpens by enhancing edge contrast.

```
Sharpened = Original + Amount x (Original - Blurred)

Parameters:
  Amount    = Strength of sharpening effect (50-200%)
  Radius    = Size of the detail to sharpen (0.5-3.0 pixels)
  Threshold = Minimum contrast difference to sharpen (0-10 levels)
```

| Parameter | Portrait | General | Product |
|---|---|---|---|
| Amount | 80-120% | 100-150% | 150-200% |
| Radius | 0.8-1.2 px | 1.0-2.0 px | 0.5-1.0 px |
| Threshold | 4-8 | 2-4 | 0-2 |

#### High-Pass Sharpening

Extracts and enhances only the fine details:

1. Duplicate the image layer
2. Apply Gaussian blur (radius 2-5 px) to the duplicate
3. Set blend mode to **Overlay** or **Soft Light**
4. Adjust opacity to control intensity (30-70%)

**Advantage:** More natural results than USM; less prone to halo artifacts.

#### Deconvolution Sharpening (Richardson-Lucy)

Reverses optical blur caused by the lens. Computationally intensive but produces the most natural sharpening.

```
Parameters:
  Iterations = Number of deconvolution passes (5-30)
  PSF radius  = Estimated point spread function of the lens (1-3 px)
```

Best for: RAW files, high-resolution images, recovering slightly out-of-focus shots.

### Subject-Selective Sharpening

The skill does NOT sharpen the entire image uniformly. Instead:

| Region | Sharpening Level | Reason |
|---|---|---|
| **Subject face** | High (with skin protection) | Eyes, eyebrows, lips should be crisp |
| **Subject body/clothing** | Medium-high | Texture and detail enhancement |
| **Subject edges** | High | Clean separation from background |
| **Background** | None | Will be blurred by bokeh step |
| **Transition zone** | Gradual falloff | Avoid abrupt sharpness boundary |

### Skin-Aware Sharpening (Portraits)

For portraits, sharpening must avoid amplifying skin texture and pores:

1. Detect skin regions using color-range masking (hue 0-50, saturation 20-70%)
2. Sharpen eyes, eyebrows, eyelashes, lips, and hair at full intensity
3. Apply sharpening to skin at 30-40% of the subject intensity
4. Use a larger radius (2-3 px) on skin to enhance structure without pore detail

### Sharpening Artifacts to Avoid

| Artifact | Cause | Prevention |
|---|---|---|
| **Halos** | Radius too large or amount too high | Keep radius under 2.0 px, use threshold |
| **Noise amplification** | Sharpening applied before noise reduction | Always denoise first, then sharpen |
| **Crunchy texture** | Over-sharpening skin or smooth surfaces | Use skin-aware masking |
| **Edge ringing** | Excessive deconvolution iterations | Limit to 15-20 iterations |

---

## 5. Toning & Color Grading

Toning transforms the mood and feel of the photo through color adjustments. The skill applies toning automatically based on the detected scene type.

### Color Correction (Pre-Toning)

Before creative toning, correct any color issues:

| Correction | Method | Goal |
|---|---|---|
| **White balance** | Analyze neutral areas; adjust temperature/tint | Remove color casts |
| **Exposure normalization** | Histogram analysis; adjust brightness/gamma | Proper exposure baseline |
| **Color cast removal** | Detect dominant unwanted hue; neutralize | Clean, accurate colors |

### Auto-Toning Profiles

Each scene type gets a tailored toning profile:

#### Portrait Toning

```
Adjustments:
  Temperature:    +5 to +15 (slightly warm)
  Tint:           +2 to +5 (slight magenta for skin warmth)
  Vibrance:       +10 to +20 (boost non-skin colors)
  Saturation:     -5 to +5 (keep skin natural)

Tone Curve:
  Shadows:        Lift slightly (raise black point to +5-10)
  Midtones:       Gentle S-curve for contrast
  Highlights:     Soft rolloff (compress highlights slightly)

Split Toning:
  Shadows:        Warm brown (Hue 30, Sat 10-15)
  Highlights:     Soft peach/gold (Hue 40, Sat 8-12)

HSL Adjustments:
  Orange hue:     Shift toward red by 5-10 (warmer skin)
  Orange sat:     Reduce by 10-15 (prevent orange skin)
  Luminance:      Boost orange/yellow +5-10 (bright, glowing skin)
```

#### Cinematic Toning

```
Adjustments:
  Temperature:    -5 to +5 (neutral to slightly cool)
  Contrast:       +15 to +25

Tone Curve:
  Shadows:        Crushed but lifted (black point at +10-15)
  Midtones:       Strong S-curve
  Highlights:     Rolled off

Split Toning:
  Shadows:        Teal/blue-green (Hue 190-210, Sat 15-25)
  Highlights:     Orange/warm (Hue 30-45, Sat 10-20)

HSL Adjustments:
  Aqua/Teal:      Boost saturation +15
  Orange:         Shift toward warm, boost luminance
```

#### Natural/Vivid Toning

```
Adjustments:
  Vibrance:       +15 to +30
  Saturation:     +5 to +10
  Clarity:        +10 to +20

Tone Curve:
  Gentle S-curve for contrast without crushing

HSL Adjustments:
  Greens:         Boost saturation +10, shift hue toward yellow
  Blues:           Boost saturation +10, deepen luminance -5
  Overall:        Enhance without oversaturating
```

#### Moody/Dark Toning

```
Adjustments:
  Exposure:       -0.3 to -0.7
  Contrast:       +20 to +30
  Blacks:         -10 to -20

Tone Curve:
  Shadows:        Deep with slight lift at absolute black
  Midtones:       Pull down for darker mood
  Highlights:     Compressed, muted

Split Toning:
  Shadows:        Deep blue or green (Hue 220-240, Sat 10-20)
  Highlights:     Desaturated warm (Hue 40, Sat 5-10)
```

### Color Harmony Principles

The toning engine follows these color theory rules:

| Principle | Application |
|---|---|
| **Complementary colors** | Teal shadows + orange highlights (most popular cinematic look) |
| **Analogous warmth** | Yellow-orange-red family for warm, inviting portraits |
| **Triadic balance** | Used sparingly for vibrant, editorial-style images |
| **Color dominance** | One dominant hue (60%), one supporting (30%), one accent (10%) |

### Skin Tone Protection

During toning, skin tones are protected to prevent unnatural results:

1. Detect skin-tone pixels (hue range 10-45, saturation 20-70%)
2. Apply toning adjustments at reduced intensity on skin (40-60% of full effect)
3. Constrain skin hue to the natural range (prevent green/blue skin casts)
4. Monitor skin luminance to prevent washed-out or overly dark skin

---

## 6. Bokeh & Background Blur

Bokeh creates a soft, creamy background blur that makes the subject the undisputed focal point. This simulates the shallow depth of field produced by wide-aperture lenses (f/1.4 - f/2.8).

### How the Bokeh Pipeline Works

```
Step 1: Subject Masking
  └── Generate a precise mask separating subject from background

Step 2: Depth Map Generation
  └── Estimate relative depth for every pixel in the image

Step 3: Blur Application
  └── Apply variable-strength blur based on depth distance from subject

Step 4: Bokeh Shape Rendering
  └── Shape specular highlights into natural bokeh circles/ovals

Step 5: Edge Refinement
  └── Blend subject edges naturally into the blurred background

Step 6: Light Bleed Simulation
  └── Add subtle background light bleeding onto subject edges
```

### Subject Masking Techniques

| Technique | Accuracy | Speed | Best For |
|---|---|---|---|
| **AI segmentation** (U-Net, DeepLab, SAM) | Very high | Medium | General subjects |
| **Trimap-based matting** | Highest | Slow | Fine details (hair, fur) |
| **Edge-aware matting** | High | Fast | Clean-edge subjects |
| **Depth-based separation** | Good | Fast | Clear foreground/background separation |

For best results, the skill uses a combination:
1. AI segmentation for the initial coarse mask
2. Trimap matting for hair and fine edge refinement
3. Depth estimation for natural blur falloff

### Depth-Dependent Blur

The blur intensity is NOT uniform across the entire background. It increases with distance from the subject's focal plane:

```
Blur Amount = Base Blur x (Depth Distance from Subject / Max Depth)^Falloff

Where:
  Base Blur          = Maximum blur radius (15-45 pixels at output resolution)
  Depth Distance     = Estimated depth difference from the subject plane
  Max Depth          = Maximum depth in the scene
  Falloff            = Curve exponent (1.0 = linear, 1.5 = gradual, 0.7 = aggressive)
```

| Depth Zone | Relative Distance | Blur Amount | Purpose |
|---|---|---|---|
| **Subject plane** | 0 | 0 px (sharp) | Keep subject crisp |
| **Near background** | 0.1-0.3 | 5-15 px | Gentle transition |
| **Mid background** | 0.3-0.6 | 15-30 px | Clear separation |
| **Far background** | 0.6-1.0 | 30-45 px | Fully diffused |
| **Foreground elements** | Varies | 5-20 px | Adds depth realism |

### Bokeh Shape & Quality

Real camera bokeh has specific optical characteristics that the skill simulates:

#### Highlight Rendering

Bright points in the background (lights, reflections, sun dapples) are rendered as **bokeh discs**:

| Property | Simulation | Real Lens Equivalent |
|---|---|---|
| **Shape** | Circular to slightly hexagonal | Determined by aperture blade count |
| **Edge** | Soft-edged with slight ring brightness | Determines "smooth" vs "busy" bokeh |
| **Size** | Proportional to brightness and depth distance | Wider aperture = larger discs |
| **Color fringing** | Subtle chromatic aberration on disc edges | Longitudinal CA in fast lenses |

#### Bokeh Styles

| Style | Character | Simulates |
|---|---|---|
| **Creamy** | Ultra-smooth, even blur | f/1.4 prime lens (85mm f/1.4) |
| **Swirly** | Slight rotation in peripheral bokeh | Vintage lenses (Helios 44-2) |
| **Dreamy** | Soft glow added to blur | Diffusion filter + wide aperture |
| **Natural** | Moderate blur with retained background context | f/2.8 zoom lens |

Default style: **Creamy** for portraits, **Natural** for other scenes.

### Edge Handling

The most critical part of convincing bokeh — where the sharp subject meets the blurred background:

| Technique | Purpose |
|---|---|
| **Alpha matting** | Sub-pixel accurate transparency at edges (hair, fur) |
| **Color decontamination** | Remove background color bleeding into edge pixels |
| **Feathered transition** | 2-5 pixel gradual transition from sharp to blurred |
| **Light wrapping** | Subtle background light wrapping onto subject edges for realism |

### Foreground Blur

For added depth realism, elements in front of the subject can also receive blur:

- Detect foreground elements using depth estimation
- Apply blur at 50-70% of the background blur intensity
- Use a slightly different blur character (more diffuse, less defined)

---

## 7. Exposure & Lighting Correction

Automatic exposure correction ensures the subject is properly lit regardless of the original shooting conditions.

### Exposure Analysis

```
Histogram Analysis:
  - Compute luminance histogram (256 bins)
  - Identify clipping: pixels at 0 (crushed blacks) or 255 (blown highlights)
  - Calculate mean luminance, standard deviation
  - Determine if image is under/over/properly exposed

Subject Exposure:
  - Compute average luminance of subject region only
  - Compare to ideal target (128 for midtones, higher for bright subjects)
  - Calculate required exposure compensation
```

### Correction Methods

| Condition | Correction | Parameters |
|---|---|---|
| **Underexposed subject** | Selective shadow lift on subject | Shadows +20 to +50, subject mask |
| **Overexposed subject** | Highlight recovery | Highlights -30 to -60, reconstruct from RAW if available |
| **Backlit subject** | Local exposure boost + background dim | +0.5 to +1.5 EV on subject |
| **Flat lighting** | Contrast enhancement | Gentle S-curve, clarity +10 to +20 |
| **Harsh contrast** | Shadow fill + highlight compress | HDR-style local tone mapping |

### White Balance Correction

| Method | How It Works | Accuracy |
|---|---|---|
| **Gray world assumption** | Assumes average of all pixels should be neutral gray | Good for diverse scenes |
| **White patch** | Finds brightest neutral area and uses it as white reference | Good when white areas exist |
| **Neural network** | AI-trained model predicts correct temperature/tint | Best overall accuracy |
| **Hybrid** | Combines all three with weighted average | Used by this skill |

### Local Adjustments

Beyond global corrections, the skill applies local adjustments:

- **Face brightening:** If faces are underexposed, apply a subtle radial gradient exposure boost centered on face regions
- **Eye brightening:** Gentle luminance boost on the iris area for catch-light enhancement
- **Shadow detail:** Lift shadows selectively in dark areas of the subject without affecting background
- **Highlight control:** Prevent specular highlights on skin from clipping

---

## 8. Noise Reduction

Noise reduction runs before sharpening to prevent amplifying grain and artifacts.

### Noise Types

| Type | Appearance | Cause | Reduction Method |
|---|---|---|---|
| **Luminance noise** | Grainy, film-like texture | High ISO, underexposure | Spatial denoising (NLM, BM3D) |
| **Chroma noise** | Random colored speckles | High ISO, long exposure | Chroma channel smoothing |
| **Banding** | Horizontal or vertical stripes | Sensor readout noise | Directional filtering |
| **Hot pixels** | Bright single-pixel dots | Sensor defects, long exposure | Median filter on isolated bright pixels |

### Noise Detection

```
Noise Level Estimation:
  1. Select flat/smooth regions of the image (low texture variance)
  2. Compute standard deviation of luminance in these regions
  3. Classify noise level:
     - σ < 3:   Clean (minimal denoising)
     - σ 3-8:   Light noise (gentle denoising)
     - σ 8-15:  Moderate noise (standard denoising)
     - σ > 15:  Heavy noise (aggressive denoising)
```

### Denoising Methods

#### Non-Local Means (NLM)

Averages similar patches across the image. Preserves edges well but can smear fine textures at high strengths.

```
Parameters:
  Filter strength:  Proportional to estimated noise level (5-30)
  Patch size:       5x5 or 7x7 pixels
  Search window:    21x21 pixels
```

#### AI-Based Denoising

Neural network models trained on millions of noisy/clean image pairs. Produces the best quality-to-detail-retention ratio.

| Model Approach | Strength | Weakness |
|---|---|---|
| **Blind denoising** | No noise level input needed | Slightly less optimal than guided |
| **Guided denoising** | Uses estimated noise level for precision | Requires accurate noise estimation |
| **RAW denoising** | Operates on linear RAW data before tone curve | Best possible quality; RAW files only |

### Subject-Aware Denoising

| Region | Denoising Intensity | Reason |
|---|---|---|
| **Skin** | High | Smooth, clean skin is expected |
| **Eyes, hair** | Low | Preserve fine detail |
| **Clothing/texture** | Medium | Balance between smooth and detailed |
| **Background** | Maximum | Will be blurred anyway; remove all noise |

---

## 9. Final Compositing & Output

After all processing steps, the final image is composited and exported.

### Compositing Order

```
1. Noise-reduced subject layer        (sharp, clean)
2. Sharpened subject layer             (detail-enhanced)
3. Toned subject layer                 (color-graded)
4. Exposure-corrected subject layer    (properly lit)
5. Bokeh-blurred background layer      (depth-blurred)
6. Toned background layer              (color-graded to match subject)
7. Edge blend layer                    (feathered transition)
8. Final adjustments layer             (global fine-tuning)
```

### Global Fine-Tuning

Applied to the entire composited image:

| Adjustment | Range | Purpose |
|---|---|---|
| **Micro-contrast** | +5 to +15 | Adds definition without harsh edges |
| **Vignette** | -5 to -20 (subtle) | Draws eye toward center/subject |
| **Grain** | 0-10 (optional) | Adds film-like character if desired |
| **Final saturation check** | Clip prevention | Ensure no channel clips at 0 or 255 |

### Output Formats

| Format | Quality | File Size | Best For |
|---|---|---|---|
| **JPEG (95%)** | High | Medium | Social media, web, sharing |
| **JPEG (85%)** | Good | Small | Quick sharing, messaging apps |
| **PNG** | Lossless | Large | When transparency or max quality needed |
| **TIFF (16-bit)** | Maximum | Very large | Further professional editing |
| **WebP (90%)** | High | Small | Web publishing, optimized delivery |

### Resolution & Sizing

| Output Preset | Max Dimension | Use Case |
|---|---|---|
| **Original** | Same as input | Full-quality archive |
| **Print** | 300 DPI at target print size | Physical printing |
| **Web** | 2048 px long edge | Website display |
| **Social** | 1080 px (Instagram), 1200 px (Facebook/X) | Social media posting |
| **Thumbnail** | 400 px long edge | Preview, gallery grids |

### Metadata Handling

| Metadata Type | Default Behavior |
|---|---|
| **EXIF (camera settings)** | Preserved |
| **IPTC (copyright, caption)** | Preserved |
| **GPS/Location** | Stripped for privacy |
| **Edit history** | Embedded as XMP sidecar data |
| **Color profile** | Converted to sRGB for web; preserved for print |

---

## 10. Processing Pipeline

The complete automated pipeline from upload to output:

```
┌─────────────────────────────────────────────────────────────────┐
│                        PHOTO UPLOAD                             │
│                   (JPEG, PNG, RAW, etc.)                        │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  STAGE 1: ANALYSIS                                              │
│  ├── Format detection & RAW decoding (if applicable)            │
│  ├── Scene classification (portrait, street, nature, etc.)      │
│  ├── Subject detection & segmentation                           │
│  ├── Depth map estimation                                       │
│  ├── Lighting condition analysis                                │
│  ├── Noise level estimation                                     │
│  └── Select processing profile based on analysis                │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  STAGE 2: CORRECTION                                            │
│  ├── White balance correction                                   │
│  ├── Exposure normalization                                     │
│  ├── Lens distortion correction (if lens data available)        │
│  ├── Chromatic aberration removal                               │
│  └── Noise reduction (luminance + chroma)                       │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  STAGE 3: SUBJECT PROCESSING                                    │
│  ├── Generate refined subject mask (AI + matting)                │
│  ├── Apply subject-selective sharpening                          │
│  │   ├── Skin-aware sharpening for portraits                    │
│  │   └── Detail-preserving sharpening for other subjects        │
│  ├── Local exposure correction on subject                       │
│  └── Face/eye enhancement (if portrait)                         │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  STAGE 4: BACKGROUND PROCESSING                                 │
│  ├── Apply depth-dependent bokeh blur                           │
│  │   ├── Variable blur radius based on depth map                │
│  │   ├── Bokeh disc rendering for specular highlights           │
│  │   └── Foreground blur (if foreground elements detected)      │
│  ├── Edge blending (alpha matting + color decontamination)       │
│  └── Light wrap simulation                                      │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  STAGE 5: TONING & COLOR GRADING                                │
│  ├── Apply scene-appropriate toning profile                     │
│  │   ├── Tone curve adjustment                                  │
│  │   ├── Split toning (shadow/highlight color)                  │
│  │   └── HSL adjustments                                        │
│  ├── Skin tone protection (portrait mode)                       │
│  ├── Vibrance & saturation tuning                               │
│  └── Color harmony verification                                 │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│  STAGE 6: FINAL COMPOSITING                                     │
│  ├── Merge all layers (subject + background + adjustments)      │
│  ├── Apply micro-contrast enhancement                           │
│  ├── Add subtle vignette                                        │
│  ├── Final clipping/gamut check                                 │
│  ├── Resize to target output dimensions                         │
│  ├── Apply output sharpening (for target medium)                │
│  └── Export in selected format with metadata                    │
└─────────────────────┬───────────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────────┐
│                     EDITED PHOTO OUTPUT                          │
│               (Ready to share, print, or archive)               │
└─────────────────────────────────────────────────────────────────┘
```

### Pipeline Timing (Approximate)

| Stage | Processing Time | Notes |
|---|---|---|
| Analysis | Fast | AI inference for segmentation is the bottleneck |
| Correction | Fast | Pixel-level math operations |
| Subject Processing | Medium | Mask refinement and selective sharpening |
| Background Processing | Medium-Slow | Bokeh blur is computationally intensive |
| Toning | Fast | Color LUT application |
| Final Compositing | Fast | Layer merge and export |

---

## 11. Presets & Styles

Pre-configured editing styles that can be applied as the default or selected per batch.

### Portrait Presets

| Preset | Tone | Bokeh | Sharpening | Best For |
|---|---|---|---|---|
| **Classic Portrait** | Warm, soft contrast | Strong creamy | Skin-aware, moderate | Professional headshots |
| **Editorial** | High contrast, desaturated | Medium | Strong detail | Fashion, magazine-style |
| **Bright & Airy** | Lifted shadows, bright | Light | Gentle | Lifestyle, family photos |
| **Moody Portrait** | Dark, cool shadows | Strong | High on eyes | Dramatic, artistic portraits |
| **Film Emulation** | Faded blacks, color shift | Medium | Soft | Vintage, analog feel |

### General Presets

| Preset | Tone | Bokeh | Sharpening | Best For |
|---|---|---|---|---|
| **Auto (Default)** | Scene-adaptive | Scene-adaptive | Scene-adaptive | General use |
| **Vibrant** | High saturation, punchy | Light | High | Social media, landscapes |
| **Clean & Minimal** | Neutral, slight contrast | None | Moderate | Product photos, documentation |
| **Cinematic** | Teal & orange, crushed blacks | Medium | High | Storytelling, atmospheric shots |
| **Black & White** | Monochrome, rich tones | Optional | High | Artistic, timeless |
| **HDR Natural** | Full dynamic range, vivid | None | High | Architecture, real estate |

### Custom Preset Parameters

For advanced users creating their own presets:

```
Preset Configuration:
{
  "name": "My Custom Style",
  "sharpening": {
    "method": "unsharp_mask",
    "amount": 120,
    "radius": 1.2,
    "threshold": 3,
    "skin_protection": true
  },
  "toning": {
    "temperature": +10,
    "tint": +3,
    "vibrance": +15,
    "saturation": +5,
    "tone_curve": "gentle_s",
    "split_tone_shadows": {"hue": 30, "saturation": 12},
    "split_tone_highlights": {"hue": 45, "saturation": 8}
  },
  "bokeh": {
    "style": "creamy",
    "base_blur_radius": 35,
    "falloff": 1.2,
    "highlight_rendering": true,
    "foreground_blur": true,
    "edge_feather": 3
  },
  "output": {
    "format": "jpeg",
    "quality": 95,
    "resize": "original",
    "color_profile": "srgb"
  }
}
```

---

## 12. Troubleshooting & Edge Cases

### Common Issues and Solutions

| Issue | Cause | Solution |
|---|---|---|
| **Subject partially blurred** | Incorrect mask boundary | System re-runs segmentation with trimap refinement |
| **Background not fully blurred** | Subject and background at similar depth | Increase base blur radius; use edge-detection fallback |
| **Unnatural skin tones after toning** | Toning profile too aggressive on skin | Increase skin protection mask strength |
| **Halo around subject edges** | Over-sharpening at boundaries | Reduce sharpening in transition zone |
| **Bokeh looks artificial** | Uniform blur without depth variation | Enable depth-dependent falloff; adjust falloff curve |
| **Over-saturated result** | Toning profile too vibrant for the scene | Reduce vibrance/saturation; switch to a subtler preset |
| **Dark subject after bokeh** | Background was brighter; blur changed overall luminance | Apply exposure compensation to maintain subject brightness |
| **Hair/fur edges look cut out** | Hard mask boundary | Enable alpha matting for fine edge details |

### Challenging Scenarios

| Scenario | Challenge | Approach |
|---|---|---|
| **Multiple subjects at different depths** | Which depth plane to keep sharp? | Keep all detected subjects sharp; blur beyond the furthest subject |
| **Subject wearing glasses** | Reflections can confuse masking | Apply reflection-aware masking; preserve glass transparency |
| **Busy patterned background** | Pattern may show through blur | Increase blur radius; apply content-aware fill on artifacts |
| **Very low resolution input** | Limited detail to work with | Reduce sharpening to avoid artifacts; apply AI upscaling first |
| **Transparent or semi-transparent subject elements** | Veils, glass, smoke | Use trimap matting with transparency preservation |
| **Subject merging with background color** | Similar colors make separation hard | Use depth estimation as primary separator instead of color |

---

## 13. Technical Reference

### Color Space Operations

All internal processing is done in **linear light** (gamma 1.0) for mathematically correct blending:

```
Input → Linearize (remove gamma) → Process → Apply gamma → Output

sRGB gamma:
  Linear = sRGB / 12.92                     (if sRGB <= 0.04045)
  Linear = ((sRGB + 0.055) / 1.055)^2.4     (if sRGB > 0.04045)
```

### Blur Kernel Reference

| Kernel Type | Shape | Bokeh Quality | Performance |
|---|---|---|---|
| **Gaussian** | Bell curve | Smooth but unrealistic | Fast |
| **Disc (pillbox)** | Flat circle | Most realistic bokeh | Medium |
| **Hexagonal** | 6-sided polygon | Simulates 6-blade aperture | Medium |
| **Custom PSF** | Lens-specific shape | Highest realism | Slow |

The skill defaults to **disc kernel** for bokeh and **Gaussian kernel** for general blur operations.

### Mask Refinement Formula

The transition between sharp subject and blurred background uses a sigmoid-based feathering:

```
Alpha(d) = 1 / (1 + exp(-k * (d - d_edge)))

Where:
  d       = distance from mask boundary (pixels)
  d_edge  = mask boundary position
  k       = steepness factor (higher = sharper transition)
           Portrait: k = 2-3 (softer blend)
           Product:  k = 5-8 (sharper cutout)
```

### Key Formulas Summary

```
Unsharp Mask:       S = O + A * (O - G(O, r))
High-Pass:          HP = O - G(O, r), then blend in Overlay mode
Depth Blur:         B(x,y) = B_max * (D(x,y) - D_subject) / D_max)^f
Bokeh Disc Size:    s = |f^2 / (N * (d_focus - d_point))| * sensor_scale
Noise Estimate:     σ = stddev(flat_region_luminance)
Exposure Comp:      EV_adj = log2(target_luminance / subject_luminance)
Skin Hue Range:     H: 10-45°, S: 20-70%, L: 30-80%
```

---

## 14. Tools & Libraries

### Recommended Implementation Stack

| Layer | Tool/Library | Purpose |
|---|---|---|
| **Core image processing** | OpenCV, Pillow (PIL) | Pixel manipulation, filters, format I/O |
| **AI segmentation** | Segment Anything (SAM), DeepLabV3+, U2-Net | Subject detection and masking |
| **Depth estimation** | MiDaS, DPT (Dense Prediction Transformer) | Monocular depth prediction |
| **Face detection** | MediaPipe Face Mesh, dlib, RetinaFace | Facial landmark detection |
| **Noise reduction** | OpenCV fastNlMeansDenoising, Restormer | Spatial denoising |
| **RAW processing** | rawpy (LibRaw), darktable-cli | RAW file decoding and development |
| **Color science** | colour-science (Python) | Color space conversions, gamut mapping |
| **GPU acceleration** | CUDA, OpenCL, Metal (via PyTorch/TensorFlow) | Real-time AI inference and blur |
| **Batch processing** | Python multiprocessing, Celery | Parallel image processing |

### Python Quick-Start Example

```python
# Minimal pipeline example using common libraries
import cv2
import numpy as np
from PIL import Image

def auto_edit_photo(input_path, output_path):
    """
    Simplified auto-edit pipeline.
    Production implementation would use AI models for segmentation and depth.
    """
    # Load image
    img = cv2.imread(input_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Step 1: Subject segmentation (placeholder — use SAM or DeepLab in production)
    subject_mask = detect_subject(img_rgb)

    # Step 2: Depth estimation (placeholder — use MiDaS in production)
    depth_map = estimate_depth(img_rgb)

    # Step 3: Noise reduction
    denoised = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

    # Step 4: Sharpening (unsharp mask on subject only)
    blurred = cv2.GaussianBlur(denoised, (0, 0), 1.5)
    sharpened = cv2.addWeighted(denoised, 1.5, blurred, -0.5, 0)
    sharpened = apply_with_mask(denoised, sharpened, subject_mask)

    # Step 5: Bokeh (depth-dependent blur on background)
    bokeh_bg = apply_depth_blur(sharpened, depth_map, subject_mask, max_radius=35)

    # Step 6: Toning (warm portrait tone)
    toned = apply_toning(bokeh_bg, temperature=+10, vibrance=+15)

    # Step 7: Export
    output = cv2.cvtColor(toned, cv2.COLOR_RGB2BGR)
    cv2.imwrite(output_path, output, [cv2.IMWRITE_JPEG_QUALITY, 95])

def apply_with_mask(original, edited, mask):
    """Blend edited result with original using a mask."""
    mask_3ch = np.stack([mask] * 3, axis=-1).astype(np.float32) / 255.0
    return (edited * mask_3ch + original * (1 - mask_3ch)).astype(np.uint8)

def apply_depth_blur(img, depth_map, subject_mask, max_radius=35):
    """Apply variable Gaussian blur based on depth distance from subject."""
    result = img.copy()
    subject_depth = np.mean(depth_map[subject_mask > 128])

    for radius in range(5, max_radius + 1, 5):
        depth_threshold = (radius / max_radius)
        blur_mask = (np.abs(depth_map - subject_depth) > depth_threshold * 255)
        blur_mask = blur_mask & (subject_mask < 128)

        blurred = cv2.GaussianBlur(img, (0, 0), radius)
        mask_3ch = np.stack([blur_mask] * 3, axis=-1).astype(np.float32)
        result = (blurred * mask_3ch + result * (1 - mask_3ch)).astype(np.uint8)

    return result

def apply_toning(img, temperature=0, vibrance=0):
    """Apply basic color toning adjustments."""
    result = img.astype(np.float32)

    # Temperature: shift blue-yellow balance
    if temperature > 0:
        result[:, :, 0] = np.clip(result[:, :, 0] + temperature * 0.5, 0, 255)  # R
        result[:, :, 2] = np.clip(result[:, :, 2] - temperature * 0.3, 0, 255)  # B

    # Vibrance: boost low-saturation colors more than high-saturation
    hsv = cv2.cvtColor(result.astype(np.uint8), cv2.COLOR_RGB2HSV).astype(np.float32)
    saturation = hsv[:, :, 1] / 255.0
    boost = vibrance * (1.0 - saturation)  # Less saturated pixels get more boost
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] + boost, 0, 255)
    result = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2RGB).astype(np.float32)

    return result.astype(np.uint8)
```

### CLI Usage Pattern

```bash
# Single photo
photo-edit input.jpg --output edited.jpg

# Batch processing
photo-edit ./photos/ --output ./edited/ --preset "classic_portrait"

# Custom settings
photo-edit input.jpg \
  --bokeh-strength 0.8 \
  --sharpen-amount 120 \
  --tone-preset cinematic \
  --output-format png \
  --output edited.png

# RAW file with full pipeline
photo-edit photo.CR2 --output photo_edited.tiff --output-bit-depth 16
```

---

## Disclaimer

This skill document describes an automated photo editing pipeline for personal and creative use. Results depend on input image quality and subject clarity. Always keep your original files — edits are non-destructive by design but the exported output is a separate file. For commercial or print use, review automated results and adjust as needed.
