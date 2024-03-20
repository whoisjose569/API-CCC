from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = '24b73b213851993e900b2ebb45b1c81f'
ALGORITHM = 'HS256'
EXPIRES_IN_MINUTES = 3600


def criar_access_token(data: dict):
    dados = data.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)
    
    dados.update({'exp': expiracao})
    
    token_jwt = jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)
    
    return token_jwt


def verificar_access_token(token: str):
    carga = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return carga.get('sub')


