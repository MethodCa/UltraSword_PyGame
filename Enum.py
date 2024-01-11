from enum import Enum
from enum import IntEnum


class Animation(IntEnum):
    IDLE = 0
    ATTACK = 1
    DEFEND = 2
    DAMAGE = 3
    DEAD = 4


class GameState(IntEnum):
    START = 0
    CHARACTER_SELECT = 1
    HISCORE = 2
    BATTLE = 3
    HELP_S = 4
    GAMEOVER = 5


class AnimationType(IntEnum):
    STATIC = 0
    LOOP = 1
    ONE_TIME = 2


class Factory(IntEnum):
    KNIGHT = 0
    SAMURAI = 1
    SKELETON = 2
    SKELETON2 = 3
    BIRD = 4
