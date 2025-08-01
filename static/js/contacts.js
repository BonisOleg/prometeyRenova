/* CONTACTS.JS - JavaScript для контактів */

document.addEventListener('DOMContentLoaded', function () {
    console.log('Contacts page loaded');

    setupContactForm();
});

function setupContactForm() {
    const contactForm = document.querySelector('[data-form-type="contact"]');
    if (!contactForm) return;

    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();
        console.log('Contact form submitted');

        // Форма буде оброблена через base.js
        if (window.prometeyApp) {
            window.prometeyApp.showSuccess('Повідомлення відправлено! Ми зв\'яжемося з вами найближчим часом.');
        }
    });
} 