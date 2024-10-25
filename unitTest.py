import g2d
from moon_patrolclassi import Actor
from moon_patrolclassi import Arena
from moon_patrolclassi import Rover
from moon_patrolclassi import Buche
from moon_patrolclassi import Roccia
from moon_patrolclassi import Alien
from moon_patrolclassi import Alien2
from moon_patrolclassi import ProiettiliAlieno
import unittest

ARENA_W, ARENA_H = 500, 330
arena=Arena(ARENA_W, ARENA_H)
alieno= Alien(arena, 200, 30) 
alieno2=Alien2(arena, -2000, 30)


cont=200
class SimpleactorsTest(unittest.TestCase):
    
    def test_Move(self):
        global cont
        #al richiamo del metodo move il rover si muove
        test_values = ( (40, 80, 40, 80),
                      (40, 215,40, 215 ),
                      (40, 220, 40, 220),
                      (40,290, 40,290),
                      (300, 80, 300, 80) )
        for param in test_values:
            x0, y0, x1, y1 = param
            #instanzio gli oggetti
            rover = Rover(arena,x0, y0) 
            proiettileAlieno=ProiettiliAlieno(arena,alieno,rover,196,230,13,20,0,5)
            roccia1=Roccia(rover,arena,295,300)
            #li faccio muovere controllando che il rover non salti sopra ad un certo y
            rover.go_up3()
            arena.move_all()
            #print(rover.position())
            #controllo che il rover non si trovi nella stessa posizione di partenza
            self.assertTrue(rover.position() != (x1, y1 ,40,30))
            #controllo che non salti a più di un certo livello
            self.assertTrue(rover.position() <= (500, 262 ,40,30))
            
           # print(alieno.position())
            #controllo che alieno sia dentro al canvas
            self.assertTrue(alieno.position2() < (500,330))
            #print(alieno2.position())
            #alieno non presente nel canvas
            self.assertTrue(alieno2.position2() < (0,330))
            #controllo che il proiettile abbia la stessa posizione dell'alieno
            proiettileAlieno.sparo()
            self.assertTrue(alieno.position2() == proiettileAlieno.position4())
            while cont>=0 :
                arena.move_all()
                if roccia1.position3()<=0:
                   arena.move_all()
                   print(roccia1.position3())
                   self.assertTrue(roccia1.position3()>=500 and roccia1.position3()<=1000)
                cont-=1
                
                
            '''
if isinstance (Rover,Roccia) :
    print(alieno2.position())
    self.assertTrue(Roccia.position3()>=Roverposition3() and Roccia.position3()<=Roverposition3()+40)
    
class SimpleAlienTest(unittest.TestCase):
    def test_MoveAlien(self):
        #l'alieno è presente all'interno del canvas 
        
class SimpleProiettileTest(unittest.TestCase):
    def test_MoveAlien(self):
        
        proiettileAlieno.sparo()
        arena.move_all()
        #il proiettile dell'alieno viene inizializzato solo al momento dello sparo
        #altrimenti non viene inizializzato
        #in questo caso il proiettile sta andando verso il basso
        print(proiettileAlieno.position())
        self.assertTrue(alieno.position3() < proiettileAlieno.position3())
        #parte sempre dalla posizione dell'alieno

'''       
    
if __name__ == '__main__':
    unittest.main()
