# clouthes-back/src/utils/logger.py

import logging

# Configuração de log básica
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("clouthes-back")

# Função para retornar o logger configurado
def get_logger(name: str = None):
    return logger.getChild(name) if name else logger
