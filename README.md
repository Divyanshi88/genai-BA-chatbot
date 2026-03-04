<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Business Strategy Generator — README</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --lime: #C8F135;
    --teal: #00D4B4;
    --coral: #FF5E62;
    --indigo: #1A1A2E;
    --violet: #6C3FE8;
    --sky: #38D9F5;
    --amber: #FFBE3C;
    --white: #F5F5F0;
    --card: #16213E;
    --muted: #8892A4;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--indigo);
    color: var(--white);
    font-family: 'Syne', sans-serif;
    overflow-x: hidden;
    line-height: 1.6;
  }

  /* ===== HERO ===== */
  .hero {
    position: relative;
    min-height: 340px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 60px 60px 50px;
    overflow: hidden;
  }

  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(ellipse 600px 400px at 80% 50%, rgba(108,63,232,0.35) 0%, transparent 70%),
      radial-gradient(ellipse 400px 300px at 10% 80%, rgba(0,212,180,0.25) 0%, transparent 70%),
      radial-gradient(ellipse 300px 300px at 50% 0%, rgba(200,241,53,0.12) 0%, transparent 60%);
  }

  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(200,241,53,0.12);
    border: 1px solid rgba(200,241,53,0.4);
    color: var(--lime);
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    padding: 6px 14px;
    border-radius: 20px;
    margin-bottom: 24px;
    width: fit-content;
    letter-spacing: 0.08em;
    position: relative;
    z-index: 1;
  }

  .hero-badge::before {
    content: '';
    width: 7px; height: 7px;
    border-radius: 50%;
    background: var(--lime);
    display: inline-block;
    animation: pulse 2s ease-in-out infinite;
  }

  @keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
  }

  .hero h1 {
    font-size: clamp(36px, 5vw, 64px);
    font-weight: 800;
    line-height: 1.05;
    position: relative;
    z-index: 1;
    max-width: 700px;
  }

  .hero h1 span.accent { color: var(--lime); }
  .hero h1 span.accent2 { color: var(--teal); }

  .hero-sub {
    color: var(--muted);
    font-size: 17px;
    margin-top: 16px;
    max-width: 500px;
    position: relative;
    z-index: 1;
  }

  .hero-grid-lines {
    position: absolute;
    right: 0; top: 0; bottom: 0;
    width: 45%;
    background-image: 
      linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    mask-image: linear-gradient(to left, black 0%, transparent 100%);
  }

  /* ===== FEATURE PILLS ===== */
  .pills-row {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 0 60px 50px;
  }

  .pill {
    padding: 7px 16px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
    border: 1.5px solid;
    display: flex;
    align-items: center;
    gap: 7px;
  }

  .pill.lime { background: rgba(200,241,53,0.08); border-color: rgba(200,241,53,0.35); color: var(--lime); }
  .pill.teal { background: rgba(0,212,180,0.08); border-color: rgba(0,212,180,0.35); color: var(--teal); }
  .pill.coral { background: rgba(255,94,98,0.08); border-color: rgba(255,94,98,0.35); color: var(--coral); }
  .pill.violet { background: rgba(108,63,232,0.15); border-color: rgba(108,63,232,0.45); color: #A87FFF; }
  .pill.amber { background: rgba(255,190,60,0.08); border-color: rgba(255,190,60,0.35); color: var(--amber); }
  .pill.sky { background: rgba(56,217,245,0.08); border-color: rgba(56,217,245,0.35); color: var(--sky); }

  /* ===== MAIN CONTENT ===== */
  .content {
    padding: 0 60px 80px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    max-width: 1200px;
  }

  .full-width { grid-column: 1 / -1; }

  /* ===== SECTION CARD ===== */
  .card {
    background: var(--card);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 28px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.25s;
  }

  .card:hover { border-color: rgba(255,255,255,0.16); }

  .card-accent {
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: 16px 16px 0 0;
  }

  .card-accent.lime { background: linear-gradient(90deg, var(--lime), var(--teal)); }
  .card-accent.coral { background: linear-gradient(90deg, var(--coral), var(--amber)); }
  .card-accent.violet { background: linear-gradient(90deg, var(--violet), var(--sky)); }
  .card-accent.teal { background: linear-gradient(90deg, var(--teal), var(--lime)); }
  .card-accent.amber { background: linear-gradient(90deg, var(--amber), var(--coral)); }
  .card-accent.sky { background: linear-gradient(90deg, var(--sky), var(--violet)); }
  .card-accent.rainbow { background: linear-gradient(90deg, var(--coral), var(--violet), var(--sky), var(--lime)); }

  .card-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 22px;
  }

  .card-icon {
    width: 38px; height: 38px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
  }

  .card-icon.lime { background: rgba(200,241,53,0.15); }
  .card-icon.coral { background: rgba(255,94,98,0.15); }
  .card-icon.violet { background: rgba(108,63,232,0.2); }
  .card-icon.teal { background: rgba(0,212,180,0.15); }
  .card-icon.amber { background: rgba(255,190,60,0.15); }
  .card-icon.sky { background: rgba(56,217,245,0.15); }

  .card-title {
    font-size: 16px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: var(--white);
  }

  .card-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 2px;
  }

  /* ===== STEP LIST ===== */
  .step-list { list-style: none; display: flex; flex-direction: column; gap: 14px; }

  .step-item {
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .step-num {
    width: 26px; height: 26px;
    border-radius: 8px;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    margin-top: 2px;
  }

  .step-num.lime { background: rgba(200,241,53,0.2); color: var(--lime); }
  .step-num.coral { background: rgba(255,94,98,0.2); color: var(--coral); }
  .step-num.teal { background: rgba(0,212,180,0.2); color: var(--teal); }
  .step-num.violet { background: rgba(108,63,232,0.3); color: #A87FFF; }
  .step-num.amber { background: rgba(255,190,60,0.2); color: var(--amber); }

  .step-content { flex: 1; }

  .step-label {
    font-size: 14px;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 3px;
  }

  .step-desc {
    font-size: 13px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* ===== CODE BLOCK ===== */
  .code-block {
    background: rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 10px;
    padding: 16px 18px;
    margin: 10px 0;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #C8F135;
    line-height: 1.7;
    overflow-x: auto;
    position: relative;
  }

  .code-block .comment { color: #4E5D72; }
  .code-block .cmd { color: var(--teal); }
  .code-block .flag { color: var(--amber); }
  .code-block .path { color: var(--sky); }
  .code-block .string { color: var(--coral); }

  /* ===== PROJECT TREE ===== */
  .tree {
    font-family: 'Space Mono', monospace;
    font-size: 12.5px;
    line-height: 2;
    color: var(--muted);
  }

  .tree .folder { color: var(--amber); font-weight: 700; }
  .tree .file { color: var(--sky); }
  .tree .file-desc { color: #4E5D72; font-size: 11px; }
  .tree .root { color: var(--lime); font-weight: 700; font-size: 14px; }

  /* ===== API ENDPOINTS ===== */
  .endpoint-list { display: flex; flex-direction: column; gap: 10px; }

  .endpoint {
    display: flex;
    align-items: center;
    gap: 12px;
    background: rgba(0,0,0,0.3);
    border-radius: 10px;
    padding: 12px 14px;
    border: 1px solid rgba(255,255,255,0.05);
  }

  .method {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 6px;
    min-width: 50px;
    text-align: center;
    letter-spacing: 0.05em;
  }

  .method.get { background: rgba(0,212,180,0.2); color: var(--teal); }
  .method.post { background: rgba(200,241,53,0.2); color: var(--lime); }
  .method.delete { background: rgba(255,94,98,0.2); color: var(--coral); }

  .endpoint-path {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: var(--white);
  }

  .endpoint-desc {
    margin-left: auto;
    font-size: 12px;
    color: var(--muted);
  }

  /* ===== TROUBLESHOOT ===== */
  .trouble-list { display: flex; flex-direction: column; gap: 12px; }

  .trouble-item {
    border-left: 3px solid;
    padding-left: 14px;
  }

  .trouble-item.coral { border-color: var(--coral); }
  .trouble-item.amber { border-color: var(--amber); }
  .trouble-item.violet { border-color: #A87FFF; }
  .trouble-item.sky { border-color: var(--sky); }

  .trouble-error {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: var(--coral);
    margin-bottom: 4px;
  }

  .trouble-amber { color: var(--amber) !important; }
  .trouble-violet { color: #A87FFF !important; }
  .trouble-sky { color: var(--sky) !important; }

  .trouble-fix {
    font-size: 13px;
    color: var(--muted);
  }

  .trouble-fix code {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--lime);
    background: rgba(200,241,53,0.07);
    padding: 1px 6px;
    border-radius: 4px;
  }

  /* ===== ENV VARS ===== */
  .env-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    gap: 12px;
  }

  .env-row:last-child { border-bottom: none; }

  .env-key {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: var(--lime);
  }

  .env-val {
    font-size: 13px;
    color: var(--muted);
    text-align: right;
  }

  /* ===== LINKS ===== */
  .links-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; }

  .link-card {
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 10px;
    padding: 14px;
    text-decoration: none;
    color: inherit;
    display: block;
    transition: border-color 0.2s, transform 0.15s;
  }

  .link-card:hover {
    border-color: rgba(200,241,53,0.35);
    transform: translateY(-2px);
  }

  .link-icon { font-size: 22px; margin-bottom: 8px; }
  .link-name { font-size: 13px; font-weight: 700; color: var(--white); margin-bottom: 3px; }
  .link-url { font-size: 11px; color: var(--teal); font-family: 'Space Mono', monospace; }

  /* ===== PREREQS ===== */
  .prereq-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }

  .prereq-item {
    background: rgba(0,0,0,0.3);
    border-radius: 10px;
    padding: 12px 14px;
    display: flex;
    align-items: center;
    gap: 10px;
    border: 1px solid rgba(255,255,255,0.05);
  }

  .prereq-check { font-size: 16px; }
  .prereq-text { font-size: 13px; color: var(--white); font-weight: 600; }
  .prereq-sub { font-size: 11px; color: var(--muted); }

  /* ===== DIVIDER ===== */
  .section-divider {
    grid-column: 1 / -1;
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 10px 0 0;
  }

  .divider-label {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--muted);
    white-space: nowrap;
  }

  .divider-line {
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, rgba(255,255,255,0.1), transparent);
  }

  /* ===== FOOTER ===== */
  .footer {
    background: rgba(0,0,0,0.4);
    border-top: 1px solid rgba(255,255,255,0.06);
    padding: 30px 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
  }

  .footer-brand { font-size: 14px; font-weight: 700; color: var(--white); }
  .footer-meta { font-size: 12px; color: var(--muted); font-family: 'Space Mono', monospace; }

  .footer-status {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    color: var(--lime);
  }

  .status-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: var(--lime);
    animation: pulse 2s infinite;
  }

  @media (max-width: 768px) {
    .content { grid-template-columns: 1fr; padding: 0 20px 60px; }
    .hero, .pills-row, .footer { padding-left: 20px; padding-right: 20px; }
    .links-grid { grid-template-columns: 1fr; }
    .prereq-grid { grid-template-columns: 1fr; }
    .endpoint-desc { display: none; }
  }
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-grid-lines"></div>
  <div class="hero-badge">✦ AI-POWERED · FLASK · VERTEX AI</div>
  <h1>Business <span class="accent">Strategy</span><br><span class="accent2">Generator</span></h1>
  <p class="hero-sub">AI-driven strategy reports with Gemini · SQLite persistence · Structured multi-section output · Responsive UI</p>
