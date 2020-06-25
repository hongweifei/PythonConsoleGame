

from gobject import Object
from enum import Enum


class PersonWay(Enum):
    UP = 0;
    DOWN = 1;
    LEFT = 2;
    RIGHT = 3;


class PersonState(Enum):
    STAND = 0;
    WALK = 1;
    RUN = 2;



class Person(Object):

    name:str = "";
    hp:float = 0;
    atk:float = 0;

    state = PersonState.STAND;
    way = PersonWay.UP;

    def __init__(self,name:str = ""):
        self.name = name;
        self.hp = 0;
        self.atk = 0;

        self.state = PersonState.STAND;
        self.way = PersonWay.UP;
        return;


