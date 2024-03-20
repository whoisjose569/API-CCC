from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models

class RepositorioConta():
    def __init__(self, db: Session) -> None:
        self.db = db
    
    def criar(self, conta: schemas.Conta):
        db_conta = models.Conta(nome=conta.nome,
                                valor=conta.valor,
                                data_venc=conta.data_venc,
                                situacao=conta.situacao,
                                familia_id=conta.familia_id)
        self.db.add(db_conta)
        self.db.commit()
        self.db.refresh(db_conta)
        return db_conta

    def listarContasAPagar(self, id: int):
        contas_a_pagar = self.db.query(models.Conta).filter(models.Conta.familia_id == id, models.Conta.situacao == False).all()
        return contas_a_pagar
    
    def buscarContaID(self, id: int, conta_id: id):
        query = self.db.query(models.Conta).join(models.Familia, models.Conta.familia_id == models.Familia.id).filter(models.Familia.id == id, models.Conta.id == conta_id).first()
        return query
    
    def listarContasPagas(self, id: int):
        contas_pagas = self.db.query(models.Conta).filter(models.Conta.familia_id == id, models.Conta.situacao == True).all()
        return contas_pagas
    
    def PagarConta(self, familia_id: int, conta_id: id):
        conta = self.db.query(models.Conta).join(models.Familia, models.Conta.familia_id == models.Familia.id).filter(models.Familia.id == familia_id, models.Conta.id == conta_id).first()
        conta.situacao = True
        self.db.commit()
        return conta