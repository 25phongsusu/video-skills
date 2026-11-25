# Premium overlay system

Use this system for elegant real-estate, personal-brand, fashion, service, and high-value offer edits.

## “Someone” hero effect

Build the frame in five layers:

1. Base video.
2. Large filled hero word, such as **someone**, in Montserrat ExtraBold Italic with mustard `#D4B52C`.
3. Foreground subject matte, so the head and torso occlude the middle of the hero word.
4. Small white supporting phrase, such as **COULD BE**, placed near the hero word without touching the face.
5. Oversized transparent outline word, such as **CHOOSING**, spanning most of the frame width and crossing the lower torso.

Use a real foreground matte when practical. Generate or track a clean person mask and composite the original subject above the hero word. Limit this effect to one or two hero phrases per short video. If the matte is unreliable around hair or hands, place the word behind the stable torso region and avoid fast edges.

### Motion

- Reveal the filled word horizontally over 8–14 frames with `clip-path` or an animated mask.
- Begin 30–60 px off position with 2–5° skew; settle smoothly with `Easing.bezier(0.16, 1, 0.3, 1)`.
- Animate the foreground matte and base video identically so their edges never drift.
- Bring the white support phrase 3–6 frames later with a quiet fade and 15–25 px rise.
- Introduce the outline word last. Animate opacity, stroke reveal, and tracking over 8–12 frames.
- Add a reverse whoosh into the hero word, a soft impact on settle, and a low swipe for the outline.

### Typography treatment

- Hero word: 145–220 px at 1080×1920, ExtraBold Italic, tracking -3 to -8 px.
- Support phrase: 40–65 px, Regular or Medium, white.
- Outline word: 120–210 px, transparent fill, 1.5–3 px white or warm-gray stroke at 35–65% opacity.
- Add a restrained shadow to the mustard word: `0 5px 16px #0008`. Avoid strong yellow glow.
- Optional texture: apply 3–7% grain or a soft moving light pass inside the hero word.

## Premium phrase stacking

Use centered text stacks with relevant speech-synchronized illustrations by default, following the saved user defaults in SKILL.md. Use the asymmetric treatment below only when explicitly requested. Never add horizontal separator lines or underlines. For the optional asymmetric treatment, combine:

- a small white setup word;
- a large mustard italic keyword;
- a thin outline echo or synonym;
- one supporting white phrase aligned to the right edge of the hero word.

Let important words partially overlap the presenter’s silhouette. Keep eyes and mouth clear.

## Icons

Use clean SVG line icons in mustard or warm yellow with 6–12 px rounded strokes at 1080×1920. Match the subject: media player for editing, megaphone for marketing, message bubbles for social content, microphone for voice, home or location pin for property.

Animate icons with stroke drawing, short scale settle, and a faint shadow. One strong icon is better than several small icons. Do not use stock emoji.

## Reference assets

Use the bundled images only to understand hierarchy and layering:

- `../assets/reference-phrase-stack.png`: filled keyword plus outline support word.
- `../assets/reference-line-icon.png`: topic-matched mustard line icon beside the presenter.
- `../assets/reference-someone-overlay.png`: behind-subject hero word, white support phrase, and oversized outline layer.

Rebuild the visual treatment for the current footage and language. Do not copy names, logos, watermarks, or unrelated text from the references.
