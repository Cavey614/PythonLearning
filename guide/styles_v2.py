CSS = """
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&display=swap');

:root {
  color-scheme: light;
  --font-display: 'Fraunces', Georgia, serif;
  --font-body: 'IBM Plex Sans', system-ui, sans-serif;
  --font-mono: 'IBM Plex Mono', ui-monospace, monospace;
  --space-1: 0.25rem;
  --space-2: 0.5rem;
  --space-3: 0.75rem;
  --space-4: 1rem;
  --space-5: 1.25rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  --space-10: 2.5rem;
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --radius-full: 999px;
  --ease-out: cubic-bezier(0.22, 1, 0.36, 1);
  --duration: 180ms;
  --canvas: oklch(0.98 0.008 85);
  --surface: oklch(1 0 0);
  --surface-muted: oklch(0.96 0.01 85);
  --text: oklch(0.22 0.02 260);
  --text-muted: oklch(0.48 0.02 260);
  --accent: oklch(0.52 0.14 145);
  --accent-hover: oklch(0.45 0.14 145);
  --accent-soft: oklch(0.92 0.04 145);
  --accent-warm: oklch(0.75 0.12 75);
  --success: oklch(0.48 0.12 145);
  --success-soft: oklch(0.94 0.04 145);
  --warning: oklch(0.72 0.12 75);
  --warning-soft: oklch(0.96 0.04 85);
  --danger: oklch(0.52 0.18 25);
  --danger-soft: oklch(0.96 0.04 25);
  --border: oklch(0.88 0.01 85);
  --code-bg: oklch(0.945 0.012 260);
  --header-bg: oklch(0.99 0.006 85 / 0.92);
  --ring: oklch(0.52 0.14 145 / 0.45);
  --sidebar-width: 272px;
}

[data-theme="dark"] {
  color-scheme: dark;
  --canvas: oklch(0.16 0.015 260);
  --surface: oklch(0.20 0.018 260);
  --surface-muted: oklch(0.24 0.02 260);
  --text: oklch(0.93 0.01 85);
  --text-muted: oklch(0.65 0.02 260);
  --accent: oklch(0.72 0.14 145);
  --accent-hover: oklch(0.78 0.14 145);
  --accent-soft: oklch(0.28 0.04 145);
  --accent-warm: oklch(0.78 0.12 75);
  --success: oklch(0.70 0.12 145);
  --success-soft: oklch(0.26 0.04 145);
  --warning: oklch(0.78 0.12 75);
  --warning-soft: oklch(0.28 0.04 85);
  --danger: oklch(0.65 0.16 25);
  --danger-soft: oklch(0.28 0.06 25);
  --border: oklch(0.30 0.02 260);
  --code-bg: oklch(0.14 0.02 260);
  --header-bg: oklch(0.18 0.015 260 / 0.92);
  --ring: oklch(0.72 0.14 145 / 0.5);
}

*, *::before, *::after { box-sizing: border-box; }

html {
  scroll-behavior: smooth;
  -webkit-font-smoothing: antialiased;
}

@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

body {
  margin: 0;
  font-family: var(--font-body);
  font-size: 1rem;
  line-height: 1.65;
  background: var(--canvas);
  color: var(--text);
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

:focus { outline: none; }
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* Header */
header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--header-bg);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border);
  padding: var(--space-3) var(--space-4);
}

.header-inner {
  max-width: 1280px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: var(--space-4);
  flex-wrap: wrap;
}

.brand {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  min-width: 0;
}

.brand-mark {
  width: 36px;
  height: 36px;
  border-radius: var(--radius-md);
  background: var(--accent-soft);
  border: 1px solid var(--border);
  display: grid;
  place-items: center;
  font-family: var(--font-mono);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--accent);
  flex-shrink: 0;
}

.logo {
  font-family: var(--font-display);
  font-size: 1.125rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--text);
  line-height: 1.2;
}

.logo-sub {
  display: block;
  font-family: var(--font-body);
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-top: 2px;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  margin-left: auto;
}

.theme-toggle {
  width: 36px;
  height: 36px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface);
  color: var(--text-muted);
  cursor: pointer;
  display: grid;
  place-items: center;
  font-size: 1rem;
  transition: background var(--duration) var(--ease-out), color var(--duration) var(--ease-out);
}
.theme-toggle:hover { background: var(--surface-muted); color: var(--text); }

.progress-bar-wrap {
  flex: 1;
  min-width: 120px;
  max-width: 220px;
}

.progress-label {
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: var(--space-1);
}

.progress-bar {
  height: 4px;
  background: var(--surface-muted);
  border-radius: var(--radius-full);
  overflow: hidden;
  border: 1px solid var(--border);
}

.progress-fill {
  height: 100%;
  background: var(--accent);
  border-radius: var(--radius-full);
  transition: width 0.5s var(--ease-out);
  width: 0;
}

.menu-toggle {
  display: none;
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface);
  color: var(--text);
  font-family: var(--font-body);
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
}

/* Layout */
.layout {
  display: flex;
  max-width: 1280px;
  margin: 0 auto;
  min-height: calc(100vh - 57px);
}

nav.sidebar {
  width: var(--sidebar-width);
  flex-shrink: 0;
  border-right: 1px solid var(--border);
  padding: var(--space-4);
  position: sticky;
  top: 57px;
  height: calc(100vh - 57px);
  overflow-y: auto;
  background: var(--canvas);
}

nav.sidebar h3 {
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin: var(--space-5) 0 var(--space-2);
  padding-left: var(--space-2);
}
nav.sidebar h3:first-child { margin-top: 0; }

.nav-link {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-3);
  border-radius: var(--radius-sm);
  color: var(--text-muted);
  font-size: 0.875rem;
  font-weight: 400;
  cursor: pointer;
  border: none;
  background: none;
  width: 100%;
  text-align: left;
  transition: background var(--duration) var(--ease-out), color var(--duration) var(--ease-out);
  border-left: 3px solid transparent;
  margin-bottom: 1px;
}

.nav-link:hover {
  background: var(--surface-muted);
  color: var(--text);
}

.nav-link.active {
  background: var(--accent-soft);
  color: var(--text);
  border-left-color: var(--accent);
  font-weight: 500;
}

.nav-num {
  font-family: var(--font-mono);
  font-size: 0.6875rem;
  color: var(--text-muted);
  min-width: 1.25rem;
}
.nav-link.active .nav-num { color: var(--accent); }

main.content {
  flex: 1;
  padding: var(--space-6) var(--space-8);
  min-width: 0;
  max-width: 900px;
}

/* Hero */
.hero {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: var(--space-8);
  margin-bottom: var(--space-6);
  position: relative;
  overflow: hidden;
}

.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 4px;
  height: 100%;
  background: var(--accent);
}

.hero h1 {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 4vw, 2.25rem);
  font-weight: 600;
  letter-spacing: -0.03em;
  line-height: 1.2;
  margin: 0 0 var(--space-3);
  color: var(--text);
}

.hero p {
  color: var(--text-muted);
  margin: 0 0 var(--space-4);
  max-width: 52ch;
}

.hero-stats {
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-4);
  margin-top: var(--space-5);
  padding-top: var(--space-5);
  border-top: 1px solid var(--border);
}

.stat {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.stat-value {
  font-family: var(--font-display);
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--accent);
  line-height: 1;
}

.stat-label {
  font-size: 0.75rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Cards */
.card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  margin-bottom: var(--space-4);
}

.card-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: var(--space-3);
  margin-bottom: var(--space-4);
  flex-wrap: wrap;
}

.card h2 {
  font-family: var(--font-display);
  font-size: 1.375rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  margin: 0;
  color: var(--text);
}

.card h3 {
  font-size: 1rem;
  font-weight: 600;
  margin: var(--space-5) 0 var(--space-2);
  color: var(--text);
}

.card h4 {
  font-size: 0.9375rem;
  font-weight: 600;
  margin: var(--space-4) 0 var(--space-2);
}

.section-label {
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: var(--space-2);
}

.tag {
  display: inline-block;
  background: var(--surface-muted);
  color: var(--text-muted);
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: 0.75rem;
  font-weight: 500;
  margin: var(--space-1) var(--space-1) var(--space-1) 0;
  border: 1px solid var(--border);
  transition: border-color var(--duration), color var(--duration);
}
.tag:hover { border-color: var(--accent-warm); color: var(--text); }

ul, ol { padding-left: 1.35rem; margin: var(--space-2) 0; }
li { margin: var(--space-2) 0; }
li::marker { color: var(--accent); }

/* Code */
pre, code { font-family: var(--font-mono); font-feature-settings: 'liga' 0; }

pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  overflow-x: auto;
  font-size: 0.8125rem;
  line-height: 1.55;
  margin: var(--space-3) 0;
}

code {
  background: var(--code-bg);
  padding: 0.1em 0.35em;
  border-radius: 4px;
  font-size: 0.875em;
  border: 1px solid var(--border);
}

/* Accordion */
.accordion {
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
  margin: var(--space-3) 0;
  overflow: hidden;
  background: var(--surface);
}

.accordion-btn {
  width: 100%;
  text-align: left;
  padding: var(--space-4);
  background: var(--surface-muted);
  border: none;
  color: var(--text);
  cursor: pointer;
  font-family: var(--font-body);
  font-size: 0.9375rem;
  font-weight: 500;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: var(--space-3);
  transition: background var(--duration);
}
.accordion-btn:hover { background: var(--accent-soft); }

.accordion-body {
  display: none;
  padding: var(--space-4);
  border-top: 1px solid var(--border);
}

.accordion.open .accordion-body { display: block; }
.accordion.open .accordion-btn .chev { transform: rotate(180deg); }

.chev {
  color: var(--text-muted);
  font-size: 0.75rem;
  transition: transform var(--duration) var(--ease-out);
}

/* Grid */
.grid-2 {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: var(--space-4);
}

/* Flashcards */
.flashcard-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: var(--space-3);
}

.flashcard {
  perspective: 900px;
  height: 140px;
  cursor: pointer;
}

.flashcard-inner {
  position: relative;
  width: 100%;
  height: 100%;
  transition: transform 0.45s var(--ease-out);
  transform-style: preserve-3d;
}

@media (prefers-reduced-motion: reduce) {
  .flashcard-inner { transition: none; }
  .flashcard.flipped .flashcard-front { display: none; }
  .flashcard.flipped .flashcard-back { transform: none; position: relative; }
}

.flashcard.flipped .flashcard-inner { transform: rotateY(180deg); }

.flashcard-front, .flashcard-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: var(--radius-md);
  padding: var(--space-4);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  border: 1px solid var(--border);
  font-size: 0.875rem;
  line-height: 1.45;
}

.flashcard-front { background: var(--surface-muted); }
.flashcard-back {
  background: var(--accent-soft);
  transform: rotateY(180deg);
  color: var(--text);
}

.flashcard-hint {
  font-size: 0.75rem;
  color: var(--text-muted);
  margin-bottom: var(--space-3);
}

/* Quiz */
.quiz-block {
  border: 1px solid var(--border);
  border-left: 3px solid var(--border);
  border-radius: var(--radius-md);
  padding: var(--space-4);
  margin: var(--space-4) 0;
  background: var(--surface-muted);
}

.quiz-block.correct {
  border-left-color: var(--success);
  background: var(--success-soft);
}

.quiz-block.wrong {
  border-left-color: var(--danger);
  background: var(--danger-soft);
}

.quiz-options {
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
  margin: var(--space-3) 0;
}

.quiz-options label {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  padding: var(--space-3) var(--space-4);
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-size: 0.9375rem;
  transition: border-color var(--duration), background var(--duration);
}

.quiz-options label:hover { border-color: var(--accent); background: var(--accent-soft); }
.quiz-options input[type="radio"] { accent-color: var(--accent); width: 1rem; height: 1rem; }

/* Buttons */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-2);
  padding: var(--space-2) var(--space-4);
  border: 1px solid transparent;
  border-radius: var(--radius-sm);
  cursor: pointer;
  font-family: var(--font-body);
  font-size: 0.875rem;
  font-weight: 500;
  transition: background var(--duration) var(--ease-out), border-color var(--duration), transform var(--duration);
}

.btn:active { transform: scale(0.98); }

.btn-primary {
  background: var(--accent);
  color: oklch(0.99 0 0);
  border-color: var(--accent);
}
.btn-primary:hover { background: var(--accent-hover); border-color: var(--accent-hover); }

.btn-secondary {
  background: var(--surface);
  color: var(--text);
  border-color: var(--border);
}
.btn-secondary:hover { background: var(--surface-muted); }

.btn-success {
  background: var(--success-soft);
  color: var(--success);
  border-color: var(--success);
}
.btn-success:hover { background: var(--accent-soft); }

.btn-sm { padding: var(--space-1) var(--space-3); font-size: 0.8125rem; }

.btn-row { display: flex; flex-wrap: wrap; gap: var(--space-2); margin-top: var(--space-3); }

/* Feedback */
.feedback {
  margin-top: var(--space-3);
  padding: var(--space-3) var(--space-4);
  border-radius: var(--radius-sm);
  font-size: 0.875rem;
  line-height: 1.5;
}

.feedback.ok {
  background: var(--success-soft);
  color: var(--success);
  border: 1px solid oklch(from var(--success) l c h / 0.25);
}

.feedback.bad {
  background: var(--danger-soft);
  color: var(--danger);
  border: 1px solid oklch(from var(--danger) l c h / 0.25);
}

/* Inputs */
.fill-blank input,
.quiz-block input[type="text"],
.exam-input {
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  background: var(--surface);
  color: var(--text);
  font-family: var(--font-body);
  font-size: 0.9375rem;
  min-width: 140px;
  transition: border-color var(--duration), box-shadow var(--duration);
}

.fill-blank input:focus,
.quiz-block input[type="text"]:focus,
.exam-input:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 3px var(--ring);
  outline: none;
}

.exam-input { width: 100%; max-width: 420px; }

/* Drag & drop */
.drag-area {
  min-height: 88px;
  border: 2px dashed var(--border);
  border-radius: var(--radius-md);
  padding: var(--space-3);
  display: flex;
  flex-wrap: wrap;
  gap: var(--space-2);
  align-items: center;
  background: var(--surface);
}

.drag-item, .drop-zone {
  padding: var(--space-2) var(--space-3);
  background: var(--surface-muted);
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  cursor: grab;
  user-select: none;
  font-size: 0.8125rem;
  font-weight: 500;
}

.drop-zone {
  min-width: 148px;
  min-height: 44px;
  border-style: dashed;
  border-color: var(--accent);
  background: var(--accent-soft);
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: default;
}

.drop-zone.filled { border-style: solid; background: var(--success-soft); }
.match-row { display: flex; flex-wrap: wrap; gap: var(--space-3); align-items: center; margin: var(--space-2) 0; }

/* Badges */
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: 0.6875rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.badge-done {
  background: var(--success-soft);
  color: var(--success);
  border: 1px solid oklch(from var(--success) l c h / 0.3);
}

.badge-todo {
  background: var(--warning-soft);
  color: var(--warning);
  border: 1px solid oklch(from var(--warning) l c h / 0.3);
}

.hidden { display: none !important; }

.section-title {
  font-family: var(--font-display);
  font-size: 1.75rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  margin: 0 0 var(--space-6);
  padding-bottom: var(--space-3);
  border-bottom: 1px solid var(--border);
}

/* Callouts */
.tip-box, .mistake-box, .practice-box {
  padding: var(--space-4);
  border-radius: var(--radius-md);
  margin: var(--space-3) 0;
  border: 1px solid var(--border);
}

.tip-box {
  border-left: 3px solid var(--accent-warm);
  background: var(--warning-soft);
}

.mistake-box {
  border-left: 3px solid var(--danger);
  background: var(--danger-soft);
}

.practice-box {
  border-left: 3px solid var(--success);
  background: var(--success-soft);
}

/* Table */
.table-wrap { overflow-x: auto; margin: var(--space-3) 0; }

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.875rem;
}

th, td {
  border: 1px solid var(--border);
  padding: var(--space-3) var(--space-4);
  text-align: left;
}

th {
  background: var(--surface-muted);
  font-weight: 600;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--text-muted);
}

tr:hover td { background: var(--surface-muted); }

/* Exam */
.exam-q {
  margin-bottom: var(--space-6);
  padding-bottom: var(--space-6);
  border-bottom: 1px solid var(--border);
}

.exam-q:last-child { border-bottom: none; }

.exam-type {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 0.6875rem;
  font-weight: 500;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--accent);
  background: var(--accent-soft);
  padding: 2px 8px;
  border-radius: var(--radius-full);
  margin-right: var(--space-2);
}

/* Study plan */
.study-day {
  border-left: 3px solid var(--accent);
  padding-left: var(--space-4);
}

/* Toast */
.toast {
  position: fixed;
  bottom: var(--space-6);
  right: var(--space-6);
  padding: var(--space-3) var(--space-5);
  background: var(--text);
  color: var(--canvas);
  border-radius: var(--radius-md);
  font-size: 0.875rem;
  font-weight: 500;
  box-shadow: 0 8px 32px oklch(0 0 0 / 0.15);
  z-index: 200;
  opacity: 0;
  transform: translateY(12px);
  transition: opacity 0.3s var(--ease-out), transform 0.3s var(--ease-out);
  pointer-events: none;
}

.toast.show {
  opacity: 1;
  transform: translateY(0);
}

/* Version badge */
.version-pill {
  font-size: 0.625rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 2px 6px;
  border-radius: var(--radius-full);
  background: var(--accent-soft);
  color: var(--accent);
  border: 1px solid var(--border);
  vertical-align: middle;
  margin-left: var(--space-2);
}

/* Responsive */
@media (max-width: 860px) {
  .menu-toggle { display: block; }
  nav.sidebar {
    position: fixed;
    left: calc(-1 * var(--sidebar-width) - 8px);
    top: 57px;
    transition: left 0.3s var(--ease-out);
    z-index: 99;
    box-shadow: 8px 0 32px oklch(0 0 0 / 0.08);
  }
  nav.sidebar.open { left: 0; }
  .layout { display: block; }
  main.content { padding: var(--space-4); max-width: none; }
  .header-actions { margin-left: 0; }
  .progress-bar-wrap { order: 3; width: 100%; max-width: none; }
}

@media (max-width: 480px) {
  .hero { padding: var(--space-5); }
  .card { padding: var(--space-4); }
  .flashcard-grid { grid-template-columns: 1fr; }
}
"""
