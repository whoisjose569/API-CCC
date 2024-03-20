from sqlalchemy.orm import Session
from schemas import schemas
from infra.sqlalchemy.models import models
from sqlalchemy import update, delete, select
import re

class RepositorioFamilia():
    
    def __init__(self, db: Session):
        self.db = db
    
    def criar(self , familia: schemas.Familia):
        
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_regex, familia.email):
            raise ValueError("O email fornecido não é válido.")
        
        db_familia = models.Familia(sobrenome= familia.sobrenome,
                                    email = familia.email,
                                    senha= familia.senha
                                    )
        
        self.db.add(db_familia)
        self.db.commit()
        self.db.refresh(db_familia)
        return db_familia

    def buscarPorID(self, id: int):
        query = select(models.Familia).where(models.Familia.id == id)
        familia = self.db.execute(query).scalars().first()
        return familia
    
    
    def buscarPorEmail(self, email: str):
        query = select(models.Familia).where(models.Familia.email == email)
        return self.db.execute(query).scalars().first()
    
    def atualizarEmail(self, id: int, email: str):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_regex, email):
            raise ValueError("O email fornecido não é válido.")
        
        update_stmt = (update(models.Familia).where(models.Familia.id == id).values(email=email))
        
        self.db.execute(update_stmt)
        self.db.commit()
        
        return {'message': 'email ATUALIZADO'}
    
    