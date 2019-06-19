from pokemonClass import Pokemon

class PokeBank:
    def __init__(self, fileName = "bankSaveFile.txt"):
        self.allPokemon = {}
        self.saveFileName = fileName
        self.loadBank()

    def addPokemon(self, nickname, pokemonSpecies, pokeTypes = ["", ""], stats = [0, 0, 0, 0], newMoves = ["", "", "", ""]):
        self.allPokemon[nickname] = Pokemon(nickname, pokemonSpecies, pokeTypes, stats, newMoves)

    def getAllNames(self):
        pokeList = []
        for name, pokemon in self.allPokemon.items():
            pokeList.append(name)
        return pokeList

#     def saveBank(self):
#         saveFile = None
#         try:
#             saveFile = open(self.saveFileName, 'r+')
#         except:
#             saveFile = open(self.saveFileName, 'w')
#
#         for name, pokemon in self.allPokemon.items():
#             saveData = name + ", " + pokemon.species + ", " + pokemon.types[0] + + str(pokemon.stats["hp"])+ ", " + str(pokemon.stats["atk"]) + ", " + str(pokemon.stats["def"]) + ", " + str(pokemon.stats["spd"]) + "\n"
#             saveFile.write(saveData)
#         saveFile.close()
#
    def loadBank(self):
        try:
            loadFile = open(self.saveFileName, 'r')
        except:
            print("Error occured opening file " + self.saveFileName)
            return
        for line in loadFile:
            print (line)
            data = line.split(", ")
            name = data[0]
            species = data[1]
            types = [data[2], data[3]]
            stats = [data[4], data[5], data[6], data[7]]
            moves = [data[8], data[9], data[10], data[11]]
            self.addPokemon(name, species, types, stats, moves)
        loadFile.close()
bank = PokeBank("testBankLoad.txt")
# bank.addPokemon("Shell", "Dragonite")
# bank.saveBank()
