#!/usr/bin/env python
import os
import sys

import environ

env = environ.Env()

# 環境変数でDJANGO_READ_ENV_FILEをTrueにしておくと.envを読んでくれる。
READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=True)
env_base = environ.Path(__file__) - 1
if READ_ENV_FILE:
    env_file = str(env_base.path('.env/develop'))
else:
    env_file = str(env_base.path(".env/production"))
env.read_env(env_file)

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          env("DJANGO_SETTINGS_MODULE"))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
