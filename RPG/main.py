#from .Class.character.character import fibi
#fibi()

#from RPG.Class.character.Character import Character
from RPG.Class.character.Hero.Hero import Hero
from RPG.Class.character.Monster.Monster import Monster


if __name__ == "__main__":
    hero_one = Hero(name="dylan", life_point=100, attk_point=10, def_point=0, dex_point=10)
    monster_one = Monster(name="polo", life_point=20, attk_point=10, def_point=0, dex_point=0)

    print(f'Hero life:{hero_one.life_point} monster life: {monster_one.life_point}')
    hero_one.on_attack(monster_one)
    print(f'Hero life:{hero_one.life_point} monster life: {monster_one.life_point}')
    monster_one.on_attack(hero_one)
    print(f'Hero life:{hero_one.life_point} monster life: {monster_one.life_point}')
    hero_one.on_attack(monster_one)
    print(f'Hero life:{hero_one.life_point} monster life: {monster_one.life_point}')