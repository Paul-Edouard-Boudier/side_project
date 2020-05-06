from dataclasses import dataclass
from RPG.Class.NPC.Merchant.Merchant_ff import buy_potion
from RPG.Class.Player.Player import Player
from RPG.Display.display_merchant_ff import display_merchant
from RPG.Class.NPC.NPC import NPC
from RPG.Class.character.Hero.Hero import Hero


@dataclass
class Merchant(NPC):
    life_potion_count = 5
    life_potion_value = 25

    def encounter_handler(self, hero: Hero):
        while True:
            display_merchant(self, hero)
            player_input = Player().get_player_input()
            buying_conditions = [
                player_input == "1",
                self.life_potion_count > 0,
                hero.hero_gold_value > self.life_potion_value
            ]
            if all(buying_conditions):
                buy_potion(self, hero)
            elif player_input == "2":
                break
