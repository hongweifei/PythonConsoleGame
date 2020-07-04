


import console
import game.game as game



import os


def main(stdscr):
    game.game_init();
    game.game_start();

    console.add_str("dawdawd\n");
    console.add_str(str(console.get_cursor_x()) + "\n");
    console.add_str(str(console.get_cursor_y()) + "\n");





console.wrapper(main);
console.pause();


































