#!/usr/bin/env python3
"""
check_contrast.py — WCAG 2.2 colour-contrast checker (no dependencies).

Why this exists: colour contrast is the single most common accessibility
failure, and it is the one place where "it looks fine to me" is unreliable —
the WCAG ratio is a precise calculation, not a judgement call. Run this on
every foreground/background and UI-element token pair instead of eyeballing.

Usage:
    python check_contrast.py <foreground> <background> [--kind text|ui] [--large]

    <foreground>, <background>  hex colours: #RGB, #RRGGBB, or without the '#'.

Options:
    --kind text   (default) text/glyph contrast — WCAG 1.4.3
    --kind ui     non-text UI contrast (borders, icons, focus rings,
                  meaningful graphics) — WCAG 1.4.11 (threshold 3:1, AA only)
    --large       treat text as "large" (>= 24px, or >= 18.66px bold).
                  Lowers the AA text threshold from 4.5:1 to 3:1.
                  Ignored when --kind ui.
    --json        print a machine-readable result instead of human text.

Thresholds (level AA, the government target):
    normal text   4.5:1
    large text    3.0:1
    UI / graphics 3.0:1
AAA thresholds for text (7:1 / 4.5:1) are reported for information only.

Exit code: 0 if the pair PASSES AA for the requested context, 1 if it FAILS
(or 2 on a usage/parsing error) — so it can be used in scripts and CI.
"""

import argparse
import json
import sys


def parse_hex(value):
    """Parse '#RGB', '#RRGGBB' (or without '#') into an (r, g, b) tuple 0-255."""
    s = value.strip().lstrip("#")
    if len(s) == 3:
        s = "".join(ch * 2 for ch in s)
    if len(s) != 6 or any(c not in "0123456789abcdefABCDEF" for c in s):
        raise ValueError(f"not a valid hex colour: {value!r}")
    return int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16)


def _channel_luminance(c):
    """Linearise one 0-255 channel per the WCAG relative-luminance formula."""
    cs = c / 255.0
    return cs / 12.92 if cs <= 0.03928 else ((cs + 0.055) / 1.055) ** 2.4


def relative_luminance(rgb):
    r, g, b = (_channel_luminance(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(rgb1, rgb2):
    l1 = relative_luminance(rgb1)
    l2 = relative_luminance(rgb2)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def evaluate(fg, bg, kind="text", large=False):
    ratio = contrast_ratio(parse_hex(fg), parse_hex(bg))
    if kind == "ui":
        aa_threshold, label = 3.0, "UI / non-text"
        aaa_threshold = None
    elif large:
        aa_threshold, label = 3.0, "large text"
        aaa_threshold = 4.5
    else:
        aa_threshold, label = 4.5, "normal text"
        aaa_threshold = 7.0
    return {
        "foreground": fg,
        "background": bg,
        "context": label,
        "ratio": round(ratio, 2),
        "aa_threshold": aa_threshold,
        "aa_pass": ratio >= aa_threshold,
        "aaa_threshold": aaa_threshold,
        "aaa_pass": (ratio >= aaa_threshold) if aaa_threshold else None,
    }


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Check a colour pair against WCAG 2.2 AA contrast thresholds."
    )
    p.add_argument("foreground", help="foreground hex colour, e.g. #1B4DB3")
    p.add_argument("background", help="background hex colour, e.g. #FFFFFF")
    p.add_argument("--kind", choices=["text", "ui"], default="text",
                   help="text contrast (1.4.3) or non-text UI contrast (1.4.11)")
    p.add_argument("--large", action="store_true",
                   help="treat text as large (>=24px or >=18.66px bold)")
    p.add_argument("--json", action="store_true", help="machine-readable output")
    args = p.parse_args(argv)

    try:
        result = evaluate(args.foreground, args.background, args.kind, args.large)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result))
        return 0 if result["aa_pass"] else 1

    verdict = "PASS" if result["aa_pass"] else "FAIL"
    print(f"{result['foreground']} on {result['background']}  ({result['context']})")
    print(f"  contrast ratio : {result['ratio']}:1")
    print(f"  WCAG AA needs  : {result['aa_threshold']}:1  ->  {verdict}")
    if result["aaa_threshold"]:
        aaa = "pass" if result["aaa_pass"] else "fail"
        print(f"  (AAA needs {result['aaa_threshold']}:1 -> {aaa}, for information)")
    if not result["aa_pass"]:
        print("  Fix: darken/lighten one colour, or pick an accessible token "
              "from the organisation's palette. Accessibility outranks brand exactness.")
    return 0 if result["aa_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
