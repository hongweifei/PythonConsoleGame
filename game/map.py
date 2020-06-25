



import console
from .gobject import Object
from enum import Enum


class TileType(Enum):
    AIR = 0;
    FLOOR = 1;
    WALL = 2;
    DOOR = 3;
    WOOD = 4;
    


class Tile(Object):

    tile_type = TileType.AIR;
    style = '#';

    def __init__(self,x:int = 0,y:int = 0,tile_type = TileType.AIR):
        self.x = x;
        self.y = y;
        self.tile_type = tile_type;
        
        if self.tile_type is TileType.AIR:
            self.style = ' ';
        elif self.tile_type is TileType.FLOOR:
            self.style = ' ';
        elif self.tile_type is TileType.WALL:
            self.style = '#';
        elif self.tile_type is TileType.DOOR:
            self.style = '$';
        elif self.tile_type is TileType.WOOD:
            self.style = '+';
        else:
            self.style = '?';
        return;


    def get_type_value(self):
        return self.tile_type.value;


    def draw(self):
        console.move_cursor(self.x,self.y);
        print(self.style);
        return;


class Map:

    tiles = [];

    def __init__(self,tiles = []):
        self.tiles = tiles;
        return;

    def write_a(self,path:str):
        f = open(path + ".map","w");
        
        for tile in self.tiles:
            f.write(str(tile.x) + "," + str(tile.y) + "," + str(tile.tile_type) + ";\n");
            pass;

        f.close();
        return;

    def read_a(self,path:str):
        f = open(path,"r");

        self.tiles = [];

        text = f.readlines();
        for data in text:
            data_list1 = data.split(",");
            data_list2 = data_list1[2].split(";");

            # self.tiles.append(Tile(data_list1[0],data_list1[1],data_list2[0]));

            if data_list2[0] == "TileType.AIR":
                self.tiles.append(Tile(data_list1[0],data_list1[1],TileType.AIR));
            elif data_list2[0] == "TileType.FLOOR":
                self.tiles.append(Tile(data_list1[0],data_list1[1],TileType.FLOOR));
            elif data_list2[0] == "TileType.WALL":
                self.tiles.append(Tile(data_list1[0],data_list1[1],TileType.WALL));
            elif data_list2[0] == "TileType.DOOR":
                self.tiles.append(Tile(data_list1[0],data_list1[1],TileType.DOOR));
            elif data_list2[0] == "TileType.FLOOR":
                self.tiles.append(Tile(data_list1[0],data_list1[1],TileType.WOOD));

            pass;

        f.close();
        return;

    def write_b(self,path:str):
        f = open(path + ".map","w");
        
        for tile in self.tiles:
            f.write(str(tile.x) + "," + str(tile.y) + "," + str(tile.tile_type.value) + ";\n");
            pass;

        f.close();

    
    def read_b(self,path:str):
        f = open(path,"r");

        self.tiles = [];

        text = f.readlines();
        for data in text:
            data_list1 = data.split(",");
            data_list2 = data_list1[2].split(";");

            self.tiles.append(Tile(data_list1[0],data_list1[1],TileType(int(data_list2[0]))));

            pass;

        f.close();


    def draw(self):
        for tile in self.tiles:
            tile.draw();
        return;








