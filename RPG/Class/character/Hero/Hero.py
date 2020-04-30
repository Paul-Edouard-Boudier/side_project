from dataclasses import dataclass
from RPG.Class.character.Character import Character
from RPG.Exceptions.FightExceptions import EndOfFight, GameOver


@dataclass
class Hero(Character):
    is_player: bool = False
    xp_point: int = 0
    gold_value: int = 0

    def on_death(self):
        if self.is_player:
            raise GameOver()
        else:
            raise EndOfFight(self)

    # def get_reward(self, reward: Reward):
    #     return
