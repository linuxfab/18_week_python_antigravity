
import pygame
import sys
import colorsys
import random
import math

"""
Week 18: 最終樂章 (The Masterpiece) - 集大成之作
核心概念: 
1. 專案結構 (Project Structure): 乾淨的 Main Loop
2. 完整功能: Snake, Food, PowerUps, Score, Sounds, Game Over
3. Vibe Coding: 極致的視覺效果 (Particles?)
"""

pygame.init()
pygame.mixer.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 18: The Ultimate Snake")
clock = pygame.time.Clock()

# --- Config & Assets ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (10, 10, 15)
TEXT_COLOR = (255, 255, 255)
MAX_FPS = 60

font_large = pygame.font.Font(None, 80)
font_small = pygame.font.Font(None, 36)

# --- Classes ---
class Snake:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.body = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = (0, 0) # 預設不動
        self.block_size = 20
        self.should_grow = False
        self.score = 0
        self.alive = True

    def handle_input(self, key):
        if not self.alive: return
        
        if key == pygame.K_UP and self.direction != (0, self.block_size):
            self.direction = (0, -self.block_size)
        elif key == pygame.K_DOWN and self.direction != (0, -self.block_size):
            self.direction = (0, self.block_size)
        elif key == pygame.K_LEFT and self.direction != (self.block_size, 0):
            self.direction = (-self.block_size, 0)
        elif key == pygame.K_RIGHT and self.direction != (-self.block_size, 0):
            self.direction = (self.block_size, 0)

    def update(self):
        if not self.alive or self.direction == (0, 0): return

        head = self.body[-1]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        
        # 邊界傳送
        nx, ny = new_head
        if nx >= WINDOW_WIDTH: nx = 0
        elif nx < 0: nx = WINDOW_WIDTH - self.block_size
        if ny >= WINDOW_HEIGHT: ny = 0
        elif ny < 0: ny = WINDOW_HEIGHT - self.block_size
        new_head = (nx, ny)

        # 自我碰撞
        if new_head in self.body[:-1]: # 排除剛加入的頭(尚未加入)
            self.alive = False
            return
            
        self.body.append(new_head)
        if self.should_grow:
            self.should_grow = False
        else:
            self.body.pop(0)

    def draw(self, surface):
        for i, segment in enumerate(self.body):
            # Vibe: Rainbow Body
            hue = (i / len(self.body)) * 0.8
            r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
            color = (int(r*255), int(g*255), int(b*255))
            
            # Head has eyes
            if i == len(self.body) - 1:
                pygame.draw.rect(surface, (255, 255, 255), (segment[0], segment[1], self.block_size, self.block_size), border_radius=4)
            else:
                rect = pygame.Rect(segment[0]+1, segment[1]+1, self.block_size-2, self.block_size-2)
                pygame.draw.rect(surface, color, rect, border_radius=4)

class Food:
    def __init__(self):
        self.block_size = 20
        self.respawn()
        
    def respawn(self):
        cols = WINDOW_WIDTH // self.block_size
        rows = WINDOW_HEIGHT // self.block_size
        self.pos = (random.randint(0, cols-1)*self.block_size, random.randint(0, rows-1)*self.block_size)
        self.color = (random.randint(50, 255), random.randint(50, 255), 255)
        
    def draw(self, surface):
        # Pulsing effect
        pulse = abs(math.sin(pygame.time.get_ticks() * 0.005)) * 5
        center = (self.pos[0] + self.block_size//2, self.pos[1] + self.block_size//2)
        pygame.draw.circle(surface, self.color, center, (self.block_size//2) + pulse)

# --- Global Logic ---
snake = Snake()
food = Food()

running = True
state = "MENU" # MENU, PLAY, GAMEOVER

while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if state == "MENU":
                if event.key == pygame.K_SPACE:
                    state = "PLAY"
                    snake.reset()
            elif state == "PLAY":
                snake.handle_input(event.key)
            elif state == "GAMEOVER":
                if event.key == pygame.K_SPACE:
                    state = "PLAY"
                    snake.reset()

    # 2. Update
    if state == "PLAY":
        snake.update()
        if not snake.alive:
            state = "GAMEOVER"
        
        # Collision Food
        if snake.body[-1] == food.pos:
            snake.should_grow = True
            snake.score += 10
            food.respawn()

    # 3. Draw
    screen.fill(BG_COLOR)
    
    if state == "MENU":
        title = font_large.render("SNAKE 2077", True, NEON_GREEN)
        sub = font_small.render("Press SPACE to Start", True, TEXT_COLOR)
        screen.blit(title, (WINDOW_WIDTH//2 - title.get_width()//2, 200))
        screen.blit(sub, (WINDOW_WIDTH//2 - sub.get_width()//2, 300))
        
    elif state == "PLAY":
        snake.draw(screen)
        food.draw(screen)
        # UI
        score_text = font_small.render(f"Score: {snake.score}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))
        
    elif state == "GAMEOVER":
        go_text = font_large.render("GAME OVER", True, (255, 50, 50))
        score_text = font_small.render(f"Final Score: {snake.score}", True, TEXT_COLOR)
        retry_text = font_small.render("Press SPACE to Retry", True, (200, 200, 200))
        
        screen.blit(go_text, (WINDOW_WIDTH//2 - go_text.get_width()//2, 150))
        screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, 250))
        screen.blit(retry_text, (WINDOW_WIDTH//2 - retry_text.get_width()//2, 350))

    pygame.display.flip()
    clock.tick(MAX_FPS) # Fixed 60 FPS for smoothness

pygame.quit()
sys.exit()
