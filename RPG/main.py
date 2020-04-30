from random import randint

from RPG.Class.Player import Player
from RPG.Class.character.Hero.Hero import Hero
from RPG.Class.character.Monster.Monster import Monster
from RPG.Functions.display_fight_ff import display_fight
from RPG.Functions.fight_ff import fight

if __name__ == "__main__":
    hero = Hero(name="dylan", max_life=100, attk_point=10, def_point=0, dex_point=10, is_player=True)
    Player(hero=hero)

    x = 1
    while True:
        name = 'monster_' + str(x)
        monster = Monster(
            name=name, max_life=randint(11, 22),
            attk_point=10+x, def_point=x, dex_point=x
        )
        fight(Player().hero, monster)
        x += 1

    print('Vous avez gagné')
