import pygame
import random
import time


# game constants
WIDTH = 800
HEIGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
w = 5
y = 0


# 10110010 = 256
# which is the total no of rules

# choose rule number
RULE = 109


binary_string = bin(RULE)[2:].zfill(8)
ruleSet = [int(bit) for bit in binary_string]

def calcState(a, b, c):
    binary = str(a) + str(b) + str(c)
    val = 7 - int(binary, 2)
    return ruleSet[val]



cells = []
n_cells = WIDTH // w
for i in range(n_cells):
    # cells.append(random.randint(0, 1))
    cells.append(0)
cells[n_cells // 2] = 1


# Initialize Pygame
pygame.init()

# Set up the display
pygame.display.set_caption('Cellular Automata')
pygame.display.set_icon(pygame.image.load('./assets/icon.png'))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # intial generation
    for i in range(n_cells):
        x = i*w;
        fill_color = BLACK if cells[i] == 1 else WHITE 
        pygame.draw.rect(screen, fill_color, (x, y, w, w)) #actual 
        # pygame.draw.rect(screen, BLACK, (x, y, w, w), 1) #border


    # next row for the next iteration
    y += w

    # next generation
    newCells = [0]*n_cells
    newCells.append(cells[0])
    newCells[n_cells - 1] = cells[n_cells - 1]

    for i in range(1, n_cells-1):
        left_state = cells[i-1]
        right_state = cells[i+1]
        curr_state = cells[i]

        newState = calcState(left_state, curr_state, right_state)
        newCells[i] = newState


    cells = newCells

    # Update the display
    pygame.display.flip()
    time.sleep(0.05)

# Quit Pygame
pygame.quit()
