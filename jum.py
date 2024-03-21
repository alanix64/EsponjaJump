import pygame
import sys
import random

# Iniciamos Pygame
pygame.init()

# Tamaño de ventana
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bumjump")

# Colores
BLACK = (0, 0, 0)

# Cargamos la imagen

jumpscare_image = pygame.image.load("wump2.png")  # spong es el jumpy
boomwup_snd = pygame.mixer.Sound("womp.wav")  #bumgump

# Y el loop
running = True
while running:
    # Lleva control de eventos 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpiamos la pantalla
    screen.fill(BLACK)

    # Y AQUI VA EL JUMPSCARE
    if random.random() < 0.0009:  # Esto es para ajustar/modificar el tiempo de espera 
        jumpscare_rect = jumpscare_image.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(jumpscare_image, jumpscare_rect)
        boomwup_snd.play()

        # Actualizamos la ventana 
        pygame.display.flip()

        # Pausa parcial del jumpscare
        pygame.time.delay(1000)  # La duracion total del jumpscare

    # Se hace un refresh de la ventana
    pygame.display.flip()

# Salimos de Pygame
pygame.quit()
sys.exit()
