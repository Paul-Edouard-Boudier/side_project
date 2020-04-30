from RPG.Class.Player import Player
from RPG.Class.character.Character import Character


def display_fight(attacker: Character, defender: Character):
    print(f' \
    ================================= \n \
    ||        {attacker.name}               \n \
    || attak = {attacker.attk_point}   def = {attacker.def_point} \n \
    || dex = {attacker.dex_point} \n \
    || life = {attacker.life_point} / {attacker.max_life}  \n \
    --------------------------------- \n \
    ||        {defender.name}               \n \
    || attak = {defender.attk_point}  def = {defender.def_point}  \n \
    || dex = {defender.def_point}  \n \
    || life = {defender.life_point} / {defender.max_life}          \n \
    =================================')


class PLayer(object):
    pass


def display_end_of_fight(beaten_fighter):
    print(f'{beaten_fighter.name} est mort')
    print(f'xp point = {Player().hero.xp_point} (+ {beaten_fighter.reward.xp_point})')
    # experience
    # loot
    #     objet
    #     armes
    # gold
