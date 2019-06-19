from pokemonClass import Pokemon

class PokeBank:
    def __init__(self, fileName = "bankSaveFile.txt"):
        self.allPokemon = {}
        self.saveFileName = fileName
        #self.loadBank()

    def addPokemon(self, nickname, pokemonSpecies, pokeTypes = [], stats = [0, 0, 0, 0], newMoves = []):
        self.allPokemon[nickname] = Pokemon(nickname, pokemonSpecies, pokeTypes, stats, newMoves)

    def getAllNames(self):
        pokeList = []
        for name, pokemon in self.allPokemon.items():
            pokeList.append(name + ": " + pokemon.species)
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
#     def loadBank(self):
#         try:
#             loadFile = open(self.saveFileName, 'r')
#         except:
#             return
#         for line in loadFile:
#             data = line.split(", ")
#             name = data[0]
#             species = data[1]
#             stats = [data[2], data[3], data[4], data[5]]
#             self.addPokemon(name, species, stats)
#         loadFile.close()
#
# bank = PokeBank()
# bank.addPokemon("Shell", "Dragonite")
# bank.saveBank()
