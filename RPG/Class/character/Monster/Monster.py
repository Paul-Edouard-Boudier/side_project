from dataclasses import dataclass
from RPG.Class.character.Character import Character, EndOfFight


@dataclass
class Monster(Character):

    def on_death(self):
        raise EndOfFight(self)
        #print(f'{self.name} est MonsterKill !!!!')


