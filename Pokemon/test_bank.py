from bank import PokeBank
from pokemonClass import Pokemon

def test_adds_pokemon():
    #adding a pokmeon to the bank
    bank = PokeBank()
    bank.addPokemonFromData("Jazz", "Bellsprout", ["grass", "poison"], [15, 5, 5, 5])
    assert bank.allPokemon[0].name == "Jazz"

def test_returns_names():
    #adding several pokemon and returning their names
    bank = PokeBank()
    bank.addPokemonFromData("Jazz", "Bellsprout", ["grass", "poison"], [15, 5, 5, 5])
    bank.addPokemonFromData("Shell", "Dragonite", ["dragon", "flying"], [65, 22, 18, 35])
    bank.addPokemonFromData("Doggo", "Lillipup", ["normal", ""], [15, 5, 5, 5])
    allMon = bank.getAllNames()
    assert allMon[0] == "Jazz"
    assert allMon[1] == "Shell"
    assert allMon[2] == "Doggo"

def test_loads_correctly():
    file = open("testBankLoad.txt", "w")
    file.write("Jackie, Pumpkaboo, grass, ghost, 25, 11, 6, 7, astonish, , , \n")
    file.write("Doggo, Lillipup, normal, , 15, 5, 5, 5, , , , \n")
    file.close()

    bank = PokeBank("testBankLoad.txt")
    bank.loadBank()
    assert bank.getAllNames()[0] == "Jackie"
    assert bank.getAllNames()[1] == "Doggo"
    assert bank.allPokemon[0].types[0] == "grass"
    assert bank.allPokemon[1].types[1] == ""
    assert bank

def test_saves_then_loads():
    bank = PokeBank("testBankSave.txt")
    bank.addPokemonFromData("Jazz", "Bellsprout", ["grass", "poison"], [15, 5, 5, 5], ["tackle", "ember", "scratch", "growl"])
    bank.addPokemonFromData("Shell", "Dragonite", ["dragon", "flying"], [65, 22, 18, 35])
    bank.addPokemonFromData("Doggo", "Lillipup", ["normal", ""], [15, 5, 5, 5])
    bank.saveBank()

    bank.loadBank()
    assert bank.getAllNames()[0] == "Jazz"
    assert bank.getAllNames()[1] == "Shell"
    assert bank.getAllNames()[2] == "Doggo"
