from fastapi import APIRouter, Depends
from typing import List
from infra.sqlalchemy.config.database import get_db, criar_bd
from schemas import schemas
from sqlalchemy.orm import Session
from infra.sqlalchemy.repositorios.repositorio_renda import RepositorioRendaMensal


criar_bd()

router = APIRouter()

@router.post('/criar_renda')
def criar_renda(renda: schemas.RendaMensal, db: Session = Depends(get_db)):
    renda_criada = RepositorioRendaMensal(db).criar(renda)
    return renda_criada

