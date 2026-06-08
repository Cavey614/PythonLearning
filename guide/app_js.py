APP_JS = r"""
const STORAGE_KEY = 'pythonStudyGuideProgress';

function loadProgress() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
  catch { return {}; }
}
function saveProgress(data) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
}
function markComplete(key) {
  const p = loadProgress();
  p[key] = true;
  saveProgress(p);
  updateProgressBar();
}
function isComplete(key) { return !!loadProgress()[key]; }

function updateProgressBar() {
  const p = loadProgress();
  const total = 12 + 11 + 1;
  let done = 0;
  for (let d = 1; d <= 12; d++) if (p['day-' + d]) done++;
  for (let r of DATA.review) if (p['review-' + r.id]) done++;
  if (p['exam']) done++;
  const pct = Math.round((done / total) * 100);
  document.getElementById('progressFill').style.width = pct + '%';
  document.getElementById('progressLabel').textContent = 'Progress: ' + done + '/' + total + ' (' + pct + '%)';
}

function esc(s) {
  const d = document.createElement('div');
  d.textContent = s;
  return d.innerHTML;
}

function renderCode(code) {
  return '<pre><code>' + esc(code) + '</code></pre>';
}

function accordion(title, body, open) {
  return `<div class="accordion${open ? ' open' : ''}">
    <button class="accordion-btn" onclick="toggleAccordion(this)">${esc(title)}<span class="chev">▼</span></button>
    <div class="accordion-body">${body}</div></div>`;
}

function toggleAccordion(btn) {
  btn.parentElement.classList.toggle('open');
}

function renderFlashcards(cards, id) {
  return cards.map((c, i) => `
    <div class="flashcard" onclick="this.classList.toggle('flipped')" id="${id}-fc-${i}">
      <div class="flashcard-inner">
        <div class="flashcard-front"><strong>Q:</strong> ${esc(c.q)}</div>
        <div class="flashcard-back"><strong>A:</strong> ${esc(c.a)}</div>
      </div></div>`).join('');
}

function renderPredict(items, id) {
  return items.map((item, i) => `
    <div class="quiz-block" id="${id}-pred-${i}">
      <pre><code>${esc(item.code)}</code></pre>
      <input type="text" class="fill-blank" placeholder="Your prediction" id="${id}-pred-in-${i}">
      <button class="btn btn-primary btn-sm" onclick="checkPredict('${id}',${i},${JSON.stringify(item.answer).replace(/"/g,'&quot;')},${JSON.stringify(item.explain).replace(/"/g,'&quot;')})">Check</button>
      <div id="${id}-pred-fb-${i}"></div></div>`).join('');
}

function checkPredict(prefix, i, answer, explain) {
  const val = document.getElementById(prefix + '-pred-in-' + i).value.trim();
  const fb = document.getElementById(prefix + '-pred-fb-' + i);
  const block = document.getElementById(prefix + '-pred-' + i);
  const ok = val.toLowerCase() === String(answer).toLowerCase();
  block.classList.remove('correct','wrong');
  block.classList.add(ok ? 'correct' : 'wrong');
  fb.className = 'feedback ' + (ok ? 'ok' : 'bad');
  fb.innerHTML = (ok ? '✓ Correct! ' : '✗ Expected: ' + esc(answer) + '. ') + esc(explain);
}

function renderFill(items, id) {
  return items.map((item, i) => `
    <div class="quiz-block" id="${id}-fill-${i}">
      <p>${esc(item.text)}</p>
      <input type="text" id="${id}-fill-in-${i}" placeholder="Answer">
      <button class="btn btn-primary btn-sm" onclick="checkFill('${id}',${i})">Check</button>
      <div id="${id}-fill-fb-${i}"></div></div>`).join('');
}

function checkFill(prefix, i) {
  const item = window._fillData[prefix][i];
  const val = document.getElementById(prefix + '-fill-in-' + i).value.trim().toLowerCase();
  const answers = [item.answer.toLowerCase(), ...(item.alt||[]).map(a=>a.toLowerCase())];
  const ok = answers.includes(val);
  const fb = document.getElementById(prefix + '-fill-fb-' + i);
  const block = document.getElementById(prefix + '-fill-' + i);
  block.classList.toggle('correct', ok);
  block.classList.toggle('wrong', !ok);
  fb.className = 'feedback ' + (ok ? 'ok' : 'bad');
  fb.textContent = ok ? '✓ Correct!' : '✗ Answer: ' + item.answer;
}

function renderMCQ(items, id) {
  return items.map((item, i) => `
    <div class="quiz-block" id="${id}-mcq-${i}">
      <p><strong>${esc(item.q)}</strong></p>
      <div class="quiz-options">${item.options.map((o,j)=>`
        <label><input type="radio" name="${id}-mcq-${i}" value="${j}"> ${esc(o)}</label>`).join('')}
      </div>
      <button class="btn btn-primary btn-sm" onclick="checkMCQ('${id}',${i},${item.answer},${JSON.stringify(item.explain).replace(/"/g,'&quot;')})">Check</button>
      <div id="${id}-mcq-fb-${i}"></div></div>`).join('');
}

function checkMCQ(prefix, i, answer, explain) {
  const sel = document.querySelector(`input[name="${prefix}-mcq-${i}"]:checked`);
  const fb = document.getElementById(prefix + '-mcq-fb-' + i);
  const block = document.getElementById(prefix + '-mcq-' + i);
  if (!sel) { fb.className='feedback bad'; fb.textContent='Select an option.'; return; }
  const ok = parseInt(sel.value) === answer;
  block.classList.toggle('correct', ok);
  block.classList.toggle('wrong', !ok);
  fb.className = 'feedback ' + (ok ? 'ok' : 'bad');
  fb.textContent = (ok ? '✓ Correct! ' : '✗ Incorrect. ') + explain;
}

function renderTF(items, id) {
  return items.map((item, i) => `
    <div class="quiz-block" id="${id}-tf-${i}">
      <p><strong>${esc(item.q)}</strong></p>
      <div class="quiz-options">
        <label><input type="radio" name="${id}-tf-${i}" value="true"> True</label>
        <label><input type="radio" name="${id}-tf-${i}" value="false"> False</label>
      </div>
      <button class="btn btn-primary btn-sm" onclick="checkTF('${id}',${i},${item.answer},${JSON.stringify(item.explain).replace(/"/g,'&quot;')})">Check</button>
      <div id="${id}-tf-fb-${i}"></div></div>`).join('');
}

function checkTF(prefix, i, answer, explain) {
  const sel = document.querySelector(`input[name="${prefix}-tf-${i}"]:checked`);
  const fb = document.getElementById(prefix + '-tf-fb-' + i);
  const block = document.getElementById(prefix + '-tf-' + i);
  if (!sel) { fb.className='feedback bad'; fb.textContent='Select True or False.'; return; }
  const ok = (sel.value === 'true') === answer;
  block.classList.toggle('correct', ok);
  block.classList.toggle('wrong', !ok);
  fb.className = 'feedback ' + (ok ? 'ok' : 'bad');
  fb.textContent = (ok ? '✓ Correct! ' : '✗ Incorrect. ') + explain;
}

function renderMatching(pairs, id) {
  const left = pairs.map((p,i)=>`<div class="drag-item" draggable="true" data-match="${i}" id="${id}-m-${i}">${esc(p[0])}</div>`).join('');
  const right = pairs.map((p,i)=>`
    <div class="match-row">
      <div class="drop-zone" data-accept="${i}" id="${id}-dz-${i}">${esc(p[1])}</div>
      <span id="${id}-match-fb-${i}"></span>
    </div>`).join('');
  return `<p>Drag each term to its matching definition:</p>
    <div class="grid-2"><div class="drag-area" id="${id}-pool">${left}</div><div>${right}</div></div>
    <button class="btn btn-primary btn-sm" onclick="checkMatching('${id}',${JSON.stringify(pairs).replace(/"/g,'&quot;')})">Check Matches</button>`;
}

function initDragDrop() {
  document.querySelectorAll('.drag-item').forEach(el => {
    el.addEventListener('dragstart', e => { e.dataTransfer.setData('text', el.id); });
  });
  document.querySelectorAll('.drop-zone').forEach(zone => {
    zone.addEventListener('dragover', e => e.preventDefault());
    zone.addEventListener('drop', e => {
      e.preventDefault();
      const id = e.dataTransfer.getData('text');
      const item = document.getElementById(id);
      if (item) { zone.innerHTML = ''; zone.appendChild(item); zone.classList.add('filled'); }
    });
  });
}

function checkMatching(id, pairs) {
  pairs.forEach((p, i) => {
    const zone = document.getElementById(id + '-dz-' + i);
    const item = zone.querySelector('.drag-item');
    const fb = document.getElementById(id + '-match-fb-' + i);
    const ok = item && parseInt(item.dataset.match) === i;
    fb.textContent = ok ? '✓' : '✗';
    fb.style.color = ok ? 'var(--success)' : 'var(--danger)';
  });
}

function renderDayTest(test, id) {
  return test.map((item, i) => {
    if (item.type === 'mcq') {
      return `<div class="quiz-block"><p><strong>Q${i+1}:</strong> ${esc(item.q)}</p>
        <div class="quiz-options">${item.options.map((o,j)=>`<label><input type="radio" name="${id}-test-${i}" value="${j}"> ${esc(o)}</label>`).join('')}
        </div><button class="btn btn-sm btn-primary" onclick="checkDayTestMCQ('${id}',${i},${item.answer},${JSON.stringify(item.explain).replace(/"/g,'&quot;')})">Check</button>
        <div id="${id}-test-fb-${i}"></div></div>`;
    }
    if (item.type === 'predict') {
      return `<div class="quiz-block"><p><strong>Q${i+1}:</strong></p><pre><code>${esc(item.q)}</code></pre>
        <input type="text" id="${id}-test-in-${i}"><button class="btn btn-sm btn-primary" onclick="checkDayTestPred('${id}',${i},${JSON.stringify(item.answer).replace(/"/g,'&quot;')},${JSON.stringify(item.explain).replace(/"/g,'&quot;')})">Check</button>
        <div id="${id}-test-fb-${i}"></div></div>`;
    }
    if (item.type === 'tf') {
      return `<div class="quiz-block"><p><strong>Q${i+1}:</strong> ${esc(item.q)}</p>
        <label><input type="radio" name="${id}-test-tf-${i}" value="true"> True</label>
        <label><input type="radio" name="${id}-test-tf-${i}" value="false"> False</label>
        <button class="btn btn-sm btn-primary" onclick="checkDayTestTF('${id}',${i},${item.answer},${JSON.stringify(item.explain).replace(/"/g,'&quot;')})">Check</button>
        <div id="${id}-test-fb-${i}"></div></div>`;
    }
    if (item.type === 'fill') {
      return `<div class="quiz-block"><p><strong>Q${i+1}:</strong> ${esc(item.q)}</p>
        <input type="text" id="${id}-test-in-${i}"><button class="btn btn-sm btn-primary" onclick="checkDayTestPred('${id}',${i},${JSON.stringify(item.answer).replace(/"/g,'&quot;')},${JSON.stringify(item.explain).replace(/"/g,'&quot;')})">Check</button>
        <div id="${id}-test-fb-${i}"></div></div>`;
    }
    return '';
  }).join('');
}

function checkDayTestMCQ(id, i, ans, exp) {
  const sel = document.querySelector(`input[name="${id}-test-${i}"]:checked`);
  const fb = document.getElementById(id + '-test-fb-' + i);
  if (!sel) { fb.className='feedback bad'; fb.textContent='Select an answer.'; return; }
  const ok = parseInt(sel.value) === ans;
  fb.className = 'feedback ' + (ok?'ok':'bad');
  fb.textContent = (ok?'✓ ':'✗ ') + exp;
}

function checkDayTestPred(id, i, ans, exp) {
  const val = document.getElementById(id + '-test-in-' + i).value.trim();
  const ok = val.toLowerCase() === String(ans).toLowerCase();
  const fb = document.getElementById(id + '-test-fb-' + i);
  fb.className = 'feedback ' + (ok?'ok':'bad');
  fb.textContent = (ok?'✓ Correct! ':'✗ Expected: '+ans+'. ') + exp;
}

function checkDayTestTF(id, i, ans, exp) {
  const sel = document.querySelector(`input[name="${id}-test-tf-${i}"]:checked`);
  const fb = document.getElementById(id + '-test-fb-' + i);
  if (!sel) { fb.className='feedback bad'; fb.textContent='Select T/F.'; return; }
  const ok = (sel.value==='true')===ans;
  fb.className = 'feedback ' + (ok?'ok':'bad');
  fb.textContent = (ok?'✓ ':'✗ ') + exp;
}

function renderDay(day) {
  const id = 'day' + day.day;
  window._fillData = window._fillData || {};
  window._fillData[id] = day.fill_blank;
  const topics = day.topics.map(t => `<span class="tag">${esc(t)}</span>`).join('');
  const objs = day.objectives.map(o => `<li>${esc(o)}</li>`).join('');
  const expl = day.explanations.map(e => accordion(e.title, `<p>${esc(e.body)}</p>${renderCode(e.code)}`)).join('');
  const beg = day.beginner_examples.map(e => `<h4>${esc(e.title)}</h4>${renderCode(e.code)}`).join('');
  const rw = day.real_world.map(r => `<li>${esc(r)}</li>`).join('');
  const mis = day.mistakes.map(m => `<li>${esc(m)}</li>`).join('');
  const bp = day.best_practices.map(b => `<li>${esc(b)}</li>`).join('');
  const mem = day.memory_tricks.map(m => `<li>${esc(m)}</li>`).join('');
  const take = day.takeaways.map(t => `<li>${esc(t)}</li>`).join('');
  const done = isComplete('day-' + day.day);

  return `<div class="hero">
    <h1>Day ${day.day}: ${esc(day.title)}</h1>
    <p>Angela Yu's 100 Days of Python — Complete study module</p>
    ${topics}
  </div>
  <div class="card">
    <h2>Learning Objectives</h2><ul>${objs}</ul>
    ${done ? '<span class="badge badge-done">Completed</span>' : '<span class="badge badge-todo">In Progress</span>'}
    <button class="btn btn-success btn-sm" onclick="markComplete('day-${day.day}');showSection('day-${day.day}')">Mark Day Complete</button>
  </div>
  <div class="card"><h2>Detailed Explanations</h2>${expl}</div>
  <div class="card"><h2>Beginner Examples</h2>${beg}</div>
  <div class="card"><h2>Real-World Examples</h2><ul>${rw}</ul></div>
  <div class="card"><h2>Common Mistakes</h2><div class="mistake-box"><ul>${mis}</ul></div></div>
  <div class="card"><h2>Best Practices</h2><div class="practice-box"><ul>${bp}</ul></div></div>
  <div class="card"><h2>Memory Tricks</h2><div class="tip-box"><ul>${mem}</ul></div></div>
  <div class="card"><h2>Key Takeaways</h2><ul>${take}</ul></div>
  <div class="card"><h2>Flashcards <small>(click to flip)</small></h2>${renderFlashcards(day.flashcards, id)}</div>
  <div class="card"><h2>Predict the Output</h2>${renderPredict(day.predict, id)}</div>
  <div class="card"><h2>Fill in the Blank</h2>${renderFill(day.fill_blank, id)}</div>
  <div class="card"><h2>Multiple Choice</h2>${renderMCQ(day.mcq, id)}</div>
  <div class="card"><h2>True or False</h2>${renderTF(day.true_false, id)}</div>
  <div class="card"><h2>Drag & Drop Matching</h2>${renderMatching(day.matching.pairs, id + '-match')}</div>
  <div class="card"><h2>End-of-Day Test</h2>${renderDayTest(day.day_test, id + '-daytest')}</div>`;
}

function renderHome() {
  return `<div class="hero">
    <h1>🐍 Python Days 1–12 Study Guide</h1>
    <p>Angela Yu's 100 Days of Python — interactive, self-contained reference with quizzes, projects, and a 100-question final exam.</p>
  </div>
  <div class="grid-2">
    <div class="card"><h2>What's Inside</h2><ul>
      <li>12 complete day modules with objectives, examples, and quizzes</li>
      <li>11 dedicated review topics</li>
      <li>13 project breakdowns</li>
      <li>7-day intensive study plan</li>
      <li>100-question final exam with explanations</li>
      <li>Progress saved in localStorage</li>
    </ul></div>
    <div class="card"><h2>How to Study</h2><ol>
      <li>Work through Days 1–12 in order</li>
      <li>Complete flashcards and end-of-day tests</li>
      <li>Build each project from the Projects section</li>
      <li>Follow the 7-day study plan for intensive prep</li>
      <li>Take the final exam — aim for 80%+</li>
    </ol></div>
  </div>
  <div class="card"><h2>Course Days Overview</h2>
    <table><tr><th>Day</th><th>Topic</th><th>Project</th><th>Status</th></tr>
    ${DATA.days.map(d => `<tr><td>${d.day}</td><td>${esc(d.title)}</td><td>${esc(d.topics[d.topics.length-1])}</td>
      <td>${isComplete('day-'+d.day)?'<span class="badge badge-done">Done</span>':'<span class="badge badge-todo">Todo</span>'}</td></tr>`).join('')}
    </table></div>`;
}

function renderReview() {
  return `<h2 class="section-title">Topic Review</h2>` + DATA.review.map(r => {
    const done = isComplete('review-' + r.id);
    return `<div class="card" id="review-${r.id}">
      <h2>${esc(r.title)} ${done?'<span class="badge badge-done">Reviewed</span>':''}</h2>
      <p>${esc(r.summary)}</p>
      <h3>Key Points</h3><ul>${r.key_points.map(k=>`<li>${esc(k)}</li>`).join('')}</ul>
      ${renderCode(r.code)}
      <button class="btn btn-success btn-sm" onclick="markComplete('review-${r.id}')">Mark Reviewed</button>
    </div>`;
  }).join('');
}

function renderProjects() {
  return `<h2 class="section-title">Project Breakdowns</h2>` + DATA.projects.map(p => `
    <div class="card">
      <h2>${esc(p.name)} <span class="tag">Day ${p.day}</span></h2>
      <p><strong>Concepts:</strong> ${p.concepts.map(c=>`<span class="tag">${esc(c)}</span>`).join('')}</p>
      <h3>Steps</h3><ol>${p.steps.map(s=>`<li>${esc(s)}</li>`).join('')}</ol>
      <div class="tip-box"><strong>Extension:</strong> ${esc(p.extension)}</div>
    </div>`).join('');
}

function renderStudyPlan() {
  const sp = DATA.studyPlan;
  const days = sp.days.map(d => `
    <div class="study-day card">
      <h3>Calendar Day ${d.day}: ${esc(d.focus)}</h3>
      <h4>Schedule</h4><ul>${d.schedule.map(s=>`<li>${esc(s)}</li>`).join('')}</ul>
      <h4>Memorization Targets</h4><ul>${d.memorize.map(m=>`<li>${esc(m)}</li>`).join('')}</ul>
      <h4>Practice Goals</h4><ul>${d.practice.map(p=>`<li>${esc(p)}</li>`).join('')}</ul>
      <p><em>Spaced repetition:</em> ${esc(d.repeat)}</p>
    </div>`).join('');
  return `<h2 class="section-title">${esc(sp.title)}</h2>
    <div class="card"><p>${esc(sp.overview)}</p>
    <h3>Spaced Repetition Strategy</h3><ul>${sp.spaced_repetition.map(s=>`<li>${esc(s)}</li>`).join('')}</ul>
    <h3>Overall Goals</h3><ul>${sp.goals.map(g=>`<li>${esc(g)}</li>`).join('')}</ul></div>${days}`;
}

function renderExam() {
  const saved = loadProgress().examAnswers || {};
  const questions = DATA.exam.map((q, i) => {
    let body = `<div class="exam-q" id="exam-q-${i}"><p><strong>Q${i+1}.</strong> [${q.type.toUpperCase()}] ${esc(q.q).replace(/\\n/g,'<br>')}</p>`;
    if (q.type === 'mcq') {
      body += `<div class="quiz-options">${q.options.map((o,j)=>`
        <label><input type="radio" name="exam-${i}" value="${j}" ${saved[i]===String(j)?'checked':''}> ${esc(o)}</label>`).join('')}</div>`;
    } else if (q.type === 'tf') {
      body += `<label><input type="radio" name="exam-${i}" value="true" ${saved[i]==='true'?'checked':''}> True</label>
        <label><input type="radio" name="exam-${i}" value="false" ${saved[i]==='false'?'checked':''}> False</label>`;
    } else {
      body += `<input type="text" id="exam-in-${i}" value="${esc(saved[i]||'')}" placeholder="Your answer" style="width:100%;max-width:400px;padding:.5rem;background:#0b1220;border:1px solid var(--surface2);color:var(--text);border-radius:6px;">`;
    }
    body += `<div id="exam-fb-${i}"></div></div>`;
    return body;
  }).join('');

  return `<h2 class="section-title">Final Exam — 100 Questions</h2>
    <div class="card"><p>Answer all questions, then submit. Progress auto-saves to localStorage as you go.</p>
    <button class="btn btn-primary" onclick="saveExamProgress()">Save Progress</button>
    <button class="btn btn-success" onclick="submitExam()">Submit & Grade Exam</button>
    <button class="btn btn-secondary" onclick="showExamKey()">Show Answer Key</button>
    <div id="exam-score"></div></div>
    <div class="card">${questions}</div>
    <div class="card hidden" id="exam-key"><h2>Answer Key</h2>${DATA.exam.map((q,i)=>{
      let ans = q.type==='mcq' ? q.options[q.answer] : q.type==='tf' ? (q.answer?'True':'False') : q.answer;
      return `<p><strong>Q${i+1}:</strong> ${esc(String(ans))} — ${esc(q.explain)}</p>`;
    }).join('')}</div>`;
}

function saveExamProgress() {
  const answers = {};
  DATA.exam.forEach((q, i) => {
    if (q.type === 'mcq' || q.type === 'tf') {
      const sel = document.querySelector(`input[name="exam-${i}"]:checked`);
      if (sel) answers[i] = sel.value;
    } else {
      const inp = document.getElementById('exam-in-' + i);
      if (inp && inp.value) answers[i] = inp.value;
    }
  });
  const p = loadProgress();
  p.examAnswers = answers;
  saveProgress(p);
  alert('Exam progress saved!');
}

function submitExam() {
  saveExamProgress();
  let score = 0;
  DATA.exam.forEach((q, i) => {
    const fb = document.getElementById('exam-fb-' + i);
    let ok = false;
    if (q.type === 'mcq') {
      const sel = document.querySelector(`input[name="exam-${i}"]:checked`);
      ok = sel && parseInt(sel.value) === q.answer;
    } else if (q.type === 'tf') {
      const sel = document.querySelector(`input[name="exam-${i}"]:checked`);
      ok = sel && (sel.value === 'true') === q.answer;
    } else {
      const inp = document.getElementById('exam-in-' + i);
      ok = inp && inp.value.trim().toLowerCase() === String(q.answer).toLowerCase();
    }
    if (ok) score++;
    if (fb) {
      fb.className = 'feedback ' + (ok?'ok':'bad');
      fb.textContent = ok ? '✓ Correct' : '✗ ' + q.explain;
    }
  });
  const pct = Math.round((score/100)*100);
  document.getElementById('exam-score').innerHTML = `<div class="feedback ${pct>=80?'ok':'bad'}" style="margin-top:1rem;font-size:1.2rem">
    Score: ${score}/100 (${pct}%) ${pct>=80?'— Great job! 🎉':'— Review weak areas and retry.'}</div>`;
  if (pct >= 80) markComplete('exam');
}

function showExamKey() {
  document.getElementById('exam-key').classList.toggle('hidden');
}

function showSection(id) {
  document.querySelectorAll('.nav-link').forEach(l => l.classList.toggle('active', l.dataset.section === id));
  const main = document.getElementById('main-content');
  if (id === 'home') main.innerHTML = renderHome();
  else if (id === 'review') main.innerHTML = renderReview();
  else if (id === 'projects') main.innerHTML = renderProjects();
  else if (id === 'study-plan') main.innerHTML = renderStudyPlan();
  else if (id === 'exam') main.innerHTML = renderExam();
  else if (id.startsWith('day-')) {
    const n = parseInt(id.split('-')[1]);
    const day = DATA.days.find(d => d.day === n);
    if (day) main.innerHTML = renderDay(day);
    initDragDrop();
  }
  if (id !== 'home') window.scrollTo(0, 0);
  updateProgressBar();
}

function toggleSidebar() {
  document.getElementById('sidebar').classList.toggle('open');
}

function init() {
  showSection('home');
  updateProgressBar();
}
document.addEventListener('DOMContentLoaded', init);
"""
