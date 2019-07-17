import pokebase as pb

class Move:
    def __init__(self, moveName):
        cleanName = moveName.lower().replace(" ", "-")
        try:
            moveData = pb.move(cleanName)
        except:
            self.name = cleanName
            self.type = ""
            self.power = -1
            self.accuracy = -1
            return
        self.name = moveData.names[2].name
        self.type = moveData.type.name
        self.power = moveData.power
        self.accuracy = moveData.accuracy

    def __eq__(self, otherMove):
        if self.name == otherMove.name and self.type == otherMove.type and self.power == otherMove.power and self.accuracy == otherMove.accuracy:
            return True
        else:
            return False
