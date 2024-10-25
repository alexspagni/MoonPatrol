import g2d
from time import time
from random import randint
ARENA_W, ARENA_H = 500, 330
import costanti

class Actor():
    
    def move(self):
        raise NotImplementedError('Abstract method')

    def collide(self, other: 'Actor'):
        raise NotImplementedError('Abstract method')

    def position(self) -> (int, int, int, int):
        raise NotImplementedError('Abstract method')

    def symbol(self) -> (int, int, int, int):
        raise NotImplementedError('Abstract method')
    
    def stay(self) -> (int, int, int, int):
        raise NotImplementedError('Abstract method')

class Arena ():
    
    def __init__(self,arenaCanvas):
        self._wCanvas, self._hCanvas = arenaCanvas
        self._actors = []
        self._actorsSfondi = []
        self._scontro=False
        self._punteggio=0
        
    def add(self, a: Actor):
        if a not in self._actors:
            self._actors.append(a)
        
    def addSfondi(self, b: Actor):
        self._actorsSfondi.append(b)
        
    def move_all(self):
       actors = list(reversed(self._actors))
       for a in actors:
            previous_pos = a.position()
            a.move()
            
            if a.position() != previous_pos:
                for other in actors:
                    
                    if other is not a and self.check_collision(a, other):
                            a.collide(other)
                            other.collide(a)
            
    def move_allSfondi(self):
        for b in self._actorsSfondi:
            b.move()
            
    def size(self):
        return self._wCanvas, self._hCanvas
    
    def remove(self, a: Actor):
        if a in self._actors:
            self._actors.remove(a)
            
    def actors(self) -> list:
        return list(self._actors)

    #I tre metodi punteggio seguenti permettono di incrementare il punteggio
    #basandosi sulla distruzione di una delle rocce o di un alieno
    
    def punteggio(self,bonus): 
        self._punteggio=bonus
        
    def punteggioGui(self,):
        return self._punteggio
    
    def modificapunteggio(self):
        self._punteggio=0
        return self._punteggio
    
    def actorsSfondi(self) -> list:
        return list(self._actorsSfondi)
    
    def modifica (self,oggetto):
        self._actors.remove(oggetto)
        
    def check_collision(self, a1: Actor, a2: Actor) -> bool:
        x1, y1, w1, h1 = a1.position()
        x2, y2, w2, h2 = a2.position()
        return (y2 < y1 + h1 and y1 < y2 + h2
            and x2 < x1 + w1 and x1 < x2 + w2
            and a1 in self._actors and a2 in self._actors)
    
class Rover(Actor):
    
    def __init__(self,arena,roverValori):
        self._x,self._y =roverValori
        self._dx, self._dy=costanti.dx_Rover,costanti.dy_Rover
        self._x2,self._y2=roverValori
        self._speed = costanti.speed_Rover
        self._w, self._h = costanti.w_Rover,costanti.h_Rover
        arena.add(self)
        self._Valore=True
        self._scontro=False
        self._macchinaScontrata=False

    def move(self):

        #Se la variabile booleana self._macchinaScontrata è True allora la macchina procede verso il basso
        
        if self._macchinaScontrata: 
            self._dy=1
            
        if self._y + self._dy <=0 or self._y + self._dy >= costanti.immagine_RoverCanvas and self._dy!=1:    #Gravità del rover 
            self._dy=0
            
        else : 
            self._dy+=costanti.gravita
            
        self._y=self._y+self._dy
        self._x+=self._dx
        
        if self._x>=self._x2+5*(self._speed): #Per fare in modo che la macchina si sposti un fotogramma alla volta verso destra
            self._dx=0
            self._x2=self._x
            
        if self._x-5*(self._speed)<=self._x2-10*(self._speed):  #Per fare in modo che la macchina si sposti un fotogramma alla volta verso sinistra
            self._dx=0
            self._x2=self._x    
       
    def position(self):
        return self._x, self._y, self._w, self._h
    
    def go_left(self):
        self._dx, self._dy = -self._speed, costanti.nullo
        self._valore=False      

    def go_right(self):
        self._dx, self._dy = +self._speed, costanti.nullo
        self._valore=True

    def go_down(self):
        self._dx, self._dy = costanti.nullo, +self._speed

    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
    def go_up3(self):
        self._dx, self._dy = costanti.speed_Rover, -self._speed

    def collide(self,other):     
        if isinstance (other,Buche) :
             x, y, w, h = other.position()
             if self._x+costanti.immagine_Rover >= x and self._x <= x: #Attraverso questo if riesco a controllare meglio il ritaglio dell'immagine 
                 self._scontro=True
                 self._macchinaScontrata=True
                 
        if isinstance (other,Roccia) :
             a,b,c,d = other.position()
             if self._x+costanti.immagine_Rover >= a and self._x <= a and self._y >= b-costanti.immagine_Roccia: #Attraverso questo if riesco a controllare meglio il ritaglio dell'immagine 
                     self._scontro=True
                     self._macchinaScontrata=True
                     
    def symbol(self):
        if self._macchinaScontrata :
            return costanti.rover_Scontrato
          
        if self._y>= 295 or self._y<= 295:
            self._yscelta=True
            return costanti.rover_salta
        '''
        Questa porzione di codice commentata permette di cambiare l'immagine del rover durante il salto

        if self._y <295 and self._y>261 and self._yscelta==True :
            return 42, 153, self._w, self._h 
        if self._y>= 262 and self._y <295 and self._yscelta==False:
            return 82, 153, self._w, self._h
        '''
    
    def position1(self) -> (int, int,int,int):
        return self._x, self._y,self._dx, self._dy
    
    def position2(self) -> (int, int): #Utilizzato nella gui
        return self._x, self._y
    
    def position3(self) -> (int): #Utilizzato negli unit test
        return self._x
    
    def restituzioneBoolena(self):  #Questo metodo serve per sapere se il rover si è scontrato oppure no con un altro oggetto
        return self._scontro
    
    def modifica(self): #Questo metodo serve per sapere quando un proiettile degli alieni colpisce il Rover
        self._macchinaScontrata=True
        
