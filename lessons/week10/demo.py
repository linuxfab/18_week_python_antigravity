
import pygame
import sys
import colorsys
import random

"""
Week 10: 分數顯示 (Score & UI) - 讓成就感可見
核心概念: 
1. Pygame Font 渲染: SysFont
2. UI 疊加 (Overlay): 將文字畫在遊戲層之上
3. 計分邏輯: 分數變數與顯示
"""

# --- 1. 初始設定 ---
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 10: The Score")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (15, 15, 20)
TEXT_COLOR = (255, 255, 255)

# --- 變數定義 ---
block_size = 40
snake_body = [(400, 300)]
head_x, head_y = 400, 300
speed_x, speed_y = 0, 0
should_grow = False 
food_x, food_y = 0, 0

# 分數系統 (Score System)
score = 0
high_score = 0 # 最高分紀錄 (本週暫時不儲存到硬碟)

# 字型初始化
# 'Arial' 是字體名稱，36 是大小
try:
    font = pygame.font.SysFont("Arial", 36, bold=True)
except:
    font = pygame.font.Font(None, 36) # 備援字體

# --- 函數定義 ---
def spawn_food():
    global food_x, food_y
    cols = WINDOW_WIDTH // block_size
    rows = WINDOW_HEIGHT // block_size
    while True:
        food_x = random.randint(0, cols - 1) * block_size
        food_y = random.randint(0, rows - 1) * block_size
        if (food_x, food_y) not in snake_body:
            break

def draw_score():
    """
    繪製分數到畫面上
    """
    # 渲染文字成圖片 (Render Text into Surface)
    # 參數: (文字內容, 是否反鋸齒, 顏色)
    score_surf = font.render(f"Score: {score}", True, TEXT_COLOR)
    
    # 畫在左上角 (10, 10)
    screen.blit(score_surf, (10, 10))

    # 如果有最高分，畫在右上角
    if score > high_score:
        pass # 先不複雜化，只要畫分數就好

spawn_food()

# --- 2. 遊戲主迴圈 ---
running = True

while running:
    # --- A. 事件處理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and speed_y == 0: speed_x, speed_y = 0, -block_size 
            elif event.key == pygame.K_DOWN and speed_y == 0: speed_x, speed_y = 0, block_size
            elif event.key == pygame.K_LEFT and speed_x == 0: speed_x, speed_y = -block_size, 0
            elif event.key == pygame.K_RIGHT and speed_x == 0: speed_x, speed_y = block_size, 0

    # --- B. 更新狀態 (Logic) ---
    head_x += speed_x
    head_y += speed_y
    
    if head_x >= WINDOW_WIDTH: head_x = 0
    elif head_x < 0: head_x = WINDOW_WIDTH - block_size
    if head_y >= WINDOW_HEIGHT: head_y = 0
    elif head_y < 0: head_y = WINDOW_HEIGHT - block_size
    
    # 碰撞檢測
    if head_x == food_x and head_y == food_y:
        should_grow = True 
        score += 10 # 吃到食物加 10 分
        print(f"得分！目前分數: {score}")
        spawn_food()       
    
    snake_body.append((head_x, head_y))
    
    if should_grow:
        should_grow = False 
    else:
        snake_body.pop(0) 

    # --- C. 畫面渲染 ---
    screen.fill((10, 10, 15))
        
    pygame.draw.rect(screen, FOOD_RED, (food_x, food_y, block_size, block_size), border_radius=10)
    
    for i, segment in enumerate(snake_body):
        # 簡單漸層
        color_val = max(50, 255 - i * 5)
        color = (50, color_val, 50 + i * 2)
        pygame.draw.rect(screen, color, (segment[0], segment[1], block_size, block_size), border_radius=4)
        
    # [本週核心] 繪製分數
    draw_score()
        
    pygame.display.flip()
    clock.tick(10) 

pygame.quit()
sys.exit()
