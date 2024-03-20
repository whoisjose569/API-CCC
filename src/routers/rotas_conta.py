from fastapi import APIRouter, Depends
from typing import List
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repositorio_conta import RepositorioConta


criar_bd()

router = APIRouter()

@router.post('/criar_conta')
def criar_conta(conta: schemas.Conta, db: Session = Depends(get_db)):
    conta_criada = RepositorioConta(db).criar(conta)
    return conta_criada

