from time import time
from random import randint
from moon_patrolclassi import Arena,Actor,Rover,Buche,Roccia,Proiettili,Alien,ProiettiliAlieno,Alien2,ProiettiliAlieno2,Sfondo,Bonus,ProiettiliCannone
import costanti

     
class moonpatrolgame:
    
    def __init__(self):
        self._arena=Arena(costanti.arenaCanvas)
        self._hero =Rover(self._arena, costanti.rover_Valori)
        roccia1=Roccia(self._hero,self._arena,costanti.valori_Roccia1)
        roccia2=Roccia(self._hero,self._arena,costanti.valori_Roccia2)
        Alieno=Alien(self._arena,costanti.valori_Alieno1)
        Alieno2=Alien2(self._arena,costanti.valori_Alieno2)
        self._proiettili_alieno1=ProiettiliAlieno(self._arena,Alieno,self._hero,costanti.valori_ProiettiliAlieno1)
        self._proiettili_alieno2=ProiettiliAlieno2(self._arena,Alieno2,self._hero,costanti.valori_ProiettiliAlieno2)
        self._cannone=Bonus(self._arena,self._hero,costanti.valori_Cannone)
        bg1,bg2,bg3,bg4=Sfondo(self._arena,costanti.valori_Sfondo1),Sfondo(self._arena,costanti.valori_Sfondo2),Sfondo(self._arena,costanti.valori_Sfondo3),Sfondo(self._arena,costanti.valori_Sfondo4)
        bg5,bg6,bg7,bg8=Sfondo(self._arena,costanti.valori_Sfondo1_1),Sfondo(self._arena,costanti.valori_Sfondo2_1),Sfondo(self._arena,costanti.valori_Sfondo3_1),Sfondo(self._arena,costanti.valori_Sfondo4_1)
        self._start = time()
        self._playtime = 120
        
    def arena(self) -> Arena:
        return self._arena
    
    def buche1(self):   #Questa funzione permette di aggiungere una nuova buca alla lista attori 
        buche1=Buche(self._hero,self._arena,costanti.xRandom5,costanti.yBuche)
        
    def buche2(self):   #Questa funzione permette di aggiungere una nuova buca alla lista attori 
        buche2=Buche(self._hero,self._arena,costanti.xRandom6,costanti.yBuche)
        
    def bucheAlieno(self,xalieno):  #Questa funzione permette di aggiungere una nuova buca alla lista attori 
        buche2=Buche(self._hero,self._arena,xalieno,costanti.yBuche)
        
    def proiettili_alieno1(self):   #Questa funzione permette di utilizzare la classe ProiettiliAlieno1 per sparare un proiettile 
        return self._proiettili_alieno1
    
    def proiettili_alieno2(self):   #Questa funzione permette di utilizzare la classe ProiettiliAlieno1 per sparare un proiettile
        return self._proiettili_alieno2
    
    def proiettileRoverDritti(self):    #Questa funzione permette al rover di sparare proiettili infiniti in direzione est
        proiettile1=Proiettili(self._arena,self._hero,costanti.valori_ProiettiliDritti)
        proiettile1.sparo()
        
    def proiettileRoverAlto(self):  #Questa funzione permette al rover di sparare proiettili infiniti in direzione nord
        proiettile2=Proiettili(self._arena,self._hero,costanti.valori_ProiettiliAlto)
        proiettile2.sparo2()
        
    def cannone(self) -> Rover: #Questa funzione permette di utilizzare la classe cannone
        return self._cannone
    
    def proiettileCannone(self):    #Questa funzione permette al cannone di sparare proiettili infiniti in direzione nord
        proiettilecannone=ProiettiliCannone(self._arena,self._cannone,costanti.valori_ProiettiliCannone)
        proiettilecannone.sparo2()
        
    def hero(self) -> Rover:
        return self._hero

    def game_over(self) -> bool:
        return self._hero.lives() == 0

    def game_won(self) -> bool:
        return time() - self._start > self._playtime

    def remaining_time(self) -> int:
        return int(self._start + self._playtime - time())
