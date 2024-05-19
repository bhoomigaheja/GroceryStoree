#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Set the port for Render.com
    port = os.environ.get('PORT', '8000')
    
    # Modify sys.argv to include the port if 'runserver' is in the command
    if 'runserver' in sys.argv:
        runserver_index = sys.argv.index('runserver')
        # Check if there is an argument after 'runserver' and if it's a port specification
        if len(sys.argv) > runserver_index + 1 and ':' not in sys.argv[runserver_index + 1]:
            sys.argv[runserver_index + 1] = f'0.0.0.0:{port}'
        else:
            sys.argv.append(f'0.0.0.0:{port}')
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
