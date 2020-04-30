from RPG.Class.character.Character import Character


class EndOfFight(Exception):
    def __init__(self, character: Character):
        self.character = character


class GameOver(Exception):

    @staticmethod
    def game_over():
        print('game over')
        exit()
