



import console
from .gobject import Object
from .camera import Camera


class TileType():
    AIR = "AIR";
    FLOOR = "FLOOR";
    WALL = "WALL";
    CLOSE_DOOR = "CLOSE_DOOR"; #关着的门
    OPEN_DOOR = "OPEN_DOOR";


    true = 1;
    false = 0;


    data = {
        "AIR":False,
        "AIR_style":" ",
        "FLOOR":False,
        "FLOOR_style":" ",
        "WALL":True,
        "WALL_style":"#",
        "CLOSE_DOOR":True,
        "CLOSE_DOOR_style":"$",
        "OPEN_DOOR":False,
        "OPEN_DOOR_style":"S",
    };



    @staticmethod
    def add_type(name,style,collision):
        TileType.data[name] = collision;
        TileType.data[str(name) + "_style"] = str(style);


    @staticmethod
    def get_type_collision(type_name):
        if type_name in TileType.data:
            return bool(TileType.data[type_name]);
        else:
            return False;


    @staticmethod
    def write_data(path:str):
        f = open(path,"w");

        for key,value in TileType.data.items():
            f.write(str(key) + ":" + str(value) + "\n");


        f.close();


    @staticmethod
    def read_data(path:str):
        f = open(path,"r");

        text = f.readlines;
        for data in text:
            data_list = data.split(":");
            if data_list[1] == "True" or data_list[1] == "true":
                TileType.data[data_list[0]] = True;
            elif data_list[1] == "False" or data_list[1] == "false":
                TileType.data[data_list[0]] = False;
            elif data_list[1] == "1":
                TileType.data[data_list[0]] = True;
            elif data_list[1] == "0":
                TileType.data[data_list[0]] = False;
            else:
                TileType.data[data_list[0]] = data_list[1];

        f.close();








class Tile(Object):

    #type_name = TileType.AIR;
    #style = '#';

    def __init__(self,x:int = 0,y:int = 0,type_name = TileType.WALL):
        super().__init__(x,y);

        self.type_name = type_name.replace("\n","");
        
        if self.type_name in TileType.data:
            self.collision = TileType.get_type_collision(self.type_name);
        else:
            TileType.add_type(self.type_name,"?",False);
            self.collision = TileType.get_type_collision(self.type_name);

        type_style_name = str(self.type_name) + "_style";
        if type_style_name in TileType.data:
            self.style = TileType.data[type_style_name];
        else:
            self.style = "?";




    def draw(self):
        console.move_cursor(self.x,self.y);
        print(self.style);
        return;


    def draw_need_camera(self,camera:Camera):
        will_x = int(self.x) - int(camera.look_x) + 39;
        will_y = int(self.y) - int(camera.look_y) + 12;

        if will_x >= 0 and will_y >= 0 and will_x <= 79 and will_y <= 25:
            console.move_cursor(will_x,will_y);
            print(self.style);
        
        return;


class Map:

    tiles = [];

    def __init__(self,tiles = []):
        self.tiles = tiles;
        return;

    
    def is_collision(self,x,y):

        for tile in self.tiles:

            if tile.collision:
                if x == int(tile.x) and y == int(tile.y):
                    return True;
        
        return False;



    def write(self,path:str):
        f = open(path + ".map","w");
        
        for tile in self.tiles:
            f.write(str(tile.x) + "," + str(tile.y) + "," + str(tile.type_name) + "\n");
            pass;

        f.close();

    
    def read(self,path:str):
        f = open(path,"r");

        self.tiles = [];

        text = f.readlines();
        for data in text:
            data_list1 = data.split(",");
            self.tiles.append(Tile(data_list1[0],data_list1[1],data_list1[2]));

        f.close();


    def draw(self):
        for tile in self.tiles:
            tile.draw();
        return;


    def draw_need_camera(self,camera:Camera):
        for tile in self.tiles:
            tile.draw_need_camera(camera);
        return;








