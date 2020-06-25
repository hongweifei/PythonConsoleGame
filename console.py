




import os
from platform import system
import ctypes


system_name = system();


#Windows系统移动光标需使用
class COORD(ctypes.Structure):

    _fields_ = [("X", ctypes.c_short),("Y", ctypes.c_short)];

    def __init__(self,x,y):
        self.X = x;
        self.Y = y;



if system_name == "Windows":
    STD_OUTPUT_HANDLE= -11;
    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE);


def pause():
    if system_name == "Windows":
        os.system("pause");
        return;
    elif system_name == "Linux":
        return;
    elif system_name == "Java":
        return;


def clear():
    if system_name == "Windows":
        os.system("cls");
        return;
    elif system_name == "Linux":
        print("\033[2J")
        return;
    elif system_name == "Java":
        return;


def move_cursor(x:int,y:int):
    if system_name == "Windows":
        try:
            position = COORD(int(x),int(y));
            ctypes.windll.kernel32.SetConsoleCursorPosition(handle,position);
        except Exception as e:
            print(e);
    elif system_name == "Linux":
        print("\033[" + y + ";" + x + "H");
    elif system_name == "Java":
        return;



