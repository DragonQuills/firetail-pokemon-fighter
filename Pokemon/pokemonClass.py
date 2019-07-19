from moves import Move
import pokebase as pb

class Pokemon:
    def __init__(self, nickname, pokemonSpecies, pokeTypes = ["", ""], stats = [0, 0, 0, 0], newMoves = ["", "", "", ""]):
        self.name = nickname
        self.species = pokemonSpecies
        self.types = ["", ""]
        self.stats = {}
        try:
            self.stats["hp"] = int(stats[0])
        except ValueError:
            self.stats["hp"] = 0

        try:
            self.stats["atk"] = int(stats[1])
        except ValueError:
            self.stats["atk"] = 0

        try:
            self.stats["def"] = int(stats[2])
        except ValueError:
            self.stats["def"] = 0

        try:
            self.stats["spd"] = int(stats[3])
        except ValueError:
            self.stats["spd"] = 0

        #making negative numbers = 0
        for x in self.stats:
            if self.stats[x] < 0:
                self.stats[x] = 0

        #making sure types are valid types
        try:
            self.types[0] = pb.type_(pokeTypes[0].lower()).name
        except:
            pass
        try:
            self.types[1] = pb.type_(pokeTypes[1].lower()).name
        except:
            pass
        #adding moves since they check themselves for validity
        self.moves = self._createMovesList(newMoves)

    def changeStat(self, statName, newValue):
        statName.lower()
        if statName == "hp":
            self.stats["hp"] = newValue
        elif statName == "atk":
            self.stats["atk"] = newValue
        elif statName == "def":
            self.stats["def"] = newValue
        elif statName == "spd":
            self.stats["spd"] = newValue
        else:
            return False
        return True

    def changeMove(self, moveNum, newMoveName):
        moveNum = moveNum - 1
        newMove = Move(newMoveName)

        #if this isn't a real move, return false and don't change the move
        if newMove.name == "Struggle" or newMove.name == "":
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

    def changeType(self, typesList):
        if len(typesList) == 2: #if given two types
            self.types = typesList
        else: #if only given one type
            self.types = typesList #make the list that new list
            self.types.append("") #then add a blank type so the database will save it correctly
