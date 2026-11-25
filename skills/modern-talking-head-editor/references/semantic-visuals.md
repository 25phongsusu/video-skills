# Speech-synchronized illustrations

Build a separate cue list with `type`, `startMs`, and `endMs`; do not infer illustration timing from the whole phrase start.

| Spoken concept | Illustration |
| --- | --- |
| ChatGPT | Recognizable ChatGPT/OpenAI knot logo, in a clean app tile if useful |
| Another named product | Its verified logo or supplied product image |
| Ảnh / image / photo | Photo frame, landscape, or stacked image icon |
| Video / clip | Video player or play icon |
| Voice / microphone | Microphone or simple audio icon |
| No useful visual referent | Leave the visual area clear |

- Obtain named-product logos from an official asset or a reliable icon package. Preserve shape and proportions; do not invent a brand mark or imply an endorsement. Record asset sources locally. Use simple SVGs for generic media illustrations.
- Start each cue within 2–5 frames of the actual spoken noun. Verify ASR product spellings. For repeated mentions, cue again when useful. Let a cue remain long enough to recognize, usually 0.6–1.2 seconds, without intruding into an unrelated idea.
- At 1080×1920, prefer a readable 160–260 px logo/icon, or a 240–340 px illustration, over a tiny corner symbol. Place it in inspected negative space above or beside the head, with safe margins; retain the face and main text as the focal points.
- Use one illustration at a time. Fade and slide in over 6–10 frames, optionally with a small scale settle. Fade out over 3–5 frames. Keep all motion frame-driven.
- Keep the centered Montserrat text separate from the visual timeline. Text defaults to a vertical fade/blur entrance from below or above; use `opacity 0→1`, `translateY ±40→0`, and `blur 6–8→0`. Keep text scale fixed and preserve a crisp reading hold.
- Inspect the logo cue, image cue, video cue, and a mid-entrance text frame. Check face clearance over the full shot, not only at the beginning; lower the text when the speaker leans toward the camera.
