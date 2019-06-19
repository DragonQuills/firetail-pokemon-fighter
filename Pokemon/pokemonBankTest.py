from pokemonBank import PokeBank
from pokemonClass import Pokemon

def test_adds_pokemon():
    bank = PokeBank()
    bank.addPokemon("Jazz", "Bellsprout", ["grass", "poison"], [15, 5, 5, 5])
    assert bank.allPokemon["Jazz"].name == "Jazz"

def test_returns_names():
    bank = PokeBank()
    bank.addPokemon("Jazz", "Bellsprout", ["grass", "poison"], [15, 5, 5, 5])
    bank.addPokemon("Shell", "Dragonite", ["dragon", "flying"], [65, 22, 18, 35])
    bank.addPokemon("Doggo", "Lillipup", ["normal"], [15, 5, 5, 5])
    allMon = bank.getAllNames()
    assert allMon[0] == "Jazz: Bellsprout"
    assert allMon[1] == "Shell: Dragonite"
    assert allMon[2] == "Doggo: Lillipup"





# def test_save_and_load():
#     file = open("testBankRead.txt", "w")
#     file.write("Jackie Pumpkaboo 25 ")
#     bank
