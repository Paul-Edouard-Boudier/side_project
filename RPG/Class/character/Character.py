from __future__ import annotations
from dataclasses import dataclass, field, InitVar

from RPG.Class.Reward import Reward
from RPG.Class.character import Character_ff


@dataclass
class Character:
    '''
    Upgrade : transform attribute variable to dict or array
    '''
    name: str = "Blob"

    is_in_fight: bool = False
    fighting_with: Character = None

    maximum_life: int = 10
    attack_point: int = 1
    defense_point: int = 1
    magic_point: int = 1
    dexterity_point: int = 1

    reward: Reward = None

    max_level: int = 99
    actual_level: int = 1

    def __post_init__(self):
        self.life_point = self.maximum_life

    def on_attack(self, receiver: Character) -> None:
        """
        if damage is int do damage else print miss
        :param receiver:
        :return: None
        """
        damage = Character_ff.calc_attack(self, receiver)
        if isinstance(damage, int):
            Character_ff.deal_damage(receiver, damage)
        else:
            print(f'attacker : {self.name} {damage}')
        return None

    def on_death(self):
        pass
        '''put del() into monster
        def del(self):
           print('Destructor called, vehicle deleted.')'''

    def up_stats(self, **kwargs) -> None:
        """
        Update dynamically the character stats
        can send positive and negative value

        :param kwargs: stats_to_update=value_to_add
        :return:
        """
        for k, v in kwargs.items():
            if k in self.__dict__:
                attr = getattr(self, k)
                # Can't have negative values for stats
                if attr + v > 0:
                    setattr(self, k, attr+v)
