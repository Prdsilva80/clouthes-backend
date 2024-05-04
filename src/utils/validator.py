# clouthes-back/src/utils/validator.py

import re
from typing import Optional

# Verifica se o e-mail é válido
def is_valid_email(email: str) -> bool:
    pattern = r"[^@]+@[^@]+\.[^@]+"
    return re.match(pattern, email) is not None

# Verifica se o nome de usuário é válido (exemplo: sem caracteres especiais)
def is_valid_username(username: str) -> bool:
    return username.isalnum()

# Função para validar senha (exemplo: mínimo de 8 caracteres)
def is_valid_password(password: str) -> bool:
    return len(password) >= 8
