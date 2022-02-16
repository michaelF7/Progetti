import pygame as pg
from random import choice
from os import system

pg.init()

system("cls")

# Misure  Finestra
LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA  = 1200, 800

# Colori 
NERO = (0, 0, 0) # Sfondo
ROSSO = (255, 0, 0) # giocatore 1
BLU = (25,102,255) # giocatore 2
BIANCO = (255, 255, 255) # Palla
GRIGIO = (105, 105, 105) # Divisore 

# Impostazioni
running = True
FPS = 120
velocità_giocatori_y = 5
velocità_palla_x = 4 * choice((1, -1))
velocità_palla_y = 4 * choice((1, -1))
punteggio_rosso = 0
punteggio_blu = 0 
font_base = pg.font.Font(None, 40)

#  Creazione 
finestra = pg.display.set_mode((LARGHEZZA_FINESTRA, ALTEZZA_FINESTRA))
pg.display.set_caption("PONG") # Titolo

# Movimento giocatore 1
def movimento_giocatore_1(tasti_premuti, giocatore_1) -> None:
    
    if tasti_premuti[pg.K_w] and  giocatore_1.y - velocità_giocatori_y > 0: 
        giocatore_1.y -= velocità_giocatori_y # Sopra

    elif tasti_premuti[pg.K_s] and giocatore_1.y + velocità_giocatori_y + giocatore_1.height < ALTEZZA_FINESTRA:  
        giocatore_1.y += velocità_giocatori_y # Sotto
        
# Movimento giocatore 2
def movimento_giocatore_2(tasti_premuti, giocatore_2) -> None:
    
    if tasti_premuti[pg.K_UP] and  giocatore_2.y - velocità_giocatori_y > 0 : 
        giocatore_2.y -= velocità_giocatori_y # Sopra 
    
    elif tasti_premuti[pg.K_DOWN] and giocatore_2.y + velocità_giocatori_y + giocatore_2.height < ALTEZZA_FINESTRA:  
        giocatore_2.y += velocità_giocatori_y # Sotto

# Movimento palla
def movimento_palla(palla) -> None:
    
    global velocità_palla_x, velocità_palla_y
    
    palla.x += velocità_palla_x
    palla.y += velocità_palla_y
    
    if palla.top <= 0 or palla.bottom >= ALTEZZA_FINESTRA:
        velocità_palla_y *= - 1

# Controllo collisioni 
def collisioni(giocatore_1, giocatore_2, palla) -> None:
    
    global velocità_palla_x
    
    if palla.colliderect(giocatore_1) or palla.colliderect(giocatore_2):
        velocità_palla_x *= - 1

# Controllo punteggio      
def punteggio(palla) -> None:
    
    global punteggio_rosso, punteggio_blu
 
    if palla.left <= 0:    
        palla.center = (LARGHEZZA_FINESTRA / 2, ALTEZZA_FINESTRA / 2)
        punteggio_blu += 1
        
    if palla.right >= LARGHEZZA_FINESTRA:     
        palla.center = (LARGHEZZA_FINESTRA / 2, ALTEZZA_FINESTRA / 2)
        punteggio_rosso += 1
        
# Punteggio 
def punteggio_giocatore_1() -> None:
   
    global font_base, punteggio_rosso
    
    testo = font_base.render(str(punteggio_rosso), True, ROSSO)
    testo_rect = testo.get_rect()
    testo_rect.center = (530, 40) # X, Y
    finestra.blit(testo, testo_rect)

def punteggio_giocatore_2() -> None:
    
    global font_base
    
    testo = font_base.render(str(punteggio_blu), True, BLU)
    testo_rect = testo.get_rect()
    testo_rect.center = (670, 40) # X, Y
    finestra.blit(testo, testo_rect)

# Controllo vittoria
def vittoria() -> None:
    
    global punteggio_rosso, punteggio_blu, font_base, running
    
    font = pg.font.Font(None, 100)
    
    if punteggio_rosso == 5:
        testo = font.render(f"HA VINTO IL ROSSO", True, ROSSO)
        testo_rect = testo.get_rect()
        testo_rect.center = (LARGHEZZA_FINESTRA / 2, ALTEZZA_FINESTRA / 2)
        finestra.fill(NERO)
        finestra.blit(testo, testo_rect)
        running = False
        
    elif punteggio_blu == 5:
        testo = font.render(f"HA VINTO IL BLU", True, BLU)
        testo_rect = testo.get_rect()
        testo_rect.center = (LARGHEZZA_FINESTRA / 2, ALTEZZA_FINESTRA / 2)
        finestra.fill(NERO)
        finestra.blit(testo, testo_rect)
        running = False
        
def disegni_finestra(giocatore_1, giocatore_2, divisore, palla) -> None:
    
    finestra.fill(NERO)
   
    pg.draw.rect(finestra, ROSSO, giocatore_1)
    pg.draw.rect(finestra, BLU, giocatore_2)
    pg.draw.rect(finestra, GRIGIO, divisore)                 
    pg.draw.ellipse(finestra, BIANCO, palla)
    
    punteggio_giocatore_1()
    punteggio_giocatore_2()
    vittoria()
    
    pg.display.update()

def main() -> None:
    
    global running
    
    clock = pg.time.Clock()
    
    # Posizioni entità
    giocatore_1 =  pg.Rect(100, 325, 10, 140)  # X, Y, LAR, ALT
    giocatore_2 =  pg.Rect(1100, 325, 10, 140) # X, Y, LAR, ALT
    palla = pg.Rect(490, 325, 20, 20) # X, Y, LAR, ALT
    divisore = pg.Rect(LARGHEZZA_FINESTRA / 2, 0, 5, ALTEZZA_FINESTRA) # X, Y, LAR, ALT

    while running:

        clock.tick(FPS)
        
        for event in pg.event.get():
            
            if event.type is pg.QUIT: 
                
                running = False

        tasti_premuti = pg.key.get_pressed()
        
        disegni_finestra(giocatore_1, giocatore_2,  divisore, palla)
        movimento_palla(palla)
        collisioni(giocatore_1, giocatore_2, palla)
        movimento_giocatore_1(tasti_premuti, giocatore_1)
        movimento_giocatore_2(tasti_premuti, giocatore_2)
        punteggio(palla)
        
    pg.quit()

main()