###################################################################################### 

class Buche(Actor):
    
    def __init__(self,rover,arena, x,y):
        self._w, self._h,self._ritaglioX,self._ritaglioy=costanti.bucaPiccola_symbol
        self._w2, self._h2,self._ritaglioX2,self._ritaglioy2=costanti.bucaGrande_symbol
        self._dx,self._dy=costanti.dxdy_Buca
        self._numerorandom=randint(0,1)
        self._x,self._y =x,y
        self._rover=rover
        self._arena=arena
        self.ARENA_W,self._ARENA_H=arena.size()
        arena.add(self)
       
    def move(self):
        self._x=self._x-self._dx
        self._y=self._y+self._dy
        
        if self._x<=costanti.nullo :    #Quando la buca esce dal canvas viene rimosso l'oggetto
            self._arena.remove(self)
            self._numerorandom=randint(0,1)
   
    def position(self):
        if self._numerorandom==0 :
            return self._x, self._y, self._w, self._h
        else :
            return self._x, self._y, self._w2, self._h2

    def collide(self,other):
        pass       

    def symbol(self):

        #In base all'immagine viene ritagliata l'una o l'altra buca
        
        if self._numerorandom==0 :
            return self._ritaglioX, self._ritaglioy, self._w, self._h
        else :
            return self._ritaglioX2, self._ritaglioy2, self._w, self._h
        
    def stay(self):
        self._dx, self._dy = 0, 0        

###############################################################################
        
class Roccia(Actor):
    
    
    def __init__(self,rover,arena,valoriroccia):
        self._w, self._h,self._ritaglioX,self._ritaglioy =costanti.rocciapiccola_Symbol
        self._w2, self._h2,self._ritaglioX2,self._ritaglioy2 =costanti.rocciaGrande_Symbol
        self._dx,self._dy=costanti.dxdy_Roccia
        self._numerorandom=randint(0,1)
        self._x,self._y = valoriroccia
        self._rover=rover
        self._arena=arena
        arena.add(self)
        self._proiettilex,self._proiettiley=0,0
       
    def move(self): #Le rocce non vengono mai eliminate, viene cambiata sotanto la coordinata x 
        if self._x <=0 :
            self._x=randint(500,1000)
            self._numerorandom=randint(0,1)
        self._x=self._x-self._dx
        self._y=self._y+self._dy
        
    def position(self):
        if self._numerorandom==0 :
            return self._x, self._y, self._w, self._h
        
        else :
            return self._x, self._y, self._w2, self._h2
        
    def position3(self):
        return self._x
            
    def collide(self,other):
        if isinstance (other,Proiettili) :
            self._arena.remove(self)
            self._arena.remove(other)
            self._x=randint(500,1000)
            self._arena.add(self)
            self._arena.punteggio(costanti.punteggio_Roccia) #Esempio: aumento del punteggio nel caso di distruzione della roccia
            
        if isinstance (other,Buche) :   #Nel caso in cui la roccia si trovi in concomitanza con la buca, la sua x viene aumentata di 200
            self._x+=costanti.collisione_buche

    def symbol(self):
        if self._numerorandom==0 :
            return self._ritaglioX, self._ritaglioy, self._w, self._h
        
        else :
            return self._ritaglioX2, self._ritaglioy2, self._w, self._h
        
    def stay(self):
        self._dx, self._dy = 0, 0
        
