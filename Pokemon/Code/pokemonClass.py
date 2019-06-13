import pokebase as pb

class Pokemon:
    def __init__(self, name, pokemonSpecies):
        self.nickname = name
        self._pokemonData = pb.pokemon(pokemonSpecies.lower())
        self._species = self._pokemonData.name
