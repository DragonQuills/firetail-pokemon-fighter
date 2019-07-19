import pokebase as pb

class Move:
    def __init__(self, moveName):
        cleanName = moveName.lower().replace(" ", "-")
        if cleanName == "":
            self.name = ""
            self.type = "normal"
            self.power = 0
            self.accuracy = 0
        else:
            moveData = None
            try:
                moveData = pb.move(cleanName)
            except:
                moveData = pb.move("struggle")
            self.name = moveData.names[2].name.strip()
            self.type = moveData.type.name
            self.power = moveData.power
            self.accuracy = moveData.accuracy

    def __eq__(self, otherMove):
        if self.name == otherMove.name and self.type == otherMove.type and self.power == otherMove.power and self.accuracy == otherMove.accuracy:
            return True
        else:
            return False
