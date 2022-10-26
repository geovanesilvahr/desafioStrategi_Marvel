from typing import List
from db import db


class HeroiModel(db.Model):
    __tablename = 'herois'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(400), nullable=False)
    imagem = db.Column(db.String(200), nullable=False)

    def __init__(self, nome, descricao, imagem):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem

    def __repr__(self):
        return f'HeroiModel(nome={self.nome}, descricao={self.descricao}, imagem={self.imagem})'

    def json(self):
        return {
            'nome': self.nome,
            'descricao': self.descricao,
            'imagem': self.imagem
        }
    @classmethod
    def find_by_nome(cls, nome) -> "HeroiModel":
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id(cls, _id) -> "HeroiModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["HeroiModel"]:
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
