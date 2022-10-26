import json
from marvel import Marvel
from keys import PUBLIC_KEY, PRIVATE_KEY

marv = Marvel(PUBLIC_KEY, PRIVATE_KEY)

def get_herois():

    characters = marv.characters
    pers = characters.all(limit=100)['data']['results']
    lista = []

    for i in range(len(pers)):
        lista += {pers[i]['name'], pers[i]['description'], pers[i]['thumbnail']['path']}

    return json.dumps(lista)

print(get_herois())