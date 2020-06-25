


import console
from .person import Person
from .person import PersonWay
from .person import PersonState

from .map import Map
from .map import Tile
from .map import TileType

class Player(Person):
    'Player Class'

    _style = '@';

    def __init__(self,x:int,y:int,name:str = ""):
        self.x = x;
        self.y = y;
        self._style = '@';
        self.name = name;
        return;


    def collision(self,map1:Map):
        dx = 0;
        dy = 0;

        if self.way is PersonWay.LEFT:
            dx = -1;
        elif self.way is PersonWay.RIGHT:
            dx = 1;
        elif self.way is PersonWay.UP:
            dy = -1;
        elif self.way is PersonWay.DOWN:
            dy = 1;

        will_x = self.x + dx;
        will_y = self.y + dy;

        if will_x < 0 or will_x > 79:
            return True;
        if will_y < 0:
            return True;

        

        for i in range(len(map1.tiles)):
            #print(i);
            #print("will_x:" + str(will_x));
            #print("tile_x:" + str(map1.tiles[i].x));
            #print("will_y:" + str(will_y));
            #print("tile_y:" + str(map1.tiles[i].y) + "\n");
            if will_x == map1.tiles[i].x and will_y == map1.tiles[i].y:
                return True;
                
        
        return False;

    
    def walk(self,way,map1:Map):
        self.way = way;


        try:
            if self.collision(map1):
                return;
        except Exception as e:
            print(e);


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
            pass;


    def draw(self):
        console.move_cursor(self.x,self.y);
        print(self._style);







