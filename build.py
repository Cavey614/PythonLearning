#!/usr/bin/env python3
"""Generate the Days 1-12 Python study guide HTML file."""
import json
from pathlib import Path

from guide.styles import CSS
from guide.app_js import APP_JS
from guide.days import get_days
from guide.content_misc import get_review, get_projects, get_study_plan, get_exam

OUTPUT = Path(__file__).parent / "index.html"


def build_html():
    data = {
        "days": get_days(),
        "review": get_review(),
        "projects": get_projects(),
        "studyPlan": get_study_plan(),
        "exam": get_exam(),
    }
    data_json = json.dumps(data, ensure_ascii=False)
    # Prevent </script> breakage in embedded JSON
    data_json = data_json.replace("</", "<\\/")

    nav_days = "\n".join(
        f'        <button class="nav-link" data-section="day-{d["day"]}" onclick="showSection(\'day-{d["day"]}\')">Day {d["day"]}: {d["title"]}</button>'
        for d in data["days"]
    )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Days 1-12 Study Guide | Angela Yu</title>
  <meta name="description" content="Interactive study guide for Angela Yu's 100 Days of Python Days 1-12 with quizzes, projects, and final exam.">
  <style>
{CSS}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <div class="logo">🐍 Python Days 1–12</div>
      <button class="menu-toggle" onclick="toggleSidebar()" aria-label="Toggle menu">☰ Menu</button>
      <div class="progress-bar-wrap">
        <div class="progress-label" id="progressLabel">Progress: 0%</div>
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
      </div>
    </div>
  </header>
  <div class="layout">
    <nav class="sidebar" id="sidebar">
      <h3>Guide</h3>
      <button class="nav-link active" data-section="home" onclick="showSection('home')">🏠 Home</button>
      <h3>Days 1–12</h3>
{nav_days}
      <h3>Review &amp; Practice</h3>
      <button class="nav-link" data-section="review" onclick="showSection('review')">📚 Topic Review</button>
      <button class="nav-link" data-section="projects" onclick="showSection('projects')">🛠 Projects</button>
      <button class="nav-link" data-section="study-plan" onclick="showSection('study-plan')">📅 7-Day Plan</button>
      <button class="nav-link" data-section="exam" onclick="showSection('exam')">📝 Final Exam (100Q)</button>
    </nav>
    <main class="content" id="main-content"></main>
  </div>
  <script>
    const DATA = {data_json};
{APP_JS}
  </script>
</body>
</html>
"""
    return html


def main():
    html = build_html()
    OUTPUT.write_text(html, encoding="utf-8")
    size_kb = OUTPUT.stat().st_size / 1024
    print(f"Generated {OUTPUT}")
    print(f"File size: {size_kb:.1f} KB ({OUTPUT.stat().st_size:,} bytes)")
    print(f"Days: {len(get_days())}, Review topics: {len(get_review())}, Projects: {len(get_projects())}, Exam questions: {len(get_exam())}")


if __name__ == "__main__":
    main()
