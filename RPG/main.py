from random import randint

from RPG.Class.Player import Player
from RPG.Class.character.Hero.Hero import Hero
from RPG.Class.character.Monster.Monster import Monster
from RPG.Functions.fight_ff import fight

if __name__ == "__main__":
    hero_stats = {'name': "dylan", 'maximum_life': 100, 'attack_point': 10,
                  'defense_point': 0, 'dexterity_point': 10}

    hero = Hero(is_player=True, **hero_stats)
    Player(hero=hero)
    # for i in range(1, 10):
    #     Player().hero.update_hero_xp_point(100)
    #     print(f' actual xp point = {Player().hero.hero_actual_xp_point}')
    #     print(f' xp to next level = {Player().hero.hero_xp_to_next_level}')
    #     print(f' actual level {Player().hero.actual_level}')
    #     print('-------------')
    # print(Player().hero.__dict__)
    # exit()

    x = 1
    while True:
        name = 'monster_' + str(x)
        monster = Monster(
            name=name, maximum_life=randint(11, 22),
            attack_point=10 + x, defense_point=x, dexterity_point=x
        )
        fight(Player().hero, monster)
        x += 1

    print('Vous avez gagné')
