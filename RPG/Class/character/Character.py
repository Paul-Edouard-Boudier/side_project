#from .Character_ff import fibo
#def fibi():
    #fibo()

from __future__ import annotations
from dataclasses import dataclass, field, InitVar
from RPG.Class.character import Character_ff


@dataclass
class Character():
    name: str = "Blob"
    life_point: int = 10
    attk_point: int = 1
    def_point: int = 1
    magick_point: int = 1
    dex_point: int = 1

    def on_attack(self, receiver: Character) -> None:
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