###################################################################################
        
class Proiettili(Actor):
    
    def __init__(self,arena,rover,valoriproiettili):
        self._ritagliox, self._ritaglioy,self._w, self._h,self._dx,self._dy = valoriproiettili
        self._x,self._y =0,0
        self._rover=rover
        self._arena=arena
        arena.add(self)
        self._x3,self._y3=rover.position2()
        
    def move(self):
        self._x+=self._dx
        self._y+=self._dy

        #Il proiettile in direzione orizzontale viene rimosso dopo una certa costante aggiunta alla x 
        
        if self._x>=self._x3+costanti.range_proiettile:
            self._arena.remove(self)

        #Il proiettile in direzione verticale viene rimosso dopo una certa costante aggiunta alla y 
            
        if self._y<=0:
            self._arena.remove(self)
                    
    def sparo (self):   #Prende la posizione del rover. Aumenta la x e la y del proiettile orizzontale
        self._x,self._y=self._rover.position2()
        self._x=self._x+costanti.allineamento_proiettilex
        self._y=self._y+costanti.allineamento_proiettiley
        
    def sparo2 (self):  #Prende la posizione del rover. Aumenta la x e la y del proiettile verticale
        self._x,self._y=self._rover.position2()
        self._x=self._x+costanti.allineamento_proiettilex
        self._y=self._y+costanti.allineamento_proiettiley
       
    def position(self):
        return self._x, self._y, self._w, self._h

    def collide(self, other):
        if isinstance (other,Roccia) :
            pass
            
    def symbol(self):
        return self._ritagliox, self._ritaglioy, self._w, self._h
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
############################################################################
        
class Alien(Actor):
    
    def __init__(self, arena,valoriAlieno1):
        self._x, self._y = valoriAlieno1
        self._xRitaglio,self._yRitaglio,self._w, self._h =costanti.alieno_symbol
        self._xmin, self._xmax = self._x, self._x + 150
        self._dx, self._dy = costanti.dxdy_Alieno
        self._arena = arena
        arena.add(self)
        self._canvasMinore,self._canvaMaggiore=costanti.rangemovimento_alieno

    def move(self): #Dato che l'alieno rientra da sinistra, prima di una certa costante (=20) l'alieno si muove soltanto verso destra e non in modo casuale
        if self._x<20 :
            self._dx=5
            self._x+=self._dx
            
        else :
            if self._canvasMinore <= self._x + self._dx <= self._canvaMaggiore:
                self._x += self._dx
                
            else:
                self._dx = -self._dx
                self._y += self._dy
                
    def position(self):
        return self._x, self._y, self._w, self._h
    
    def position2(self) -> (int, int):
        return self._x, self._y
    
    def position3(self): #Utilizzata nel unit test
        return self._y

    def symbol(self):
        return self._xRitaglio,self._yRitaglio, self._w, self._h

    def collide(self, other):
        if isinstance(other, Proiettili):
            self._arena.remove(self)

            #Vengono date delle nuove coordinate all'alieno in modo tale da farlo rientrare sempre da sinistra
            #nel caso in cui venisse ucciso dai proiettili del rover
            
            self._x=costanti.allineamento_alienox
            self._y=costanti.allineamento_alienoy
            self._arena.add(self)
            self._arena.punteggio(costanti.punteggio_Alieno)
            
        if isinstance(other, ProiettiliCannone):

            #Vengono date delle nuove coordinate all'alieno in modo tale da farlo rientrare sempre da sinistra
            #nel caso in cui venisse ucciso dai proiettili del rover
            
            self._arena.remove(self)
            self._x=(-3000,-2000)
            self._y=costanti.allineamento_alienoy
            self._arena.add(self)
            self._arena.punteggio(costanti.punteggio_Alieno)
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
#####################################################################
        
