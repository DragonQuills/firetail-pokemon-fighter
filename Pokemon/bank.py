from pokemonClass import Pokemon

class PokeBank:
    def __init__(self, fileName = "bankSaveFile.txt"):
        self.allPokemon = []
        self.saveFileName = fileName

    def addPokemonFromData(self, nickname, pokemonSpecies, pokeTypes = ["", ""], stats = [0, 0, 0, 0], newMoves = ["", "", "", ""]):
        self.allPokemon.append(Pokemon(nickname, pokemonSpecies, pokeTypes, stats, newMoves))

    def addPokemonFromObject(self, pokemon):
        self.allPokemon.append(pokemon)

    def getAllNames(self):
        pokeList = []
        for pokemon in self.allPokemon:
            pokeList.append(pokemon.name)
        return pokeList

    def saveBank(self):
        saveFile = None
        try:
            saveFile = open(self.saveFileName, 'w')
        except:
            print("Error, couldn't save")
            saveFile.close()
            return

        for i in range(0, len(self.allPokemon)):
            pokemon = self.allPokemon[i]
            saveData = pokemon.name + ", " + pokemon.species + ", " + pokemon.types[0] + ", " + pokemon.types[1] + ", " + str(pokemon.stats["hp"])+ ", " + str(pokemon.stats["atk"]) + ", " + str(pokemon.stats["def"]) + ", " + str(pokemon.stats["spd"]) + ", " + pokemon.moves[0].name + ", " + pokemon.moves[1].name + ", " + pokemon.moves[2].name + ", " + pokemon.moves[3].name
            if i < len(self.allPokemon)-1:
                saveData = saveData + "\n"
            saveFile.write(saveData)
        saveFile.close()

    def loadBank(self):
        try:
            loadFile = open(self.saveFileName, 'r')
        except:
            print("Error occured opening file " + self.saveFileName)
            return
        try:
            for line in loadFile:
                data = line.split(", ")
                name = data[0]
                species = data[1]
                types = [data[2], data[3]]
                stats = [data[4], data[5], data[6], data[7]]
                moves = [data[8], data[9], data[10], data[11]]
                self.addPokemonFromData(name, species, types, stats, moves)
            loadFile.close()
        except:
            print("Error occured reading from file.")
            loadFile.close()
            return
