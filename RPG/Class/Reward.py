class Reward:

    def __init__(self, character: 'Character'):
        self.reward_gold_value = 0
        self.reward_xp_point = 0
        self.set_reward(character)

    def set_reward(self, character: 'Character'):
        self.set_gold_value(character)
        self.set_xp_point(character)
        # self.set_item_list(self, character)

    def set_gold_value(self, character: 'Character') -> None:
        self.reward_gold_value = 10

    def set_xp_point(self, character: 'Character') -> None:
        self.reward_xp_point = 50
