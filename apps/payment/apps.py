from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'apps.payment'
    verbose_name = 'Payment'

    def ready(self):
        # Можна підключати сигнали за потреби
        pass

