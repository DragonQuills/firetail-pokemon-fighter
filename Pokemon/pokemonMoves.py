import pokebase as pb

class Move:
    def __init__(self, moveName):
        self.name = moveName
        try:
            moveData = pb.move(moveName)
        except:
            self.type = ""
            self.power = -1
            self.accuracy = -1
            return
        self.type = moveData.type.name
        self.power = moveData.power
        self.accuracy = moveData.accuracy
