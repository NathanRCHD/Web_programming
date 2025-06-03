from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

import sys
from pathlib import Path

# Ajouter le dossier racine du projet au sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

# Importer la configuration et les modèles depuis le package src
from src.config import settings
from src.models.base import Base
from src import models  # charge les modèles via __init__.py
from src.models import books, users, loans  # s'assurer que tous les modules sont importés

# Lecture du fichier alembic.ini
config = context.config

# Configuration du logging
fileConfig(config.config_file_name)

# Metadonnées utilisées pour les migrations automatiques
target_metadata = Base.metadata

# Remplacer l'URL de base de données par celle de settings
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)


def run_migrations_offline():
    """Exécute les migrations en mode offline."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Exécute les migrations en mode online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
