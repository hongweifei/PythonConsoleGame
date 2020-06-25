




import console
from gobject import Object


class Tile(Object):

    style = "#"

    def __init__(self,x:int = 0,y:int = 0,style = "#"):
        self.x = x;
        self.y = y;
        self.style = style;
        return;

    def draw(self):
        console.move_cursor(self.x,self.y);
        print(self.style);
        return;


class Map:

    tiles = [];

    def __init__(self,tiles = []):
        self.tiles = tiles;
        return;

    def draw(self):
        for tile in self.tiles:
            tile.draw();
        return;
