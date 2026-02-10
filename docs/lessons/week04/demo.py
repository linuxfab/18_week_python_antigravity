
import pygame
import sys
import random

"""
Week 04: 變數的超能力 (Variables: The Super Memory)
核心概念: 
1. 變數 (Variable) = 記憶體裡的盒子
2. 賦值 (Assignment) (x = x + 1)
3. 速度向量 (Velocity Vector)
4. Vibe Coding: 彈跳特效 (Bouncing Box)
"""

# --- 1. 初始設定 (Setup) ---
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 04: The Runner")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_COLORS = [
    (255, 0, 80),    # Cyber Pink
    (0, 255, 255),   # Cyan
    (255, 255, 0),   # Electric Yellow
    (57, 255, 20),   # Alien Green
]
current_color = NEON_COLORS[0]

# --- 變數定義區 (Variable Zone) ---
# [位置變數] 紀錄方塊目前在哪裡 (Memory)
block_x = 400
block_y = 300
block_size = 50

# [速度變數] 決定每一幀移動多少距離 (Velocity)
# 正數代表向右/下，負數代表向左/上
speed_x = 5
speed_y = 5

# --- 2. 遊戲主迴圈 ---
running = True
print("方塊啟動！觀察它的座標變化...")

while running:
    # --- A. 事件處理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # [Vibe Feature] 按空白鍵隨機改變速度
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed_x = random.randint(-8, 8)
                speed_y = random.randint(-8, 8)
                print(f"速度突變！({speed_x}, {speed_y})")

    # --- B. 更新狀態 (Update State) ---
    # 這是本週的核心魔法：舊的位置 + 速度 = 新的位置
    # 在數學課本上 x = x + 5 是錯的，但在程式裡，這是「更新」的意思
    block_x = block_x + speed_x
    block_y = block_y + speed_y
    
    # [邊界反彈邏輯] (Bouncing Logic)
    # 如果撞到右牆 OR 撞到左牆
    if block_x > (WINDOW_WIDTH - block_size) or block_x < 0:
        # 速度反轉 (5 變成 -5，向右變成向左)
        speed_x = -speed_x
        # 換個顏色慶祝一下
        current_color = random.choice(NEON_COLORS)
        print("Boing! 撞牆反彈")
        
    # 如果撞到地板 OR 撞到天花板
    if block_y > (WINDOW_HEIGHT - block_size) or block_y < 0:
        speed_y = -speed_y
        current_color = random.choice(NEON_COLORS)
        print("Bam! 地板反彈")

    # --- C. 畫面渲染 ---
    # 稍微留一點殘影 (Trail Effect) 的小技巧：
    # 不要完全塗黑背景，而是塗上一層半透明的黑色 (進階技巧，這裡先用標準塗黑)
    screen.fill((10, 10, 20)) 
    
    # 畫出方塊
    # 我們必須把浮點數座標轉成整數 (Rect 只接受整數)
    target_rect = pygame.Rect(int(block_x), int(block_y), block_size, block_size)
    pygame.draw.rect(screen, current_color, target_rect, border_radius=8)
    
    pygame.display.flip()
    clock.tick(60) # 鎖定 60 FPS

# --- 3. 結束 ---
pygame.quit()
sys.exit()
