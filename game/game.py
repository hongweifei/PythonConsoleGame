

import console

from .map import Tile
from .map import TileType
from .map import Map

from .player import Player
import game.person as person

import ctypes


tiles = [
            Tile(0,0,TileType.WALL),Tile(1,0),Tile(2,0),Tile(3,0),Tile(4,0),Tile(5,0),
            Tile(0,1),Tile(0,2),Tile(0,3),Tile(0,4),Tile(0,5),Tile(0,6),
            Tile(5,1),Tile(5,2),Tile(5,3),Tile(5,4),Tile(5,5),Tile(5,6),
            Tile(0,7),Tile(1,7),Tile(2,7),Tile(3,7),Tile(4,7),Tile(5,7),
        ]
map1 = Map(tiles);


player1 = Player(5,3,"Fly");


def game_init():
    map1.write_b("./map1");
    map1.read_b("./map1.map");
    return;



def game_start():
    quit = False;

    while quit == False:

        ch = ord(console.getch());

        console.clear();
        console.move_cursor(10,10);
        print(ch);

        if ch == 27:                                    # ESC
            quit = True;
            pass


        if ch == 97:                                    # ord('a');
            console.move_cursor(10,11);
            print("player move");
            player1.walk(person.PersonWay.LEFT,map1);
            pass
        elif ch == ord('d'):
            player1.walk(person.PersonWay.RIGHT,map1);
            pass
        elif ch == ord('w'):
            player1.walk(person.PersonWay.UP,map1);
            pass
        elif ch == ord('s'):
            player1.walk(person.PersonWay.DOWN,map1);
            pass

        map1.draw();
        player1.draw();

        pass;

    game_exit();


def game_exit():
    console.clear();
    pass;
