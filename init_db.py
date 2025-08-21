#!/usr/bin/env python3
"""
Скрипт для ініціалізації бази даних на Render
"""
import os
import django

# Налаштування Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prometey_project.settings')
django.setup()

from django.db import connection
from django.core.management import call_command
from django.apps import apps

def init_database():
    """Ініціалізація бази даних"""
    print("🔧 Ініціалізація бази даних...")
    
    try:
        # Створюємо таблиці
        print("📋 Створення таблиць...")
        with connection.schema_editor() as schema_editor:
            for app_config in apps.get_app_configs():
                for model in app_config.get_models():
                    try:
                        schema_editor.create_model(model)
                        print(f"✅ Створено таблицю: {model._meta.db_table}")
                    except Exception as e:
                        print(f"⚠️  Таблиця {model._meta.db_table} вже існує: {e}")
        
        # Застосовуємо міграції
        print("🔄 Застосування міграцій...")
        call_command('migrate', '--noinput')
        
        # Збираємо статичні файли
        print("📁 Збір статичних файлів...")
        call_command('collectstatic', '--noinput')
        
        print("✅ База даних успішно ініціалізована!")
        
    except Exception as e:
        print(f"❌ Помилка ініціалізації: {e}")
        return False
    
    return True

if __name__ == '__main__':
    init_database()
