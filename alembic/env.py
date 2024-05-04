from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Este é o objeto de configuração do Alembic
config = context.config

# Configura loggers
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importar os metadados do projeto
from clouthes_back.database.db import Base

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executar migrações no modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executar migrações no modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
