from dataclasses import dataclass
from RPG.Class.character.Character import Character
from RPG.Exceptions.FightExceptions import EndOfFight, GameOver


@dataclass
class Hero(Character):
    is_player: bool = False
    hero_gold_value: int = 0
    life_potion_count: int = 1

    hero_actual_xp_point: int = 0
    hero_xp_to_next_level: int = 100

    def on_death(self) -> None:
        if self.is_player:
            raise GameOver()
        else:
            raise EndOfFight(self)

    def get_reward(self, reward: 'Reward') -> None:
        self.update_hero_xp_point(reward.reward_xp_point)
        self.hero_gold_value += reward.reward_gold_value

    def level_up(self) -> None:
        self.actual_level += 1
        self.hero_actual_xp_point = 0
        self.hero_xp_to_next_level = int(self.hero_xp_to_next_level * 1.25)

        self.up_stats(
            maximum_life=10, attack_point=1, defense_point=1,
            dexterity_point=1, magic_point=1
        )

    def update_hero_xp_point(self, reward_xp: int) -> None:
        new_value = self.hero_actual_xp_point + reward_xp
        if (x := new_value - self.hero_xp_to_next_level) >= 0:
            self.level_up()
            self.hero_actual_xp_point = x
        else:
            self.hero_actual_xp_point = new_value

    def on_use_life_potion(self):
        if self.life_potion_count:
            self.life_potion_count -= 1
            self.on_heal(20)
