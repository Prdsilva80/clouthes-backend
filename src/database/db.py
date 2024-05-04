# clouthes-back/src/database/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Configuração do banco de dados
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/dbname')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função para inicializar o banco de dados
def init_db():
    from ..models import product, order, user
    return
    auth
    Base.metadata.create_all(bind=engine)
