


import console
from .person import Person

class Player(Person):
    'Player Class'

    style = '@';

    def __init__(self,name:str = ""):
        self.style = '@';
        self.name = name;
        return;

    def draw(self):
        console.move_cursor(self.x,self,y);
        print(self.style);







