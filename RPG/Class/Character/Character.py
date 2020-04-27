#from .Character_ff import fibo
#def fibi():
    #fibo()

from dataclasses import dataclass, field, InitVar

@dataclass
class Character(object):
    name: str
    life_point: int
    attk_point: int
    def_point: int
    magick_point: int
    dex_point: int

