from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship
from infra.sqlalchemy.config.database import Base

class Familia(Base):
    __tablename__ = 'familia'
    
    id = Column(Integer, primary_key=True, index=True)
    sobrenome = Column(String)
    email = Column(String)
    senha = Column(String)
    
    contas = relationship('Conta', back_populates='familia')
    renda_mensal = relationship('RendaMensal', back_populates='familia')


class Conta(Base):
    __tablename__ = 'conta'
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    valor = Column(Float)
    data_venc = Column(String)
    situacao = Column(Boolean)
    
    familia_id = Column(Integer, ForeignKey('familia.id', name='fk_familia'))
    familia = relationship('Familia', back_populates='contas')

class RendaMensal(Base):
    __tablename__ = 'renda_mensal'
    
    id = Column(Integer, primary_key=True, index=True)
    valor = Column(Float)
    
    familia_id = Column(Integer, ForeignKey('familia.id', name='fk_familia'))
    familia = relationship('Familia', back_populates='renda_mensal')