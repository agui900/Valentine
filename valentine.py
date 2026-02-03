import streamlit as st

st.set_page_config(page_title="Valentine", page_icon="💘", layout="centered")

html = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>For My Favorite Person</title>
  <style>
    :root {
      --bg: #fff6f8;
      --ink: #2b1a1f;
      --accent: #ff5c8a;
      --accent-dark: #d63b6c;
      --shadow: rgba(32, 14, 20, 0.12);
      --soft: #fbe0e8;
    }

    * {
      box-sizing: border-box;
    }

    html,
    body {
      height: 100%;
    }

    body {
      margin: 0;
      font-family: "Georgia", "Times New Roman", serif;
      background-color: var(--bg);
      background-image: radial-gradient(circle at top, #ffe1ea 0%, var(--bg) 45%, #fff 100%);
      color: var(--ink);
      min-height: 100vh;
    }

    .bg-hearts {
      position: fixed;
      inset: 0;
      background-image:
        radial-gradient(circle at 20% 20%, rgba(255, 92, 138, 0.15) 0 18px, transparent 19px),
        radial-gradient(circle at 80% 30%, rgba(255, 92, 138, 0.12) 0 14px, transparent 15px),
        radial-gradient(circle at 50% 70%, rgba(214, 59, 108, 0.12) 0 16px, transparent 17px);
      background-size: 220px 220px, 260px 260px, 300px 300px;
      filter: blur(0.2px);
      opacity: 0.8;
      pointer-events: none;
    }

    .wrap {
      position: relative;
      max-width: 900px;
      margin: 0 auto;
      padding: 48px 20px 80px;
    }

    .hero {
      text-align: center;
      margin-bottom: 32px;
    }

    .kicker {
      text-transform: uppercase;
      letter-spacing: 0.2em;
      font-size: 12px;
      color: var(--accent-dark);
      margin-bottom: 12px;
    }

    h1 {
      font-size: clamp(32px, 6vw, 54px);
      margin: 0 0 12px;
    }

    .sub {
      font-size: 18px;
      margin: 0 auto 18px;
      max-width: 640px;
    }

    .proposal {
      position: relative;
      display: inline-flex;
      gap: 16px;
      align-items: center;
      justify-content: center;
      padding: 8px 0 6px;
      min-height: 56px;
    }

    #noBtn {
      position: fixed;
      left: 50%;
      top: 50%;
      transform: translate(40px, 0);
      z-index: 2;
    }

    .btn,
    button.btn {
      background: var(--accent) !important;
      color: #fff !important;
      border: none;
      border-radius: 999px;
      padding: 12px 22px;
      font-size: 16px;
      cursor: pointer;
      transition: transform 0.15s ease, box-shadow 0.2s ease, background 0.2s ease;
      box-shadow: 0 10px 20px rgba(255, 92, 138, 0.25);
    }

    .btn:hover {
      transform: translateY(-2px);
      background: var(--accent-dark);
    }

    .btn.ghost,
    button.btn.ghost {
      background: transparent !important;
      color: var(--accent-dark) !important;
      border: 1px solid var(--soft) !important;
      box-shadow: none;
    }

    .btn.locked {
      background: var(--accent) !important;
      color: #fff !important;
      cursor: default;
      pointer-events: none;
      opacity: 0.95;
    }

    .btn.locked:hover {
      transform: none;
      background: var(--accent) !important;
    }

    .secret {
      margin-top: 16px;
      font-size: 18px;
      min-height: 24px;
      color: var(--accent-dark);
    }

    .funny {
      margin-top: 10px;
      min-height: 22px;
      color: #8d4c62;
      font-style: italic;
    }

    @media (max-width: 600px) {
      .wrap {
        padding-top: 32px;
      }
    }
  </style>
</head>
<body>
  <div class="bg-hearts" aria-hidden="true"></div>

  <main class="wrap">
    <header class="hero">
      <p class="kicker">Happy Valentine’s Day</p>
      <h1>Will you be my Valentine?</h1>
      <p class="sub">Choose carefully.</p>
      <div class="proposal" aria-live="polite">
        <button id="yesBtn" class="btn">Yes</button>
        <button id="noBtn" class="btn ghost">No</button>
      </div>
      <p id="answer" class="secret" aria-live="polite"></p>
      <p id="funny" class="funny" aria-live="polite"></p>
    </header>
  </main>

  <script>
    const answerEl = document.getElementById("answer");
    const funnyEl = document.getElementById("funny");
    const yesBtn = document.getElementById("yesBtn");
    const noBtn = document.getElementById("noBtn");

    const funnyLines = [
      "Oops, it slipped away.",
      "The 'No' button is shy today.",
      "Not so fast, try again.",
      "Plot twist: the answer is yes.",
      "The universe keeps nudging you.",
      "Nice try, but destiny says yes.",
    ];

    let moveCount = 0;
    let lastMove = 0;

    function celebrateYes() {
      if (!answerEl || !yesBtn || !noBtn) return;
      answerEl.textContent = "Yay! Happy Valentine's Day!";
      yesBtn.classList.add("locked");
      noBtn.classList.add("locked");
      yesBtn.textContent = "It's a yes";
      if (funnyEl) funnyEl.textContent = "";
    }

    function showFunnyLine() {
      if (!funnyEl) return;
      const line = funnyLines[moveCount % funnyLines.length];
      funnyEl.textContent = line;
    }

    function moveNoButton() {
      if (!noBtn) return;
      const now = Date.now();
      if (now - lastMove < 150) return;
      lastMove = now;
      noBtn.style.position = "fixed";
      const noBox = noBtn.getBoundingClientRect();

      const maxX = Math.max(0, window.innerWidth - noBox.width - 12);
      const maxY = Math.max(0, window.innerHeight - noBox.height - 12);

      const x = Math.random() * maxX;
      const y = Math.random() * maxY;

      noBtn.style.left = `${x}px`;
      noBtn.style.top = `${y}px`;
      noBtn.style.transform = "translate(0, 0)";
      moveCount += 1;
      showFunnyLine();
    }

    if (yesBtn) yesBtn.addEventListener("click", celebrateYes);
    if (noBtn) {
      noBtn.addEventListener("mouseenter", moveNoButton);
      noBtn.addEventListener("mouseover", moveNoButton);
      noBtn.addEventListener("pointerenter", moveNoButton);
      noBtn.addEventListener("pointerdown", moveNoButton);
      noBtn.addEventListener("click", moveNoButton);
      noBtn.addEventListener("touchstart", moveNoButton, { passive: true });
    }

    if (noBtn) {
      document.addEventListener("mousemove", (event) => {
        const rect = noBtn.getBoundingClientRect();
        const dx = event.clientX - (rect.left + rect.width / 2);
        const dy = event.clientY - (rect.top + rect.height / 2);
        const distance = Math.hypot(dx, dy);
        if (distance < 90) moveNoButton();
      });
    }
  </script>
</body>
</html>
"""

st.components.v1.html(html, height=800, scrolling=True)
