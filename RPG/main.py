#from .Class.character.character import fibi
#fibi()

from RPG.Class.character.Character import Character
from RPG.Class.character.Hero.Hero import Hero
from RPG.Class.character.Monster.Monster import Monster, EndOfFight


def fight(attacker: Character, defender: Character) -> None:
    initiate_fighters_status(attacker, defender)
    fighting = True
    try:
        while fighting:
            fight_turn(attacker)
            fight_turn(defender)
    except EndOfFight as e:
        if isinstance(e.character, Hero) and e.character.is_player:
            print(f'{e.character.name} est mort et c\'est un game over')
        else:
            print(f'{e.character.name} est mort')
            del defender
            print(f'{e.character.name} est mort')


def fight_turn(fighter: Character) -> None:
    if isinstance(fighter, Hero) and fighter.is_player:
        player_turn(fighter)
    else:
        other_turn(fighter)


def player_turn(player: Hero) -> None:
    if input() == "1":
        player.on_attack(player.fighting_with)
    print(player.fighting_with.life_point)


def other_turn(other: Character) -> None:
    other.on_attack(other.fighting_with)
    print(other.fighting_with.life_point)
    return


def initiate_fighters_status(fighter_one: Character, fighter_two: Character) -> None:
    fighter_one.is_in_fight = fighter_two.is_in_fight = True
    fighter_one.fighting_with = fighter_two
    fighter_two.fighting_with = fighter_one
    return None


def end_of_combat():
    return


if __name__ == "__main__":
    hero_one = Hero(name="dylan", life_point=100, attk_point=10, def_point=0, dex_point=10, is_player=True)
    monster_one = Monster(name="polo", life_point=20, attk_point=10, def_point=0, dex_point=0)
    player_input = ""
    fight(hero_one, monster_one)
    print(monster_one)
