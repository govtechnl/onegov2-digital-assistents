---
name: wcag-accessibility
description: "Use this skill whenever you are building, styling, or reviewing anything a person will see or operate as part of a digital assistant — a chat or chatbot interface, a web page, a web component, a form, a button, a rendered email, or a citizen-facing document/PDF — to make it conform to WCAG (Web Content Accessibility Guidelines) 2.2 level AA, the accessibility standard required for (Dutch) government digital services. Triggers include 'accessible', 'accessibility', 'toegankelijk', 'toegankelijkheid', 'WCAG', 'a11y', 'screen reader', 'schermlezer', 'contrast', 'keyboard navigation', 'toetsenbordbediening', or any work on a front-end / user interface, even when accessibility is not mentioned explicitly. Apply it especially to streamed chat messages, typing indicators, focus handling, colour contrast, and form errors. Do NOT use this skill for backend-only, API, data-pipeline, model/prompt, or infrastructure work that produces no user-facing surface — there is nothing to make accessible there."
---

# WCAG accessibility for user-facing assistant interfaces

Anything a person sees or operates in a digital assistant must be usable by people with disabilities — including those who navigate by keyboard, use a screen reader, rely on high contrast or magnification, or have cognitive or motor differences. This skill makes the user-facing parts you build conform to **WCAG 2.2 level AA**. For (Dutch) government services that conformance is also a legal obligation, not a nice-to-have.

## First: does this even apply?

Apply this skill **only** when your work produces something a human will perceive or operate — a chat/chatbot interface, a web page or component, a form, a button, a rendered email, or a citizen-facing document (HTML/PDF). That is the gate, and it is deliberate.

Do **not** spend accessibility effort on work with no user-facing surface: backend services, APIs, data pipelines, model or prompt engineering, infrastructure, batch jobs. WCAG is about the perception and operation of an interface; there is nothing to make perceivable in a cron job, and forcing accessibility framing onto non-UI code wastes effort and muddies scope.

If you are unsure whether a task is user-facing, ask the developer one question: *"Will a person see or interact with the output of this directly?"* If no, skip the skill. Note the common boundary case: an API that returns text which is later shown to a user is itself **not** the user-facing surface — the component that renders that text is. Apply the skill there, not in the API.

## The standard you build to

**Build target: WCAG 2.2, level AA.**

- *Why 2.2 and not 2.1:* WCAG 2.2 is a strict superset of 2.1 — the same criteria plus a handful more — so building to 2.2 never violates 2.1. The added 2.2 criteria map directly onto real chat-UI problems: focus that isn't hidden behind a sticky header, minimum target sizes, accessible authentication, and a consistently placed help option. (One subtlety: success criterion 4.1.1 "Parsing" was *removed* in 2.2 — ignore it.)
- *Why AA and not A or AAA:* AA is the conformance level governments require. AAA contains criteria that cannot be met for all content; reach for AAA where it is cheap, but never block delivery on it.

**Legal floor (NL government): WCAG 2.1 level AA**, made binding through the European standard **EN 301 549** under the *Besluit digitale toegankelijkheid overheid* (now part of the Wet digitale overheid). WCAG 2.2 is not yet legally mandatory because it has not been folded into EN 301 549, but it is recommended for new builds and central government already reports against it. So treat 2.1 AA as the line you must never fall below, and 2.2 AA as what you actually ship. A **published accessibility statement** (toegankelijkheidsverklaring) is also legally required. Read `references/dutch-legal-context.md` before you consider the work done.

## Start from accessible building blocks

The cheapest accessibility is the bug you never write. Prefer components from the **NL Design System (NLDS)**: they are white-label and already tested for accessibility, and you apply the organisation's house style to them purely through design tokens (that is what the companion `organisatie-huisstijl` skill produces, and a community `nl-design-system` skill covers the components themselves in depth). Building on vetted components removes whole classes of contrast, focus, and semantics bugs before they start. Hand-rolling a custom `<div>`-based dropdown, modal, or tab set is where accessibility tends to die — if you must, budget real time for keyboard and screen-reader support.

## Get these right every time

These are the highest-leverage items. The complete level A + AA criteria list, with notes on what each means for a chat UI, is in `references/wcag-aa-checklist.md` — walk it before final review.

