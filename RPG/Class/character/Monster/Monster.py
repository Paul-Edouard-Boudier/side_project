from dataclasses import dataclass
from RPG.Class.character.Character import Character


@dataclass
class Monster(Character):

    def on_death(self):
        print(f'{self.name} est MonsterKill !!!!')