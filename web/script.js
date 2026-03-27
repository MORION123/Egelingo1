let currentTask = 0;
let correctAnswers = 0;

const questionEl = document.getElementById("question");
const answerEl = document.getElementById("answer");
const resultEl = document.getElementById("result");
const progressEl = document.getElementById("progress");

// Telegram WebApp
const tg = window.Telegram.WebApp;
tg.expand();

function loadTask() {
    if (currentTask < tasks.length) {
        questionEl.innerText = tasks[currentTask].question;
        answerEl.value = "";
        resultEl.innerText = "";
    } else {
        finish();
    }
}

function checkAnswer() {
    const userAnswer = answerEl.value.trim();

    if (userAnswer === tasks[currentTask].answer) {
        correctAnswers++;
        resultEl.innerText = "✅ Правильно!";
    } else {
        resultEl.innerText = "❌ Неправильно";
    }

    currentTask++;
    updateProgress();

    setTimeout(loadTask, 1000);
}

function updateProgress() {
    const percent = Math.round((currentTask / tasks.length) * 100);
    progressEl.innerText = percent;
}

function finish() {
    questionEl.innerText = "Тест завершён!";
    resultEl.innerText = `Ваш результат: ${correctAnswers} / ${tasks.length}`;

    tg.MainButton.setText("Отправить результат");
    tg.MainButton.show();

    tg.MainButton.onClick(() => {
        tg.sendData(JSON.stringify({
            score: correctAnswers
        }));
    });
}

// старт
loadTask();
