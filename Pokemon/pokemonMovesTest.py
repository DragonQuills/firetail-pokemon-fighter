from pokemonMoves import Move

def test_initializes_correctly():
    scratch = Move("scratch")
    assert scratch.name == "scratch"
    assert scratch.type == "normal"
    assert scratch.power == 40
    assert scratch.accuracy == 100

    ember = Move("ember")
    assert ember.name == "ember"
    assert ember.type == "fire"
    assert ember.power == 40
    assert ember.accuracy == 100
