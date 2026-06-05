# Finding an organisation's house style

Read this when you need to locate and extract a Dutch organisation's huisstijl, or work out what to ask for when none is published. It also walks the Gemeente Amsterdam example end to end.

## Where Dutch government house styles live

Search in roughly this order:

1. **An existing NLDS theme** — NL Design System Themes Storybook, the `nl-design-system/themes` repo, and (for central government) the Rijkshuisstijl Community. An official theme is the most authoritative and least error-prone source. See `references/nl-design-system.md`.
2. **The organisation's own brand pages** — search for `<organisation> huisstijl`, `<organisation> stijlgids`, `<organisation> merkbeleid`, `<organisation> design system`, or `<organisation> brand guidelines`. Larger municipalities and ministries publish a living style guide.
3. **developer.overheid.nl** — sometimes links an organisation's front-end/design-system resources.

Prefer official, current sources. A Pinterest board, an old logo on a third-party site, or a marketing agency's case study is **not** an authoritative source — note the distinction when you report what you found.

## What to extract

- **Colours** — primary, secondary/accent, and a neutral palette (background, surface, border, text). Capture exact hex values and, where stated, which colour is used for what (don't assume the brightest colour is the text colour).
- **Typography** — heading and body font families, weights, and crucially **how to obtain the font legally** (many government fonts are licensed and only available to suppliers on request). Record a sensible fallback stack.
- **Logo** — the official asset (SVG if available), plus usage rules: clear space, minimum size, allowed variants, what you may *not* do to it.
- **Spacing / shape** — border-radius and spacing conventions if specified; they carry a lot of the "feel".
- **Variants** — any dark-mode or high-contrast version.

## Worked example: Gemeente Amsterdam

- **Living style guide:** Stijlweb — https://www.amsterdam.nl/stijlweb/ (the single, maintained source for Amsterdam's house style).
- **Online brand policy:** https://www.amsterdam.nl/digitalservices/online-beleid/merkbeleid/ — states that all departments use the same logo and house style, and that the city communicates via one website (Amsterdam.nl). The design-system rules for online media live here.
- **Handboek Huisstijl:** https://www.amsterdam.nl/handboekhuisstijl/ — detailed layout and design rules (logo bar, placement grid based on the crosses, etc.).
- **Typeface:** **Amsterdam Sans** — a bespoke face by Bold Monday with Thonik, successor to Avenir, optimised for digital. Suppliers download it from the typeface page on Stijlweb (licensed — don't self-host without the right to).
- **Core colours:** **Amsterdam red** and **black** (the red plus the three St Andrew's crosses / Andreaskruisen from the city's coat of arms are the heart of the identity).
- **Logo:** the three Andreaskruisen with the wordmark; the handbook specifies the exact variant and placement grid. Use the official asset; never recreate it.
- **NLDS:** Amsterdam is one of the organisations NLDS components are actively built for, so check for an Amsterdam theme/tokens before deriving your own.

Note how the example reinforces the rules: the colours and crosses are protected identity, the font is licensed (download via the official page, don't recreate), and the authoritative source is one maintained style guide — not whatever a web search surfaces first.

## When nothing is published

Ask the developer for the checklist in `SKILL.md` ("What to ask for when nothing is published"): logo files, primary/secondary colours, neutral palette, heading/body fonts (and where to obtain them), spacing/radius feel, and any dark/high-contrast variant. If the organisation is small and genuinely has no house style and is not bound to a government identity, you may propose a neutral, accessible default — but say clearly that it is a proposed default, not the organisation's official brand.

## Confirmation discipline

Whatever you find, present it back before applying: the source URL, the colours, the font, the logo. Get an explicit yes. Brand values pulled from the web are often outdated or unofficial, and a government interface wearing the wrong identity is a trust problem. Never fabricate values to fill a gap — ask instead.

## Sources

- Gemeente Amsterdam — Stijlweb: https://www.amsterdam.nl/stijlweb/
- Gemeente Amsterdam — online merkbeleid: https://www.amsterdam.nl/digitalservices/online-beleid/merkbeleid/
- Gemeente Amsterdam — Handboek Huisstijl: https://www.amsterdam.nl/handboekhuisstijl/
- NL Design System: https://nldesignsystem.nl/
- NLDS themes: https://github.com/nl-design-system/themes
