from ma import ma 
from models.herois import HeroiModel

class HeroiSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HeroiModel
        load_instance = True