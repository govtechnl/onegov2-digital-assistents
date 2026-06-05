# NL Design System (NLDS) — how theming works

Read this when applying a house style via NLDS: it explains the token model, where to find existing themes, how to build one, and the licensing rules you must respect.

## What NLDS is

NLDS is not a single, fixed design system — it is an **architecture and a community**: a set of standards, processes, and shared building blocks that any government organisation can adopt and theme to its own house style. Its components are **white-label**: they ship with no house style of their own, and you apply an organisation's identity to them through **design tokens** (CSS custom properties that capture design decisions such as colours, fonts, and spacing). The pay-off is that the same component code is reusable across organisations, and an organisation can apply its huisstijl with little or no component development — often just a CSS token file.

NLDS gives you three things:
1. **A method to apply your house style** — design tokens.
2. **Infrastructure to test, share, and roll out work** — an example repository with Storybook and visual-regression tests.
3. **A style guide** to use the organisation's house style consistently.

## The three-layer token model: Brand → Common → Component

A design token is a `name` with a `value` (e.g. `link.color` → a blue). The name stays the same across organisations; the value changes per theme. NLDS organises tokens into three layers:

- **Brand tokens** — the organisation's *raw* values: its specific colours, font families, border radii. Naming here is free; these are the only values that change per organisation. Every house style is essentially a colour palette plus one or more typefaces — NLDS calls these *brand identity design tokens*, usually shortened to "brand tokens".
- **Common tokens** — the *semantic*, shared decisions with standardised, predictable names that NLDS components actually reference (so a component is reusable across all themes). These get their value from the Brand layer.
- **Component tokens** — everything a single component needs (e.g. a button's background, a text field's error border). They derive their values from the Common layer, and sometimes directly from Brand.

The key move when theming: **define the organisation's Brand tokens and link them to the Common tokens.** Because the components read Common tokens, the entire interface — buttons, forms, navigation — then adapts to the house style automatically.

## Where to find existing themes (try this before building one)

- **NL Design System Themes Storybook** — the place to see which organisation themes already exist.
- **`nl-design-system/themes`** (https://github.com/nl-design-system/themes) — design tokens and themes for organisations that don't run their own Storybook; its `proprietary/example-design-tokens/` includes a template and Dutch instructions for adding a new theme.
- **Rijkshuisstijl Community** (https://github.com/nl-design-system/rijkshuisstijl-community) — an open-source implementation of the Rijkshuisstijl (central-government house style) as NLDS components. (Community-maintained; not endorsed by the Ministry of General Affairs.)

If an official theme for the target organisation already exists, prefer reusing its tokens over re-deriving them.

## How to build a theme when none exists

1. Start from the **example template** repository on GitHub (it already contains the structure, Storybook, and token files to fill in).
2. Populate the organisation's **Brand tokens** with its real colours and fonts (from its style guide, or from values the developer supplies).
3. **Link** Brand tokens to the Common tokens the components expect.
4. Load the resulting CSS token file in the application; the NLDS components adopt the house style with no per-component restyling.

`templates/theme-tokens.css.template` in this skill gives a starting skeleton.

## Component maturity (Estafettemodel)

NLDS tracks component maturity with the *Estafettemodel*. The top status ("Hall of Fame") means a component is a stable, final version, **guaranteed accessible and reusable**, and in production at **at least two organisations with different house styles**. Prefer mature components; treat early-stage ones as provisional.

## Licensing and intellectual property

- The NLDS **components** are open source under **EUPL 1.2**.
- The **house style applied to them** is the organisation's intellectual property. You may use NLDS without building your own theme only with the **permission of the theme's maker** — for example, the design system of Gemeente Utrecht is copyrighted. Using another organisation's component or theme will also make your interface look like *that* organisation, which is usually not what you want.
- **Logos and bespoke fonts are protected/licensed** separately (e.g. Amsterdam Sans). Reference official assets from their official source; don't self-host or recreate them without the right to do so.

So: build the *target* organisation's own theme; don't lift another's.

## Why this also helps accessibility

A major reason to prefer NLDS is that its components are built to be accessible, and mature ones are verified as such. Starting from them removes many WCAG failures before they happen — but it does **not** exempt you from checking the house-style choices themselves (especially colour contrast). See the `wcag-accessibility` skill.

## Sources

- NL Design System: https://nldesignsystem.nl/
- Design tokens (handbook): https://nldesignsystem.nl/handboek/huisstijl/design-tokens/
- Design tokens (meedoen / contributor docs): https://nldesignsystem.nl/meedoen/design-tokens/
- Developer handbook — architecture: https://nldesignsystem.nl/handboek/developer/architectuur/
- NLDS on developer.overheid.nl: https://developer.overheid.nl/kennisbank/front-end/nl-design-system/
- Themes repo: https://github.com/nl-design-system/themes
- Rijkshuisstijl Community: https://github.com/nl-design-system/rijkshuisstijl-community
