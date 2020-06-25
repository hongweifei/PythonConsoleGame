



from map import Tile
from map import Map


tiles = [
            Tile(0,0,"&"),Tile(1,0,"@"),Tile(2,0),Tile(3,0),Tile(4,0),Tile(5,0),
            Tile(0,1),Tile(0,2),Tile(0,3),Tile(0,4),Tile(0,5),Tile(0,6),
            Tile(5,1),Tile(5,2),Tile(5,3),Tile(5,4),Tile(5,5),Tile(5,6),
            Tile(0,7),Tile(1,7),Tile(2,7),Tile(3,7),Tile(4,7),Tile(5,7),
        ]
map1 = Map(tiles);


def game_init():
    map1.draw();
    return;




