from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from infra.sqlalchemy.config.database import get_db, criar_bd
from schemas import schemas
from sqlalchemy.orm import Session
from infra.sqlalchemy.repositorios.repositorio_familia import RepositorioFamilia
from infra.providers import hash_provider, token_provider
from routers.auth_utils import obter_usuario_logado

criar_bd()
router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED, response_model=schemas.FamiliaSimples)
def signup(familia: schemas.Familia, db: Session = Depends(get_db)):
    familia_localizada = RepositorioFamilia(db).buscarPorEmail(familia.email)
    
    if familia_localizada:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Ja existe um usuario com esse email')
    
    
    familia.senha = hash_provider.gerar_hash(familia.senha)
    familia_criada = RepositorioFamilia(db).criar(familia)
    return familia_criada

@router.post('/token', response_model=schemas.LoginSucesso)
def login(login_data: schemas.LoginData, db: Session = Depends(get_db)):
    email = login_data.email
    senha = login_data.senha
    
    usuario = RepositorioFamilia(db).buscarPorEmail(email)
    
    if not usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email ou senha incorretos')
    
    senha_valida = hash_provider.verificar_hash(senha, usuario.senha)
    
    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email ou senha incorretos')
    

    token = token_provider.criar_access_token({'sub': usuario.email})
    return {'usuario': usuario, 'access_token': token}

@router.get('/me', response_model=schemas.FamiliaSimples)
def me(usuario: schemas.Familia = Depends(obter_usuario_logado)):
    return usuario