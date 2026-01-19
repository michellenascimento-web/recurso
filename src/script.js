// Sistema de progresso das aulas
let completedLessons = new Set();

// Navegação entre páginas
function showPage(pageId) {
    document.querySelectorAll('[id^="page-"], [id^="lesson-"]').forEach(el => el.classList.add('hidden'));
    const page = document.getElementById(pageId);
    if (page) {
        page.classList.remove('hidden');
        window.scrollTo(0, 0);
    }
}

// Verificar se aula está desbloqueada
function isLessonUnlocked(lessonNum) {
    if (lessonNum === 1) return true; // Aula 1 sempre desbloqueada
    return completedLessons.has(lessonNum - 1); // Precisa completar a anterior
}

// Marcar aula como completa
function completeLesson(lessonNum) {
    completedLessons.add(lessonNum);
    updateLessonCards();
    updateTocItems();
}

// Atualizar visual dos cards
function updateLessonCards() {
    document.querySelectorAll('.interactive-card[data-lesson]').forEach(card => {
        const lessonNum = parseInt(card.dataset.lesson);
        const isUnlocked = isLessonUnlocked(lessonNum);
        const isCompleted = completedLessons.has(lessonNum);

        if (!isUnlocked) {
            card.style.opacity = '0.5';
            card.style.filter = 'grayscale(100%)';
            card.style.cursor = 'not-allowed';
            card.style.pointerEvents = 'none';
        } else {
            card.style.opacity = '1';
            card.style.filter = 'none';
            card.style.cursor = 'pointer';
            card.style.pointerEvents = 'auto';
        }

        if (isCompleted) {
            card.style.borderColor = '#10b981';
            card.style.borderWidth = '3px';
        }
    });
}

// Atualizar visual do sumário
function updateTocItems() {
    document.querySelectorAll('.toc-item[data-lesson]').forEach(item => {
        const lessonNum = parseInt(item.dataset.lesson);
        const isUnlocked = isLessonUnlocked(lessonNum);
        const isCompleted = completedLessons.has(lessonNum);

        if (!isUnlocked) {
            item.style.opacity = '0.5';
            item.style.filter = 'grayscale(100%)';
            item.style.cursor = 'not-allowed';
            item.style.pointerEvents = 'none';
        } else {
            item.style.opacity = '1';
            item.style.filter = 'none';
            item.style.cursor = 'pointer';
            item.style.pointerEvents = 'auto';
        }

        if (isCompleted) {
            item.style.backgroundColor = '#d1fae5';
            item.querySelector('span:first-child').innerHTML += ' ✅';
        }
    });
}

// Botão INICIAR da capa (Página 1 → Página 2)
const btnNextToPage2 = document.getElementById('next-to-page2');
if (btnNextToPage2) {
    btnNextToPage2.addEventListener('click', () => showPage('page-2'));
}

// Página 2 navegação
document.getElementById('page2-prev')?.addEventListener('click', () => showPage('page-1'));
document.getElementById('page2-next')?.addEventListener('click', () => showPage('page-3'));

// Página 3 navegação
document.getElementById('page3-prev')?.addEventListener('click', () => showPage('page-2'));
document.getElementById('page3-next')?.addEventListener('click', () => showPage('page-4'));

// Página 4 navegação
document.getElementById('page4-prev')?.addEventListener('click', () => showPage('page-3'));
document.getElementById('page4-next')?.addEventListener('click', () => showPage('page-5'));

// Página 5 (Sumário) navegação
document.getElementById('page5-prev')?.addEventListener('click', () => showPage('page-4'));
document.getElementById('page5-next')?.addEventListener('click', () => showPage('page-6'));

// Página 6 navegação
document.getElementById('page6-prev')?.addEventListener('click', () => showPage('page-5'));
document.getElementById('page6-next')?.addEventListener('click', () => showPage('page-7'));

