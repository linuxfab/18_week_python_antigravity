
import pygame
import sys
import random

"""
Week 05: 鍵盤車神 (Keyboard Drifter) - 掌控命運
核心概念: 
1. 條件判斷 (if-elif-else) 的完整邏輯
2. 事件監聽 (Event Handling) 的進階運用
3. 連續移動 (Continuous Movement) vs. 瞬間移動
4. Vibe Coding: 瞬間移動 (Teleportation) 與 Turbo 模式
"""

# --- 1. 初始設定 (Setup) ---
pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 05: The Drifter")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_BLUE = (0, 255, 255)
NEON_PURPLE = (255, 0, 255)
WARNING_RED = (255, 50, 50)
TURBO_YELLOW = (255, 255, 0)

current_color = NEON_BLUE

# --- 變數定義區 ---
# 主角位置 (Starting Player Position)
player_x = 400
player_y = 300
player_size = 40

# 主角速度 (Velocity) - 預設靜止
speed_x = 0
speed_y = 0

# 基礎速度常數
NORMAL_SPEED = 5
TURBO_SPEED = 10

# --- 2. 遊戲主迴圈 ---
running = True
print("按下方向鍵 (Arrow Keys) 或 WASD 開始移動！")
print("按住 SHIFT 鍵開啟 Turbo 加速模式！")

while running:
    # --- A. 事件處理 (The Brain) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # [控制權核心] 當按鍵被「按下」的那一瞬間 (KEYDOWN)
        elif event.type == pygame.KEYDOWN:
            
            # 檢查是否按住 Shift (Turbo Mode Check)
            # pygame.key.get_mods() 可以檢查修飾鍵 (Shift/Ctrl/Alt)
            is_turbo = pygame.key.get_mods() & pygame.KMOD_SHIFT
            current_speed = TURBO_SPEED if is_turbo else NORMAL_SPEED
            
            # [多重選擇題] if-elif 結構
            # 這是貪食蛇移動的核心邏輯：
            # 按下一個方向後，速度會持續保持，直到按下另一個方向
            
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                speed_x = 0
                speed_y = -current_speed # 記得嗎？Y 軸向上是減少
                current_color = NEON_BLUE
                print("↑ 北上")
                
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                speed_x = 0
                speed_y = current_speed
                current_color = NEON_PURPLE
                print("↓ 南下")
                
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                speed_x = -current_speed
                speed_y = 0
                current_color = NEON_BLUE
                print("← 西進")
                
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                speed_x = current_speed
                speed_y = 0
                current_color = NEON_PURPLE
                print("→ 東征")
                
            # [緊急煞車] 按空白鍵停止
            elif event.key == pygame.K_SPACE:
                speed_x = 0
                speed_y = 0
                current_color = WARNING_RED
                print("🛑 緊急煞車！")

    # --- B. 更新狀態 (The Physics) ---
    
    # 1. 根據目前的速度，更新位置
    player_x += speed_x
    player_y += speed_y
    
    # 2. [Vibe Feature] 瞬間移動 (Pac-Man Effect)
    # 當方塊跑出右邊界，讓它從左邊出現，而不是撞牆反彈
    # 這比 Week 4 的撞牆更適合貪食蛇遊戲
    
    if player_x > WINDOW_WIDTH:
        player_x = 0 - player_size # 從左邊慢慢滑出來
    elif player_x < 0 - player_size:
        player_x = WINDOW_WIDTH
        
    if player_y > WINDOW_HEIGHT:
        player_y = 0 - player_size
    elif player_y < 0 - player_size:
        player_y = WINDOW_HEIGHT

    # --- C. 畫面渲染 (The Art) ---
    screen.fill((10, 15, 20)) # 深色背景
    
    # 根據是否加速改變外框
    # 如果速度大於正常速度，畫一個黃色外框代表 Turbo
    if abs(speed_x) > NORMAL_SPEED or abs(speed_y) > NORMAL_SPEED:
        pygame.draw.rect(screen, TURBO_YELLOW, (player_x-5, player_y-5, player_size+10, player_size+10), width=2)
    
    # 畫出主角
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    pygame.draw.rect(screen, current_color, player_rect, border_radius=8)
    
    pygame.display.flip()
    clock.tick(60)

# --- 3. 結束 ---
pygame.quit()
sys.exit()
