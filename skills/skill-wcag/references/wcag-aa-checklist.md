# WCAG 2.2 level A + AA checklist (for assistant interfaces)

Use this as the criteria list to walk during final review. It is organised so you spend your attention where it matters most for conversational/chat interfaces, then confirm the rest.

This list **paraphrases** each success criterion's intent and adds a one-line note on what it means in a chat UI — it is a working aid, not a substitute for the normative text. For the authoritative wording and techniques, use the W3C Quick Reference: https://www.w3.org/WAI/WCAG22/quickref/ (filter to levels A and AA).

Criteria marked **[new in 2.2]** did not exist in WCAG 2.1. Success criterion 4.1.1 "Parsing" was **removed** in 2.2 and is intentionally absent.

## Contents

- [Part A — The criteria that bite hardest in chat UIs](#part-a)
- [Part B — Full A + AA list, condensed (by POUR)](#part-b)
  - [Perceivable](#perceivable)
  - [Operable](#operable)
  - [Understandable](#understandable)
  - [Robust](#robust)

---

<a id="part-a"></a>
## Part A — The criteria that bite hardest in chat UIs

Get these right and you have handled most of what goes wrong in assistant interfaces specifically.

1. **1.4.3 Contrast (Minimum) — AA.** Text ≥ 4.5:1, large text ≥ 3:1 against background. Run `scripts/check_contrast.py`. The usual failure: light-grey timestamps, placeholder text, and brand-coloured buttons.

2. **1.4.11 Non-text Contrast — AA.** UI components and meaningful graphics (icon buttons, input borders, focus indicators, the send arrow) need ≥ 3:1 against adjacent colours. A focus ring you can't see fails this.

3. **2.1.1 Keyboard / 2.1.2 No Keyboard Trap — A.** Everything operable by keyboard; focus can always move away again. Test: send a message, open and close any menu/panel, and reach every quick-reply — mouse unplugged.

4. **2.4.7 Focus Visible — AA**, and **2.4.11 Focus Not Obscured (Minimum) — AA [new in 2.2].** A visible focus indicator on every focusable element, and that focused element must not be hidden behind a sticky header, sticky composer bar, or floating widget. Chat layouts with fixed top/bottom bars routinely violate 2.4.11.

5. **4.1.3 Status Messages — AA.** Status changes that don't move focus must be announced via an ARIA live region. This is the criterion behind **announcing streamed assistant replies and the "typing…" state**. Use `aria-live="polite"` (often `role="log"` on the transcript); announce per completed message, not per token.

6. **4.1.2 Name, Role, Value — A.** Every control exposes a correct name, role, and state to assistive tech. The message input needs a programmatic label; custom chips/toggles need correct roles and pressed/expanded state. Prefer native elements so you get this for free.

7. **1.3.1 Info and Relationships — A.** Structure conveyed visually is also available programmatically: the transcript as a list, messages as list items, headings in order, inputs tied to labels. Don't fake structure with styled `<div>`s.

8. **1.1.1 Non-text Content — A.** Descriptive `alt` for meaningful images; `alt=""` for decorative ones. Avatars, inline images the assistant returns, and icon-only buttons all need accessible names.

9. **1.4.1 Use of Color — A.** Don't distinguish user vs assistant messages, or signal errors/success, by colour alone — add a label, icon, or text.

10. **2.2.1 Timing Adjustable — A.** If a session or conversation can time out, warn the user and let them extend it; don't drop their input silently. Common in authenticated government flows.

11. **2.5.8 Target Size (Minimum) — AA [new in 2.2].** Interactive targets at least 24×24 CSS px (with spacing exceptions). Quick-reply chips, icon buttons, and the send button are the usual offenders.

12. **3.3.1 Error Identification / 3.3.2 Labels or Instructions / 3.3.3 Error Suggestion — A/A/AA.** Inputs have visible labels and instructions; errors are identified in text and tied to the field (`aria-describedby`); where known, a correction is suggested.

13. **3.3.8 Accessible Authentication (Minimum) — AA [new in 2.2].** If the assistant is behind a login, don't require solving a cognitive puzzle (e.g. transcribing distorted text or doing arithmetic). Allow password managers, copy-paste, and passkeys.

14. **2.3.3 Animation from Interactions — AAA (aim for it) + `prefers-reduced-motion`.** Typing-dot animations, message slide-ins, and auto-scroll should respect reduced-motion preferences. (2.3.3 is AAA, but honouring the OS reduced-motion setting is cheap and expected.)

---

<a id="part-b"></a>
## Part B — Full A + AA list, condensed (by POUR)

Confirm each of these. Items already detailed in Part A are marked → A#.

<a id="perceivable"></a>
### Perceivable

- **1.1.1 Non-text Content (A)** — text alternatives for non-text content. → A8
- **1.2.1 Audio-only / Video-only (Prerecorded) (A)** — transcript for audio-only; transcript or audio track for video-only. Relevant if the assistant returns media.
- **1.2.2 Captions (Prerecorded) (A)** — captions for prerecorded video with audio.
- **1.2.3 Audio Description or Media Alternative (Prerecorded) (A)** — describe important visual info in prerecorded video.
- **1.2.4 Captions (Live) (AA)** — captions for live audio content.
- **1.2.5 Audio Description (Prerecorded) (AA)** — audio description for prerecorded video.
- **1.3.1 Info and Relationships (A)** — structure/relationships available programmatically. → A7
- **1.3.2 Meaningful Sequence (A)** — reading/navigation order makes sense (e.g. messages in chronological DOM order).
- **1.3.3 Sensory Characteristics (A)** — instructions don't rely solely on shape, size, or position ("press the button on the right").
- **1.3.4 Orientation (AA)** — works in both portrait and landscape; don't lock orientation.
- **1.3.5 Identify Input Purpose (AA)** — set `autocomplete` on inputs collecting user info (name, email) so they can be autofilled.
- **1.4.1 Use of Color (A)** — colour isn't the only means of conveying meaning. → A9
- **1.4.2 Audio Control (A)** — if audio plays automatically for >3s, provide a way to pause/stop it.
- **1.4.3 Contrast (Minimum) (AA)** — text contrast 4.5:1 / 3:1 large. → A1
- **1.4.4 Resize Text (AA)** — text scalable to 200% without loss of content/function; use relative units, don't disable zoom.
- **1.4.5 Images of Text (AA)** — use real text, not images of text (logos excepted).
- **1.4.10 Reflow (AA)** — content reflows to a 320px-wide viewport without two-dimensional scrolling. Chat windows and side panels must reflow on mobile/zoom.
- **1.4.11 Non-text Contrast (AA)** — UI components and graphics ≥ 3:1. → A2
- **1.4.12 Text Spacing (AA)** — no loss of content when users override line height / letter / word / paragraph spacing.
- **1.4.13 Content on Hover or Focus (AA)** — tooltips/popovers triggered on hover/focus are dismissable, hoverable, and persistent. Affects chat tooltips and "info" popovers.

<a id="operable"></a>
### Operable

- **2.1.1 Keyboard (A)** — all functionality via keyboard. → A3
- **2.1.2 No Keyboard Trap (A)** — focus can always leave a component. → A3
- **2.1.4 Character Key Shortcuts (A)** — single-character shortcuts can be turned off or remapped (don't trap "/" or "j/k" for screen-reader users).
- **2.2.1 Timing Adjustable (A)** — time limits adjustable/extendable. → A10
- **2.2.2 Pause, Stop, Hide (A)** — moving/auto-updating content can be paused/stopped/hidden (auto-scrolling transcript, carousels).
- **2.3.1 Three Flashes or Below Threshold (A)** — nothing flashes more than 3×/second.
- **2.4.1 Bypass Blocks (A)** — a way to skip repeated blocks (skip link to main/composer).
- **2.4.2 Page Titled (A)** — pages have descriptive `<title>`.
- **2.4.3 Focus Order (A)** — focus order preserves meaning and operability.
- **2.4.4 Link Purpose (In Context) (A)** — link purpose clear from text or context (avoid bare "click here").
- **2.4.5 Multiple Ways (AA)** — more than one way to find pages (search + nav). N/A for a single-screen widget.
- **2.4.6 Headings and Labels (AA)** — headings and labels are descriptive.
- **2.4.7 Focus Visible (AA)** — visible focus indicator. → A4
- **2.4.11 Focus Not Obscured (Minimum) (AA) [new in 2.2]** — focused element not fully hidden by other content. → A4
- **2.5.1 Pointer Gestures (A)** — multipoint/path-based gestures have a single-pointer alternative.
- **2.5.2 Pointer Cancellation (A)** — actions trigger on up-event, not down; allow abort.
- **2.5.3 Label in Name (A)** — a control's accessible name contains its visible label text (critical for voice control).
- **2.5.4 Motion Actuation (A)** — functionality triggered by device motion has a UI alternative and can be disabled.
- **2.5.7 Dragging Movements (AA) [new in 2.2]** — any drag operation has a single-tap/click alternative.
- **2.5.8 Target Size (Minimum) (AA) [new in 2.2]** — targets ≥ 24×24px (with spacing exceptions). → A11

<a id="understandable"></a>
### Understandable

- **3.1.1 Language of Page (A)** — page language set (`<html lang="nl">` / `"en"`).
- **3.1.2 Language of Parts (AA)** — mark inline language changes (e.g. an English phrase inside Dutch content) with `lang`.
- **3.2.1 On Focus (A)** — receiving focus doesn't trigger an unexpected change of context.
- **3.2.2 On Input (A)** — changing a setting doesn't auto-trigger an unexpected context change unless the user is warned.
- **3.2.3 Consistent Navigation (AA)** — navigation is consistent across pages.
- **3.2.4 Consistent Identification (AA)** — components with the same function are identified consistently.
- **3.2.6 Consistent Help (A) [new in 2.2]** — if a help mechanism exists (contact, FAQ, human handoff), it appears in a consistent location across pages. Directly relevant to an assistant's "talk to a human" / fallback option.
- **3.3.1 Error Identification (A)** — input errors identified in text. → A12
- **3.3.2 Labels or Instructions (A)** — labels/instructions provided for inputs. → A12
- **3.3.3 Error Suggestion (AA)** — suggest a correction when known. → A12
- **3.3.4 Error Prevention (Legal, Financial, Data) (AA)** — for legal/financial/data submissions, make actions reversible, checked, or confirmed. Applies when the assistant submits a government request, application, or payment.
- **3.3.7 Redundant Entry (A) [new in 2.2]** — don't make users re-enter info they already provided in the same session (auto-populate or let them reuse it).
- **3.3.8 Accessible Authentication (Minimum) (AA) [new in 2.2]** — no cognitive-function test required to log in. → A13

<a id="robust"></a>
### Robust

- **4.1.2 Name, Role, Value (A)** — correct name/role/value/state for all UI components. → A6
- **4.1.3 Status Messages (AA)** — status messages exposed to assistive tech without moving focus. → A5
- *(4.1.1 Parsing — removed in WCAG 2.2; do not test against it.)*

---

### Quick reminder on verification

Walking this list is a manual review. Pair it with: the contrast script (`scripts/check_contrast.py`), an automated scan (axe-core / pa11y / Lighthouse), a keyboard-only pass, and a screen-reader smoke test. Automated tooling alone catches only part of these criteria — many (focus order, meaningful sequence, error suggestions, label-in-name) require human judgement.
