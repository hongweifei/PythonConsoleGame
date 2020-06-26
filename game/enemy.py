

from .person import Person


class Enemy(Person):


    def __init__(self,x:int = 0,y:int = 0,name:str = ""):
        super().__init__(x,y,name);
        self.name = name;











