from moonpatrolgame import moonpatrolgame
import g2d
from time import time
from random import randint
import costanti

class moonpatrolGui:
    
    def __init__(self):
        
        self._game = moonpatrolgame()
        g2d.init_canvas(self._game.arena().size())
        self._sprites = g2d.load_image("moon-patrol.png")
        self._spritessfondi = g2d.load_image("moon-patrol-bg.png")
        self._Pause= g2d.load_image("pausa.png")
        g2d.main_loop(self.tick)
        
    def handle_keyboard(self):
        
        hero = self._game.hero()
        x2,y2,dx,dy=hero.position1()
        
        if y2>=295 and y2<=300 : 
            if g2d.key_pressed("Spacebar"):
                hero.go_up3()
                
        if g2d.key_pressed("ArrowRight"):
            hero.go_right()
            
        if g2d.key_pressed("ArrowLeft"):
            hero.go_left()
            
        if g2d.key_pressed("a"):
            self._game.cannone().go_left()
            
        if g2d.key_pressed("d"):
            self._game.cannone().go_right()
            
        if g2d.key_pressed("w"):    
            self._game.proiettileCannone()
            
        if g2d.key_pressed("ArrowUp"):  
            self._game.proiettileRoverDritti()
            self._game.proiettileRoverAlto()
            
        if g2d.key_pressed("Enter"): #Premere enter per mettere il gioco in pausa
            costanti.stato=2
            costanti.arresta=True
        
        if g2d.key_pressed("LeftButton"): #Premere il tasto sinistro del mouse per avviare la partita
            costanti.stato=1
            costanti.arresta=False
            
    def tick(self):
        
            hero = self._game.hero()
            cannone = self._game.cannone()
            proiettilialieno1 = self._game.proiettili_alieno1()
            proiettilialieno2 = self._game.proiettili_alieno2()
            self.handle_keyboard()
            arena = self._game.arena()
            
            if not costanti.arresta:
                costanti.tempo=costanti.start + costanti.playtime - time()
                
            if costanti.stato==0: #Questa porzione di codice permette distampare a schermo le regole del gioco prima dell'inizio della partita quando lo stato del gioco è uguale a 0
                    for b in arena.actorsSfondi(): 
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position())
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position2())
                        
                    
                    for a in arena.actors(): 
                        g2d.draw_image_clip(self._sprites, a.symbol(), a.position())
                        g2d.set_color((255,255,255))
                        g2d.draw_text_centered("Get over a score of 4000 points ",(250,130),20)
                        g2d.draw_text_centered("or survive for two minutes to win.",(250,150),20)
                        g2d.draw_text_centered("TO JUMP press button SPACEBAR",(250,190),20)
                        g2d.draw_text_centered("TO GO RIGHT press button ARROW_RIGHT",(250,220),20)
                        g2d.draw_text_centered("TO GO LEFT press button ARROW_LEFT",(250,250),20)
                        g2d.draw_text_centered("TO SHOOT press button ENTER",(250,280),20)
                        g2d.draw_image_clip(self._sprites, (67,5,152,87), (170,15,158,91))
                                
            if costanti.stato==2: #Questa porzione di codice permette di mettere il gioco in pausa mostrandolo anche a schermo quando lo stato del gioco è uguale a 2
                for b in arena.actorsSfondi(): 
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position())
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position2())
                        
                for a in arena.actors(): 
                       g2d.draw_image_clip(self._sprites, a.symbol(), a.position())
                       g2d.set_color((255,255,255))
                       g2d.draw_text_centered("GAME IN PAUSE ",(250,100),20)
                       g2d.draw_text_centered(costanti.punteggio,(470,80),20)
                       g2d.draw_text(" " + costanti.toplay, (400, 40),20 )
                       g2d.draw_text_centered("RECORD",(30,50),10)         
                       g2d.draw_text_centered(costanti.punteggio_Classifica2,(30,70),20)
                g2d.draw_image(self._Pause, (200,150))
                g2d.draw_text_centered("press left button to restart",(250,120),20)
                
            if costanti.stato==3: #Questa porzione di codice permette di mettere il gioco in pausa mostrandolo anche a schermo quando lo stato del gioco è uguale a 2
                for b in arena.actorsSfondi(): 
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position())
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position2())
                        
                for a in arena.actors(): 
                        g2d.draw_image_clip(self._sprites, a.symbol(), a.position())
                        g2d.set_color((255,255,255))
                        g2d.draw_text_centered("CONGRATULATIONS! YOU HAVE GOT A BONUS! ",(250,150),20)
                        g2d.draw_text_centered(costanti.punteggio,(470,80),20)
                        g2d.draw_text(" " + costanti.toplay, (400, 40),20 )
                        g2d.draw_text_centered("RECORD",(30,50),10)         
                        g2d.draw_text_centered(costanti.punteggio_Classifica2,(30,70),20)
                        g2d.draw_text_centered("TO GO RIGHT press button D",(250,190),20)
                        g2d.draw_text_centered("TO GO LEFT press button A",(250,210),20)
                        g2d.draw_text_centered("TO SHOOT press button W",(250,230),20)
                        g2d.draw_text_centered("Press left button to restart",(250,270),20)
                        g2d.draw_image_clip(self._sprites, (67,5,152,87), (170,15,158,91))

                
            if costanti.stato==1: #Questa porzione di codice permette di giocare quando lo stato del gioco è uguale a 1   
                    arena.move_all()      
                    arena.move_allSfondi()
                    #Le variabili scontro sono variabili booleane che permettono di bloccare il gioco nel caso in cui ci sia stata una collisione tra il rover e un altro oggetto
                    scontro=hero.restituzioneBoolena()
                    scontro2=proiettilialieno1.restituzioneBoolena()
                    scontro3=proiettilialieno2.restituzioneBoolena()
                    g2d.clear_canvas()
                    
                    for b in arena.actorsSfondi(): 
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position())
                        g2d.draw_image_clip(self._spritessfondi, b.symbol(), b.position2())
                        if scontro or scontro2 or scontro3 :
                            b.stay()

                    #Il metodo stay è implementato sia nella lista degli sfondi sia nella lista degli attori, e permette di bloccare tutto il gioco
                            
                    for a in arena.actors(): 
                        g2d.draw_image_clip(self._sprites, a.symbol(), a.position())
                        if scontro or scontro2 or scontro3 :
                            a.stay()
                            costanti.arresta=True
                            
