
import pygame
import sys
import colorsys

"""
Week 07: 程式美學 (The Art of Functions) - 畫筆與網格
核心概念: 
1. 函數 (Function) 定義: def draw_something()
2. 封裝 (Encapsulation): 讓主迴圈變乾淨
3. For 迴圈進階: 網格繪製 (Grid System)
4. Vibe Coding: 賽博網格 (Cyber Grid)
"""

# --- 1. 初始設定 (Setup) ---
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 07: The Architect")
clock = pygame.time.Clock()

# --- Vibe colors ---
GRID_COLOR = (40, 40, 50)
NEON_CYAN = (0, 255, 255)

# --- 變數定義 ---
block_size = 40
snake_body = []
head_x, head_y = 400, 300
speed_x, speed_y = 5, 0
target_length = 30

# --- Vibe Coding: 函數定義區 (The Tool Belt) ---
# 這是本週的重點！我們把會重複用到的程式碼打包成「工具」。

def get_rainbow_color(index, total):
    """
    輸入索引與總數，回傳對應的彩虹 RGB 顏色
    """
    if total == 0: return (255, 255, 255) # 防呆機制
    hue = (index / total)
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (int(r*255), int(g*255), int(b*255))

def draw_grid():
    """
    繪製背景網格線，創造空間感
    """
    # 畫垂直線 (Vertical Lines)
    # range(start, stop, step) -> 從 0 開始，每隔 40 像素畫一條
    for x in range(0, WINDOW_WIDTH, block_size):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT))
    
    # 畫水平線 (Horizontal Lines)
    for y in range(0, WINDOW_HEIGHT, block_size):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

def draw_snake():
    """
    繪製整條蛇的身體
    """
    for i, segment in enumerate(snake_body):
        seg_x, seg_y = segment
        
        # 取得顏色
        color = get_rainbow_color(i, len(snake_body))
        
        # 繪製方塊 (稍微縮小一點點，創造間隙感)
        rect = pygame.Rect(seg_x + 2, seg_y + 2, block_size - 4, block_size - 4)
        pygame.draw.rect(screen, color, rect, border_radius=4)
        
        # [Vibe Check] 如果是頭部 (最後一節)，畫個外框強調
        if i == len(snake_body) - 1:
            pygame.draw.rect(screen, (255, 255, 255), rect, width=2, border_radius=4)

# --- 2. 遊戲主迴圈 ---
running = True
print("程式碼變得更乾淨了！觀察一下 main loop...")

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

    # --- B. 更新狀態 (Logic Update) ---
    head_x += speed_x
    head_y += speed_y
    
    if head_x >= WINDOW_WIDTH: head_x = 0
    elif head_x < 0: head_x = WINDOW_WIDTH - block_size
    if head_y >= WINDOW_HEIGHT: head_y = 0
    elif head_y < 0: head_y = WINDOW_HEIGHT - block_size
    
    snake_body.append((head_x, head_y))
    if len(snake_body) > target_length:
        snake_body.pop(0)

    # --- C. 畫面渲染 (Rendering) ---
    screen.fill((10, 10, 15)) # 稍微帶點藍的黑色背景
    
    # 呼叫我們的專屬函數！
    # 看看這裡變得多簡潔：
    draw_grid()   # 1. 畫網格
    draw_snake()  # 2. 畫蛇
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
