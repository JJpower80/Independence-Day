import pygame
import random
import math
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

#Funcion para obtener la ruta de los recursos
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Load assets
asset_background = resource_path("assets/images/background.png")
background = pygame.image.load(asset_background)

# Load icon window
asset_icon = resource_path("assets/images/ufo.png")
icon = pygame.image.load(asset_icon)
pygame.display.set_icon(icon)

# Load background sound
asset_background_sound = resource_path("assets/audios/background_music.mp3")
background_sound = pygame.mixer.Sound(asset_background_sound)
background_sound.play(-1)

#Cargar imagen del jugador
asset_playerimg = resource_path("assets/images/space-invaders.png")
playerimg = pygame.image.load(asset_playerimg)

#Cargar el disparo
asset_bulletimg = resource_path("assets/images/bullet.png")
bulletimg = pygame.image.load(asset_bulletimg)

#Cargar fuente Game Over
asset_gameoverfont = resource_path("assets/fonts/RAVIE.TTF")
gameoverfont = pygame.font.Font(asset_gameoverfont, 64)

#Cargar fuente Score
asset_scorefont = resource_path("assets/fonts/comicbd.TTF")
scorefont = pygame.font.Font(asset_scorefont, 32)

#Titulo de ventana
pygame.display.set_caption("Independence Day")

#Establecer icono de la ventana
pygame.display.set_icon(icon)

#Reproducir sonido de fondo en loop
pygame.mixer.Sound.play(background_sound, loops=-1) 

#Reloj para controlar los FPS
clock = pygame.time.Clock()

#Posicion inicial del jugador
playerX = 370
playerY = 470
playerX_change = 0
playerY_change = 0

#Posicion inicial del enemigo
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 10

#Variables para guardar la posicion de los enemigos
for i in range(num_of_enemies):
    #Se carga la imagen para los enemigos1
    enemy1 = resource_path("assets/images/enemy1.png")
    enemyimg.append(pygame.image.load(enemy1))

    #Se carga la imagen para los enemigos2
    
    enemy2 = resource_path("assets/images/enemy2.png")
    enemyimg.append(pygame.image.load(enemy2))

    #Se asigna una posicion aleatoria para cada enemigo
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))

    #Se asigna una velocidad de movimiento para cada enemigo
    enemyX_change.append(5)
    enemyY_change.append(20)

#Posicion inicial del disparo
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready" # "ready" - No se ve el disparo, "fire" - El disparo se esta moviendo

#Puntaje inicial
score_value = 0

#Funcion para mostrar el puntaje en pantalla
def show_score(x, y):
    score = scorefont.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

#Funcion para mostrar el jugador en pantalla
def player(x, y):
    screen.blit(playerimg, (x, y))

#Funcion para mostrar el enemigo en pantalla
def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))

#Funcion para disparar la bala
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10)) 

#Funcion para detectar colision entre el disparo y el enemigo
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False       
    
#Funcion mostrar mensaje de Game Over
def game_over_text():
    over_text = gameoverfont.render("GAME OVER", True, (255, 255, 255))
    text_rect = over_text.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(over_text, text_rect)

#Game Loop
def game_loop():
    
    #Declarar las variables globales para poder modificarlas dentro de la funcion
    global playerX, playerY, playerX_change
    global enemyX, enemyY, enemyX_change, enemyY_change
    global bulletX, bulletY, bullet_state
    global score_value

    running = True
    while running:
        #Maneja eventos, actualiza y renderiza el juego
        screen.fill((0, 0, 0)) #Rellena la pantalla
        screen.blit(background, (0, 0)) #Dibuja el fondo    


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #Detecta si se presiona una tecla
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)

            #Detecta si se suelta una tecla
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0  
            
        #Actualiza la posicion del jugador
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736   

        #Actualiza la posicion de los enemigos
        for i in range(num_of_enemies):
            #Game Over
            if enemyY[i] > 440:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 5
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -5
                enemyY[i] += enemyY_change[i]

            #Detecta colision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                print(score_value)
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 150)

            enemy(enemyX[i], enemyY[i], i)

        #Actualiza la posicion del disparo
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        show_score(10, 10)
        player(playerX, playerY)
        pygame.display.update()
        clock.tick(60) #Limita a 60 FPS

    pygame.quit()

if __name__ == "__main__":
    game_loop()
