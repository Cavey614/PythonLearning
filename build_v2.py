#!/usr/bin/env python3
"""Generate index-v2.html with Impeccable-style design system."""
import json
import re
from pathlib import Path

from guide.styles_v2 import CSS
from guide.app_js import APP_JS
from guide.days import get_days
from guide.content_misc import get_review, get_projects, get_study_plan, get_exam

OUTPUT = Path(__file__).parent / "index-v2.html"

V2_JS = r"""
const THEME_KEY = 'pythonStudyGuideTheme';

function toast(msg) {
  let el = document.getElementById('toast');
  if (!el) {
    el = document.createElement('div');
    el.id = 'toast';
    el.className = 'toast';
    el.setAttribute('role', 'status');
    document.body.appendChild(el);
  }
  el.textContent = msg;
  el.classList.add('show');
  clearTimeout(toast._t);
  toast._t = setTimeout(() => el.classList.remove('show'), 2800);
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem(THEME_KEY, theme);
  const btn = document.getElementById('themeToggle');
  if (btn) btn.textContent = theme === 'dark' ? '☀' : '☾';
  btn?.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
}

function toggleTheme() {
  const cur = document.documentElement.getAttribute('data-theme') || 'light';
  applyTheme(cur === 'dark' ? 'light' : 'dark');
}

function countCompletedDays() {
  let n = 0;
  for (let d = 1; d <= 12; d++) if (isComplete('day-' + d)) n++;
  return n;
}
"""

# Patch render functions for v2 UI
RENDER_FLASHCARDS_V2 = """
function renderFlashcards(cards, id) {
  const inner = cards.map((c, i) => `
    <div class="flashcard" onclick="this.classList.toggle('flipped')" id="${id}-fc-${i}" role="button" tabindex="0" onkeydown="if(event.key==='Enter'||event.key===' ')this.click()">
      <div class="flashcard-inner">
        <div class="flashcard-front"><strong>Q</strong> ${esc(c.q)}</div>
        <div class="flashcard-back"><strong>A</strong> ${esc(c.a)}</div>
      </div></div>`).join('');
  return `<p class="flashcard-hint">Click a card to reveal the answer</p><div class="flashcard-grid">${inner}</div>`;
}
"""

RENDER_HOME_V2 = """
function renderHome() {
  const daysDone = countCompletedDays();
  return `<div class="hero">
    <div class="section-label">Angela Yu · 100 Days of Python</div>
    <h1>Days 1–12 Study Guide</h1>
    <p>Master variables through scope in seven focused days. Every lesson, quiz, project, and the 100-question final exam — in one calm, self-contained page.</p>
    <div class="hero-stats">
      <div class="stat"><span class="stat-value">12</span><span class="stat-label">Day modules</span></div>
      <div class="stat"><span class="stat-value">100</span><span class="stat-label">Exam questions</span></div>
      <div class="stat"><span class="stat-value">${daysDone}/12</span><span class="stat-label">Days complete</span></div>
    </div>
  </div>
  <div class="grid-2">
    <div class="card">
      <div class="section-label">Contents</div>
      <h2>What's inside</h2>
      <ul>
        <li>12 day modules — objectives, examples, interactive drills</li>
        <li>11 topic review sheets with code samples</li>
        <li>13 project walkthroughs (Band Name → Blackjack)</li>
        <li>7-day intensive study schedule</li>
        <li>Progress saved automatically in your browser</li>
      </ul>
    </div>
    <div class="card">
      <div class="section-label">Method</div>
      <h2>How to study</h2>
      <ol>
        <li>Work Days 1–12 in order from the sidebar</li>
        <li>Flip flashcards and pass each end-of-day test</li>
        <li>Build projects from the Projects section</li>
        <li>Follow the 7-day plan for exam prep</li>
        <li>Score 80%+ on the final exam</li>
      </ol>
    </div>
  </div>
  <div class="card">
    <div class="section-label">Overview</div>
    <h2>Course progress</h2>
    <div class="table-wrap">
      <table>
        <tr><th>Day</th><th>Topic</th><th>Capstone</th><th>Status</th></tr>
        ${DATA.days.map(d => `<tr>
          <td><span class="nav-num">${String(d.day).padStart(2,'0')}</span></td>
          <td>${esc(d.title)}</td>
          <td>${esc(d.topics[d.topics.length-1])}</td>
          <td>${isComplete('day-'+d.day)?'<span class="badge badge-done">Done</span>':'<span class="badge badge-todo">Todo</span>'}</td>
        </tr>`).join('')}
      </table>
    </div>
  </div>`;
}
"""

