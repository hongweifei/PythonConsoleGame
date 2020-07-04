

import console

from .map import Tile
from .map import TileType
from .map import Map

from .player import Player
from .person import PersonWay

from .camera import Camera

import time



map1 = Map();



player1 = Player(5,3,"Fly");
camera = Camera(player1.x,player1.y);


def game_clear():
    console.move_cursor(0,0);
    
    i = 0;
    while i < console.get_max_height():
        print("                                                                            ");
        i += 1;


def game_draw_information(ch):
    
    if ch > 0:
        console.move_buffer_cursor(0,0);
        console.add_str("按下的按键：" + str(chr(ch)))
        console.move_buffer_cursor(0,1);
        console.add_str("ASCII码值：" + str(ch));

    console.move_buffer_cursor(20,0);
    console.add_str("玩家名字：" + str(player1.name));
    console.move_buffer_cursor(20,1);
    console.add_str("玩家HP：" + str(player1.hp));
    console.move_buffer_cursor(20,2);
    console.add_str("玩家X：" + str(player1.x) + "      玩家Y：" + str(player1.y));


def game_init():

    map1.create(80,60);   
    map1.create_tiles(0,0,80,1,TileType.WALL);
    map1.create_tiles(0,25,35,1,TileType.WALL);
    map1.create_tiles(45,25,35,1,TileType.WALL);
    map1.create_tiles(0,0,1,26,TileType.WALL);
    map1.create_tiles(80,0,1,26,TileType.WALL);
    map1.write("./map1");

    TileType.write_json("./data1.json");
    TileType.read_json("./data1.json");
    
    map1.read("./map1.map");




def game_start():
    quit = False;
    sleep_time = 1/60;

    map1.updata();

    map1.draw_need_camera(camera);
    player1.draw_need_camera(camera);
    game_draw_information(0);

    while quit == False:

        ch = ord(console.getch());

        # game_clear();
        console.clear_buffer();


        if ch == 27:                                    # ESC
            quit = True;


        if ch == ord('a') or ch == 75 or ch == 260:
            player1.walk(PersonWay.LEFT,map1);
        elif ch == ord('d') or ch == 77 or ch == 261:
            player1.walk(PersonWay.RIGHT,map1);
        elif ch == ord('w') or ch == 72 or ch == 259:
            player1.walk(PersonWay.UP,map1);
        elif ch == ord('s') or ch == 80 or ch == 258:
            player1.walk(PersonWay.DOWN,map1);


            
            
        camera.look_x = player1.x;
        camera.look_y = player1.y;


        map1.draw_in_buffer_need_camera(camera);
        player1.draw_in_buffer_need_camera(camera);
        game_draw_information(ch);
        map1.draw_tile_information(player1.x,player1.y);

        console.refresh();

        time.sleep(sleep_time);

        pass;

    game_exit();


def game_exit():
    console.clear();
    map1.draw();
    player1.draw();

    console.move_cursor(0,24);
    pass;






