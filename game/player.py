


import console
from .person import Person
from .person import PersonWay
from .person import PersonState

from .map import Map
from .map import Tile
from .map import TileType

from .camera import Camera

class Player(Person):
    'Player Class'

    #_style = '@';

    def __init__(self,x:int = 0,y:int = 0,name:str = ""):
        super().__init__(x,y,name);
        self._style = '@';
        return;


    def is_collision(self,will_x,will_y,map1:Map):

        if will_x < 0 or will_x > 79:
            return True;
        if will_y < 0:
            return True;
        

        return map1.is_collision(will_x,will_y);


    def is_collision_tile(self,will_x,will_y,map1:Map):
        return map1.is_collision(will_x,will_y);

    
    def walk(self,way,map1:Map):
        self.way = way;

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

        try:
            if self.is_collision_tile(will_x,will_y,map1):
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


    def draw_need_camera(self,camera:Camera):
        will_x = int(self.x) - int(camera.look_x) + console.get_width() / 2;
        will_y = int(self.y) - int(camera.look_y) + console.get_height() / 2;

        console.move_cursor(will_x,will_y);
        print(self._style);


    def draw_in_cache(self):
        #console.move_cursor(self.x,self.y);
        #print(self._style);

        console.move_cache_cursor(self.x,self.y);
        console.add_str(self._style);


    def draw_in_cache_need_camera(self,camera:Camera):
        will_x = int(self.x) - int(camera.look_x) + console.get_width() / 2;
        will_y = int(self.y) - int(camera.look_y) + console.get_height() / 2;


        console.move_cache_cursor(will_x,will_y);
        console.add_str(self._style);





