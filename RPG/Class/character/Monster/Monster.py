from dataclasses import dataclass

from RPG.Class.Reward import Reward
from RPG.Class.character.Character import Character
from RPG.Exceptions.FightExceptions import EndOfFight


@dataclass
class Monster(Character):

    def __post_init__(self):
        super().__post_init__()
        self.reward = Reward(self)

    def on_death(self):
        raise EndOfFight(self)
