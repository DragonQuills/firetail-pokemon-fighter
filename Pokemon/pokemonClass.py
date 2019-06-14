import pokebase as pb

class Pokemon:
    def __init__(self, name, pokemonSpecies, hp, atk, defen, spd):
        self.nickname = name
        self.species = pokemonSpecies
        self.hitpoints = hp
        self.attack = atk
        self.defense = defen
        self.speed = spd
