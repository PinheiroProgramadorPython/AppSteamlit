from sqlalchemy import create_engine, String, Column, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///Database/database.db")

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    email = Column("email", String)
    senha = Column("senha", String)
    admin = Column("admin", Boolean)

    def __init__(self, name, email, senha, admin=False):
        self.name = name
        self.email = email
        self.senha = senha
        self.admin = admin


Base.metadata.create_all(bind=db)
