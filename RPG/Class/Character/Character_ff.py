# Functions
from .Character import Character
import random

def attack(attacker: Character, receiver: Character) -> None:
    calc_attack(attacker, receiver)
    deal_damage()
    return


def calc_attack(attacker: Character, receiver: Character) -> int|str:
    if  attacker_has_hit(attacker.dex_point, receiver.dex_point):
        damage = attacker.attk_point - receiver.def_point
        damage_deal = (damage,0)[damage<0]
        return damage_deal
    else:
        return "Miss"


def attacker_has_hit(att_dex: int, rec_dex: int) -> bool:
    """
    calc if attacker hit receiver. decrease hit chance by 5% for each dex point less
    :param att_dex:
    :param rec_dex:
    :return:
    """
    i = rec_dex - att_dex
    return i < random.randint(1, 20)


def deal_damage(damaged_Character: int) -> None: