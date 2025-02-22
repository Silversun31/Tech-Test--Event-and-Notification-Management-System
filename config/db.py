import environ
from pathlib import Path

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(Path.joinpath(BASE_DIR, ".env"))

__SQLITE = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": Path.joinpath(BASE_DIR, "db.sqlite3"),
    }
}

__POSTGRESQL = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env('DB_NAME', default=None),
        "USER": env('DB_USER', default=None),
        "PASSWORD": env('DB_PASSWORD', default=None),
        "HOST": env('DB_HOST', default=None),
        "PORT": env('DB_PORT', default=None),
    }
}

DATABASE = __POSTGRESQL if env('DATABASE_HOST', default=None) else __SQLITE
