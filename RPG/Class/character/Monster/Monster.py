from dataclasses import dataclass
from RPG.Class.character.Character import Character
from RPG.Exceptions.FightExceptions import EndOfFight


@dataclass
class Monster(Character):

    def on_death(self):
        raise EndOfFight(self)