class ProiettiliAlieno(Actor):
    
    def __init__(self,arena,alieno,rover,valoriProiettiliAlieno1):
        self._ritagliox, self._ritaglioy,self._w, self._h,self._dx,self._dy = valoriProiettiliAlieno1
        self._x,self._y =alieno.position2()
        self._arena=arena
        self._rover=rover
        self._alieno=alieno
        arena.add(self)
        self._booleano2=False
        
    def move(self):
        self._x+=self._dx
        self._y+=self._dy
      
    def sparo (self):
        self._x,self._y=self._alieno.position2()
        
    def position(self):
        return self._x, self._y, self._w, self._h
    
    def position4(self):
        return self._x, self._y
    
    def position3(self):
        return self._y

    def collide(self, other):
        
        if isinstance(other, Rover):    #Il proiettile si è scontrato con il rover?
            a,b,c,d = other.position()
            if self._x >= a and self._x <= a+costanti.immagine_Roverx2 and self._y >= b+costanti.immagine_Rovery2:
                self._arena.remove(self)
                self._booleano2=True
                self._rover.modifica()
                
        if isinstance(other, ProiettiliCannone):      #Il proiettile si è scontrato con il cannone? 
                self._arena.remove(other)
                self._arena.remove(self)
                self._x,self._y=self._alieno.position2()
                self._arena.add(self)
                
        if isinstance(other, Proiettili):   #Il proiettile si è scontrato con i proiettili del rover?
            self._arena.remove(self)
            self._arena.remove(other)
            self._x,self._y=self._alieno.position2()
            self._arena.add(self)
            
        if isinstance(other, Bonus):    #Ho distrutto il cannone?
            self._arena.remove(other)
                
    def symbol(self):
        return self._ritagliox, self._ritaglioy, self._w, self._h
    
    def restituzioneBoolena(self) :
        return self._booleano2
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
########################################################################
        
class Alien2(Actor):
    
    def __init__(self, arena,valoriAlieno2):
        self._x, self._y = valoriAlieno2
        self._xRitaglio,self._yRitaglio,self._w, self._h=costanti.alieno_symbol2
        self._xmin, self._xmax = self._x, self._x + 150
        self._dx, self._dy = costanti.dxdy_Alieno2
        self._arena = arena
        arena.add(self)
        self._canvasMinore,self._canvaMaggiore=costanti.rangemovimento_alieno2

    def move(self):
        if self._x<20 :
            self._dx=5
            self._x+=self._dx
            
        else :
            if self._canvasMinore <= self._x + self._dx <= self._canvaMaggiore:
                self._x += self._dx
            else:
                self._dx = -self._dx
                self._y += self._dy

    def position(self):
        return self._x, self._y, self._w, self._h
    
    def position2(self) -> (int, int):
        return self._x, self._y

    def symbol(self):
        return self._xRitaglio,self._yRitaglio, self._w, self._h

    def collide(self, other):
        if isinstance(other, Proiettili):
            self._arena.remove(self)
            self._x=costanti.allineamento_alienox2
            self._y=costanti.allineamento_alienoy2
            self._arena.add(self)
            self._arena.punteggio(costanti.punteggio_Alieno2)
            
        if isinstance(other, ProiettiliCannone):
            self._arena.remove(self)
            self._x=randint(-2000,-1000)
            self._y=costanti.allineamento_alienoy2
            self._arena.add(self)
            self._arena.punteggio(costanti.punteggio_Alieno2)
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
##########################################################################
        
class ProiettiliAlieno2(Actor):
    
    def __init__(self,arena,Alieno2,rover,valoriProiettiliAlieno2):
        self._ritagliox, self._ritaglioy,self._w, self._h,self._dx,self._dy = valoriProiettiliAlieno2
        self._x,self._y =Alieno2.position2()
        self._arena=arena
        self._rover=rover
        self._Alieno=Alieno2
        arena.add(self)
        self._booleano2=False
        
    def move(self):
        self._x+=self._dx
        self._y+=self._dy
             
    def sparo (self):
        self._x,self._y=self._Alieno.position2()
        
    def position(self):
        return self._x, self._y, self._w, self._h
    
    def position4(self):
        return self._x, self._y

    def collide(self, other):
        if isinstance(other, Rover):
            a,b,c,d = other.position()
            if self._x >= a and self._x <= a+costanti.immagine_Roverx and self._y >= b+costanti.immagine_Rovery:
                self._arena.remove(self)
                self._booleano2=True
                self._rover.modifica()
                
        if isinstance(other, ProiettiliCannone):
                self._arena.remove(other)
                self._arena.remove(self)
                self._x,self._y=self._Alieno.position2()
                self._arena.add(self)

        if isinstance(other, Proiettili):
            self._arena.remove(self)
            self._arena.remove(other)
            self._x,self._y=self._Alieno.position2()
            self._arena.add(self)
            
        if isinstance(other, Bonus):
            self._arena.remove(other)
                
    def symbol(self):
        return self._ritagliox, self._ritaglioy, self._w, self._h
    
    def restituzioneBoolena(self) :
        return self._booleano2
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
############################################################################
class Sfondo(Actor):

    #Utilizzo due liste di sfondi affinchè non si sovrappongano tra di loro.
    #Utilizzo una x ausiliaria per controllare quando spostare il secondo sfondo.
    
    def __init__(self,arena,valorisfondo):
        self._x,self._y,self._ritagliox, self._ritaglioy,self._w, self._h,self._dx = valorisfondo
        self._dy=costanti.nullo
        self._x1=self._x
        arena.addSfondi(self)
        self._arena=arena
        
    def move(self):
        arena_w, arena_h = self._arena.size()
        self._x = (self._x - self._dx) % -arena_w
        self._x1 = (self._x1 - self._dx) % arena_w
        
        if self._x == -arena_w and self._x1 == costanti.costant_nullo :
            self._x, self._x1 == costanti.costant_nullo, arena_w
            self._x -= self._dx
            self._x1 -= self._x   
        
    def position(self):
        return self._x, self._y, self._w, self._h
    
    def position2(self):
        return self._x1, self._y, self._w, self._h

    def collide(self, other):
        pass            
            
    def restituzione(self):
        return self._numeroRandom

    def symbol(self):
        return self._ritagliox, self._ritaglioy, self._w, self._h
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
#############################################################################
        
