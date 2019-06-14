import pokebase as pb

class Pokemon:
    def __init__(self, name, pokemonSpecies, hp = 0, atk = 0, defen = 0, spd = 0):
        self.nickname = name
        self.species = pokemonSpecies
        self.hitpoints = hp
        self.attack = atk
        self.defense = defen
        self.speed = spd
