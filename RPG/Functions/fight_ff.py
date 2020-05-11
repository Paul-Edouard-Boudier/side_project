from RPG.Class.Player.Player import Player
from RPG.Class.character.Character import Character
from RPG.Class.character.Hero.Hero import Hero
from RPG.Exceptions.FightExceptions import EndOfFight, GameOver
from RPG.Display.display_fight_ff import display_fight, display_end_of_fight


def fight(attacker: Character, defender: Character) -> None:
    initiate_fighters_status(attacker, defender)
    fighting = True
    try:
        while fighting:
            display_fight(attacker, defender)
            fight_turn(attacker)
            fight_turn(defender)
            display_fight(attacker, defender)
    except EndOfFight as e:
        end_of_fight(e.character)
        # print(hero_one)
        # display_fight_reward(e.character.get_reward())
    except GameOver:
        GameOver.game_over()


# -----------------------------------------------------------------------------


def fight_turn(fighter: Character) -> None:
    if isinstance(fighter, Hero) and fighter.is_player:
        player_turn(fighter)
    else:
        other_turn(fighter)


def player_turn(player_hero: Hero) -> None:
    player_input = Player().get_player_input()
    if player_input == "1":
        player_hero.on_attack(player_hero.fighting_with)
    elif player_input == "2":
        player_hero.on_use_life_potion()


def other_turn(other: Character) -> None:
    other.on_attack(other.fighting_with)
    return


def initiate_fighters_status(fighter_one: Character, fighter_two: Character) -> None:
    fighter_one.is_in_fight = fighter_two.is_in_fight = True
    fighter_one.fighting_with = fighter_two
    fighter_two.fighting_with = fighter_one
    return None


def end_of_fight(beaten_fighter: Character):
    Player().hero.get_reward(beaten_fighter.reward)
    display_end_of_fight(beaten_fighter)