RENDER_DAY_V2 = """
function renderDay(day) {
  const id = 'day' + day.day;
  window._fillData = window._fillData || {};
  window._fillData[id] = day.fill_blank;
  const topics = day.topics.map(t => `<span class="tag">${esc(t)}</span>`).join('');
  const objs = day.objectives.map(o => `<li>${esc(o)}</li>`).join('');
  const expl = day.explanations.map((e, i) => accordion(e.title, `<p>${esc(e.body)}</p>${renderCode(e.code)}`, i === 0)).join('');
  const beg = day.beginner_examples.map(e => `<h4>${esc(e.title)}</h4>${renderCode(e.code)}`).join('');
  const rw = day.real_world.map(r => `<li>${esc(r)}</li>`).join('');
  const mis = day.mistakes.map(m => `<li>${esc(m)}</li>`).join('');
  const bp = day.best_practices.map(b => `<li>${esc(b)}</li>`).join('');
  const mem = day.memory_tricks.map(m => `<li>${esc(m)}</li>`).join('');
  const take = day.takeaways.map(t => `<li>${esc(t)}</li>`).join('');
  const done = isComplete('day-' + day.day);

  return `<div class="hero">
    <div class="section-label">Day ${day.day} of 12</div>
    <h1>${esc(day.title)}</h1>
    <p>Complete study module with lessons, drills, and an end-of-day test.</p>
    <div style="margin-top:1rem">${topics}</div>
  </div>
  <div class="card">
    <div class="card-header">
      <div><div class="section-label">Goals</div><h2>Learning objectives</h2></div>
      ${done ? '<span class="badge badge-done">Completed</span>' : '<span class="badge badge-todo">In progress</span>'}
    </div>
    <ul>${objs}</ul>
    <div class="btn-row">
      <button class="btn btn-success btn-sm" onclick="markComplete('day-${day.day}');showSection('day-${day.day}');toast('Day ${day.day} marked complete')">Mark day complete</button>
    </div>
  </div>
  <div class="card"><div class="section-label">Learn</div><h2>Detailed explanations</h2>${expl}</div>
  <div class="card"><div class="section-label">Practice</div><h2>Beginner examples</h2>${beg}</div>
  <div class="card"><h2>Real-world examples</h2><ul>${rw}</ul></div>
  <div class="card"><h2>Common mistakes</h2><div class="mistake-box"><ul>${mis}</ul></div></div>
  <div class="card"><h2>Best practices</h2><div class="practice-box"><ul>${bp}</ul></div></div>
  <div class="card"><h2>Memory tricks</h2><div class="tip-box"><ul>${mem}</ul></div></div>
  <div class="card"><h2>Key takeaways</h2><ul>${take}</ul></div>
  <div class="card"><div class="section-label">Recall</div><h2>Flashcards</h2>${renderFlashcards(day.flashcards, id)}</div>
  <div class="card"><div class="section-label">Drill</div><h2>Predict the output</h2>${renderPredict(day.predict, id)}</div>
  <div class="card"><h2>Fill in the blank</h2>${renderFill(day.fill_blank, id)}</div>
  <div class="card"><h2>Multiple choice</h2>${renderMCQ(day.mcq, id)}</div>
  <div class="card"><h2>True or false</h2>${renderTF(day.true_false, id)}</div>
  <div class="card"><h2>Drag & drop matching</h2>${renderMatching(day.matching.pairs, id + '-match')}</div>
  <div class="card"><div class="section-label">Assessment</div><h2>End-of-day test</h2>${renderDayTest(day.day_test, id + '-daytest')}</div>`;
}
"""

RENDER_EXAM_V2 = """
function renderExam() {
  const saved = loadProgress().examAnswers || {};
  const questions = DATA.exam.map((q, i) => {
    let body = `<div class="exam-q" id="exam-q-${i}">
      <p><strong>Q${i+1}.</strong> <span class="exam-type">${q.type}</span> ${esc(q.q).split(String.fromCharCode(10)).join('<br>')}</p>`;
    if (q.type === 'mcq') {
      body += `<div class="quiz-options">${q.options.map((o,j)=>`
        <label><input type="radio" name="exam-${i}" value="${j}" ${saved[i]===String(j)?'checked':''}> ${esc(o)}</label>`).join('')}</div>`;
    } else if (q.type === 'tf') {
      body += `<div class="quiz-options">
        <label><input type="radio" name="exam-${i}" value="true" ${saved[i]==='true'?'checked':''}> True</label>
        <label><input type="radio" name="exam-${i}" value="false" ${saved[i]==='false'?'checked':''}> False</label>
      </div>`;
    } else {
      body += `<input type="text" class="exam-input" id="exam-in-${i}" value="${esc(saved[i]||'')}" placeholder="Your answer">`;
    }
    body += `<div id="exam-fb-${i}"></div></div>`;
    return body;
  }).join('');

  return `<h2 class="section-title">Final exam</h2>
    <div class="card">
      <p>100 questions covering Days 1–12. Save progress anytime; aim for 80% to pass.</p>
      <div class="btn-row">
        <button class="btn btn-primary" onclick="saveExamProgress()">Save progress</button>
        <button class="btn btn-success" onclick="submitExam()">Submit & grade</button>
        <button class="btn btn-secondary" onclick="showExamKey()">Answer key</button>
      </div>
      <div id="exam-score"></div>
    </div>
    <div class="card">${questions}</div>
    <div class="card hidden" id="exam-key">
      <h2>Answer key</h2>
      ${DATA.exam.map((q,i)=>{
        let ans = q.type==='mcq' ? q.options[q.answer] : q.type==='tf' ? (q.answer?'True':'False') : q.answer;
        return `<p><strong>Q${i+1}:</strong> ${esc(String(ans))} — ${esc(q.explain)}</p>`;
      }).join('')}
    </div>`;
}
"""

