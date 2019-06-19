from pokemonMoves import Move

class Pokemon:
    def __init__(self, nickname, pokemonSpecies, pokeTypes = [], stats = [0, 0, 0, 0], newMoves = []):
        self.name = nickname
        self.species = pokemonSpecies
        self.stats = {"hp" : stats[0], "atk" : stats[1], "def" : stats[2], "spd" : stats[3]}
        self.types = pokeTypes
        self.moves = self._createMovesList(newMoves)

    def changeStat(self, statName, newValue):
        if statName == "hp":
            self.stats["hp"] = newValue
        elif statName == "atk":
            self.stats["atk"] = newValue
        elif statName == "def":
            self.stats["def"] = newValue
        elif statName == "spd":
            self.stats["spd"] = newValue

    def changeMove(self, moveNum, newMoveName):
        pass

    def changeSpecies(self, newSpecies):
        self.species = newSpecies

    def _createMovesList(self, namesList):
        movesList = []
        for name in namesList:
            if name != "":
                movesList.append(Move(name))
        return movesList
