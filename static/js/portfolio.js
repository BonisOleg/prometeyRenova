// PORTFOLIO.JS - Card Stack ефект з фоновими відео

document.addEventListener('DOMContentLoaded', function () {
    // Ініціалізація всіх систем
    initVideoSystem();
    initScrollNavigation();
    initCardStackEffect();
    initModalSystem();
    initViewportHeight();
});

// Система фонових відео для портфоліо
function initVideoSystem() {
    const videos = document.querySelectorAll('.video-background, .project-video');

    videos.forEach(video => {
        // Забезпечуємо автоплей на iOS
        video.setAttribute('playsinline', '');
        video.setAttribute('webkit-playsinline', '');
        video.muted = true;

        // Перезапуск відео при завершенні
        video.addEventListener('ended', () => {
            video.currentTime = 0;
            video.play();
        });

        // Обробка помилок завантаження відео
        video.addEventListener('error', () => {
            console.log('Portfolio video loading error, applying fallback');
            video.style.display = 'none';
            const parent = video.closest('.portfolio-hero, .project-card');
            if (parent) {
                parent.style.background = 'linear-gradient(135deg, #000000 0%, #1a1a1a 100%)';
            }
        });
    });

    // Оптимізація для мобільних
    if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
        optimizeVideosForMobile();
    }
}

// Оптимізація відео для мобільних
function optimizeVideosForMobile() {
    const videos = document.querySelectorAll('.mobile-video');

    videos.forEach(video => {
        video.setAttribute('preload', 'metadata');

        // Керування відтворенням при visibility change
        document.addEventListener('visibilitychange', () => {
            if (document.hidden) {
                video.pause();
            } else {
                video.play();
            }
        });
    });
}

// Навігація з прозорим хедером
function initScrollNavigation() {
    const nav = document.querySelector('.main-navigation');

    window.addEventListener('scroll', () => {
        const scrollTop = window.pageYOffset;

        if (scrollTop > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });
}

// Card Stack ефект при скролі
function initCardStackEffect() {
    const projectCards = document.querySelectorAll('.project-card');
    if (projectCards.length === 0) return;

    let currentCardIndex = 0;
    let isScrolling = false;

    // Встановлюємо початковий стан
    updateCardStates();

    // Обробник скролу з throttling
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }

        scrollTimeout = setTimeout(() => {
            handleScroll();
        }, 16); // ~60fps
    }, { passive: true });

    function handleScroll() {
        if (isScrolling) return;

        const scrollTop = window.pageYOffset;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight;

        // Розраховуємо поточну картку на основі скролу
        const scrollProgress = scrollTop / (documentHeight - windowHeight);
        const newCardIndex = Math.min(
            Math.floor(scrollProgress * projectCards.length),
            projectCards.length - 1
        );

        if (newCardIndex !== currentCardIndex) {
            currentCardIndex = newCardIndex;
            updateCardStates();
        }
    }

    function updateCardStates() {
        projectCards.forEach((card, index) => {
            // Очищуємо всі класи
            card.classList.remove('active', 'exiting', 'entering', 'pending', 'passed');

            if (index === currentCardIndex) {
                card.classList.add('active');
            } else if (index < currentCardIndex) {
                card.classList.add('passed');
            } else {
                card.classList.add('pending');
            }
        });
    }

    // Keynavigation для розробки
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowDown' && currentCardIndex < projectCards.length - 1) {
            currentCardIndex++;
            updateCardStates();
            smoothScrollToCard(currentCardIndex);
        } else if (e.key === 'ArrowUp' && currentCardIndex > 0) {
            currentCardIndex--;
            updateCardStates();
            smoothScrollToCard(currentCardIndex);
        }
    });

    function smoothScrollToCard(index) {
        const targetCard = projectCards[index];
        if (targetCard) {
            isScrolling = true;
            targetCard.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });

            setTimeout(() => {
                isScrolling = false;
            }, 1000);
        }
    }
}

// Система модальних вікон (спрощена версія)
function initModalSystem() {
    const modalTriggers = document.querySelectorAll('[data-modal]');
    const closeButtons = document.querySelectorAll('.modal-close');
    const modals = document.querySelectorAll('.modal');

    modalTriggers.forEach(trigger => {
        trigger.addEventListener('click', (e) => {
            e.preventDefault();
            const modalId = trigger.getAttribute('data-modal');
            openModal(modalId);
        });
    });

    closeButtons.forEach(button => {
        button.addEventListener('click', closeAllModals);
    });

    modals.forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal || e.target.classList.contains('modal-backdrop')) {
                closeAllModals();
            }
        });
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeAllModals();
        }
    });
}

function openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.classList.add('active');
        modal.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
    }
}

function closeAllModals() {
    const modals = document.querySelectorAll('.modal.active');
    modals.forEach(modal => {
        modal.classList.remove('active');
        modal.setAttribute('aria-hidden', 'true');
    });
    document.body.style.overflow = '';
}

// Viewport height для iOS Safari
function initViewportHeight() {
    function setVH() {
        const vh = window.innerHeight * 0.01;
        document.documentElement.style.setProperty('--vh', `${vh}px`);
    }

    setVH();
    window.addEventListener('resize', setVH);
    window.addEventListener('orientationchange', () => {
        setTimeout(setVH, 100);
    });
}

// Intersection Observer для оптимізації відео
function initVideoIntersectionObserver() {
    const videos = document.querySelectorAll('.project-video');

    const videoObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const video = entry.target;

            if (entry.isIntersecting) {
                video.play();
            } else {
                video.pause();
            }
        });
    }, { threshold: 0.5 });

    videos.forEach(video => {
        videoObserver.observe(video);
    });
}

// Ініціалізуємо спостерігач відео після завантаження
setTimeout(initVideoIntersectionObserver, 1000);

// Tracking для аналітики
function trackProjectView(projectNumber) {
    if (typeof gtag !== 'undefined') {
        gtag('event', 'project_view', {
            project_number: projectNumber,
            page_location: window.location.href
        });
    }
}

// Performance optimizations
function optimizePerformance() {
    // Lazy loading для відео які не в viewport
    const videos = document.querySelectorAll('.project-video');
    videos.forEach(video => {
        video.setAttribute('preload', 'none');
    });

    // Перший і другий проект завантажуємо одразу
    const firstVideos = document.querySelectorAll('[data-project="1"] .project-video, [data-project="2"] .project-video');
    firstVideos.forEach(video => {
        video.setAttribute('preload', 'metadata');
    });
}

// Запускаємо оптимізації
optimizePerformance();

// SEO Enhancement
let portfolioViewTime = 0;
setInterval(() => {
    portfolioViewTime += 1;
    if (portfolioViewTime === 60 && typeof gtag !== 'undefined') {
        gtag('event', 'portfolio_engaged', {
            view_time: portfolioViewTime
        });
    }
}, 1000); 