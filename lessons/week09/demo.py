
import pygame
import sys
import colorsys
import random

"""
Week 09: 碰撞檢測 (Collision Detection) - 真正吃到食物！
核心概念: 
1. 座標重疊: if head == food
2. 吃掉邏輯: 食物消失 + 身體變長
3. Vibe Coding: 吃掉的瞬間特效 (Pulse Effect)
"""

# --- 1. 初始設定 ---
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 09: The Feast")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (15, 15, 20)

# --- 變數定義 ---
block_size = 40
snake_body = [(400, 300)]
head_x, head_y = 400, 300
speed_x, speed_y = 0, 0
# 注意！我們把 target_length 移除了，因為現在長度是由食物決定的
# 取而代之的是「是否變長」的旗標
should_grow = False 

# 食物變數
food_x, food_y = 0, 0
spawn_timer = 0 # 用來做吃掉的特效

# --- 函數定義 ---
def get_rainbow_color(index, total):
    if total == 0: return (255, 255, 255)
    hue = (index / total) 
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (int(r*255), int(g*255), int(b*255))

def spawn_food():
    global food_x, food_y
    cols = WINDOW_WIDTH // block_size
    rows = WINDOW_HEIGHT // block_size
    # 確保食物不會生在蛇身上 (防呆機制)
    while True:
        food_x = random.randint(0, cols - 1) * block_size
        food_y = random.randint(0, rows - 1) * block_size
        if (food_x, food_y) not in snake_body:
            break
    print(f"新食物生成: {food_x}, {food_y}")

# 先生成第一顆
spawn_food()

# --- 2. 遊戲主迴圈 ---
running = True
print("快去吃掉那個紅色的方塊！")

while running:
    # --- A. 事件處理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and speed_y == 0: speed_x, speed_y = 0, -block_size # 一次移動一格
            elif event.key == pygame.K_DOWN and speed_y == 0: speed_x, speed_y = 0, block_size
            elif event.key == pygame.K_LEFT and speed_x == 0: speed_x, speed_y = -block_size, 0
            elif event.key == pygame.K_RIGHT and speed_x == 0: speed_x, speed_y = block_size, 0

    # --- B. 更新狀態 (Logic) ---
    # 為了讓遊戲更好控制，我們稍微降低速度，讓蛇「一格一格」跳
    # 或者我們可以用計時器來控制移動頻率 (這裡先用簡單的 frame skip)
    # 本週簡化：假設每一幀都移動 (速度要調慢一點，不然太快)
    # 修正：直接把 block_size 當速度，並降低 FPS 到 10，這是最經典的貪食蛇手感
    
    head_x += speed_x
    head_y += speed_y
    
    # 邊界傳送
    if head_x >= WINDOW_WIDTH: head_x = 0
    elif head_x < 0: head_x = WINDOW_WIDTH - block_size
    if head_y >= WINDOW_HEIGHT: head_y = 0
    elif head_y < 0: head_y = WINDOW_HEIGHT - block_size
    
    # [本週核心] 碰撞檢測 (Collision)
    # 蛇頭與食物重疊了吗？
    if head_x == food_x and head_y == food_y:
        print("Yummy! 吃到了！")
        should_grow = True # 標記：這次移動不要刪除尾巴
        spawn_food()       # 生成下一個
        spawn_timer = 10   # 啟動特效計時器
    
    # 更新身體
    snake_body.append((head_x, head_y))
    
    if should_grow:
        should_grow = False # 用掉了，重置
        # 不執行 pop(0)，身體就會變長一節
    else:
        snake_body.pop(0) # 沒吃到，維持長度 (刪除尾巴)

    # --- C. 畫面渲染 ---
    # Vibe Check: 吃到的瞬間閃一下背景
    if spawn_timer > 0:
        screen.fill((50, 20, 20)) # 暗紅色閃光
        spawn_timer -= 1
    else:
        screen.fill((10, 10, 15))
        
    # 畫食物
    pygame.draw.rect(screen, FOOD_RED, (food_x, food_y, block_size, block_size), border_radius=10)
    
    # 畫蛇
    for i, segment in enumerate(snake_body):
        color = get_rainbow_color(i, len(snake_body))
        pygame.draw.rect(screen, color, (segment[0], segment[1], block_size, block_size), border_radius=4)
        
    pygame.display.flip()
    clock.tick(10) # 降低 FPS 到 10，讓格子移動感更強

pygame.quit()
sys.exit()