// Página 7 navegação
document.getElementById('page7-prev')?.addEventListener('click', () => showPage('page-6'));
const btnPage7Next = document.getElementById('page7-next');
if (btnPage7Next) {
    btnPage7Next.addEventListener('click', () => {
        showPage('lesson-1');
    });
}
// document.getElementById('page7-next')?.addEventListener('click', () => showPage('lesson-1')); // Removido para usar versão mais robusta acima

// Página 8 navegação
document.getElementById('page8-prev')?.addEventListener('click', () => showPage('page-7')); // Ajustar se necessário, mas Page 8 é o fim
document.getElementById('page8-next')?.addEventListener('click', () => showPage('page-9'));

// Página 9 navegação
document.getElementById('page9-prev')?.addEventListener('click', () => showPage('page-8'));
document.getElementById('page9-next')?.addEventListener('click', () => showPage('page-10'));

// Página 10 navegação
document.getElementById('page10-prev')?.addEventListener('click', () => showPage('page-9'));
document.getElementById('page10-next')?.addEventListener('click', () => showPage('page-11'));

// Página 11 navegação
document.getElementById('page11-prev')?.addEventListener('click', () => showPage('page-10'));
document.getElementById('page11-to-start')?.addEventListener('click', () => {
    // Resetar aulas completadas se quiser reiniciar o progresso
    // completedLessons.clear();
    // updateLessonCards();
    // updateTocItems();
    showPage('page-1');
});

// Sumário - cliques nos itens
document.querySelectorAll('.toc-item').forEach(item => {
    item.addEventListener('click', () => {
        const pageNum = item.dataset.page;
        const lessonNum = item.dataset.lesson;
        if (pageNum) {
            showPage(`page-${pageNum}`);
        }
        if (lessonNum) {
            const lesson = parseInt(lessonNum);
            if (isLessonUnlocked(lesson)) {
                showPage(`lesson-${lessonNum}`);
            }
        }
    });
});

// Cards de aulas (Página 7)
document.querySelectorAll('.interactive-card[data-lesson]').forEach(card => {
    card.addEventListener('click', () => {
        const lessonNum = parseInt(card.dataset.lesson);
        if (isLessonUnlocked(lessonNum)) {
            showPage(`lesson-${lessonNum}`);
        }
    });
});

// Botões "Voltar para Aulas"
document.querySelectorAll('.back-to-page7').forEach(btn => {
    btn.addEventListener('click', () => showPage('page-7'));
});

// Botões "Sumário"
document.querySelectorAll('.back-to-sumario').forEach(btn => {
    btn.addEventListener('click', () => showPage('page-5'));
});

// Navegação entre aulas (marca como completa ao avançar)
document.getElementById('lesson1-next')?.addEventListener('click', () => {
    completeLesson(1);
    showPage('lesson-2');
});
document.getElementById('lesson2-next')?.addEventListener('click', () => {
    completeLesson(2);
    showPage('lesson-3');
});
document.getElementById('lesson3-next')?.addEventListener('click', () => {
    completeLesson(3);
    showPage('lesson-4');
});
document.getElementById('lesson4-next')?.addEventListener('click', () => {
    completeLesson(4);
    showPage('lesson-5');
});
document.getElementById('lesson5-next')?.addEventListener('click', () => {
    completeLesson(5);
    showPage('lesson-6');
});
document.getElementById('lesson6-next')?.addEventListener('click', () => {
    completeLesson(6);
    showPage('lesson-7');
});
document.getElementById('lesson7-next')?.addEventListener('click', () => {
    completeLesson(7);
    showPage('lesson-8');
});
document.getElementById('lesson8-next')?.addEventListener('click', () => {
    completeLesson(8);
    showPage('lesson-9');
});
document.getElementById('lesson9-next')?.addEventListener('click', () => {
    completeLesson(9);
    showPage('lesson-10');
});
document.getElementById('lesson10-next')?.addEventListener('click', () => {
    completeLesson(10);
    showPage('lesson-11');
});
document.getElementById('lesson11-to-page8')?.addEventListener('click', () => {
    // completeLesson(11); // Se Aula 11 for "completável"
    showPage('page-8');
});

// Inicializar visual ao carregar
updateLessonCards();
updateTocItems();
