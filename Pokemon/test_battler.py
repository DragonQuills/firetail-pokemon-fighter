from battler import PokemonBattler
from pokemonClass import Pokemon
from moves import Move

def test_move_effectiveness_function():
    battler = PokemonBattler()

    #half damage test
    ember = Move("ember")
    flambi = Pokemon("Flambi", "Flareon", ["fire", ""])
    assert battler.moveTypeModifier(ember, flambi) == 0.5

    #double damage test with two moves
    iceBeam = Move("ice beam")
    pidgey = Pokemon("Pipi", "Pidgey", ["normal", "flying"])
    assert battler.moveTypeModifier(iceBeam, pidgey) == 2

    #no damage test
    thunderBolt = Move("thunderbolt")
    phanpy = Pokemon("Cheerio", "Phanpy", ["ground", ""])
    assert battler.moveTypeModifier(thunderBolt, phanpy) == 0

    #quadrouble damage test
    rockBlast = Move("rock blast")
    butterfree = Pokemon("Flutter", "Butterfree", ["bug", "flying"])
    assert battler.moveTypeModifier(rockBlast, butterfree) == 4

    #quarter damage test
    #reuses ember move from above
    kingdra = Pokemon("King", "Kingdra", ["water", "dragon"])
    assert battler.moveTypeModifier(ember, kingdra) == 0.25
