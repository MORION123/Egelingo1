// Инициализация Telegram WebApp
const tg = window.Telegram.WebApp;
tg.expand(); // Разворачиваем на весь экран
tg.enableClosingConfirmation(); // Подтверждение закрытия

// Состояние приложения
let currentPage = 'home';
let currentSubject = null;
let currentLesson = null;
let userData = {
    level: 1,
    points: 0,
    streak: 0
};

// Данные предметов
const subjects = {
    math: {
        name: 'Математика',
        icon: '📐',
        lessons: [
            { id: 1, name: 'Уравнения', xp: 10, questions: [] },
            { id: 2, name: 'Производные', xp: 15, questions: [] }
        ]
    },
    russian: {
        name: 'Русский язык',
        icon: '📖',
        lessons: [
            { id: 1, name: 'Орфография', xp: 10, questions: [] },
            { id: 2, name: 'Пунктуация', xp: 15, questions: [] }
        ]
    },
    physics: {
        name: 'Физика',
        icon: '⚛️',
        lessons: [
            { id: 1, name: 'Механика', xp: 10, questions: [] },
            { id: 2, name: 'Электричество', xp: 15, questions: [] }
        ]
    }
};

// Загрузка данных пользователя
async function loadUserData() {
    // Здесь будет запрос к боту через WebAppData
    const urlParams = new URLSearchParams(window.location.search);
    const userId = urlParams.get('user_id');
    
    // Отправляем запрос на получение статистики
    tg.sendData(JSON.stringify({
        action: 'get_stats',
        user_id: userId
    }));
    
    // В реальном приложении здесь будет получение данных от бота
    updateUI();
}

// Обновление интерфейса
function updateUI() {
    document.getElementById('level').textContent = userData.level;
    document.getElementById('points').textContent = userData.points;
    document.getElementById('streak').textContent = userData.streak;
    
    const progress = (userData.points % 100) / 100 * 100;
    document.getElementById('dailyProgress').style.width = `${progress}%`;
    document.getElementById('dailyStats').textContent = `${userData.points % 100}/100 XP`;
}

// Отображение главной страницы
function renderHome() {
    const subjectsGrid = document.getElementById('subjects');
    subjectsGrid.innerHTML = '';
    
    Object.entries(subjects).forEach(([key, subject]) => {
        const card = document.createElement('div');
        card.className = 'subject-card';
        card.innerHTML = `
            <div class="subject-icon">${subject.icon}</div>
            <div class="subject-name">${subject.name}</div>
        `;
        card.onclick = () => openSubject(key);
        subjectsGrid.appendChild(card);
    });
}

