# Style system

## Choose a mode

| Mode | Use for | Accent | Character |
| --- | --- | --- | --- |
| Youthful tech | AI tools, tutorials, app reviews | Cyan `#A7EFFF` | Bright, clean, energetic |
| Premium editorial | Real estate, personal brand, fashion, luxury services | Mustard `#D4B52C` | Elegant, layered, cinematic |
| Premium hybrid | General talking head when the user asks for “sang” | Mustard + white with restrained cyan | Editorial hierarchy with modern motion |

Preserve the previously saved youthful tech system. Use premium hybrid as the default for requests that mention elegant text, overlay typography, “someone”, or attractive icons.

## Typography

| Role | Font | Weight | Typical size at 1080×1920 |
| --- | --- | --- | --- |
| Setup phrase | Montserrat Italic | 400 | 52–68 px |
| Main keyword | Montserrat Italic | 800 | 105–155 px |
| Small label | Montserrat | 400–800 | 34–48 px |
| Background outline | Montserrat | 400–800 | 115–200 px |

Keep tracking between -1 and -4 px for filled large words. Use neutral or slightly expanded tracking for outline words. Use tight line height around 1.1–1.25. Avoid all-caps for every phrase; reserve it for warnings, outlines, reveals, or final impact.

## Glow recipe

For a cyan keyword, start with:

```ts
textShadow: '0 3px 12px #0008, 0 0 16px #A7EFFF88, 0 0 38px #A7EFFF44'
```

Adjust the glow to remain subtle on bright backgrounds. Supporting white text can use `0 3px 12px #0009` plus a very faint white halo. For mustard editorial text, prefer a tight dark shadow and minimal warm glow so the letter edges remain sharp.

## Composition

- Default to centered phrase stacks: small white italic setup above the large glowing keyword, `left: 80px`, `right: 80px`, `textAlign: 'center'`, with both lines sharing the canvas center axis.
- Add one relevant speech-synchronized illustration by default when useful. Follow semantic-visuals.md for product logos and image/video cues. Do not add horizontal rules, underlines, separator bars, or unrelated decorations.
- Allow glow to extend beyond the glyphs without clipping it; use the cyan glow recipe above and keep edges sharp.

- Face: central, visually unobstructed.
- Large phrase: lower-middle, usually 55–72% of frame height.
- Graphic: upper-middle, usually 8–25% of frame height.
- Premium hero word: cross the subject at head or shoulder height and pass behind the foreground subject matte.
- Outline support word: span 65–95% of frame width and overlap the torso without reducing facial readability.
- TikTok safe area: keep key text inside 80 px side margins and away from the bottom interface region.

## Motion vocabulary

- Phrase entrance: slide vertically from +40 px (below) or -40 px (above), fade 0→1, blur 6–8 px→0 over 8–12 frames; keep scale at 1. Alternate direction by semantic beat.
- Phrase exit: fade out and continue vertical movement by 12–20 px over 3–5 frames, with a subtle blur if useful.
- Floating card: scale 0.7→1, rotate ±3–10°, then settle.
- Warning beat: quick scale 1.5→0.94→1 with coral accent.
- Reveal beat: layered cards slide inward, central icon rotates slightly, final keyword lands with a small flash.
- Editorial overlay: masked horizontal wipe, 10–25 px drift, small skew correction, then a quiet hold.
- Outline word: draw or fade its stroke while tracking narrows into the final position.
- Line icon: animate `strokeDashoffset`, then settle from scale 0.92 to 1 with a small rotation correction.

## SFX map

| Visual event | SFX | Mix guidance |
| --- | --- | --- |
| Small text switch | Click | Quiet, short |
| Card or keyword entrance | Whoosh | Light and airy |
| Warning/interruption | Whip + low hit | One strong event |
| Final reveal | Ding | Clean, short tail |
| Masked hero word | Reverse whoosh + soft impact | Airy lead-in, restrained landing |
| Outline draw | Swipe or pencil texture | Quiet, no sharp transient |
| Line icon | UI click or soft tick | Match the stroke completion |

Build SFX around the dialogue. If an effect masks consonants or makes the voice feel quieter, lower it.

## Avoid

- Heavy glow that softens letter edges
- Long sentences shown as a single block
- Text covering eyes, mouth, or key hand gestures
- Multiple competing graphics at once
- Repeating the same zoom strength on every phrase
- Using emoji when a clean vector icon is available
- Placing every word behind the subject; reserve depth masking for hero words
- Strong yellow glow that makes premium mustard text look neon
