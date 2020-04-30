from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from RPG.Class.character.Hero.Hero import Hero


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
@dataclass()
class Player:
    hero: Hero = None
