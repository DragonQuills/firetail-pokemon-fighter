import pokebase
from pokemonClass import Pokemon

class PokemonBattler:
    def __init__(self):
        pass

    def moveTypeModifier(self, move, pokemon):
        pokeTypes = pokemon.types
        moveType = pokebase.type_(move.type)
        modifier = 1

        #create lists to store what the moves effectiveness is against certain types
        doubleD = []
        halfD = []
        noD = []
        for i in moveType.damage_relations.double_damage_to:
            doubleD.append(i["name"])
        for i in moveType.damage_relations.half_damage_to:
            halfD.append(i["name"])
        for i in moveType.damage_relations.no_damage_to:
            noD.append(i["name"])

        #for each type the pokemon has
        for type in pokeTypes:
            if type == "":
                continue
            #change the modifier if it's in any of the lists
            if type in doubleD:
                modifier = modifier*2
            elif type in halfD:
                modifier = modifier*0.5
            elif type in noD:
                modifier = modifier*0

        return modifier
