import pokebase as pb

class Pokemon:
    def __init__(self, name, pokemonSpecies, stats = [0, 0, 0, 0]):
        self.nickname = name
        self.species = pokemonSpecies
        self.stats = {"hp" : stats[0], "atk" : stats[1], "def" : stats[2], "spd" : stats[3]}

    def changeStat(self, statName, newValue):
        if statName == "hp":
            self.stats["hp"] = newValue
        elif statName == "atk":
            self.stats["atk"] = newValue
        elif statName == "def":
            self.stats["def"] = newValue
        elif statName == "spd":
            self.stats["spd"] = newValue
