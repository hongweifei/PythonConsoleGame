


import console
from .gobject import Object
from .camera import Camera

import json


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
        "AIR_forecolor":console.Color.WHITE,
        "AIR_backcolor":console.Color.BLACK,
        "FLOOR":False,
        "FLOOR_style":".",
        "FLOOR_forecolor":console.Color.WHITE,
        "FLOOR_backcolor":console.Color.BLACK,
        "WALL":True,
        "WALL_style":"#",
        "WALL_forecolor":console.Color.BLACK,
        "WALL_backcolor":console.Color.RED,
        "CLOSE_DOOR":True,
        "CLOSE_DOOR_style":"$",
        "CLOSE_DOOR_forecolor":console.Color.BLACK,
        "CLOSE_DOOR_backcolor":console.Color.YELLOW,
        "OPEN_DOOR":False,
        "OPEN_DOOR_style":"[",
        "OPEN_DOOR_forecolor":console.Color.YELLOW,
        "OPEN_DOOR_backcolor":console.Color.BLACK
    };



    @staticmethod
    def add_type(name,style:str,fore_color:int = console.Color.WHITE,back_color:int = console.Color.WHITE,collision:bool = False):
        type_name = name.replace("\n","");
        type_style = style.rstrip("\n");

        TileType.data[type_name] = collision;
        TileType.data[str(type_name) + "_style"] = str(type_style);
        TileType.data[str(type_name) + "_forecolor"] = fore_color;
        TileType.data[str(type_name) + "_backcolor"] = back_color;


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
            if data_list[1] == "True" or data_list[1] == "true" or data_list[1] == "True\n" or data_list[1] == "true\n":
                TileType.data[data_list[0]] = True;
            elif data_list[1] == "False" or data_list[1] == "false" or data_list[1] == "False\n" or data_list[1] == "false\n":
                TileType.data[data_list[0]] = False;
            else:
                TileType.data[data_list[0]] = data_list[1].rstrip("\n");

        f.close();


    @staticmethod
    def write_json(path:str):
        f = open(path,"w",encoding='utf-8');
        json.dump(TileType.data,f,indent = 4,sort_keys = True);
        f.close();


    @staticmethod
    def read_json(path:str):
        f = open(path,"r",encoding='utf-8')
        TileType.data = json.load(f);
        f.close();




class Tile(Object):

    #type_name = TileType.AIR;
    #style = '#';

    def __init__(self,x:int = 0,y:int = 0,type_name = TileType.FLOOR):
        self.x = x;
        self.y = y;

        self.type_name = type_name.replace("\n","");
        
        if self.type_name in TileType.data:
            self.collision = TileType.get_type_collision(self.type_name);
        else:
            TileType.add_type(self.type_name,"?",console.Color.WHITE,False);
            self.collision = TileType.get_type_collision(self.type_name);

        type_style_name = str(self.type_name) + "_style";
        if type_style_name in TileType.data:
            self.style = TileType.data[type_style_name];
        else:
            self.style = "?";

        
        self.updata();


    
    def updata(self):
        try:
            #碰撞
            self.collision = TileType.get_type_collision(self.type_name);
            self.style = TileType.data[str(self.type_name) + "_style"];

            #宽高，样式
            style_list = self.style.split("\n");
            if style_list[len(style_list) - 1] == "" or style_list[len(style_list) - 1] == " ":
                self.style = style_list[0];
                self.height = len(style_list) - 1;
            elif style_list[len(style_list) - 1] != "":
                self.height = len(style_list);

            style_list.sort(reverse=True);
            self.width = len(style_list[0]);

            #颜色
            type_forecolor_name = str(self.type_name) + "_forecolor";
            type_backcolor_name = str(self.type_name) + "_backcolor";

            if type_forecolor_name in TileType.data:
                self.forecolor = int(TileType.data[type_forecolor_name]);
            else:
                self.forecolor = console.Color.WHITE;
                TileType.data[type_forecolor_name] = self.forecolor;
            
            if type_backcolor_name in TileType.data:
                self.backcolor = int(TileType.data[type_backcolor_name]);
            else:
                self.backcolor = console.Color.BLACK;
                TileType.data[type_backcolor_name] = self.backcolor;

        except Exception as e:
            print(e);
        

    
    def draw(self):
        if int(self.x) >= 0 and int(self.y) >= 0 and int(self.x) < console.get_max_width() and int(self.y) < console.get_max_height() - 1:
            console.move_cursor(int(self.x),int(self.y));
            print(self.style);

    
    def draw_need_camera(self,camera:Camera):
        will_x = int(self.x) - int(camera.look_x) + int(console.get_max_width() / 2);
        will_y = int(self.y) - int(camera.look_y) + int(console.get_max_height() / 2);

        if will_x >= 0 and will_y >= 0 and will_x < console.get_max_width() and will_y < console.get_max_height() - 1:
            console.move_cursor(int(will_x),int(will_y));
            print(self.style);


    def draw_in_buffer(self):
        #console.move_cursor(self.x,self.y);
        #print(self.style);

        if self.x >= 0 and self.y >= 0 and self.x < console.get_max_width() and self.y < console.get_max_height() - 1:
            console.move_buffer_cursor(int(self.x),int(self.y));
            console.add_str(self.style,self.forecolor,self.backcolor);

    
    def draw_in_buffer_need_camera(self,camera:Camera):
        will_x = int(self.x) - int(camera.look_x) + int(console.get_max_width() / 2);
        will_y = int(self.y) - int(camera.look_y) + int(console.get_max_height() / 2);

        if will_x >= 0 and will_y >= 0 and will_x < console.get_max_width() and will_y < console.get_max_height() - 1:
            console.move_buffer_cursor(int(will_x),int(will_y));
            console.add_str(self.style,self.forecolor,self.backcolor);


    def draw_information(self):
        console.move_buffer_cursor(0,4);
        console.add_str("TypeName:" + str(self.type_name));

        console.move_buffer_cursor(0,5);
        console.add_str("TypeCollision:" + str(self.collision));

        console.move_buffer_cursor(0,6);
        console.add_str("TypeStyle:" + str(self.style));

        console.move_buffer_cursor(0,7);
        console.add_str("TypeForegroundColor:" + str(self.forecolor));

        console.move_buffer_cursor(0,8);
        console.add_str("TypeBackgroundColor:" + str(self.backcolor));

        console.move_buffer_cursor(0,9);
        console.add_str("X:" + str(self.x));

        console.move_buffer_cursor(0,10);
        console.add_str("Y:" + str(self.y));

        console.move_buffer_cursor(0,11);
        console.add_str("Width:" + str(self.width));

        console.move_buffer_cursor(0,12);
        console.add_str("Height:" + str(self.height));
        


