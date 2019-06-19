from pokemonClass import Pokemon
import pytest

def test_initializes_correctly():
    steve = Pokemon("Steve", "Charmander", ["fire",""], [20, 5, 5, 5], ["ember", "scratch"])
    assert steve.name == "Steve"
    assert steve.species == "Charmander"
    assert steve.types[0] == "fire"
    assert steve.types[1] == ""
    assert steve.stats["hp"] == 20
    assert steve.stats["atk"] == 5
    assert steve.stats["def"] == 5
    assert steve.stats["spd"] == 5
    assert steve.moves[0].name == "ember"
    assert steve.moves[1].name == "scratch"
    assert steve.moves[1].type == "normal"

    jazz = Pokemon("Jazz", "Bellsprout")
    assert jazz.name == "Jazz"
    assert jazz.species == "Bellsprout"
    assert jazz.stats["hp"] == 0
    assert jazz.types == ["", ""]
    assert jazz.moves == []

def test_changes_stat():
    jazz = Pokemon("Jazz", "Bellsprout")
    assert jazz.stats["hp"] == 0
    assert jazz.stats["atk"] == 0
    assert jazz.stats["def"] == 0
    assert jazz.stats["spd"] == 0

    jazz.changeStat("hp", 25)
    assert jazz.stats["hp"] == 25

    jazz.changeStat("atk", 5)
    assert jazz.stats["atk"] == 5

    jazz.changeStat("def", 7)
    assert jazz.stats["def"] == 7

    jazz.changeStat("spd", 6)
    assert jazz.stats["spd"] == 6

def test_changes_move():
    steve = Pokemon("Steve", "Charmander", ["fire",""], [20, 5, 5, 5], ["ember", "scratch"])
    steve.changeMove(0, "flamethrower")

def test_changes_species():
    jazz = Pokemon("Jazz", "Bellsprout")
    jazz.changeSpecies("Weepinbell")
    assert jazz.species == "Weepinbell"
