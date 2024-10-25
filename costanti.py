from time import time
from random import randint
import g2d

#############################################

#COSTANTI ROVER

dx_Rover,dy_Rover=0,2
speed_Rover=2
w_Rover,h_Rover=40,30
immagine_RoverCanvas=295
immagine_Rover=35
gravita=0.06
immagine_Roccia=25
rover_Scontrato=170, 288,40,30
rover_salta=247, 159, 40,30

#############################################

#COSTANTI BUCHE

yBuche=311
bucaPiccola_symbol=15,30,130,166
bucaGrande_symbol=15,32,158,166
dxdy_Buca=3,0

#############################################

#COSTANTI ROCCE

yRoccia=305
rocciapiccola_Symbol=15,17,95,200
rocciaGrande_Symbol=15,17,111,197
dxdy_Roccia=3,0
punteggio_Roccia=100
collisione_buche=200

#############################################

#COSTANTI PROIETTILI

range_proiettile=200
allineamento_proiettilex=20
allineamento_proiettiley=5

#############################################

#COSTANTI ALIENO 1

alieno_symbol=121,228,20, 20
dxdy_Alieno=5, 5
rangemovimento_alieno=20,490
allineamento_alienox=-1000
allineamento_alienoy=30
punteggio_Alieno=200

#############################################

#COSTANTI PROIETTILI ALIENO 1

#randomproiettili_buca=4
immagine_Roverx=40
immagine_Rovery=15

#############################################

#COSTANTI ALIENO 2

alieno_symbol2=86,224,20, 20
dxdy_Alieno2=5, 5
rangemovimento_alieno2=20,490
allineamento_alienox2=-1000
allineamento_alienoy2=30
punteggio_Alieno2=200

#############################################

#COSTANTI PROIETTILI ALIENO 2

#randomproiettilibuca2=4
immagine_Roverx2=40
immagine_Rovery2=15

#############################################

#COSTANTI CANNONE

velocita_cannone=3
allineamento_CannoneX=60
allineamento_CannoneY=300

#############################################

#COSTANTI PROIETTILI CANNONE

velocita_cannone=3
allineamentoproiettili_CannoneY=5
punteggioProiettili_Cannone=200

#############################################

#COSTANTI GLOBALI

nullo=0

#############################################

#COSTANTI PRESENTI NEL FILE GUI

cont=0
punteggio=0
vittoria=False
arresta=False
numeroRandomico_Alieni=0
numeroRandomico_Alieni2=0
xRandom_Alieni=randint(0,500)
punteggio_Classifica=0
costante1=100
toplay=0
tempo=130
booleano=True
booleano2=True
playtime = 130
count5=0
booleano=True
booleano2=True
count2= 0
punteggio_Classifica=0
start = time()
playtime = 130
numero_Randomico=0
numero_Randomico2=0
xRandom1=0
xRandom2=0
max_Proiettili=310
stato=0
punteggio_Classifica2=0

#############################################

#COSTANTI PRESENTI NEL FILE BOARDGAME

xRandom5=randint(200,1000)
xRandom6=randint(1000,2000)+xRandom5+costante1
xRandom7=randint(200,1000)
xRandom8=randint(1500,2000)+xRandom7

#############################################

#COSTANTI ARENA

arenaCanvas=500, 330
ARENA_W, ARENA_H = 500, 330

#############################################

#OGGETTI PRESENTI NEL FILE BOARDGAME

rover_Valori=40,ARENA_H-35
valori_Roccia1=xRandom5,305
valori_Roccia2=xRandom6,305
valori_Alieno1= randint(-3000,300), 30
valori_Alieno2= randint(-1000,300), 30
valori_ProiettiliAlieno1=196,230,13,20,0,5
valori_ProiettiliAlieno2=196,230,13,20,0,5
valori_Cannone=100,ARENA_H+100,109,244,20,20
valori_Sfondo1= 0,0,1,50,500,175,1
valori_Sfondo1_1=500,0,1,50,500,175,1
valori_Sfondo2=0,130,1,256,500,125,2
valori_Sfondo2_1=500,130,1,256,500,125,2
valori_Sfondo3=0,190,1,387,500,125,2
valori_Sfondo3_1=500,190,1,387,500,125,2
valori_Sfondo4=0,310,1,512,500,40,3
valori_Sfondo4_1=500,310,1,512,500,40,2
valori_ProiettiliDritti=238,139,13,20,5,0
valori_ProiettiliAlto=238,139,13,20,0,-5
valori_ProiettiliCannone=196,230,13,20,0,-5
