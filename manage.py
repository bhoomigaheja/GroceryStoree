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
        addrport_index = sys.argv.index('runserver') + 1
        if len(sys.argv) > addrport_index and ':' not in sys.argv[addrport_index]:
            sys.argv.insert(addrport_index, f'0.0.0.0:{port}')
        else:
            sys.argv.insert(addrport_index, '0.0.0.0')
            sys.argv.insert(addrport_index + 1, port)

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
