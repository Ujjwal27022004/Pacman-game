import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL_SIZE = 40
BACKGROUND_COLOR = (0, 0, 0)
WALL_COLOR = (0, 0, 255)
DOT_COLOR = (255, 255, 255)
PACMAN_COLOR = (255, 255, 0)
PACMAN_RADIUS = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pac-Man')

map_data = [
    "####################",
    "#..................#",
    "#.###.###..###.###.#",
    "#.#...#......#...#.#",
    "#.#.###.####.###.#.#",
    "#.#.#..........#.#.#",
    "#.....####.####.....",
    "#.#.#..........#.#.#",
    "#.#.###.####.###.#.#",
    "#.#...#......#...#.#",
    "#.###.###..###.###.#",
    "#..................#",
    "####################",
]

walls = []
dots = []
for y, row in enumerate(map_data):
    for x, cell in enumerate(row):
        if cell == "#":
            walls.append((x, y))
        elif cell == ".":
            dots.append((x, y))

pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_direction = 0  

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pacman_direction = 0
    elif keys[pygame.K_UP]:
        pacman_direction = 1
    elif keys[pygame.K_LEFT]:
        pacman_direction = 2
    elif keys[pygame.K_DOWN]:
        pacman_direction = 3

  
    pacman_speed = 5
    if pacman_direction == 0:
        pacman_x += pacman_speed
    elif pacman_direction == 1:
        pacman_y -= pacman_speed
    elif pacman_direction == 2:
        pacman_x -= pacman_speed
    elif pacman_direction == 3:
        pacman_y += pacman_speed

    
    pacman_rect = pygame.Rect(pacman_x - PACMAN_RADIUS, pacman_y - PACMAN_RADIUS, PACMAN_RADIUS * 2, PACMAN_RADIUS * 2)
    for wall in walls:
        wall_rect = pygame.Rect(wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if pacman_rect.colliderect(wall_rect):
            if pacman_direction == 0:
                pacman_x = wall[0] * CELL_SIZE - PACMAN_RADIUS
            elif pacman_direction == 1:
                pacman_y = wall[1] * CELL_SIZE + CELL_SIZE + PACMAN_RADIUS
            elif pacman_direction == 2:
                pacman_x = wall[0] * CELL_SIZE + CELL_SIZE + PACMAN_RADIUS
            elif pacman_direction == 3:
                pacman_y = wall[1] * CELL_SIZE - PACMAN_RADIUS

    eaten_dots = []
    for dot in dots:
        dot_rect = pygame.Rect(dot[0] * CELL_SIZE, dot[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if pacman_rect.colliderect(dot_rect):
            eaten_dots.append(dot)
            score += 10
    for dot in eaten_dots:
        dots.remove(dot)

  
    screen.fill(BACKGROUND_COLOR)

   
    for wall in walls:
        pygame.draw.rect(screen, WALL_COLOR, (wall[0] * CELL_SIZE, wall[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

   
    for dot in dots:
        pygame.draw.circle(screen, DOT_COLOR, (dot[0] * CELL_SIZE + CELL_SIZE // 2, dot[1] * CELL_SIZE + CELL_SIZE // 2), 5)

    pygame.draw.circle(screen, PACMAN_COLOR, (pacman_x, pacman_y), PACMAN_RADIUS)
    
    
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
  
    pygame.display.flip()


    pygame.time.Clock().tick(30)
