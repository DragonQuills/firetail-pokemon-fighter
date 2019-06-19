import pokebase as pb

class Move:
    def __init__(self, moveName):
        self.name = moveName
        moveData = pb.move(moveName)
        self.type = moveData.type.name
        self.power = moveData.power
        self.accuracy = moveData.accuracy
