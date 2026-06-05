---
name: organisatie-huisstijl
description: "Use this skill whenever you are building or styling a user-facing surface of a digital assistant for a specific organisation and need to apply that organisation's house style / corporate identity — its colours, typography, and logo. This is the skill that makes a chatbot or web app built for, say, the Gemeente Amsterdam actually look like Amsterdam: it first tries to find the organisation's official house style (preferring an existing NL Design System theme, then the organisation's own brand/style guide) and otherwise asks the developer to provide it, then expresses it as design tokens. Triggers include 'huisstijl', 'house style', 'corporate identity', 'branding', 'brand', 'logo', 'kleuren', 'colours', 'lettertype', 'font', 'design tokens', 'NL Design System', 'NLDS', 'make it look like <organisation>', 'in de stijl van <gemeente/organisatie>', or any UI work tied to a named government body or organisation, even when styling is not requested explicitly. Do NOT use this skill for backend, API, data, model, or infrastructure work that has no user-facing surface."
---

# Organisation house style for assistant interfaces

A digital assistant for a public body should look and feel like that body — citizens trust an interface that visibly belongs to their municipality or agency, and an off-brand one reads as untrustworthy or even fake. This skill applies an organisation's **house style (huisstijl)**: its colours, typography, logo, and spacing. For Dutch government the right vehicle is the **NL Design System (NLDS)**: white-label, accessibility-tested components that you theme per organisation with **design tokens**. This skill finds the organisation's house style (or asks for it) and expresses it as those tokens, then wires the interface to consume them.

## First: does this apply, and to which organisation?

Apply this skill only when your work produces a user-facing surface (chat/chatbot UI, web app, web page, form, rendered email, citizen-facing document). If there is no UI — backend, API, data pipeline, model/prompt, infrastructure — there is nothing to brand; skip it.

You also need to know **which** organisation the assistant is for. If the surface is user-facing but no organisation is named, ask one question first: *"Which organisation is this assistant for? I'll match its house style."* Don't guess, and don't quietly apply a generic look — getting the wrong municipality's identity onto a government service is worse than asking.

## Prefer the NL Design System

Don't restyle components by hand. NLDS components are **white-label and already tested for accessibility**, and they take an organisation's identity purely through a three-layer token model — **Brand → Common → Component**. You supply the organisation's *Brand* tokens (its raw colours and fonts), link them to the *Common* (semantic) tokens, and the whole interface — buttons, forms, navigation — adapts automatically. Building on NLDS inherits its accessibility work and removes whole classes of bespoke-styling bugs (this is also why the `wcag-accessibility` skill recommends NLDS). Read `references/nl-design-system.md` for the token model, where themes live, how to build one, and the licensing rules.

## Find the house style — a ladder, best source first

Work top-down and stop at the first rung that yields an **authoritative** result. Whatever rung you land on, you must confirm before applying (see below).

1. **An existing NLDS theme for this organisation.** Check the NL Design System Themes Storybook and the `nl-design-system/themes` repository — and, for central government, the Rijkshuisstijl Community. If an official theme exists, use its design tokens directly: it is authoritative, maintained, and already accessibility-aware. This is the best outcome — don't reinvent a theme that already exists.
2. **The organisation's own brand / style guide.** Find its official *huisstijl* / *stijlgids* / *merkbeleid* and extract: primary and secondary colours (as hex), typography (font families and how to obtain them), the official logo (the asset itself plus its usage rules), and any spacing or border-radius conventions. (Worked example: Gemeente Amsterdam's living style guide is **Stijlweb**; its typeface is **Amsterdam Sans** and its core colours are **Amsterdam red and black**. See `references/finding-house-styles.md`.)
3. **Ask the developer.** If neither yields a reliable source, ask them to provide it — give the concrete checklist below.

**Always show what you found and get explicit confirmation before applying it** — the source URL, the colours, the font, the logo. Scraped or inferred brand values are frequently wrong, outdated, or from an unofficial page, and applying them silently risks shipping the wrong brand or breaching brand policy. If you cannot browse the web in this environment, skip straight to asking the developer; never fabricate brand values to fill the gap.

## What to ask for when nothing is published

If there is no usable published house style, ask the developer for:

- the **logo** as official files (SVG preferred), with any clear-space and usage rules;
- the **primary** and **secondary/accent** colours as hex;
- a **neutral / background** palette (surfaces, borders, text);
- the **font family** for headings and for body text — and where to obtain it legally (many government fonts are licensed, supplier-download only);
- the **border-radius / spacing** feel (sharp and formal, or soft and rounded);
- any **dark-mode** or **high-contrast** variant they need.

Then build the theme from those values.

## Express it as design tokens, never hard-coded values

Emit a token file (start from `templates/theme-tokens.css.template`): put the organisation's raw values in Brand tokens, then link them to the NLDS Common tokens so every component picks them up. Tokens keep the brand swappable, consistent across the whole interface, and themeable (light / dark / high-contrast); hard-coding `#EC0000` in fifty places is unmaintainable and drifts out of sync. After generating the tokens, **wire the interface to consume them** — don't leave a token file the components never read.

Reference the real logo and font from their official source; do not recreate or approximate them in code (see IP, below).

## Respect intellectual property and brand policy

This is a legal and reputational matter, not a style preference:

- **Don't reuse another organisation's theme, tokens, or styled components as-is** for a different organisation — that needs the maker's permission (for example, Utrecht's design system is copyrighted, and an Amsterdam-styled component will make your site look like Amsterdam). Build the *target* organisation's own theme.
- **Logos and custom fonts are protected and licensed.** Don't embed a logo or self-host a licensed font (e.g. Amsterdam Sans) unless the developer confirms they have the right to use it; point them to the official source instead (for Amsterdam, the typeface page on Stijlweb).
- **Never recreate a logo with code or generate a look-alike.** Use the official asset only.
- The NLDS components themselves are open source (EUPL 1.2); the *house style applied to them* is the organisation's intellectual property.

## Accessibility outranks brand exactness

A brand colour still has to be legible. Run a contrast check on every brand foreground/background and UI pair — the companion `wcag-accessibility` skill bundles `scripts/check_contrast.py` for exactly this. If a brand pair fails WCAG AA, **accessibility wins**: pick an accessible token from the organisation's palette, or derive an accessible variant of the brand colour, and tell the developer about the adjustment. A perfectly on-brand button that nobody can read is a failure, not a brand win. See the `wcag-accessibility` skill for the full standard.

## Sources

- NL Design System: https://nldesignsystem.nl/
- NL Design System — design tokens (handbook): https://nldesignsystem.nl/handboek/huisstijl/design-tokens/
- NLDS themes (existing organisation themes): https://github.com/nl-design-system/themes
- Rijkshuisstijl Community (central government): https://github.com/nl-design-system/rijkshuisstijl-community
- NL Design System on developer.overheid.nl: https://developer.overheid.nl/kennisbank/front-end/nl-design-system/
- Gemeente Amsterdam — Stijlweb (living style guide): https://www.amsterdam.nl/stijlweb/
