from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional


class Familia(BaseModel):
    id: Optional[int] = None
    sobrenome: str
    email: str
    senha: str
    contas: Optional[List[ContaSimples]] = []
    renda_mensal: Optional[RendaMensalSimples] = []
    
    class Config:
        orm_mode = True


class FamiliaSimples(BaseModel):
    sobrenome: str
    email: str
    
class LoginData(BaseModel):
    email: str
    senha: str

class LoginSucesso(BaseModel):
    usuario: FamiliaSimples
    access_token : str
    

class Conta(BaseModel):
    id: Optional[int] = None
    nome: str
    valor: float
    data_venc: str
    situacao: Optional[bool] = False
    
    familia_id: Optional[int] = None
    familia: Optional[Familia] = None

    class Config:
        orm_mode = True

class ContaSimples(BaseModel):
    nome: str
    valor: float
    data_venc: str
    
    familia: Optional[FamiliaSimples] = None


class RendaMensal(BaseModel):
    id: Optional[int] = None
    valor: float 
    
    familia_id: Optional[int] = None
    familia: Optional[Familia] = None
    
    class Config:
        orm_mode = True

class RendaMensalSimples(BaseModel):
    valor: float
    familia: Optional[FamiliaSimples] = None
    
class RendaMensalFamilia(BaseModel):
    valor: float