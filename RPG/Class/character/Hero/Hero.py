from dataclasses import dataclass
from RPG.Class.character.Character import Character, EndOfFight


@dataclass
class Hero(Character):
    is_player: bool = False
    xp_point: int = 1

    def on_death(self):
        raise EndOfFight(self)
        super(Hero, self).on_death()
        print("Game Over")
