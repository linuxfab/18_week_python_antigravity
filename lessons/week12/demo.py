
import pygame
import sys
import colorsys
import random

"""
Week 12: 物件導向 (OOP) - 封裝與抽象
核心概念: 
1. 類別 (Class) 與 物件 (Instance)
2. 初始化 (Constructor) __init__
3. 方法 (Methods) move(), draw()
"""

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 12: The Snake Class")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (15, 15, 20)
TEXT_COLOR = (255, 255, 255)

# --- 類別定義 (Class Definitions) ---
# 這是本週的重點！我們把原本散亂的變數和函數，打包成「物件」。

class Snake:
    def __init__(self):
        """ 初始化蛇的狀態 """
        self.body = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = (0, 0)
        self.should_grow = False
        self.block_size = 40
        self.color = NEON_GREEN
    
    def handle_keys(self, key):
        """ 處理鍵盤輸入 """
        if key == pygame.K_UP and self.direction != (0, self.block_size):
            self.direction = (0, -self.block_size)
        elif key == pygame.K_DOWN and self.direction != (0, -self.block_size):
            self.direction = (0, self.block_size)
        elif key == pygame.K_LEFT and self.direction != (self.block_size, 0):
            self.direction = (-self.block_size, 0)
        elif key == pygame.K_RIGHT and self.direction != (-self.block_size, 0):
            self.direction = (self.block_size, 0)

    def move(self):
        """ 移動邏輯 """
        if self.direction == (0, 0): return # 還沒按鍵，不動
        
        # 取得頭部
        current_head = self.body[-1]
        dx, dy = self.direction
        new_head = (current_head[0] + dx, current_head[1] + dy)
        
        # 邊界傳送 (Pac-Man)
        if new_head[0] >= WINDOW_WIDTH: new_head = (0, new_head[1])
        elif new_head[0] < 0: new_head = (WINDOW_WIDTH - self.block_size, new_head[1])
        if new_head[1] >= WINDOW_HEIGHT: new_head = (new_head[0], 0)
        elif new_head[1] < 0: new_head = (new_head[0], WINDOW_HEIGHT - self.block_size)
        
        self.body.append(new_head)
        
        if self.should_grow:
            self.should_grow = False # 消耗成長機會
        else:
            self.body.pop(0) # 保持長度

    def check_self_collision(self):
        """ 檢查是否咬到自己 """
        head = self.body[-1]
        # 身體包含除了頭以外的所有部分
        body_parts = self.body[:-1] 
        return head in body_parts

    def draw(self, surface):
        """ 繪製自己 """
        for segment in self.body:
            rect = pygame.Rect(segment[0], segment[1], self.block_size, self.block_size)
            pygame.draw.rect(surface, self.color, rect, border_radius=4)

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.block_size = 40
        self.randomize_position()
        
    def randomize_position(self):
        cols = WINDOW_WIDTH // self.block_size
        rows = WINDOW_HEIGHT // self.block_size
        self.position = (
            random.randint(0, cols-1) * self.block_size,
            random.randint(0, rows-1) * self.block_size
        )
        
    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], self.block_size, self.block_size)
        pygame.draw.rect(surface, FOOD_RED, rect, border_radius=10)

# --- 遊戲主流程 ---
# 這些是全域物件 (Instance)
snake = Snake()
food = Food()
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            snake.handle_keys(event.key) # 交給 Snake 類別處理
    
    # 邏輯更新
    snake.move()
    
    # 碰撞檢查 (Head vs Food)
    if snake.body[-1] == food.position:
        snake.should_grow = True
        score += 10
        food.randomize_position()
        
    # 自我碰撞
    if snake.check_self_collision():
        print("Game Over Logic Placeholder") # 下週再優化這裡
        snake = Snake() # 簡單重置
        score = 0

    # 畫面渲染
    screen.fill(BG_COLOR)
    snake.draw(screen)
    food.draw(screen)
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()
