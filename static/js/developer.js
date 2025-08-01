/* DEVELOPER.JS - JavaScript для курсів */

document.addEventListener('DOMContentLoaded', function () {
    console.log('Developer page loaded');

    setupCourseCards();
});

function setupCourseCards() {
    const courseCards = document.querySelectorAll('.course-card');

    courseCards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-5px)';
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(0)';
        });
    });
} 