class Bonus(Actor):

    #Il cannone è un alleato del rover e lo aiuta nella sconfitta degli alieni. è immune alle buche e alle rocce. può essere distrutto dagli alieni.
    
    def __init__(self,arena,rover,valoriCannone):
        self._x,self._y,self._ritagliox, self._ritaglioy,self._w, self._h = valoriCannone
        self._dx,self._dy=costanti.nullo,costanti.nullo
        self._rover=rover
        self._arena=arena
        arena.add(self)
        self._Valore=True
        self._x2=self._x
        self._speed = costanti.velocita_cannone
        
    def move(self): #Stesso move del rover senza jump.
       if self._x + self._dx<=costanti.nullo or self._y + self._dy >= ARENA_W :
            self._dx=costanti.costant_nullo
       self._x+=self._dx
       
       if self._x>=self._x2+5*(self._speed):
            self._dx=costanti.nullo
            self._x2=self._x
            
       if self._x-5*(self._speed)<=self._x2-10*(self._speed):
            self._dx=costanti.nullo
            self._x2=self._x       
        
    def position(self):
        return self._x, self._y, self._w, self._h
    
    def position2(self):
        return self._x, self._y

    def collide(self, other):
        pass
            
    def modifica(self):
        self._x,self._y=self._rover.position2()
        self._x=self._x+costanti.allineamento_CannoneX
        self._y=costanti.allineamento_CannoneY
        
    def symbol(self):
        return self._ritagliox, self._ritaglioy, self._w, self._h
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
    def go_left(self):
        self._dx, self._dy = -self._speed, costanti.nullo
        self._valore=False

    def go_right(self):
        self._dx, self._dy = +self._speed, costanti.nullo
        self._valore=True
        
##########################################################################
        
class ProiettiliCannone(Actor):

    #Stesso andamento dei proiettili del rover
    
    def __init__(self,arena,Cannone,valori_ProiettiliCannone):
        self._ritagliox, self._ritaglioy,self._w, self._h,self._dx,self._dy = valori_ProiettiliCannone
        self._x,self._y =100,100
        self._Cannone=Cannone
        self._arena=arena
        arena.add(self)
        self._x3,self._y3=self._Cannone.position2()
        
    def move(self):
        self._x+=self._dx
        self._y+=self._dy
        if self._y<=costanti.nullo:
            self._arena.remove(self)
        if self._y>=330:
            self._arena.remove(self)
        
    def sparo2 (self):
        self._x,self._y=self._Cannone.position2()
        self._x=self._x
        self._y=self._y-costanti.allineamentoproiettili_CannoneY     
        
    def position(self):
        return self._x, self._y, self._w, self._h

    def collide(self, other):
        if isinstance(other, Alien):
                self._arena.remove(self)
                self._arena.remove(other)
                self._x,self._y=self._Cannone.position2()
                self._arena.add(self)
                self._arena.punteggio(costanti.punteggioProiettili_Cannone)
            
    def symbol(self):
        return self._ritagliox, self._ritaglioy, self._w, self._h
    
    def stay(self):
        self._dx, self._dy = costanti.nullo, costanti.nullo
        
