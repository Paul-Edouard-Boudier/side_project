from dataclasses import dataclass
from RPG.Class.character.Character import Character


@dataclass
class Hero(Character):
    xp_point: int = 1

    def on_death(self):
        super(Hero, self).on_death()
        print("Game Over")
