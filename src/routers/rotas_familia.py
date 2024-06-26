from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from infra.sqlalchemy.config.database import get_db, criar_bd
from schemas import schemas
from sqlalchemy.orm import Session
from infra.sqlalchemy.repositorios.repositorio_familia import RepositorioFamilia
from infra.sqlalchemy.repositorios.repositorio_conta import RepositorioConta
from infra.sqlalchemy.repositorios.repositorio_renda import RepositorioRendaMensal
from routers.rotas_auth import obter_usuario_logado


criar_bd()
router = APIRouter()



@router.put('/atualizar-email')
def atualizar_email( email: str, db: Session = Depends(get_db), usuario: schemas.Familia = Depends(obter_usuario_logado)):
    familia = RepositorioFamilia(db).buscarPorID(usuario.id)
    if not familia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Familia não Localizada')
    
    RepositorioFamilia(db).atualizarEmail(usuario.id, email)
    return {"message": "Email Atualizado"}


@router.get('/contas-a-pagar', response_model=List[schemas.ContaSimples])
def listar_contas_a_pagar(usuario: schemas.Familia = Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    contas = RepositorioConta(db).listarContasAPagar(usuario.id)
    return contas

@router.get('/conta')
def buscar_conta(conta_id: int, db: Session = Depends(get_db), usuario: schemas.Familia = Depends(obter_usuario_logado)):
    conta_localizada = RepositorioConta(db).buscarContaID(usuario.id, conta_id)
    if conta_localizada is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Conta nao Localizada')
    return conta_localizada

@router.get('/contas-pagas', response_model=List[schemas.ContaSimples])
def listar_contas_pagas(usuario: schemas.Familia = Depends(obter_usuario_logado), db: Session = Depends(get_db)):
    contas = RepositorioConta(db).listarContasPagas(usuario.id)
    return contas

@router.get('/pagar-conta')
def pagar_conta(conta_id: int, db: Session = Depends(get_db), usuario: schemas.Familia = Depends(obter_usuario_logado)):
    conta_localizada = RepositorioConta(db).pagarConta(usuario.id, conta_id)
    if conta_localizada is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Conta nao Localizada')
    return {"message": 'Conta Paga'}

@router.get('/listar-renda')
def listar_renda(db: Session = Depends(get_db),usuario: schemas.Familia = Depends(obter_usuario_logado)):
    renda_localizada = RepositorioRendaMensal(db).listarRenda(usuario.id)
    return renda_localizada

@router.delete('/deletar-conta')
def deletar_conta(conta_id: int, db: Session = Depends(get_db), usuario: schemas.Familia = Depends(obter_usuario_logado)):
    conta_localizada = RepositorioConta(db).deletarConta(conta_id, usuario.id)
    if conta_localizada is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Conta nao Localizada')
    return {"message": 'Conta Deletada'}