import json
from marvel import Marvel
from models.herois import HeroiModel
from server.keys import PRIVATE_KEY, PUBLIC_KEY

marv = Marvel(PUBLIC_KEY, PRIVATE_KEY)

def get_herois():

    characters = marv.characters
    pers = characters.all(limit=100)['data']['results']
    
    return pers

def herois():
    lista = get_herois()
    return list(map(lambda heroi: HeroiModel(
        heroi['name'],
        heroi['description'],
        heroi['thumbnail']['path'] + "." + heroi['thumbnail']['extension']
    ), lista))
    