</div>

<!-- PILLS -->
<div class="pills-row">
  <div class="pill lime">✓ AI Strategy Generation</div>
  <div class="pill teal">✓ SQLite Persistence</div>
  <div class="pill coral">✓ Report Download</div>
  <div class="pill violet">✓ Input Validation</div>
  <div class="pill amber">✓ Error Handling</div>
  <div class="pill sky">✓ Responsive UI</div>
</div>

<!-- CONTENT GRID -->
<div class="content">

  <!-- SECTION: PREREQUISITES -->
  <div class="section-divider full-width">
    <span class="divider-label">Getting Started</span>
    <div class="divider-line"></div>
  </div>

  <!-- Prerequisites -->
  <div class="card full-width">
    <div class="card-accent lime"></div>
    <div class="card-header">
      <div class="card-icon lime">📋</div>
      <div>
        <div class="card-title">Prerequisites</div>
        <div class="card-subtitle">Before you begin, make sure you have these ready</div>
      </div>
    </div>
    <div class="prereq-grid">
      <div class="prereq-item">
        <span class="prereq-check">🐍</span>
        <div>
          <div class="prereq-text">Python 3.8+</div>
          <div class="prereq-sub">With pip package manager</div>
        </div>
      </div>
      <div class="prereq-item">
        <span class="prereq-check">☁️</span>
        <div>
          <div class="prereq-text">Google Cloud Project</div>
          <div class="prereq-sub">With Vertex AI API enabled</div>
        </div>
      </div>
      <div class="prereq-item">
        <span class="prereq-check">🔑</span>
        <div>
          <div class="prereq-text">GCP Credentials</div>
          <div class="prereq-sub">Service account or ADC configured</div>
        </div>
      </div>
      <div class="prereq-item">
        <span class="prereq-check">💻</span>
        <div>
          <div class="prereq-text">Terminal / CLI</div>
          <div class="prereq-sub">macOS, Linux, or WSL on Windows</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Project Structure -->
  <div class="card full-width">
    <div class="card-accent amber"></div>
    <div class="card-header">
      <div class="card-icon amber">📁</div>
      <div>
        <div class="card-title">Project Structure</div>
        <div class="card-subtitle">File layout overview</div>
      </div>
    </div>
    <div class="tree">
      <div><span class="root">business-strategy-generator/</span></div>
      <div>├── <span class="folder">app/</span></div>
      <div>│   ├── <span class="file">__init__.py</span> &nbsp;&nbsp;<span class="file-desc">— Flask app init</span></div>
      <div>│   ├── <span class="file">models.py</span> &nbsp;&nbsp;&nbsp;&nbsp;<span class="file-desc">— Database models</span></div>
      <div>│   ├── <span class="file">routes.py</span> &nbsp;&nbsp;&nbsp;&nbsp;<span class="file-desc">— API endpoints</span></div>
      <div>│   ├── <span class="file">validators.py</span> &nbsp;<span class="file-desc">— Input validation</span></div>
      <div>│   ├── <span class="file">gemini_service.py</span> <span class="file-desc">— Gemini API</span></div>
      <div>│   ├── <span class="folder">templates/</span> &nbsp;&nbsp;&nbsp;<span class="file-desc">index.html</span></div>
      <div>│   └── <span class="folder">static/</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="file-desc">css/ &amp; js/</span></div>
      <div>├── <span class="folder">instance/</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="file-desc">— SQLite storage</span></div>
      <div>├── <span class="file">run.py</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="file-desc">— Entry point</span></div>
      <div>├── <span class="file">config.py</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="file-desc">— Configuration</span></div>
      <div>├── <span class="file">requirements.txt</span> <span class="file-desc">— Dependencies</span></div>
      <div>└── <span class="file">.env.example</span> &nbsp;&nbsp;&nbsp;<span class="file-desc">— Env template</span></div>
    </div>
  </div>

  <!-- SECTION: SETUP STEPS -->
  <div class="section-divider full-width">
    <span class="divider-label">Setup & Installation</span>
    <div class="divider-line"></div>
  </div>

  <!-- Steps 1–3 -->
  <div class="card">
    <div class="card-accent lime"></div>
    <div class="card-header">
      <div class="card-icon lime">🚀</div>
      <div>
        <div class="card-title">Steps 1–3: Install</div>
        <div class="card-subtitle">Clone, virtualenv, and dependencies</div>
      </div>
    </div>
    <ul class="step-list">
      <li class="step-item">
        <div class="step-num lime">01</div>
        <div class="step-content">
          <div class="step-label">Navigate to Project</div>
          <div class="code-block"><span class="cmd">cd</span> <span class="path">/path/to/business-strategy-generator</span></div>
        </div>
      </li>
      <li class="step-item">
        <div class="step-num lime">02</div>
        <div class="step-content">
          <div class="step-label">Create Virtual Environment</div>
          <div class="code-block"><span class="cmd">python3</span> -m venv venv<br><span class="cmd">source</span> venv/bin/activate</div>
        </div>
      </li>
      <li class="step-item">
        <div class="step-num lime">03</div>
        <div class="step-content">
          <div class="step-label">Install Dependencies</div>
          <div class="code-block"><span class="cmd">pip install</span> -r requirements.txt</div>
        </div>
      </li>
    </ul>
  </div>

  <!-- Step 4: Google Cloud -->
  <div class="card">
    <div class="card-accent teal"></div>
    <div class="card-header">
      <div class="card-icon teal">☁️</div>
      <div>
        <div class="card-title">Step 4: Google Cloud</div>
        <div class="card-subtitle">Configure credentials & project</div>
      </div>
    </div>
    <ul class="step-list">
      <li class="step-item">
        <div class="step-num teal">4a</div>
        <div class="step-content">
          <div class="step-label">Copy env file</div>
          <div class="code-block"><span class="cmd">cp</span> .env.example .env</div>
        </div>
      </li>
      <li class="step-item">
        <div class="step-num teal">4b</div>
        <div class="step-content">
          <div class="step-label">Set Project ID in .env</div>
          <div class="code-block">GOOGLE_CLOUD_PROJECT_ID=<span class="string">your-project-id</span></div>
        </div>
      </li>
      <li class="step-item">
        <div class="step-num teal">4c</div>
        <div class="step-content">
          <div class="step-label">Auth — Service Account</div>
          <div class="code-block"><span class="cmd">export</span> GOOGLE_APPLICATION_CREDENTIALS=<span class="path">/path/to/creds.json</span></div>
        </div>
      </li>
      <li class="step-item">
        <div class="step-num teal">4d</div>
        <div class="step-content">
          <div class="step-label">Auth — Application Default</div>
          <div class="code-block"><span class="cmd">gcloud auth</span> application-default login</div>
        </div>
      </li>
    </ul>
  </div>

  <!-- Steps 5–6 -->
  <div class="card full-width">
    <div class="card-accent coral"></div>
    <div class="card-header">
      <div class="card-icon coral">▶️</div>
      <div>
        <div class="card-title">Steps 5–6: Run & Use</div>
        <div class="card-subtitle">Launch the app and generate your first strategy</div>
      </div>
    </div>
    <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 24px;">
      <div>
        <ul class="step-list">
          <li class="step-item">
            <div class="step-num coral">05</div>
            <div class="step-content">
              <div class="step-label">Start the server</div>
              <div class="code-block"><span class="cmd">python3</span> run.py</div>
              <div class="step-desc" style="margin-top:8px;">App starts at <code style="color:var(--lime);font-family:'Space Mono',monospace;font-size:12px;">http://localhost:5000</code></div>
              <div class="step-desc" style="margin-top:4px;">Stop with <code style="color:var(--coral);font-family:'Space Mono',monospace;font-size:12px;">Ctrl+C</code></div>
            </div>
          </li>
        </ul>
      </div>
      <div>
        <ul class="step-list">
          <li class="step-item">
            <div class="step-num coral">06</div>
            <div class="step-content">
              <div class="step-label">Fill in the form</div>
              <div class="step-desc">Enter: <strong style="color:var(--white);">Business Type</strong>, <strong style="color:var(--white);">Target Audience</strong>, <strong style="color:var(--white);">Problem Statement</strong>, and <strong style="color:var(--white);">Budget</strong></div>
              <div class="step-desc" style="margin-top:8px;">Click <strong style="color:var(--lime);">Generate Strategy</strong> to receive a full AI-generated report with Strategy · Marketing · Revenue · Risks · Competitors</div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <!-- SECTION: REFERENCE -->
  <div class="section-divider full-width">
    <span class="divider-label">Reference</span>
    <div class="divider-line"></div>
  </div>

  <!-- API Endpoints -->
  <div class="card">
    <div class="card-accent violet"></div>
    <div class="card-header">
      <div class="card-icon violet">⚡</div>
      <div>
        <div class="card-title">API Endpoints</div>
        <div class="card-subtitle">REST interface</div>
      </div>
    </div>
    <div class="endpoint-list">
      <div class="endpoint">
        <span class="method post">POST</span>
        <span class="endpoint-path">/api/generate-strategy</span>
        <span class="endpoint-desc">Create strategy</span>
      </div>
      <div class="endpoint">
        <span class="method get">GET</span>
        <span class="endpoint-path">/api/reports</span>
        <span class="endpoint-desc">All reports</span>
      </div>
      <div class="endpoint">
        <span class="method get">GET</span>
        <span class="endpoint-path">/api/reports/&lt;id&gt;</span>
        <span class="endpoint-desc">Single report</span>
      </div>
      <div class="endpoint">
        <span class="method delete">DELETE</span>
        <span class="endpoint-path">/api/reports/&lt;id&gt;</span>
        <span class="endpoint-desc">Remove report</span>
      </div>
    </div>
  </div>

  <!-- Environment Variables -->
  <div class="card">
    <div class="card-accent sky"></div>
    <div class="card-header">
      <div class="card-icon sky">⚙️</div>
      <div>
        <div class="card-title">Environment Vars</div>
        <div class="card-subtitle">Edit your .env file</div>
      </div>
    </div>
    <div class="env-row">
      <span class="env-key">FLASK_ENV</span>
      <span class="env-val">development / production</span>
    </div>
    <div class="env-row">
      <span class="env-key">FLASK_PORT</span>
      <span class="env-val">Default: 5000</span>
    </div>
    <div class="env-row">
      <span class="env-key">GOOGLE_CLOUD_PROJECT_ID</span>
      <span class="env-val">Your GCP project ID</span>
    </div>
    <div style="margin-top: 16px;">
      <div class="step-label" style="font-size:13px; margin-bottom:10px; color:var(--muted); text-transform:uppercase; letter-spacing:0.06em;">Reset Database</div>
      <div class="code-block">
        <span class="comment"># Delete and restart</span><br>
        <span class="cmd">rm</span> <span class="path">instance/business_strategy.db</span><br>
        <span class="cmd">python3</span> run.py
      </div>
    </div>
  </div>

  <!-- Troubleshooting -->
  <div class="card full-width">
    <div class="card-accent amber"></div>
    <div class="card-header">
      <div class="card-icon amber">🔧</div>
      <div>
        <div class="card-title">Troubleshooting</div>
        <div class="card-subtitle">Common issues and fixes</div>
      </div>
    </div>
    <div class="trouble-list">
      <div class="trouble-item coral">
        <div class="trouble-error">ModuleNotFoundError: No module named 'google'</div>
        <div class="trouble-fix">Run <code>pip install -r requirements.txt</code> to install all dependencies.</div>
      </div>
      <div class="trouble-item amber">
        <div class="trouble-error trouble-amber">Error calling Gemini API</div>
        <div class="trouble-fix">Check that <code>GOOGLE_APPLICATION_CREDENTIALS</code> is set correctly and Vertex AI API is enabled in GCP Console.</div>
      </div>
      <div class="trouble-item violet">
        <div class="trouble-error trouble-violet">Port already in use</div>
        <div class="trouble-fix">Change <code>FLASK_PORT</code> in .env, or run <code>lsof -i :5000</code> and kill the PID.</div>
      </div>
      <div class="trouble-item sky">
        <div class="trouble-error trouble-sky">Database errors</div>
        <div class="trouble-fix">Delete <code>instance/business_strategy.db</code> and restart the application.</div>
      </div>
    </div>
  </div>

  <!-- SECTION: LINKS -->
  <div class="section-divider full-width">
    <span class="divider-label">Documentation & Support</span>
    <div class="divider-line"></div>
  </div>

  <div class="card full-width">
    <div class="card-accent rainbow"></div>
    <div class="card-header">
      <div class="card-icon lime">🔗</div>
      <div>
        <div class="card-title">External Resources</div>
        <div class="card-subtitle">Official documentation and references</div>
      </div>
    </div>
    <div class="links-grid">
      <a href="https://cloud.google.com/vertex-ai" class="link-card" target="_blank">
        <div class="link-icon">☁️</div>
        <div class="link-name">Google Vertex AI</div>
        <div class="link-url">cloud.google.com/vertex-ai</div>
      </a>
      <a href="https://flask.palletsprojects.com" class="link-card" target="_blank">
        <div class="link-icon">🌶️</div>
        <div class="link-name">Flask Documentation</div>
        <div class="link-url">flask.palletsprojects.com</div>
      </a>
      <a href="https://www.sqlalchemy.org" class="link-card" target="_blank">
        <div class="link-icon">🗄️</div>
        <div class="link-name">SQLAlchemy</div>
        <div class="link-url">sqlalchemy.org</div>
      </a>
    </div>
  </div>

</div>

<!-- FOOTER -->
<div class="footer">
  <div>
    <div class="footer-brand">Business Strategy Generator</div>
    <div class="footer-meta">Flask · SQLite · Google Vertex AI · Gemini</div>
  </div>
  <div class="footer-status">
    <div class="status-dot"></div>
    Ready to deploy
  </div>
  <div class="footer-meta">Open http://localhost:5000 after python3 run.py</div>
</div>

</body>
</html>