############################################################################################################

                    #CODICE SPAWN BUCHE
                            
                    costanti.numero_Randomico=randint(0,500)
                    costanti.numero_Randomico2=randint(0,500)

                    #Questa porzione di codice permette di creare buche (possibilmente distanziate) utilizzando un numero random
                    
                    if costanti.numero_Randomico==5:
                        costanti.xRandom1=randint(200,1000)+costanti.costante1
                        self._game.buche1()
                        costanti.numero_Randomico=randint(0,500)

                    if costanti.numero_Randomico2==100 :
                        costanti.xRandom2=randint(1000,2000)+costanti.xRandom1+costanti.costante1
                        self._game.buche2()
                        costanti.numero_Randomico2=randint(0,500)
                        
#############################################################################################################       

                    #CODICE PROIETTILE ALIENI
                        
                    #Questa porzione di codice permette di far sparare agli alieni soltanto un proiettile per volta.
                    #Lo sparo dei proiettili è gestito da delle variabili booleane che vengono inizializzate:
                    #True nel momento in cui viene sparato il proiettile per poi diventare False nel momento in cui il proiettile supera una certa quota y

                    if costanti.count5==0:
                        costanti.numeroRandomico_Alieni=randint(0,10)
                        
                    if costanti.numeroRandomico_Alieni==7 :
                            costanti.count5=costanti.count5-1
                            costanti.booleano=True
                            proiettilialieno1.sparo()
                            costanti.numeroRandomico_Alieni=randint(0,10)
                            
                    if costanti.booleano and costanti.numeroRandomico_Alieni==6 :
                        xAlieno,yAlieno=proiettilialieno1.position4()
                        if yAlieno>=310 :
                            self._game.bucheAlieno(xAlieno)
                            costanti.count5=costanti.count5+1
                            costanti.booleano=False
                    
                    if costanti.booleano and costanti.numeroRandomico_Alieni!=6  :
                        xAlieno,yAlieno=proiettilialieno1.position4()
                        if yAlieno>=costanti.max_Proiettili :
                            costanti.booleano=False
                            costanti.count5=costanti.count5+1

                    #Viene utilizzata la funzione costanti.count5<=-2 affinchè l'alieno possa continuare a sparare proiettili anche nel momento in cui viene eliminato. In seguito l'alieno tornerà a giocare. 
                            
                    if costanti.count5<=-2 : 
                        costanti.count5+=1

                    if costanti.count2==0:
                        costanti.numeroRandomico_Alieni2=randint(0,10)
                        
                    if costanti.numeroRandomico_Alieni2==7 :
                        costanti.count2=costanti.count2-1
                        costanti.booleano2=True
                        proiettilialieno2.sparo()
                        costanti.numeroRandomico_Alieni2=randint(0,10)
                            
                    if costanti.booleano2 and costanti.numeroRandomico_Alieni2==6 :
                        xAlieno2,yAlieno2=proiettilialieno2.position4()
                        if yAlieno2>=310 :
                            self._game.bucheAlieno(xAlieno2)
                            costanti.count2=costanti.count2+1
                            costanti.booleano2=False
                    
                    if costanti.booleano2 and costanti.numeroRandomico_Alieni2!=6  :
                        xAlieno2,yAlieno2=proiettilialieno2.position4()
                        if yAlieno2>=310 :
                            costanti.booleano2=False
                            costanti.count2=costanti.count2+1
                            
                    if costanti.count2<=-2 :
                        costanti.count2+=1
                    
