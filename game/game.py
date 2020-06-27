

import console

from .map import Tile
from .map import TileType
from .map import Map

from .player import Player
from .person import PersonWay

from .camera import Camera

import time


tiles = [
            Tile(0,0),Tile(1,0,"TREE"),Tile(2,0),Tile(3,0),Tile(4,0),Tile(5,0),Tile(6,0),Tile(7,0),Tile(8,0),Tile(9,0),Tile(10,0),
            Tile(0,1),Tile(0,2),Tile(0,3),Tile(0,4),Tile(0,5),Tile(0,6),
            Tile(10,1),Tile(10,2),Tile(10,3),Tile(10,4),Tile(10,5),Tile(10,6),
            Tile(0,7),Tile(1,7),Tile(2,7),Tile(3,7),Tile(4,7),Tile(5,7),
        ]
map1 = Map(tiles);


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
        console.move_cache_cursor(0,0);
        console.add_str("按下的按键：" + str(chr(ch)))
        console.move_cache_cursor(0,1);
        console.add_str("ASCII码值：" + str(ch));

    console.move_cache_cursor(20,0);
    console.add_str("玩家名字：" + str(player1.name));
    console.move_cache_cursor(20,1);
    console.add_str("玩家HP：" + str(player1.hp));
    console.move_cache_cursor(20,2);
    console.add_str("玩家X：" + str(player1.x) + "      玩家Y：" + str(player1.y));


def game_init():
    map1.write("./map1");
    map1.read("./map1.map");
    
    TileType.write_data("./data1");
    TileType.read_data("./data1");


    #TileType.read_data("./data1");
    #map1.read("./map1.map");



def game_start():
    quit = False;
    sleep_time = 1/30;

    map1.updata();

    map1.draw_need_camera(camera);
    player1.draw_need_camera(camera);
    game_draw_information(0);

    while quit == False:

        ch = ord(console.getch());

        # game_clear();
        console.clear_cache();


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


        map1.draw_in_cache_need_camera(camera);
        player1.draw_in_cache_need_camera(camera);
        game_draw_information(ch);

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






