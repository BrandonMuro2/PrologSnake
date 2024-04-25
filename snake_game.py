import pygame
import sys
import random
from pyswip import Prolog

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Inicializar Prolog
prolog = Prolog()
prolog.consult("snake.pl")

# Tamaño de cada bloque de la serpiente
block_size = 10

# Función para obtener la dirección de Prolog
def format_for_prolog(list_of_positions):
    return "[" + ", ".join(f"pos({pos[0]}, {pos[1]})" for pos in list_of_positions) + "]"

def get_direction(snake, fruit):
    snake_prolog = format_for_prolog(snake)
    fruit_prolog = f"pos({fruit[0]}, {fruit[1]})"
    query = f"move({snake_prolog}, {fruit_prolog}, Direction)"
    result = list(prolog.query(query))
    return result[0]['Direction'] if result else 'right'  # Default direction if query fails

# Mover la serpiente según la dirección
def move_snake(snake, direction):
    head = snake[0].copy()
    if direction == 'left':
        head[0] -= block_size
    elif direction == 'right':
        head[0] += block_size
    elif direction == 'up':
        head[1] -= block_size
    elif direction == 'down':
        head[1] += block_size

    # Inserta la nueva cabeza al principio de la lista de la serpiente
    snake.insert(0, head)

    # Verifica si la serpiente ha comido la fruta
    if head == fruit:
        return True  # La serpiente crece, no eliminamos la cola
    else:
        # Si no ha comido, elimina el último segmento
        snake.pop()
        return False

# Verificar colisiones con los bordes o consigo misma
def check_collisions(snake):
    head = snake[0]
    # Verifica colisión con los bordes
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
        return True
    # Verifica colisión con su propio cuerpo
    if head in snake[1:]:
        return True
    return False

# Variables del juego
snake = [[200, 200], [190, 200], [180, 200]]
fruit = [random.randint(0, (width - block_size) // block_size) * block_size,
         random.randint(0, (height - block_size) // block_size) * block_size]
direction = 'RIGHT'

# Bucle del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Actualizar la dirección desde Prolog
    direction = get_direction(snake, fruit)

    # Mover la serpiente
    if move_snake(snake, direction):
        # Si la serpiente ha comido la fruta, genera una nueva
        fruit = [random.randint(0, (width - block_size) // block_size) * block_size,
                 random.randint(0, (height - block_size) // block_size) * block_size]

    # Verificar colisiones
    if check_collisions(snake):
        print("Game Over!")
        running = False

    # Dibujar todo
    screen.fill((0, 0, 0))
    for pos in snake:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], block_size, block_size))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fruit[0], fruit[1], block_size, block_size))

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
sys.exit()