#############################################################################################################

                    #SCRITTURA PUNTEGGIO E RECORD


                    with open ("record.txt", "r") as f1:
                             record = f1.read()
                             costanti.punteggio_Classifica2= int(record)
                             
                    g2d.set_color((255,255,255))
                    g2d.draw_text_centered("RECORD",(30,50),10)         
                    g2d.draw_text_centered(costanti.punteggio_Classifica2,(30,70),20)

                    #Nel caso in cui il rover non si sia scontrato con nessun altro oggetto viene incrementato il punteggio e decrementato il tempo 
                    
                    if not costanti.arresta:

                        #Il punteggio è dato non solo dal numero di secondi di esecuzione del tick
                        #ma anche da un punteggio aggiuntivo ottenuto a seguito della distruzione di una roccia o di un alieno
                        
                        costanti.punteggio=costanti.punteggio+arena.punteggioGui()
                        g2d.draw_text_centered(costanti.punteggio,(480,70),20)
                        costanti.punteggio+=1

                        #Il punteggio ottenuto dalla distruzione di un alieno o di una roccia viene riportato a 0 ogni volta
                        
                        arena.modificapunteggio()

                    if not costanti.arresta :
                        costanti.toplay = "Time: " + str(self._game.remaining_time())
                        g2d.draw_text(" " + costanti.toplay, (400, 40),20 )

                    #Nel caso in cui il rover si sia scontrato con un altro oggetto oppure il giocatore abbia vinto viene stampato il punteggio e il tempo rimanente 
                        
                    if costanti.arresta or costanti.vittoria:
                        g2d.draw_text_centered(costanti.punteggio,(470,70),20)
                        g2d.draw_text(" " + costanti.toplay, (400, 40),20 )
                 
#############################################################################################################

                    #SCRITTURA PUNTEGGIO E RECORD

                        with open ("record.txt", "r") as f1:
                             record = f1.read()
                             costanti.punteggio_Classifica= int(record)

                    #Nel caso in cui il giocatore abbia totalizzato un punteggio maggiore di quelli ottenuti precedentemente il record viene sovrascritto
   
                    if costanti.punteggio_Classifica!=0:
                         if costanti.punteggio>=costanti.punteggio_Classifica:
                            g2d.set_color((255,255,255))
                            g2d.draw_text_centered("New record!" ,(250,150),50)
                            with open ("record.txt", "w") as f2:
                                print(costanti.punteggio,file=f2)
                                
#############################################################################################################
                                
                    #CONTROLLO VITTORIA

                    if costanti.punteggio>=10000 or self._game.game_won():
                        g2d.draw_text_centered("Game won" ,(250,150),50)
                        g2d.alert("Game won")
                        g2d.close_canvas()

                    #Il giocatore dopo un certo punteggio dispone di un bonus        
                           
                    if costanti.punteggio>=1000 and costanti.cont==0:
                        cannone.modifica()
                        costanti.cont+=1
                        costanti.stato=3
                        
gui=moonpatrolGui()
