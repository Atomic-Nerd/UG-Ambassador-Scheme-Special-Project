import pygame

# --- CONFIG ---
TILE_SIZE = 32        # size of each tile in pixels
FPS = 60

# Colors
BLACK = (0, 0, 0)      # wall
WHITE = (255, 255, 255) # empty space
BLUE = (0, 0, 255)      # player
GREEN = (0, 255, 0)     # finish

# --- LOAD MAZE ---
with open("maze.txt", "r", encoding="utf-8") as f:
    maze = [line.rstrip("\n") for line in f]

ROWS = len(maze)
COLS = len(maze[0])

# --- INIT PYGAME ---
pygame.init()
screen = pygame.display.set_mode((COLS * TILE_SIZE, ROWS * TILE_SIZE))
pygame.display.set_caption("Maze - Grid Movement")
clock = pygame.time.Clock()

# --- PLAYER START ---
player_pos = None
for r, row in enumerate(maze):
    for c, cell in enumerate(row):
        if cell == "X":
            player_pos = [c, r]

if player_pos is None:
    raise ValueError("Maze must have a start 'X'!")

# --- MAIN LOOP ---
running = True
while running:
    clock.tick(FPS)

    # --- EVENT HANDLING ---
    dx, dy = 0, 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # only on key press, not hold
            if event.key == pygame.K_LEFT:
                dx = -1
            elif event.key == pygame.K_RIGHT:
                dx = 1
            elif event.key == pygame.K_UP:
                dy = -1
            elif event.key == pygame.K_DOWN:
                dy = 1

            # --- COLLISION CHECK ---
            new_x = player_pos[0] + dx
            new_y = player_pos[1] + dy
            if 0 <= new_x < COLS and 0 <= new_y < ROWS:
                if maze[new_y][new_x] != "█":
                    player_pos = [new_x, new_y]

    # --- DRAW ---
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            rect = pygame.Rect(c * TILE_SIZE, r * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if cell == "█":
                pygame.draw.rect(screen, BLACK, rect)
            elif cell == "F":
                pygame.draw.rect(screen, GREEN, rect)
            else:
                pygame.draw.rect(screen, WHITE, rect)

    # Draw player
    player_rect = pygame.Rect(player_pos[0] * TILE_SIZE, player_pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, BLUE, player_rect)

    pygame.display.flip()

pygame.quit()
