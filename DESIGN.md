# Design System — The Code Classroom

## Overview

**Creative North Star:** *The Code Classroom* — a warm, well-lit study desk: paper-toned surfaces, ink-dark type, amber highlights like a desk lamp, and code blocks that feel like index cards.

**Register:** Product UI (learning tool). Density favors readability over marketing flair. Motion is functional, not decorative.

**Layout:** Fixed sidebar navigation + scrollable content column. Max content width ~720px for reading; wider for tables and exam grids.

## Colors

| Token | Role | Light | Dark |
|-------|------|-------|------|
| `--canvas` | Page background | oklch(0.98 0.008 85) warm cream | oklch(0.16 0.015 260) deep ink |
| `--surface` | Cards, sidebar | oklch(1 0 0) | oklch(0.20 0.018 260) |
| `--surface-muted` | Nested blocks | oklch(0.96 0.01 85) | oklch(0.24 0.02 260) |
| `--text` | Primary copy | oklch(0.22 0.02 260) | oklch(0.93 0.01 85) |
| `--text-muted` | Secondary | oklch(0.48 0.02 260) | oklch(0.65 0.02 260) |
| `--accent` | Primary action | oklch(0.62 0.14 145) python green | oklch(0.72 0.14 145) |
| `--accent-warm` | Highlights, tags | oklch(0.75 0.12 75) amber | oklch(0.78 0.12 75) |
| `--success` | Correct answers | oklch(0.55 0.12 145) | oklch(0.70 0.12 145) |
| `--danger` | Errors | oklch(0.55 0.18 25) | oklch(0.65 0.16 25) |
| `--border` | Dividers | oklch(0.88 0.01 85) | oklch(0.30 0.02 260) |
| `--code-bg` | Code blocks | oklch(0.94 0.015 260) | oklch(0.14 0.02 260) |

## Typography

- **Display / headings:** `"Fraunces", Georgia, serif` — optical size for warmth, not generic sans.
- **Body:** `"IBM Plex Sans", system-ui, sans-serif` — product-fluent, highly readable.
- **Code:** `"IBM Plex Mono", ui-monospace, monospace` — ligatures off, tabular nums.

**Scale (1.25 ratio):** 0.8125rem labels · 1rem body · 1.25rem h4 · 1.563rem h3 · 1.953rem h2 · 2.441rem h1

**Line height:** 1.65 body · 1.25 headings · 1.55 code

## Elevation

No drop shadows on cards by default — **border + surface contrast** defines hierarchy.

- Level 0: canvas
- Level 1: card (`1px border`, `--surface`)
- Level 2: sticky header (`border-bottom` only)
- Level 3: modal/toast (future) — single soft shadow `0 8px 32px oklch(0 0 0 / 0.12)`

## Components

**Sidebar nav:** Text buttons, 8px radius, active state = `--surface-muted` + left accent bar (3px green).

**Cards:** 16px padding, 12px radius, optional section label in uppercase tracking.

**Buttons:** Primary = solid green, white text. Secondary = bordered. Focus = 2px ring offset.

**Quiz blocks:** Muted inset background; correct/wrong = left border accent only (not full recolor).

**Flashcards:** Horizontal flip, reduced motion = instant swap.

**Progress bar:** 4px height, rounded, green fill — no gradient.

**Tags:** Pill, `--surface-muted` bg, `--text-muted` text, warm accent on hover.

## Do's and Don'ts

**Do**
- Use warm tinted neutrals, not pure gray
- Keep code blocks visually distinct from prose
- Provide `:focus-visible` on all interactive elements
- Honor `prefers-reduced-motion`
- Support light and dark themes via `data-theme`

**Don't**
- Purple/indigo gradient heroes
- Gradient text logos
- Backdrop blur / glass panels
- More than two font families (+ mono)
- Alert() for feedback — use inline toast
