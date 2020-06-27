



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

        text = f.readlines();
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

        
        style_list = self.style.split("\n");
        if style_list[len(style_list) - 1] == "" or style_list[len(style_list) - 1] == " ":
            self.height = len(style_list) - 1;
        elif style_list[len(style_list) - 1] != "":
            self.height = len(style_list);
            
        style_list.sort(reverse=True);
        self.width = len(style_list[0]);


        
    def updata(self):
        try:
            self.collision = TileType.get_type_collision(self.type_name);
            self.style = TileType.data[str(self.type_name) + "_style"];

            style_list = self.style.split("\n");
            if style_list[len(style_list) - 1] == "" or style_list[len(style_list) - 1] == " ":
                self.height = len(style_list) - 1;
            elif style_list[len(style_list) - 1] != "":
                self.height = len(style_list);

            style_list.sort(reverse=True);
            self.width = len(style_list[0]);

        except Exception as e:
            print(e);
        


    def draw(self):
        if self.x >= 0 and self.y >= 0 and self.x < console.get_width() and self.y < console.get_height() - 1:
            console.move_cursor(int(self.x),int(self.y));
            print(self.style);

    
    def draw_need_camera(self,camera:Camera):
        will_x = int(self.x) - int(camera.look_x) + console.get_width() / 2;
        will_y = int(self.y) - int(camera.look_y) + console.get_height() / 2;

        if will_x >= 0 and will_y >= 0 and will_x < console.get_width() and will_y < console.get_height() - 1:
            console.move_cursor(int(will_x),int(will_y));
            print(self.style);


    def draw_in_cache(self):
        #console.move_cursor(self.x,self.y);
        #print(self.style);

        if slef.x >= 0 and self.y >= 0 and self.x < console.get_width() and self.y < console.get_height() - 1:
            console.move_cache_cursor(int(self.x),int(self.y));
            console.add_str(self.style);


    def draw_in_cache_need_camera(self,camera:Camera):
        will_x = int(self.x) - int(camera.look_x) + console.get_width() / 2;
        will_y = int(self.y) - int(camera.look_y) + console.get_height() / 2;

        if will_x >= 0 and will_y >= 0 and will_x < console.get_width() and will_y < console.get_height() - 1:
            console.move_cache_cursor(int(will_x),int(will_y));
            console.add_str(self.style);
        


class Map:

    tiles = [];

    def __init__(self,tiles = []):
        self.tiles = tiles;
        return;


    def updata(self):
        for tile in self.tiles:
            tile.updata();

    
    def is_collision(self,x,y):

        for tile in self.tiles:

            if tile.collision:
                if x >= int(tile.x) and x < int(tile.x) + int(tile.width) and y >= int(tile.y) and y < int(tile.y) + int(tile.height):
                    console.move_cache_cursor(0,22);
                    print(tile);
                    print("X:" + str(tile.x));
                    print("Y:" + str(tile.y));
                    print("Width:" + str(tile.width));
                    print("Height:" + str(tile.height));
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


    def draw_in_cache(self):
        for tile in self.tiles:
            tile.draw_in_cache();
        return;


    def draw_in_cache_need_camera(self,camera:Camera):
        for tile in self.tiles:
            tile.draw_in_cache_need_camera(camera);
        return;








