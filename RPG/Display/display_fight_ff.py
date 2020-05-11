from RPG.Class.Player.Player import Player
from RPG.Class.character.Character import Character
from RPG.Class.character.Hero.Hero import Hero


def display_fight(attacker: Character, defender: Character):
    if isinstance(attacker, Hero) and attacker.is_player:
        life_potion_line = f'|| Life potion = {attacker.life_potion_count}\n '

    print(f' \
    ================================= \n \
    ||        {attacker.name}               \n \
    || attak = {attacker.attack_point}   def = {attacker.defense_point} \n \
    || dex = {attacker.dexterity_point} \n \
    {life_potion_line}\
    || life = {attacker.life_point} / {attacker.maximum_life}  \n \
    --------------------------------- \n \
    ||        {defender.name}               \n \
    || attak = {defender.attack_point}  def = {defender.defense_point}  \n \
    || dex = {defender.dexterity_point}  \n \
    || life = {defender.life_point} / {defender.maximum_life}          \n \
    =================================')


def display_end_of_fight(beaten_fighter):
    print(f'{beaten_fighter.name} est mort')
    print(f'xp point = {Player().hero.hero_actual_xp_point} (+ {beaten_fighter.reward.reward_xp_point})')
    print(f'level = {Player().hero.actual_level}')
    print(f'player gold = {Player().hero.hero_gold_value} (+ {beaten_fighter.reward.reward_gold_value})')
