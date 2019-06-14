from pokemonClass import Pokemon

class Bank:
    def __init__(self):
        self.allPokemon = {}

    def addPokemon(self, name, species, stats):
        self.allPokemon[name] = Pokemon(name, species, stats)
