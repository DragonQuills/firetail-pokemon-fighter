from pokemonBank import Bank
from pokemonClass import Pokemon

def test_adds_pokemon():
    bank = Bank()
    bank.addPokemon("Jazz", "Bellsprout", [15, 5, 5, 5])
    jazz = Pokemon("Jazz", "Bellsprout", [15, 5, 5, 5])
    assert bank.allPokemon["Jazz"].nickname == jazz.nickname
