

from .gobject import Object
from enum import Enum

import console

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

    #name:str = "";
    #hp:float = 0;
    #atk:float = 0;

    #state = PersonState.STAND;
    #way = PersonWay.UP;

    def __init__(self,x:int = 0,y:int = 0,name:str = ""):
        super().__init__(x,y);
        self.name = name;
        self.hp = 0;
        self.atk = 0;

        self.state = PersonState.STAND;
        self.way = PersonWay.UP;
        return;


    def walk(self,way):
        self.way = way;

        if self.way is PersonWay.LEFT:
            self.x -= 1;
            pass;
        elif self.way is PersonWay.RIGHT:
            self.x += 1;
            pass;
        elif self.way is PersonWay.UP:
            self.y -= 1;
            pass;
        elif self.way is PersonWay.DOWN:
            self.y += 1;


    def draw(self):
        console.move_cursor(self.x,self.y);
        print("@");









    

