from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models

class RepositorioRendaMensal():
    def __init__(self, db: Session) -> None:
        self.db = db
        
    def criar(self, renda: schemas.RendaMensal):
        db_renda = models.RendaMensal(valor = renda.valor,
                                    familia_id = renda.familia_id)
        
        self.db.add(db_renda)
        self.db.commit()
        self.db.refresh(db_renda)
        return db_renda
    
    def listarRenda(self, familia_id):
        renda = self.db.query(models.RendaMensal).where(models.RendaMensal.familia_id == familia_id).first()
        return renda
        

