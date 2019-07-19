from moves import Move

def test_initializes_correctly():
    #testing for damage dealing moves
    scratch = Move("scratch")
    assert scratch.name == "Scratch"
    assert scratch.type == "normal"
    assert scratch.power == 40
    assert scratch.accuracy == 100

    ember = Move("ember")
    assert ember.name == "Ember"
    assert ember.type == "fire"
    assert ember.power == 40
    assert ember.accuracy == 100

    #testing for move with spaces and upper case
    jumpKick = Move("Jump Kick")
    assert jumpKick.name == "Jump Kick"
    assert jumpKick.type == "fighting"
    assert jumpKick.power == 100
    assert jumpKick.accuracy == 95

    #testing for non-valid moves
    blank = Move("")
    assert blank.name == ""
    assert blank.type == "normal"
    assert blank.power == 0
    assert blank.accuracy == 0

    fake = Move("fake")
    assert fake.name == "Struggle"
    assert fake.type == "normal"
    assert fake.power == 50
    assert fake.accuracy == None

def test_equals_overload_works():
    scratch1 = Move("scratch")
    scratch2 = Move("scratch")
    ember = Move("ember")

    assert scratch1 == scratch2
    assert not(scratch1 == ember)
