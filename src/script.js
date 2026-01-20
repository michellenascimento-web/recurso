// Sistema de progresso das aulas (Multi-Page Version)

// Chave para localStorage
const STORAGE_KEY = 'edu_tech_progress';

// Carregar progresso salvo
function loadProgress() {
    try {
        const saved = localStorage.getItem(STORAGE_KEY);
        return saved ? new Set(JSON.parse(saved)) : new Set();
    } catch (e) {
        console.warn('LocalStorage not available:', e);
        return new Set();
    }
}

// Salvar progresso
function saveProgress(completedSet) {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify([...completedSet]));
    } catch (e) {
        console.warn('LocalStorage not available:', e);
    }
}

// Estado atual
let completedLessons = loadProgress();

// Verificar se aula está desbloqueada
function isLessonUnlocked(lessonNum) {
    if (lessonNum === 1) return true; // Aula 1 sempre desbloqueada
    return completedLessons.has(lessonNum - 1); // Precisa completar a anterior
}

// Marcar aula como completa
function completeLesson(lessonNum) {
    completedLessons.add(lessonNum);
    saveProgress(completedLessons);
    updateUI();
}

// Atualizar interface (Cards e Sumário)
function updateUI() {
    updateLessonCards();
    updateTocItems();
}

// Atualizar visual dos cards (usado na página de menu de aulas)
function updateLessonCards() {
    const cards = document.querySelectorAll('.interactive-card[data-lesson]');
    if (cards.length === 0) return;

    cards.forEach(card => {
        const lessonNum = parseInt(card.dataset.lesson);
        const isUnlocked = isLessonUnlocked(lessonNum);
        const isCompleted = completedLessons.has(lessonNum);

        if (!isUnlocked) {
            card.style.opacity = '0.5';
            card.style.filter = 'grayscale(100%)';
            card.style.cursor = 'not-allowed';
            // card.style.pointerEvents = 'none'; // Permitir clique para mostrar aviso se quiser
            card.onclick = (e) => {
                e.preventDefault();
                alert('Complete a aula anterior para desbloquear esta!');
            };
        } else {
            card.style.opacity = '1';
            card.style.filter = 'none';
            card.style.cursor = 'pointer';
            card.style.pointerEvents = 'auto';

            // Link direto
            card.onclick = () => {
                window.location.href = `../aulas/aula${lessonNum.toString().padStart(2, '0')}/index.html`;
            };
        }

        if (isCompleted) {
            card.style.borderColor = '#10b981';
            card.style.borderWidth = '3px';
            // Adicionar indicador visual de completo se não tiver
            if (!card.querySelector('.completed-badge')) {
                const badge = document.createElement('div');
                badge.className = 'completed-badge absolute top-2 right-2 bg-green-500 text-white rounded-full p-1';
                badge.innerHTML = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" class="stroke-current stroke-2"><path d="M20 6L9 17l-5-5"/></svg>';
                card.style.position = 'relative';
                card.appendChild(badge);
            }
        }
    });
}

// Atualizar visual do sumário (usado na página de sumário)
function updateTocItems() {
    const items = document.querySelectorAll('.toc-item[data-lesson]');
    if (items.length === 0) return;

    items.forEach(item => {
        const lessonNum = parseInt(item.dataset.lesson);
        const isUnlocked = isLessonUnlocked(lessonNum);
        const isCompleted = completedLessons.has(lessonNum);

        // Resetar estilos base
        item.classList.remove('opacity-50', 'grayscale', 'cursor-not-allowed', 'bg-green-100');

        if (!isUnlocked) {
            item.classList.add('opacity-50', 'grayscale', 'cursor-not-allowed');
            item.onclick = (e) => {
                e.preventDefault();
                alert('Complete a aula anterior para desbloquear esta!');
            };
        } else {
            item.style.cursor = 'pointer';
            item.onclick = () => {
                window.location.href = `../aulas/aula${lessonNum.toString().padStart(2, '0')}/index.html`;
            };
        }

        if (isCompleted) {
            item.classList.add('bg-green-50');
            if (!item.innerHTML.includes('✅')) {
                const titleSpan = item.querySelector('span:first-child');
                if (titleSpan) titleSpan.innerHTML += ' ✅';
            }
        }
    });
}

// Inicialização Global
document.addEventListener('DOMContentLoaded', () => {
    updateUI();

    // Tratamento para botões de "Próxima Aula/Página" que marcam conclusão
    // Exemplo: Botão "Próximo" na Aula 1 que leva à Aula 2 (ou menu) e marca Aula 1 como feita
    const completeBtn = document.getElementById('btn-complete-lesson');
    if (completeBtn) {
        completeBtn.addEventListener('click', (e) => {
            const lessonNum = parseInt(completeBtn.dataset.lesson);
            if (lessonNum) {
                completeLesson(lessonNum);
                // O href do link cuidará da navegação
            }
        });
    }
});