SAVE_EXAM_V2 = "toast('Exam progress saved');"
INIT_V2 = """
function init() {
  applyTheme(localStorage.getItem(THEME_KEY) || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'));
  showSection('home');
  updateProgressBar();
}
document.addEventListener('DOMContentLoaded', init);
"""


def patch_js(base: str) -> str:
    js = base.replace("const STORAGE_KEY = 'pythonStudyGuideProgress';",
                      "const STORAGE_KEY = 'pythonStudyGuideProgress';\n" + V2_JS)
    js = re.sub(r"function renderFlashcards\(cards, id\) \{[\s\S]*?\n\}", RENDER_FLASHCARDS_V2.strip(), js, count=1)
    js = re.sub(r"function renderHome\(\) \{[\s\S]*?\n\}", RENDER_HOME_V2.strip(), js, count=1)
    js = re.sub(r"function renderDay\(day\) \{[\s\S]*?\n\}", RENDER_DAY_V2.strip(), js, count=1)
    js = re.sub(r"function renderExam\(\) \{[\s\S]*?\n\}", RENDER_EXAM_V2.strip(), js, count=1)
    js = js.replace("alert('Exam progress saved!');", SAVE_EXAM_V2)
    js = re.sub(r"function init\(\) \{[\s\S]*?document\.addEventListener\('DOMContentLoaded', init\);",
                INIT_V2.strip(), js, count=1)
    return js


def build_html():
    data = {
        "days": get_days(),
        "review": get_review(),
        "projects": get_projects(),
        "studyPlan": get_study_plan(),
        "exam": get_exam(),
    }
    data_json = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    app_js = patch_js(APP_JS)

    nav_days = "\n".join(
        f'        <button class="nav-link" data-section="day-{d["day"]}" onclick="showSection(\'day-{d["day"]}\');toggleSidebar(false)">'
        f'<span class="nav-num">{d["day"]:02d}</span> {d["title"]}</button>'
        for d in data["days"]
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Python Days 1–12 Study Guide · v2</title>
  <meta name="description" content="Impeccable-style interactive study guide for Angela Yu's 100 Days of Python Days 1–12.">
  <style>
{CSS}
  </style>
</head>
<body>
  <header>
    <div class="header-inner">
      <div class="brand">
        <div class="brand-mark" aria-hidden="true">&gt;_</div>
        <div>
          <div class="logo">Code Classroom <span class="version-pill">v2</span></div>
          <span class="logo-sub">Python Days 1–12</span>
        </div>
      </div>
      <button class="menu-toggle" onclick="toggleSidebar()" aria-label="Open navigation">Menu</button>
      <div class="header-actions">
        <div class="progress-bar-wrap">
          <div class="progress-label" id="progressLabel">Progress 0%</div>
          <div class="progress-bar" role="progressbar" aria-valuemin="0" aria-valuemax="100"><div class="progress-fill" id="progressFill"></div></div>
        </div>
        <button class="theme-toggle" id="themeToggle" onclick="toggleTheme()" aria-label="Toggle theme">☾</button>
      </div>
    </div>
  </header>
  <div class="layout">
    <nav class="sidebar" id="sidebar" aria-label="Study guide navigation">
      <h3>Start</h3>
      <button class="nav-link active" data-section="home" onclick="showSection('home');toggleSidebar(false)">Overview</button>
      <h3>Days 1–12</h3>
{nav_days}
      <h3>Review</h3>
      <button class="nav-link" data-section="review" onclick="showSection('review');toggleSidebar(false)">Topic review</button>
      <button class="nav-link" data-section="projects" onclick="showSection('projects');toggleSidebar(false)">Projects</button>
      <button class="nav-link" data-section="study-plan" onclick="showSection('study-plan');toggleSidebar(false)">7-day plan</button>
      <button class="nav-link" data-section="exam" onclick="showSection('exam');toggleSidebar(false)">Final exam</button>
    </nav>
    <main class="content" id="main-content"></main>
  </div>
  <script>
    const DATA = {data_json};
{app_js}
function toggleSidebar(force) {{
  const sb = document.getElementById('sidebar');
  if (force === false) {{ sb.classList.remove('open'); return; }}
  sb.classList.toggle('open');
}}
  </script>
</body>
</html>
"""


def main():
    html = build_html()
    OUTPUT.write_text(html, encoding="utf-8")
    size = OUTPUT.stat().st_size
    print(f"Generated {OUTPUT}")
    print(f"File size: {size / 1024:.1f} KB ({size:,} bytes)")


if __name__ == "__main__":
    main()
