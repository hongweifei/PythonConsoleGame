

import console

from .map import Tile
from .map import TileType
from .map import Map

from .player import Player
from .person import PersonWay

from .camera import Camera

import time


tiles = [
            Tile(0,0),Tile(1,0),Tile(2,0),Tile(3,0),Tile(4,0),Tile(5,0),Tile(6,0),Tile(7,0),Tile(8,0),Tile(9,0),Tile(10,0),
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
    while i < 24:
        print("                                                                            ");
        i += 1;


def game_draw_information(ch):
    console.move_cursor(0,0);
    print("按下的按键：" + str(chr(ch)))
    print("键值：" + str(ch));

    console.move_cursor(20,0);
    print("玩家名字：" + str(player1.name));
    console.move_cursor(20,1);
    print("玩家HP：" + str(player1.hp));
    console.move_cursor(20,2);
    print("玩家X：" + str(player1.x) + "      玩家Y：" + str(player1.y));


def game_init():
    map1.write("./map1");
    map1.read("./map1.map");

    
    TileType.add_type("TREE","+",True);
    TileType.write_data("./data1");



def game_start():
    quit = False;
    sleep_time = 1/30;

    map1.draw_need_camera(camera);
    player1.draw_need_camera(camera);

    while quit == False:

        ch = ord(console.getch());

        # game_clear();
        console.clear();


        if ch == 27:                                    # ESC
            quit = True;


        if ch == 97:                                    # ord('a');
            player1.walk(PersonWay.LEFT,map1);
        elif ch == ord('d'):
            player1.walk(PersonWay.RIGHT,map1);
        elif ch == ord('w'):
            player1.walk(PersonWay.UP,map1);
        elif ch == ord('s'):
            player1.walk(PersonWay.DOWN,map1);
            
            
        camera.look_x = player1.x;
        camera.look_y = player1.y;


        map1.draw_need_camera(camera);
        player1.draw_need_camera(camera);
        game_draw_information(ch);

        

        time.sleep(sleep_time);

        pass;

    game_exit();


def game_exit():
    console.clear();
    map1.draw();
    player1.draw();

    console.move_cursor(0,24);
    pass;






