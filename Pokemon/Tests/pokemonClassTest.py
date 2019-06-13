from pokemonClass import Pokemon
import pytest

def test_initializes_correctly():
    steve = Pokemon("Steve", "Charmander")
    assert steve.nickname == "Steve"
    assert steve._species == "charmander"
