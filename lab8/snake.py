import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
WHITE, GREEN, RED = (255, 255, 255), (0, 255, 0), (255, 0, 0)

# Create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font_small = pygame.font.SysFont("Verdana", 20)    
score = 0
level = 1

# Initial snake parameters
snake = [(100, 100)]
SPEED = 10  # Controls FPS, not movement step
direction = (CELL_SIZE, 0)

# Generate food at a random position
food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
        random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)
    
    # Update snake position
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    
    if new_head in snake or not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        running = False  # Game over
    else:
        snake.insert(0, new_head)
        
        if new_head == food:
            score += 1
            food = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                    random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

            # level up every 3 points 
            if score % 3 == 0:
                level += 1
                SPEED += 2  

        else:
            snake.pop()
    
    # Draw snake and food
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (*food, CELL_SIZE, CELL_SIZE))

    # Display score and level
    screen.blit(font_small.render(f"Points: {score}", True, (0,0,0)), (10, 10))
    screen.blit(font_small.render(f"Level: {level}", True, (0,0,0)), (10, 30))

    pygame.display.flip()
    clock.tick(SPEED)  # Controls game speed properly

pygame.quit()
