from imp import load_compiled
from tkinter.tix import Tree
from ma import ma 
from models.herois import HeroiModel

class HeroiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeroiModel
        load_instance = True