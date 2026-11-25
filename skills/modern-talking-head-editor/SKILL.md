---
name: modern-talking-head-editor
description: 'Edit vertical talking-head videos in Remotion with a premium modern real-estate/reel style: Montserrat typography, short kinetic phrases, elegant mustard and white hierarchy, large outline overlays, the masked behind-subject someone text effect, subtle glow, line-art icons, punch-in camera movement, smooth transitions, and synchronized sound effects. Use for presenter, UGC, review, AI tutorial, sales, property, TikTok/Reels clips, or requests for phong cách clip mẫu, text sang, motion trẻ trung, real estate subtitles, dynamic typography, premium overlay, someone effect, Montserrat glow, or attractive icons.'
---

# Modern Talking Head Editor

Use Remotion to produce the finished MP4 and an editable project when requested.

## Saved user defaults: centered text, semantic visuals, and soft motion

- Center every phrase horizontally on the canvas: small white italic setup above the large Montserrat ExtraBold Italic keyword, around the lower chest (roughly 62–72% of frame height). Keep the face clear and both lines on the same center axis.
- Add relevant illustrations by default when the voice names a recognizable product, object, or medium: ChatGPT → recognizable ChatGPT logo; ảnh/image → image icon; video → video/play icon. Use one clear visual at a time and omit visuals for words without a useful illustration. Do not add unrelated decorations, separator bars, or underlines. Honor an explicit text-only request.
- Apply the saved subtle glow recipe to the hero text; keep the letters crisp. Use white setup text and cyan `#A7EFFF` for tech clips. Do not clip the glow with a tight mask or overflow container.
- Default text entrance: fade from transparent and softly blurred to crisp while moving gently up from below or down from above. Alternate direction by semantic beat, not randomly per word. Keep the centered axis and subtle glow. These defaults take precedence over optional asymmetric layouts, wipes, and scale effects below. Retain restrained SFX where requested.

## Workflow

1. Inspect the source with `ffprobe`, contact sheets, and representative frames. Preserve the real face, original footage, and original voice.
2. Transcribe or use supplied dialogue. Split it into short semantic beats of roughly 1–4 words. Keep full Vietnamese diacritics and exact spelling.
3. Build an independent visual cue timeline from word timestamps, following [references/semantic-visuals.md](references/semantic-visuals.md). Cue each relevant illustration at its spoken noun, not automatically at the start of its caption phrase. Build a 9:16 composition at 1080×1920 and the source frame rate unless the user specifies otherwise.
4. Load local Montserrat Regular and ExtraBold, normal and italic. Verify that bundled font files contain every Vietnamese glyph before rendering.
5. Choose the style mode from [references/style-system.md](references/style-system.md). Default to the premium hybrid mode when the user asks for a more elegant or expensive look.
6. Keep the presenter central. Place primary text around the lower chest area or other negative space. Place supporting graphics above or beside the head. Keep key content at least 80 px from the sides and 100 px from the top and bottom.
7. Animate text with frame-driven Remotion `interpolate()` or spring timing. Default to a vertical slide plus opacity and blur entrance; reserve masked wipe, scale, and tracking for optional emphasis. Use controlled punch-in zooms at major sentence beats.
8. Use behind-subject typography for one or two hero words when it adds emphasis. Create a foreground subject matte or tracked mask and place the word between the base video and foreground layer. Follow [references/premium-overlay-system.md](references/premium-overlay-system.md).
9. Synchronize sound effects to visual events. Use a light click for small text changes, airy whoosh for phrase reveals, soft impact for hero words, pen/swipe for outlines, and a clean ding for the final reveal. Keep speech clearly dominant.
10. Render representative stills from the opening, strongest emphasis, and ending. Include each illustration and a frame during the text entrance. Fix cue timing, overlap, overflow, face obstruction throughout head movement, weak contrast, weak depth separation, or excessive glow before rendering the full video.
11. Render H.264/AAC MP4. Verify dimensions, duration, decoding, and audio peaks. Save the editable Remotion project alongside the video when the user asks for reusable source files.

## Visual defaults

- Use Montserrat Regular/ExtraBold with italic emphasis.
- Use white plus either cyan `#A7EFFF` for the youthful tech mode or mustard `#D4B52C` for the premium editorial mode. Use coral `#FF856E` sparingly for warnings.
- Apply glow only to highlighted words: a tight colored glow plus a softer outer glow. Keep white supporting text mostly clean.
- Use a two- or three-level phrase: smaller regular setup line, large ExtraBold keyword, and optional oversized outline word behind or across the presenter.
- Use real-estate reel pacing: frequent phrase changes, clear hierarchy, smooth movement, and one focal idea per beat.
- Prefer clean topic-matched line icons with rounded strokes, waveforms, question marks, microphone symbols, media cards, or messaging symbols. Animate icon strokes or use a short scale settle. Avoid generic emoji and decorative clutter.
- Keep the original skin tone and footage color natural. Darken only the lower/background region needed for readability.

## Timing and motion

- Start a phrase within 2–5 frames of its spoken beat.
- Use 8–12 frames for the default fade entrance: opacity `0 → 1`, vertical offset `+40 → 0` px from below or `-40 → 0` px from above, and blur `6–8 → 0` px. Use 3–5 frames for a gentle fade-out with a small continuation of the motion. Shorten entrances for very short phrases so the crisp hold remains readable.
- Keep text scale at `1` for default fade/slide motion. If a special reveal uses scale, keep overshoot subtle; do not replace the requested fade with a popping zoom.
- Use `Easing.bezier(0.16, 1, 0.3, 1)` for smooth editorial movement.
- Use punch-in zoom changes around 2–8%; reserve larger zooms for one strong interruption or reveal.
- Let hero text travel behind the subject over 8–14 frames with a masked horizontal reveal, slight skew, and small tracking change. Hold long enough to read before introducing the outline support word.
- Never use CSS transitions or animations; all motion must be frame-driven for deterministic rendering.

## Captions

Store dialogue timing in Remotion Caption-compatible JSON:

```json
{"text":"Voice AI","startMs":1600,"endMs":2800,"timestampMs":null,"confidence":null}
```

Use the caption data to drive kinetic phrases. Do not display a second redundant subtitle layer unless the user asks for conventional subtitles.

## Sound

Create a single mixed SFX stem for predictable levels. Match one primary sound to each important text event instead of adding a sound to every word. Use licensed or permitted effects and document their sources in the project. Aim for no clipping; keep the finished peak below 0 dBFS and speech clearly intelligible.

## Quality bar

Read [references/style-system.md](references/style-system.md) when choosing typography, glow, text placement, motion, and SFX intensity. Read [references/premium-overlay-system.md](references/premium-overlay-system.md) for premium typography, subject masking, the “someone” overlay, and icon treatment. Treat references as a style direction rather than a frame-for-frame copy. Do not invent product names or claims that are absent from the dialogue.