class Map:

    #tiles = [];

    def __init__(self,tiles = {}):
        self.tiles = tiles;
        self.collision_tile = {};


    def updata_collision(self):
        for key,tile in self.tiles.items():
            if tile.collision:
                self.collision_tile[key] = str(tile.width) + "," + str(tile.height);


    def updata(self):
        for tile in self.tiles.values():
            tile.updata();

        self.updata_collision();

    


    def create(self,width:int,height:int,type_name:str = TileType.FLOOR):
        
        i = 0;
        while i < height:
            j = 0;
            while j < width:
                self.tiles[str(j) + "," + str(i)] = Tile(j,i,type_name);
                j += 1;
            i += 1;


        if TileType.get_type_collision(type_name):
            self.updata_collision();

    
    def create_tiles(self,x:int,y:int,width:int,height:int,type_name:str = TileType.FLOOR):
        i = 0;
        while i < height:
            j = 0;
            while j < width:
                tile_x = x + j;
                tile_y = y + i;
                self.tiles[str(tile_x) + "," + str(tile_y)] = Tile(tile_x,tile_y,type_name);
                j += 1;
            i += 1;


        if TileType.get_type_collision(type_name):
            self.updata_collision();

    

    
    def is_collision(self,x,y):

        """
        for tile in self.tiles.values():

            if tile.collision:
                if x >= int(tile.x) and x < int(tile.x) + int(tile.width) and y >= int(tile.y) and y < int(tile.y) + int(tile.height):
                    console.move_buffer_cursor(0,22);
                    print(tile);
                    print("TypeName:" + str(tile.type_name));
                    print("TypeCollision:" + str(tile.collision));
                    print("TypeStyle:" + str(tile.style));
                    print("TypeForegroundColor:" + str(tile.forecolor));
                    print("TypeBackgroundColor:" + str(tile.backcolor));
                    print("X:" + str(tile.x));
                    print("Y:" + str(tile.y));
                    print("Width:" + str(tile.width));
                    print("Height:" + str(tile.height));
                    return True;
        """


        tile_key = str(x) + "," + str(y);


        if tile_key not in self.collision_tile:
            return False;
        else:
            value = self.collision_tile[tile_key];

            test_list1 = tile_key.split(",");
            test_list2 = value.split(",");

            tile_x = test_list1[0];
            tile_y = test_list1[1];
            tile_width = test_list2[0];
            tile_height = test_list2[1];
            
            if x >= int(tile_x) and x < int(tile_x) + int(tile_width) and y >= int(tile_y) and y < int(tile_y) + int(tile_height):
                return True


        """
        for key,value in self.collision_tile.items():
            test_list1 = key.split(",");
            test_list2 = value.split(",");

            tile_x = test_list1[0];
            tile_y = test_list1[1];
            tile_width = test_list2[0];
            tile_height = test_list2[1];
            
            if x >= int(tile_x) and x < int(tile_x) + int(tile_width) and y >= int(tile_y) and y < int(tile_y) + int(tile_height):
                return True
        """
        
        return False;



    def write(self,path:str):
        f = open(path + ".map","w");
        
        for key,tile in self.tiles.items():
            f.write(str(key) + ":" + str(tile.x) + "," + str(tile.y) + "," + str(tile.type_name) + "\n");
            pass;

        f.close();

    
    def read(self,path:str):
        f = open(path,"r");

        self.tiles = {};

        i = 0;
        text = f.readlines();
        for data in text:
            data_list1 = data.split(":");
            data_list2 = data_list1[1].split(",");
            self.tiles[data_list1[0]] = Tile(data_list2[0],data_list2[1],data_list2[2]);
            i += 1;

        f.close();

    


    def draw(self):
        for tile in self.tiles.values():
            tile.draw();
        return;


    def draw_need_camera(self,camera:Camera):
        for tile in self.tiles.values():
            tile.draw_need_camera(camera);
        return;


    def draw_in_buffer(self):
        for tile in self.tiles.values():
            tile.draw_in_buffer();
        return;


    def draw_in_buffer_need_camera(self,camera:Camera):
        for tile in self.tiles.values():
            tile.draw_in_buffer_need_camera(camera);
        return;


    def draw_tile_information(self,x,y):
        key = str(x) + "," + str(y);

        if key in self.tiles:
            tile = self.tiles[key];
            tile.draw_information();












