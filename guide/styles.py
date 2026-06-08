CSS = """
:root {
  --bg: #0f172a;
  --surface: #1e293b;
  --surface2: #334155;
  --text: #f1f5f9;
  --muted: #94a3b8;
  --accent: #38bdf8;
  --accent2: #818cf8;
  --success: #4ade80;
  --warning: #fbbf24;
  --danger: #f87171;
  --radius: 12px;
  --shadow: 0 4px 24px rgba(0,0,0,.35);
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Segoe UI,system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
header{position:sticky;top:0;z-index:100;background:rgba(15,23,42,.95);backdrop-filter:blur(8px);border-bottom:1px solid var(--surface2);padding:.75rem 1rem}
.header-inner{max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}
.logo{font-size:1.15rem;font-weight:700;background:linear-gradient(135deg,var(--accent),var(--accent2));-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.progress-bar-wrap{flex:1;min-width:140px;max-width:280px}
.progress-label{font-size:.75rem;color:var(--muted);margin-bottom:.25rem}
.progress-bar{height:8px;background:var(--surface2);border-radius:99px;overflow:hidden}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--accent),var(--success));transition:width .4s;width:0}
.layout{display:flex;max-width:1200px;margin:0 auto;min-height:calc(100vh - 60px)}
nav.sidebar{width:260px;flex-shrink:0;border-right:1px solid var(--surface2;padding:1rem;position:sticky;top:60px;height:calc(100vh - 60px);overflow-y:auto;background:var(--bg)}
nav.sidebar h3{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:1rem 0 .5rem}
nav.sidebar h3:first-child{margin-top:0}
.nav-link{display:block;padding:.45rem .65rem;border-radius:8px;color:var(--muted);font-size:.9rem;cursor:pointer;border:none;background:none;width:100%;text-align:left}
.nav-link:hover,.nav-link.active{background:var(--surface);color:var(--text)}
main.content{flex:1;padding:1.5rem;min-width:0}
.menu-toggle{display:none;background:var(--surface);border:1px solid var(--surface2);color:var(--text);padding:.5rem .75rem;border-radius:8px;cursor:pointer}
.hero{background:linear-gradient(135deg,rgba(56,189,248,.15),rgba(129,140,248,.15));border:1px solid var(--surface2);border-radius:var(--radius);padding:2rem;margin-bottom:1.5rem}
.hero h1{margin:0 0 .5rem;font-size:1.75rem}
.hero p{color:var(--muted);margin:0}
.card{background:var(--surface);border:1px solid var(--surface2);border-radius:var(--radius);padding:1.25rem;margin-bottom:1rem;box-shadow:var(--shadow)}
.card h2{margin:0 0 1rem;font-size:1.35rem;color:var(--accent)}
.card h3{margin:1.25rem 0 .5rem;font-size:1.05rem;color:var(--accent2)}
.card h4{margin:1rem 0 .35rem;font-size:.95rem}
.tag{display:inline-block;background:var(--surface2);color:var(--accent);padding:.15rem .55rem;border-radius:99px;font-size:.75rem;margin:.15rem .25rem .15rem 0}
ul,ol{padding-left:1.25rem}
li{margin:.35rem 0}
pre,code{font-family:Consolas,Monaco,monospace}
pre{background:#0b1220;border:1px solid var(--surface2);border-radius:8px;padding:1rem;overflow-x:auto;font-size:.85rem;margin:.75rem 0}
code{background:#0b1220;padding:.1rem .35rem;border-radius:4px;font-size:.85rem}
.accordion{border:1px solid var(--surface2);border-radius:8px;margin:.75rem 0;overflow:hidden}
.accordion-btn{width:100%;text-align:left;padding:.85rem 1rem;background:var(--surface2);border:none;color:var(--text);cursor:pointer;font-size:.95rem;display:flex;justify-content:space-between;align-items:center}
.accordion-btn:hover{background:#3d4f6a}
.accordion-body{display:none;padding:1rem;background:var(--surface)}
.accordion.open .accordion-body{display:block}
.accordion.open .accordion-btn .chev{transform:rotate(180deg)}
.chev{transition:transform .2s}
.grid-2{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1rem}
.flashcard{perspective:800px;height:160px;cursor:pointer;margin:.5rem 0}
.flashcard-inner{position:relative;width:100%;height:100%;transition:transform .5s;transform-style:preserve-3d}
.flashcard.flipped .flashcard-inner{transform:rotateY(180deg)}
.flashcard-front,.flashcard-back{position:absolute;width:100%;height:100%;backface-visibility:hidden;border-radius:8px;padding:1rem;display:flex;align-items:center;justify-content:center;text-align:center;border:1px solid var(--surface2)}
.flashcard-front{background:var(--surface2)}
.flashcard-back{background:#1a2744;transform:rotateY(180deg)}
.quiz-block{border:1px solid var(--surface2);border-radius:8px;padding:1rem;margin:1rem 0;background:#141f33}
.quiz-block.correct{border-color:var(--success);background:rgba(74,222,128,.08)}
.quiz-block.wrong{border-color:var(--danger);background:rgba(248,113,113,.08)}
.quiz-options{display:flex;flex-direction:column;gap:.5rem;margin:.75rem 0}
.quiz-options label{display:flex;align-items:center;gap:.5rem;padding:.55rem .75rem;background:var(--surface2);border-radius:8px;cursor:pointer}
.quiz-options label:hover{background:#3d4f6a}
.btn{padding:.55rem 1rem;border:none;border-radius:8px;cursor:pointer;font-size:.9rem;font-weight:600;transition:opacity .2s}
.btn:hover{opacity:.9}
.btn-primary{background:var(--accent);color:#0f172a}
.btn-secondary{background:var(--surface2);color:var(--text)}
.btn-success{background:var(--success);color:#0f172a}
.btn-sm{padding:.35rem .65rem;font-size:.8rem}
.feedback{margin-top:.75rem;padding:.75rem;border-radius:8px;font-size:.9rem}
.feedback.ok{background:rgba(74,222,128,.15);color:var(--success)}
.feedback.bad{background:rgba(248,113,113,.15);color:var(--danger)}
.fill-blank input{padding:.4rem .6rem;border:1px solid var(--surface2);border-radius:6px;background:#0b1220;color:var(--text);font-family:inherit;min-width:120px}
.drag-area{min-height:80px;border:2px dashed var(--surface2);border-radius:8px;padding:.75rem;display:flex;flex-wrap:wrap;gap:.5rem;align-items:center}
.drag-item,.drop-zone{padding:.45rem .75rem;background:var(--surface2);border-radius:8px;cursor:grab;user-select:none;font-size:.85rem}
.drop-zone{min-width:140px;min-height:44px;border:2px dashed var(--accent);background:rgba(56,189,248,.08);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:.25rem}
.drop-zone.filled{border-style:solid;background:rgba(74,222,128,.1)}
.match-row{display:flex;flex-wrap:wrap;gap:1rem;align-items:center;margin:.5rem 0}
.badge{display:inline-block;padding:.2rem .5rem;border-radius:99px;font-size:.7rem;font-weight:600}
.badge-done{background:rgba(74,222,128,.2);color:var(--success)}
.badge-todo{background:rgba(251,191,36,.2);color:var(--warning)}
.tabs{display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:1rem}
.tab{padding:.45rem .85rem;background:var(--surface2);border:none;border-radius:8px;color:var(--muted);cursor:pointer;font-size:.85rem}
.tab.active{background:var(--accent);color:#0f172a;font-weight:600}
.hidden{display:none!important}
.section-title{font-size:1.5rem;margin:0 0 1rem;padding-bottom:.5rem;border-bottom:2px solid var(--surface2)}
.tip-box{border-left:4px solid var(--warning);background:rgba(251,191,36,.08);padding:.75rem 1rem;border-radius:0 8px 8px 0;margin:.75rem 0}
.mistake-box{border-left:4px solid var(--danger);background:rgba(248,113,113,.08);padding:.75rem 1rem;border-radius:0 8px 8px 0;margin:.75rem 0}
.practice-box{border-left:4px solid var(--success);background:rgba(74,222,128,.08);padding:.75rem 1rem;border-radius:0 8px 8px 0;margin:.75rem 0}
table{width:100%;border-collapse:collapse;margin:.75rem 0;font-size:.9rem}
th,td{border:1px solid var(--surface2);padding:.55rem .75rem;text-align:left}
th{background:var(--surface2)}
.exam-q{margin-bottom:1.5rem;padding-bottom:1.5rem;border-bottom:1px solid var(--surface2)}
.exam-nav{display:flex;gap:.5rem;flex-wrap:wrap;margin:1rem 0}
.exam-nav button{min-width:36px}
.study-day{border-left:4px solid var(--accent2);padding-left:1rem;margin:1rem 0}
@media(max-width:768px){
  .menu-toggle{display:block}
  nav.sidebar{position:fixed;left:-280px;top:60px;transition:left .3s;z-index:99;box-shadow:var(--shadow)}
  nav.sidebar.open{left:0}
  .layout{display:block}
  main.content{padding:1rem}
}
"""
