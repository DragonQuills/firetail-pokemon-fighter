from moves import Move

class Pokemon:
    def __init__(self, nickname, pokemonSpecies, pokeTypes = ["", ""], stats = [0, 0, 0, 0], newMoves = ["", "", "", ""]):
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
        moveNum = moveNum - 1
        newMove = Move(newMoveName)

        #if this isn't a real move, return false and don't change the move
        if newMove.accuracy == -1:
            return False

        #if it is a real move
        if moveNum >= len(self.moves): #and the slot doesn't have a move in it
            self.moves.append(newMove) #add the mvoe as a new move
        else: #and the slot already has a move in it
            self.moves[moveNum] = newMove #replace the old move with the new one
        return True

    def changeSpecies(self, newSpecies):
        self.species = newSpecies

    def _createMovesList(self, namesList):
        movesList = []
        for name in namesList:
            movesList.append(Move(name))
        return movesList
