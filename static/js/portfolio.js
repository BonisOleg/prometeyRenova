// PORTFOLIO.JS - Sticky Scroll ефект з фоновими відео

document.addEventListener('DOMContentLoaded', function () {
    // Ініціалізація всіх систем
    initVideoSystem();
    initScrollNavigation();
    initStickyScrollEffect();
    initModalSystem();
    initViewportHeight();
    initMobileOptimizations();
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
            const parent = video.closest('.portfolio-hero, .sticky-section');
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

// Sticky Scroll ефект при скролі
function initStickyScrollEffect() {
    const stickySections = document.querySelectorAll('.sticky-section');
    if (stickySections.length === 0) return;

    let currentSectionIndex = 0;
    let isScrolling = false;
    let isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    // Встановлюємо початковий стан
    updateSectionStates();

    // Обробник скролу з throttling
    let scrollTimeout;
    window.addEventListener('scroll', () => {
        if (scrollTimeout) {
            clearTimeout(scrollTimeout);
        }

        scrollTimeout = setTimeout(() => {
            handleScroll();
        }, isMobile ? 32 : 16); // ~30fps для мобільних, ~60fps для десктопу
    }, { passive: true });

    function handleScroll() {
        if (isScrolling) return;

        const scrollTop = window.pageYOffset;
        const windowHeight = window.innerHeight;
        const heroHeight = document.querySelector('.portfolio-hero').offsetHeight;

        // Розраховуємо поточну секцію на основі скролу після hero
        const scrollAfterHero = Math.max(0, scrollTop - heroHeight);
        const sectionHeight = windowHeight;
        const newSectionIndex = Math.min(
            Math.floor(scrollAfterHero / sectionHeight),
            stickySections.length - 1
        );

        if (newSectionIndex !== currentSectionIndex) {
            currentSectionIndex = newSectionIndex;
            updateSectionStates();
        }
    }

    function updateSectionStates() {
        stickySections.forEach((section, index) => {
            // Очищуємо всі класи
            section.classList.remove('active', 'exiting', 'entering', 'pending', 'passed');

            if (index === currentSectionIndex) {
                section.classList.add('active');
            } else if (index < currentSectionIndex) {
                section.classList.add('passed');
            } else {
                section.classList.add('pending');
            }
        });
    }

    // Keynavigation для розробки
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowDown' && currentSectionIndex < stickySections.length - 1) {
            currentSectionIndex++;
            updateSectionStates();
            smoothScrollToSection(currentSectionIndex);
        } else if (e.key === 'ArrowUp' && currentSectionIndex > 0) {
            currentSectionIndex--;
            updateSectionStates();
            smoothScrollToSection(currentSectionIndex);
        }
    });

    function smoothScrollToSection(index) {
        const heroHeight = document.querySelector('.portfolio-hero').offsetHeight;
        const targetScroll = heroHeight + (index * window.innerHeight);

        isScrolling = true;
        window.scrollTo({
            top: targetScroll,
            behavior: 'smooth'
        });

        setTimeout(() => {
            isScrolling = false;
        }, isMobile ? 1200 : 1000); // Більший timeout для мобільних
    }
}

// Мобільні оптимізації
function initMobileOptimizations() {
    const isMobile = /iPhone|iPad|iPod|Android/i.test(navigator.userAgent);

    if (isMobile) {
        // Відключаємо zoom на double tap
        let lastTouchEnd = 0;
        document.addEventListener('touchend', (event) => {
            const now = (new Date()).getTime();
            if (now - lastTouchEnd <= 300) {
                event.preventDefault();
            }
            lastTouchEnd = now;
        }, false);

        // Оптимізація для iOS Safari
        if (/iPhone|iPad|iPod/i.test(navigator.userAgent)) {
            // Виправлення для iPhone з вирізами
            const meta = document.querySelector('meta[name="viewport"]');
            if (meta) {
                meta.setAttribute('content', 'width=device-width, initial-scale=1, viewport-fit=cover');
            }

            // Додаткові iOS специфічні оптимізації
            document.documentElement.style.setProperty('--vh', `${window.innerHeight * 0.01}px`);
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

    // Додаткові обробники для мобільних
    if (/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)) {
        window.addEventListener('scroll', setVH);
        window.addEventListener('focus', setVH);
    }
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