// Открытие предмета
function openSubject(subjectId) {
    currentSubject = subjectId;
    const subject = subjects[subjectId];
    
    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = `
        <button class="back-btn" onclick="goBack()">← Назад</button>
        <h2>${subject.name}</h2>
        <div class="lessons-list">
            ${subject.lessons.map(lesson => `
                <div class="lesson-card" onclick="startLesson(${lesson.id})">
                    <div class="lesson-info">
                        <span class="lesson-name">${lesson.name}</span>
                        <span class="lesson-xp">+${lesson.xp} XP</span>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// Начало урока
function startLesson(lessonId) {
    const lesson = subjects[currentSubject].lessons.find(l => l.id === lessonId);
    currentLesson = lesson;
    
    // Генерация вопросов (в реальном приложении будут из БД)
    const questions = generateQuestions(currentSubject, lessonId);
    showQuestion(questions, 0, 0);
}

// Генерация вопросов
function generateQuestions(subject, lessonId) {
    // Пример вопросов для демонстрации
    const questionsBySubject = {
        math: [
            {
                text: 'Решите уравнение: 2x + 5 = 15',
                options: ['x = 5', 'x = 10', 'x = 2.5', 'x = 7.5'],
                correct: 0
            },
            {
                text: 'Чему равна производная функции f(x) = x²?',
                options: ['2x', 'x²', '2', 'x'],
                correct: 0
            }
        ],
        russian: [
            {
                text: 'В каком слове пропущена буква "И"?',
                options: ['ц_рк', 'ц_ган', 'ц_фра', 'ц_тата'],
                correct: 0
            }
        ]
    };
    
    return questionsBySubject[subject] || [];
}

// Показ вопроса
function showQuestion(questions, index, score) {
    if (index >= questions.length) {
        completeLesson(score);
        return;
    }
    
    const question = questions[index];
    const mainContent = document.querySelector('.main-content');
    
    mainContent.innerHTML = `
        <div class="lesson-container">
            <div class="lesson-progress">Вопрос ${index + 1}/${questions.length}</div>
            <div class="lesson-question">${question.text}</div>
            <div class="lesson-options">
                ${question.options.map((opt, i) => `
                    <div class="lesson-option" onclick="checkAnswer(${i}, ${index}, ${score}, '${question.correct}')">
                        ${opt}
                    </div>
                `).join('')}
            </div>
        </div>
    `;
}

// Проверка ответа
function checkAnswer(selected, questionIndex, currentScore, correctIndex) {
    const isCorrect = selected === parseInt(correctIndex);
    const newScore = currentScore + (isCorrect ? 10 : 0);
    
    const options = document.querySelectorAll('.lesson-option');
    options.forEach((opt, idx) => {
        if (idx === parseInt(correctIndex)) {
            opt.classList.add('correct');
        } else if (idx === selected && !isCorrect) {
            opt.classList.add('wrong');
        }
        opt.style.pointerEvents = 'none';
    });
    
    setTimeout(() => {
        // Загружаем следующий вопрос
        const questions = generateQuestions(currentSubject, currentLesson.id);
        showQuestion(questions, questionIndex + 1, newScore);
    }, 1000);
}

// Завершение урока
function completeLesson(score) {
    const xpEarned = Math.floor(score / 2);
    userData.points += xpEarned;
    userData.level = Math.floor(userData.points / 100) + 1;
    
    updateUI();
    
    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = `
        <div class="lesson-complete">
            <h2>🎉 Урок завершен!</h2>
            <p>Ваш результат: ${score}%</p>
            <p>Получено XP: +${xpEarned}</p>
            <button onclick="goBack()" class="continue-btn">Продолжить</button>
        </div>
    `;
    
    // Отправка данных боту
    tg.sendData(JSON.stringify({
        action: 'complete_lesson',
        lesson_id: currentLesson.id,
        score: score
    }));
}

// Навигация
function goBack() {
    renderHome();
    currentSubject = null;
    currentLesson = null;
}

// Инициализация
document.addEventListener('DOMContentLoaded', () => {
    loadUserData();
    renderHome();
    
    // Обработка навигации
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            const page = btn.dataset.page;
            switchPage(page);
        });
    });
});

function switchPage(page) {
    currentPage = page;
    document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.page === page) {
            btn.classList.add('active');
        }
    });
    
    // Рендеринг разных страниц
    if (page === 'home') {
        renderHome();
    } else if (page === 'profile') {
        renderProfile();
    } else if (page === 'leaderboard') {
        renderLeaderboard();
    }
}

function renderProfile() {
    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = `
        <div class="profile">
            <div class="profile-header">
                <div class="avatar">👤</div>
                <h2>${tg.initDataUnsafe.user?.first_name || 'Пользователь'}</h2>
            </div>
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-value">${userData.level}</span>
                    <span class="stat-label">Уровень</span>
                </div>
                <div class="stat-item">
                    <span class="stat-value">${userData.points}</span>
                    <span class="stat-label">Всего XP</span>
                </div>
                <div class="stat-item">
                    <span class="stat-value">${userData.streak}</span>
                    <span class="stat-label">Дней подряд</span>
                </div>
            </div>
            <div class="achievements">
                <h3>Достижения</h3>
                <div class="achievement-list">
                    <div class="achievement">🏆 Первый урок</div>
                    <div class="achievement">⭐️ 100 XP</div>
                </div>
            </div>
        </div>
    `;
}

function renderLeaderboard() {
    const mainContent = document.querySelector('.main-content');
    mainContent.innerHTML = `
        <div class="leaderboard">
            <h2>🏆 Таблица лидеров</h2>
            <div class="leaderboard-list">
                <div class="leaderboard-item">
                    <span class="rank">1</span>
                    <span class="name">Иван</span>
                    <span class="points">2500 XP</span>
                </div>
                <div class="leaderboard-item">
                    <span class="rank">2</span>
                    <span class="name">Мария</span>
                    <span class="points">2100 XP</span>
                </div>
                <div class="leaderboard-item">
                    <span class="rank">3</span>
                    <span class="name">Алексей</span>
                    <span class="points">1850 XP</span>
                </div>
            </div>
        </div>
    `;
}
