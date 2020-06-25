




import os
from platform import system
import ctypes

#Windows系统移动光标需使用
class COORD(ctypes.Structure):

    _fields_ = [("X", ctypes.c_short),("Y", ctypes.c_short)];

    def __init__(self,x,y):
        self.X = x;
        self.Y = y;


STD_OUTPUT_HANDLE= -11;


def pause():
    system_name = system();

    if system_name == "Windows":
        os.system("pause");
        return;
    elif system_name == "Linux":
        return;
    elif system_name == "Java":
        return;


def clear():
    system_name = system();

    if system_name == "Windows":
        os.system("cls");
        return;
    elif system_name == "Linux":
        print("\033[2J")
        return;
    elif system_name == "Java":
        return;


def move_cursor(x:int,y:int):
    system_name = system();

    if system_name == "Windows":
        position = COORD(x,y);
        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE);
        ctypes.windll.kernel32.SetConsoleCursorPosition(handle,position);
        return;
    elif system_name == "Linux":
        print("\033[" + y + ";" + x + "H");
        return;
    elif system_name == "Java":
        return;