- **Colour contrast.** Body text needs ≥ 4.5:1 against its background; large text (≈ 24px, or 18.66px bold) and meaningful UI elements/icons need ≥ 3:1. Do not eyeball it — run `scripts/check_contrast.py <foreground> <background>` on every text and UI token pair. Brand-palette colours frequently fail here; that is the main friction point with house style (see *How this fits with house style* below). (1.4.3, 1.4.11)
- **Keyboard, fully.** Every action must be reachable and operable with the keyboard alone (Tab / Shift+Tab / Enter / Space / Esc / arrows), in a sensible order, with a **clearly visible focus indicator**, and no traps. Many users never touch a pointer device. Verify by navigating with the mouse unplugged. (2.1.1, 2.1.2, 2.4.3, 2.4.7)
- **Real semantics and names.** Use real elements — `<button>`, `<nav>`, `<main>`, headings in order, `<label>` tied to each input. Every control needs an accessible name. Screen readers convey structure through semantics; a styled `<div>` communicates nothing to them. (1.3.1, 2.4.6, 4.1.2)
- **Text alternatives.** Meaningful images get descriptive `alt`; purely decorative images get empty `alt=""` so they are skipped. Icons that carry meaning need an accessible label. (1.1.1)
- **Never rely on colour or shape alone** to carry meaning — pair it with text or an icon. A red border with no message is invisible to a colour-blind user. (1.4.1, 1.3.3)
- **Errors that help.** Tie each validation message to its field programmatically (`aria-describedby`), state the problem in plain text, and suggest a fix. (3.3.1–3.3.3)

## Conversational interfaces have their own traps

This is where assistant UIs diverge from ordinary web pages, and where generic accessibility advice runs out. Handle these explicitly — they are easy to miss and badly hurt the users who depend on them:

- **Announce streamed replies.** A screen-reader user does not "see" a reply materialise token by token. Put the transcript (or a dedicated status region) in an ARIA live region — `aria-live="polite"`, often with `role="log"` on the message list — so a new assistant message is announced *after* the user's current activity rather than interrupting it. Announce **per completed message, not per token**, or you flood the user with noise. Never use `aria-live="assertive"` for ordinary replies.
- **Make "assistant is typing" perceivable.** A bouncing-dots animation is invisible to a screen reader and a problem for reduced-motion users. Expose typing/loading state as text in a status region, and honour `prefers-reduced-motion`. (4.1.3, 2.3.3)
- **Manage focus deliberately.** When a reply arrives, generally do *not* yank focus away from the input — that is disorienting mid-typing — but make the new content reachable and offer a way to jump to the latest message. When you open a panel or dialog, move focus into it and return focus to the trigger on close.
- **Distinguish speakers without colour.** Tell user and assistant messages apart with labels, position, and structure, not just a colour swap; give any avatar a text alternative. (1.4.1)
- **Sessions and timeouts.** If a conversation or form session can expire, warn first and let the user extend it — don't silently discard their input. (2.2.1)
- **Quick-reply chips and buttons** must be keyboard-focusable, labelled, and at least ~24×24px as targets, and their focus ring must not be hidden behind a sticky chat header or footer. (2.5.8, 2.4.11 — both new in 2.2)
- **If the assistant sits behind a login**, do not gate it with a cognitive puzzle (transcribe-this-distorted-text); allow password managers and passkeys. (3.3.8 — new in 2.2)

## Verify before you call it done

Accessibility is verified, not asserted. Run this pass and fix what it surfaces:

1. **Contrast** — run `scripts/check_contrast.py` on every foreground/background and UI token pair. Re-derive or replace any pair that fails.
2. **Automated scan** — run an automated checker against the rendered UI (e.g. `axe-core` via Playwright or `@axe-core/cli`, `pa11y`, or Lighthouse). Treat a pass as a floor, not a finish line: automated tools catch only roughly 30–50% of issues, so they are necessary but not sufficient.
3. **Keyboard pass** — tab through everything: sensible order, focus always visible, no traps, every action reachable.
4. **Screen-reader smoke test** — confirm new messages are announced, controls are named, and the typing indicator is perceivable.
5. **Checklist** — walk `references/wcag-aa-checklist.md` for the criteria not covered above.
6. **Statement** — ensure a toegankelijkheidsverklaring is planned or published; it is legally required for government services. See `references/dutch-legal-context.md`.

## How this fits with house style

The companion `organisatie-huisstijl` skill chooses the organisation's colours, typography, and logo and emits them as design tokens. Accessibility constrains those choices. If a brand foreground/background pair fails AA contrast, **accessibility wins** — choose an accessible pair from the organisation's palette, or derive an accessible variant of the brand colour, rather than shipping text nobody can read. Surface the conflict to the developer explicitly instead of quietly degrading either the brand or the contrast.

## When you genuinely can't comply

If something cannot be made fully conformant in the time available, be honest. Flag it to the developer and record it in the accessibility statement as a known limitation with a remediation plan — statements explicitly allow declaring *partial* conformance. A declared gap is auditable and gets fixed; a hidden one resurfaces as a complaint from the people least able to work around it.

## Sources

- Web Content Accessibility Guidelines (WCAG) 2.2 — W3C Recommendation: https://www.w3.org/TR/WCAG22/
- How to Meet WCAG 2.2 (Quick Reference): https://www.w3.org/WAI/WCAG22/quickref/
- DigiToegankelijk — wetgeving en richtlijnen (NL): https://www.digitoegankelijk.nl/
- Toegankelijkheidsverklaring (invulassistent): https://www.toegankelijkheidsverklaring.nl/
- EN 301 549 (referenced by the Besluit digitale toegankelijkheid overheid)
- NL Design System: https://nldesignsystem.nl/
