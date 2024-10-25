class Actor():
    '''Interface to be implemented by each game character
    '''
    def move(self):
        '''Called by Arena, at the actor's turn
        '''
        raise NotImplementedError('Abstract method')

    def collide(self, other: 'Actor'):
        '''Called by Arena, whenever the `self` actor collides with some
        `other` actor
        '''
        raise NotImplementedError('Abstract method')

    def position(self) -> (int, int, int, int):
        '''Return the rectangle containing the actor, as a 4-tuple of ints:
        (left, top, width, height)
        '''
        raise NotImplementedError('Abstract method')

    def symbol(self) -> (int, int, int, int):
        '''Return the position (x, y, w, h) of current sprite, if it is contained in
        a larger image, with other sprites. Otherwise, simply return (0, 0, 0, 0)
        '''
        raise NotImplementedError('Abstract method')
    
    def stay(self) -> (int, int, int, int):
      
        raise NotImplementedError('Abstract method')


class Arena (): 
    def __init__(self, w, h):
        self._wCanvas, self._hCanvas = w, h
        self._actors = []
        self._actorsSfondi = []
        self._scontro=False
        
    def add(self, a: Actor):
        if a not in self._actors:
            self._actors.append(a)
        #print (len(self._actors))
        #print (self._actors)
        
    def addSfondi(self, b: Actor):
        self._actorsSfondi.append(b)
        
    def move_all(self):
       actors = list(reversed(self._actors))
       for a in actors:
            previous_pos = a.position()
            a.move()
            if a.position() != previous_pos:  # optimization for stationary actors
                for other in actors:
                    # reversed order, so actors drawn on top of others
                    # (towards the end of the cycle) are checked first
                    if other is not a and self.check_collision(a, other):
                            a.collide(other)
                            other.collide(a)
                            #if a.collide(other)==False:
                               # sys.exit()
            
    def move_allSfondi(self):
        for b in self._actorsSfondi:
            b.move()
            
    def size(self):
        return self._wCanvas, self._hCanvas
    
    def remove(self, a: Actor):
        '''Cancel an actor from this arena
        '''
        if a in self._actors:
            self._actors.remove(a)
    def actors(self) -> list:
        return list(self._actors)
    def actorsSfondi(self) -> list:
        return list(self._actorsSfondi)
    
    def modifica (self,oggetto):
        self._actors.remove(oggetto)
        
    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        '''Check the two actors (args) for mutual collision (bounding-box
        collision detection). Return True if colliding, False otherwise
        '''
        x1, y1, w1, h1 = a1.position()
        x2, y2, w2, h2 = a2.position()
        
        return (y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2
            and a1 in self._actors and a2 in self._actors)
class Rover(Actor):
    def __init__(self,arena, x:float, y:float):
        self._x,self._y = x,y
        self._dx, self._dy=0,2
        self._x2=x
        self._speed = 2
        self._w, self._h = 40,30
        arena.add(self)
        self._Valore=True
        self._scontro=False
        self._macchinaScontrata=False

    def move(self):
        
        if self._macchinaScontrata:
            self._dy=1
        #print ("x,y del rover",self._x,self._y)
        if self._y + self._dy <=0 or self._y + self._dy >= ARENA_H-35 and self._dy!=1:
            self._dy=0
        else :
            self._dy+=0.06
        self._y=self._y+self._dy
        self._x+=self._dx
        
        
            
        if self._x>=self._x2+5*(self._speed):
            self._dx=0
            self._x2=self._x
        if self._x-5*(self._speed)<=self._x2-10*(self._speed):
            self._dx=0
            self._x2=self._x
        
    
       
    def position(self):
        return self._x, self._y, self._w, self._h
    
    def go_left(self):
        self._dx, self._dy = -self._speed, 0
        self._valore=False

    def go_right(self):

        self._dx, self._dy = +self._speed, 0
        self._valore=True

    def go_down(self):
        self._dx, self._dy = 0, +self._speed

    def stay(self):
        self._dx, self._dy = 0, 0
    def go_up3(self):
        self._dx, self._dy = +2, -self._speed
        

    def collide(self,other):
        
        if isinstance (other,Buche) :
             x, y, w, h = other.position()
             if self._x+35 >= x and self._x <= x:
                 self._scontro=True
                 self._macchinaScontrata=True
                 
        if isinstance (other,Roccia) :
             a,b,c,d = other.position()
             if self._x+35 >= a and self._x <= a and self._y >= b-25:
                     self._scontro=True
                     self._macchinaScontrata=True
                     
    def symbol(self):
        if self._macchinaScontrata :
            return 170, 288, self._w, self._h
        '''
        if self._y >262 and self._y<263 :
            self._yscelta=False
        '''
           
        if self._y>= 295 or self._y<= 295:
            self._yscelta=True
           
            return 247, 159, self._w, self._h
        '''
        if self._y <295 and self._y>261 and self._yscelta==True :
            return 42, 153, self._w, self._h 
        if self._y>= 262 and self._y <295 and self._yscelta==False:
            return 82, 153, self._w, self._h
        '''
    def ritorno(self) :
        return self._Valore
    def position1(self) -> (int, int,int,int):
        return self._x, self._y,self._dx, self._dy
    def position2(self) -> (int, int):
        return self._x, self._y
    def restituzioneBoolena(self):
        return self._scontro
    def modifica(self):
        self._macchinaScontrata=True
    

    
