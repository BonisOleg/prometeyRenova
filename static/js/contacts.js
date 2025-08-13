/* Контактна форма - JavaScript обробник */

document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('contactForm');
    const formResponse = document.getElementById('formResponse');

    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();
            submitContactForm();
        });
    }

    // Функція для відправки форми
    function submitContactForm() {
        // Отримуємо дані з форми
        const name = document.getElementById('name').value.trim();
        const phone = document.getElementById('phone').value.trim();
        const email = document.getElementById('email').value.trim();
        const message = document.getElementById('message').value.trim();

        // Базова валідація
        if (!name || !phone) {
            showFormMessage('Будь ласка, заповніть обов\'язкові поля', 'error');
            return;
        }

        // Підготовка даних для відправки
        const formData = new FormData();
        formData.append('name', name);
        formData.append('phone', phone);
        formData.append('email', email);
        formData.append('message', message);
        formData.append('form_type', 'contact');

        // Додаємо CSRF token
        const csrftoken = getCookie('csrftoken');

        // Показуємо стан завантаження
        showFormMessage('Відправляємо ваше повідомлення...', 'loading');

        // Відправка запиту
        fetch('/forms/submit/', {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Успішна відправка
                    showFormMessage(data.message, 'success');
                    contactForm.reset();
                } else {
                    // Помилка
                    showFormMessage(data.message || 'Сталася помилка при відправці форми', 'error');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showFormMessage('Сталася помилка при відправці форми. Спробуйте ще раз.', 'error');
            });
    }

    // Функція для показу повідомлення
    function showFormMessage(message, type) {
        formResponse.textContent = message;
        formResponse.className = 'form-response';

        if (type === 'error') {
            formResponse.classList.add('form-error');
        } else if (type === 'success') {
            formResponse.classList.add('form-success');
        } else if (type === 'loading') {
            formResponse.classList.add('form-loading');
        }
    }

    // Функція для отримання CSRF токену з кукі
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
