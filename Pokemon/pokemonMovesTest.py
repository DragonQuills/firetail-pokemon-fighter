from pokemonMoves import Move

def test_initializes_correctly():
    #testing for damage dealing moves
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

    #testing for non-valid moves
    blank = Move("")
    assert blank.name == ""
    assert blank.type == ""
    assert blank.power == -1
    assert blank.accuracy == -1

    fake = Move("fake")
    assert fake.name == "fake"
    assert fake.type == ""
    assert fake.power == -1
    assert fake.accuracy == -1

def test_equals_overload_works():
    scratch1 = Move("scratch")
    scratch2 = Move("scratch")
    ember = Move("ember")

    assert scratch1 == scratch2
    assert not(scratch1 == ember)
