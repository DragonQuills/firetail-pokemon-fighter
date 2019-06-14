from pokemonClass import Pokemon
import pytest

def test_initializes_correctly():
    steve = Pokemon("Steve", "Charmander", 20, 5, 5, 5)
    assert steve.nickname == "Steve"
    assert steve.species == "Charmander"
    assert steve.hitpoints == 20
    assert steve.attack == 5
    assert steve.defense == 5
    assert steve.speed == 5

    jazz = Pokemon("Jazz", "Bellsprout")
    assert jazz.nickname == "Jazz"
    assert jazz.species == "Bellsprout"
    assert jazz.hitpoints == 0

# def test_changes_stat():
#     jazz = Pokemon()
