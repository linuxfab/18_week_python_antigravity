
import pygame
import sys
import colorsys

"""
Week 06: 光速戰記 (The Trail Blaster) - 打造貪食蛇身體
核心概念: 
1. 清單 (List) 資料結構: `snake_body = []`
2. 隊列邏輯 (Queue Logic): 先進先出 (FIFO)
3. For 迴圈渲染 (Rendering Loop)
4. Vibe Coding: 漸層色軌跡 (Gradient Trail)
"""

# --- 1. 初始設定 (Setup) ---
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 06: The Trail")
clock = pygame.time.Clock()

# --- Vibe colors function ---
# 利用 HSV 色彩模型產生彩虹
def get_rainbow_color(index, total):
    # Hue (色相) 0.0 ~ 1.0
    hue = (index / total) 
    # 轉換為 RGB (0~255)
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    return (int(r*255), int(g*255), int(b*255))

# --- 變數定義區 ---
# 主角位置 (Head)
head_x = 400
head_y = 300
block_size = 20
speed_x = 5  # 預設向右移動 (自動移動)
speed_y = 0

# [本週核心] 身體清單 (The Body List)
# 這是一個空的清單，等等我們會把頭的位置一直塞進去
# 格式範例: [(400, 300), (405, 300), (410, 300)...]
snake_body = []

# 蛇的目標長度
# 既然是貪食蛇，身體當然要有長度！
target_length = 50 

# --- 2. 遊戲主迴圈 ---
running = True
print("移動滑鼠或按方向鍵控制方向！")
print("觀察終端機：你的 List 正在變長...")

while running:
    # --- A. 事件處理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed_x, speed_y = 0, -5
            elif event.key == pygame.K_DOWN:
                speed_x, speed_y = 0, 5
            elif event.key == pygame.K_LEFT:
                speed_x, speed_y = -5, 0
            elif event.key == pygame.K_RIGHT:
                speed_x, speed_y = 5, 0
            
            # [除錯功能] 按空白鍵印出目前的 List
            elif event.key == pygame.K_SPACE:
                print(f"目前身體長度: {len(snake_body)}")
                print(f"身體數據: {snake_body}")

    # --- B. 更新狀態 (List Logic) ---
    
    # 1. 更新頭的位置 (Head Movement)
    head_x += speed_x
    head_y += speed_y
    
    # [邊界處理 - Pac-Man Style]
    if head_x > WINDOW_WIDTH: head_x = 0
    if head_x < 0: head_x = WINDOW_WIDTH
    if head_y > WINDOW_HEIGHT: head_y = 0
    if head_y < 0: head_y = WINDOW_HEIGHT
    
    # 2. [List Operation] 將新的頭加入清單 (Append Logic)
    # 我們把目前的座標打包成一個 Tuple (元組) -> (x, y)
    current_pos = (head_x, head_y)
    snake_body.append(current_pos)
    
    # 3. [Key Concept] 保持長度 (Length Control)
    # 如果身體太長了，就把最舊的那一節 (尾巴) 刪掉
    # snake_body[0] 是最舊的 (Tail)，snake_body[-1] 是最新的 (Head)
    if len(snake_body) > target_length:
        removed_tail = snake_body.pop(0) # 移除第 0 個元素
        
    # --- C. 畫面渲染 (Loop Rendering) ---
    screen.fill((0, 0, 0)) # 全黑背景
    
    # [Loop Magic] 遍歷清單畫出每一節身體
    # enumerate 可以同時拿到「索引 (index)」和「內容 (segment)」
    # 我們利用 index 來計算漸層顏色
    
    for i, segment in enumerate(snake_body):
        # 解包座標
        seg_x, seg_y = segment 
        
        # 計算 Vibe 顏色 (彩虹漸層)
        color = get_rainbow_color(i, len(snake_body))
        
        # 畫出身體
        # 這裡有個小技巧：越接近頭部 (i 越大)，方塊越大
        # 這樣會有一種「彗星」的拖尾效果
        dynamic_size = block_size * (i / len(snake_body))
        
        # 為了置中繪製，我們需要根據新的大小調整座標
        offset = (block_size - dynamic_size) / 2
        
        rect = pygame.Rect(seg_x + offset, seg_y + offset, dynamic_size, dynamic_size)
        pygame.draw.rect(screen, color, rect)
        
    pygame.display.flip()
    clock.tick(60)

# --- 3. 結束 ---
pygame.quit()
sys.exit()
