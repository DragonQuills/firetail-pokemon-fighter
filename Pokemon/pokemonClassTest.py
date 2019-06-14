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

def test_changes_stat():
    jazz = Pokemon("Jazz", "Bellsprout")
    assert jazz.hitpoints == 0
    assert jazz.attack == 0
    assert jazz.defense == 0
    assert jazz.speed == 0

    jazz.changeStat("hp", 25)
    assert jazz.hitpoints == 25

    jazz.changeStat("atk", 5)
    assert jazz.attack == 5

    jazz.changeStat("def", 7)
    assert jazz.defense == 7

    jazz.changeStat("spd", 6)
    assert jazz.speed == 6
