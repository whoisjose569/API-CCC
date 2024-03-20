from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider
from jose import JWTError
from src.infra.sqlalchemy.repositorios.repositorio_familia import RepositorioFamilia


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def obter_usuario_logado(token:str =  Depends(oauth2_schema), db: Session = Depends(get_db)): # type: ignore
    
    try:
        email = token_provider.verificar_access_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido')
    
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido')
    
    usuario = RepositorioFamilia(db).buscarPorEmail(email)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token invalido')
    
    return usuario