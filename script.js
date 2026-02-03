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

function celebrateYes() {
  if (!answerEl) return;
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
  noBtn.addEventListener("click", moveNoButton);
  noBtn.addEventListener("touchstart", moveNoButton, { passive: true });
}
