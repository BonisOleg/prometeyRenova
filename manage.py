#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prometey_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Додаткова команда для створення таблиць
    if len(sys.argv) > 1 and sys.argv[1] == 'create_tables':
        from django.core.management import execute_from_command_line
        from django.db import connection
        from django.apps import apps
        
        print("Creating database tables...")
        with connection.schema_editor() as schema_editor:
            for app_config in apps.get_app_configs():
                for model in app_config.get_models():
                    try:
                        schema_editor.create_model(model)
                        print(f"Created table for {model._meta.db_table}")
                    except Exception as e:
                        print(f"Table {model._meta.db_table} already exists or error: {e}")
        return
    
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
