
import pygame
import sys
import colorsys
import random # 這是本週的主角！

"""
Week 08: 混沌理論 (Chaos Theory) - 食物的誕生
核心概念: 
1. 隨機性 (Randomness): 電腦如何擲骰子？
2. 網格對齊 (Grid Snapping): 數學計算確保食物出生在格子內
3. 模組引用 (Refactoring): 將食物邏輯與繪圖分開
4. Vibe Coding: 霓虹食物 (Neon Food)
"""

# --- 1. 初始設定 (Setup) ---
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 08: The Food")
clock = pygame.time.Clock()

# --- Vibe colors ---
GRID_COLOR = (30, 30, 40)
FOOD_NEON = (255, 50, 50) # 預設紅色食物

# --- 變數定義 ---
block_size = 40
snake_body = [(400, 300)]
head_x, head_y = 400, 300
speed_x, speed_y = 0, 0
target_length = 5

# --- [本週核心] 食物變數 ---
# 這些變數會被 spawn_food() 函數修改
food_x = 0
food_y = 0
food_color = FOOD_NEON

# --- Vibe Coding: 函數定義區 ---

def get_rainbow_color(index, total):
    if total == 0: return (255, 255, 255)
    hue = (index / total)
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (int(r*255), int(g*255), int(b*255))

def draw_grid():
    for x in range(0, WINDOW_WIDTH, block_size):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, block_size):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

def spawn_food():
    """
    這個函數負責計算新的食物位置
    """
    # 宣告 global 變數，讓我們可以在函數裡面修改外面的變數
    global food_x, food_y, food_color
    
    # 1. 計算橫向有幾格？ (800 / 40 = 20 格)
    # 我們要把 0~19 的隨機數，還原成像素座標
    cols = WINDOW_WIDTH // block_size
    rows = WINDOW_HEIGHT // block_size
    
    # 隨機選一格 (0 到 cols-1) 
    # random.randint(a, b) 會包含 b，所以要減 1
    rand_col = random.randint(0, cols - 1)
    rand_row = random.randint(0, rows - 1)
    
    # 2. 轉換回像素座標 (Pixel Coordinate)
    # 格子編號 * 格子大小 = 實際位置
    food_x = rand_col * block_size
    food_y = rand_row * block_size
    
    # 3. [Vibe Feature] 隨機顏色
    # 讓每次食物出現都有驚喜
    food_color = (
        random.randint(50, 255),
        random.randint(50, 255),
        random.randint(50, 255)
    )
    print(f"食物生成於: ({food_x}, {food_y})")

def draw_food():
    """
    單純負責把食物畫出來
    """
    rect = pygame.Rect(food_x, food_y, block_size, block_size)
    # 使用稍微縮小的圓角矩形，看起來比較像「蘋果」或「膠囊」
    pygame.draw.rect(screen, food_color, rect, border_radius=12)
    # 畫個白色亮點，增加立體感
    pygame.draw.circle(screen, (255, 255, 255), (food_x + 10, food_y + 10), 4)

# --- 遊戲開始前，先生成第一顆食物 ---
spawn_food()

# --- 2. 遊戲主迴圈 ---
running = True
print("按 [空白鍵] 可以測試『吃掉』食物並重新生成的效果！")

while running:
    # --- A. 事件處理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: speed_x, speed_y = 0, -5
            elif event.key == pygame.K_DOWN: speed_x, speed_y = 0, 5
            elif event.key == pygame.K_LEFT: speed_x, speed_y = -5, 0
            elif event.key == pygame.K_RIGHT: speed_x, speed_y = 5, 0
            
            # [模擬測試] 手動觸發食物生成 logic
            elif event.key == pygame.K_SPACE:
                spawn_food()

    # --- B. 更新狀態 (Logic Update) ---
    head_x += speed_x
    head_y += speed_y
    
    # [邊界檢查]
    if head_x >= WINDOW_WIDTH: head_x = 0
    elif head_x < 0: head_x = WINDOW_WIDTH - block_size
    if head_y >= WINDOW_HEIGHT: head_y = 0
    elif head_y < 0: head_y = WINDOW_HEIGHT - block_size
    
    snake_body.append((head_x, head_y))
    if len(snake_body) > target_length:
        snake_body.pop(0)

    # --- C. 畫面渲染 (Rendering) ---
    screen.fill((15, 15, 20)) 
    
    draw_grid()   
    draw_food()    # 記得把食物畫出來！
    
    # 畫蛇 (這次直接寫在迴圈裡示範，如果不封裝成 draw_snake 也可以)
    for i, segment in enumerate(snake_body):
        color = get_rainbow_color(i, len(snake_body))
        pygame.draw.rect(screen, color, (segment[0], segment[1], block_size, block_size), border_radius=4)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
