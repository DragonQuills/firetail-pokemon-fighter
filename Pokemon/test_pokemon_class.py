from pokemonClass import Pokemon
from moves import Move
import pytest

def test_initializes_correctly():
    #pokemon with type, stats, and blank moves
    steve = Pokemon("Steve", "Charmander", ["fire",""], [20, 5, 5, 5], ["ember", "scratch", "", ""])
    assert steve.name == "Steve"
    assert steve.species == "Charmander"
    assert steve.types[0] == "fire"
    assert steve.types[1] == ""
    assert steve.stats["hp"] == 20
    assert steve.stats["atk"] == 5
    assert steve.stats["def"] == 5
    assert steve.stats["spd"] == 5
    assert steve.moves[0].name == "Ember"
    assert steve.moves[1].name == "Scratch"
    assert steve.moves[1].type == "normal"
    assert steve.moves[2].name == ""

    #testing pokemon with just name and species
    jazz = Pokemon("Jazz", "Bellsprout")
    assert jazz.name == "Jazz"
    assert jazz.species == "Bellsprout"
    assert jazz.stats["hp"] == 0
    assert jazz.types == ["", ""]
    assert jazz.moves[0].name == ""

    #tests pokemon class handles bad inputs correctly
    badType = Pokemon("Bad Type", "Pokemon", ["normal", "punching"], [10, 10, 10, 10], ["tackle", "", "", ""])
    assert badType.types[1] == ""

    missingStat = Pokemon("Missing Stat", "Pokemon", ["normal", "fighting"], ["", 10, 10, 10], ["tackle", "", "", ""])
    assert missingStat.stats["hp"] == 0

    badStat = Pokemon("Missing Stat", "Pokemon", ["normal", "fighting"], ["fishfinger", 10, 10, 10], ["tackle", "", "", ""])
    assert badStat.stats["hp"] == 0

def test_changes_stat():
    #testing default stats
    jazz = Pokemon("Jazz", "Bellsprout")
    assert jazz.stats["hp"] == 0
    assert jazz.stats["atk"] == 0
    assert jazz.stats["def"] == 0
    assert jazz.stats["spd"] == 0

    #changing each stat
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

    #tests function returns true if a valid move is given and false if not
    assert steve.changeMove(1, "fake move") == False
    assert steve.changeMove(2, "fury swipes") == True
    assert steve.changeMove(3, "bite") == True

    #tests that fake move wasn't changed
    assert steve.moves[0] != Move("fake move")

    #tests that a new move is appened
    assert steve.moves[2] == Move("bite")

def test_changes_species():
    #testing species change for evolution
    jazz = Pokemon("Jazz", "Bellsprout")
    jazz.changeSpecies("Weepingbell")
    assert jazz.species == "Weepingbell"


def test_changes_type():
    #tests changing one type
    trina = Pokemon("Trina", "customSpecies", ["water", ""])
    trina.changeType(["grass"])
    assert trina.types[0] == "grass"
    assert trina.types[1] == ""

    #tests changing both types at once
    tori = Pokemon("Tori", "Torchic", ["fire", ""])
    tori.changeType(["fire", "fighting"])
    assert tori.types[0] == "fire"
    assert tori.types[1] == "fighting"
