
import pygame
import sys
import math

"""
Week 03: 遊戲迴圈的心跳 (The Heartbeat of the Game Loop)
核心概念: 
1. 遊戲迴圈 (Game Loop) 的標準結構
2. FPS (Frames Per Second) 控制
3. 事件處理 (Event Handling) 的完整流程
4. Vibe Coding: 視覺化心跳 (Visual Heartbeat)
"""

# --- 1. 初始設定 (Setup) ---
pygame.init()

# 定義視窗大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 03: The Heartbeat")

# --- Vibe Coding: 配色方案 ---
BACKGROUND_COLOR = (20, 20, 30)   # 深邃灰
HEART_COLOR = (255, 50, 50)       # 熱血紅
TEXT_COLOR = (200, 200, 200)      # 銀灰色

# --- 重要的時間控制 (Time Control) ---
clock = pygame.time.Clock()  # 建立一個時鐘物件
FPS = 60                     # 設定目標幀率 (每秒跑 60 次迴圈)

# --- 心跳動畫變數 ---
base_size = 100              # 心臟的基礎大小
pulse_speed = 0.1            # 心跳速度
time_counter = 0             # 時間計數器

# --- 字型設定 ---
font = pygame.font.SysFont("Arial", 24)

# --- 2. 遊戲主迴圈 (Game Loop Start) ---
running = True

while running:
    # --- A. 事件處理 (Event Handling) ---
    # 每一幀都要問作業系統：「有什麼事發生嗎？」
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # --- B. 更新狀態 (Update State) ---
    # 讓心臟跳動！利用 sin 波函數創造平滑的縮放效果
    # sin 函數的值會在 -1 到 1 之間擺盪，非常適合做動畫
    time_counter += pulse_speed
    pulse_amount = math.sin(time_counter) * 20  # 縮放幅度 20 像素
    current_size = base_size + pulse_amount
    
    # 計算心臟的位置 (保持在視窗正中央)
    # 注意：因為大小一直在變，所以每一幀都要重新計算左上角位置
    center_x = WINDOW_WIDTH // 2
    center_y = WINDOW_HEIGHT // 2
    rect_x = center_x - (current_size // 2)
    rect_y = center_y - (current_size // 2)
    
    # 建立心臟矩形 (這裡我們用正方形代表心臟)
    heart_rect = pygame.Rect(rect_x, rect_y, current_size, current_size)

    # --- C. 畫面渲染 (Rendering) ---
    screen.fill(BACKGROUND_COLOR)
    
    # 畫出心臟
    pygame.draw.rect(screen, HEART_COLOR, heart_rect, border_radius=20) # 圓角矩形看起來更像有機體
    
    # 顯示 FPS 資訊
    # clock.get_fps() 可以抓到實際運行的幀率
    fps_text = f"FPS: {clock.get_fps():.2f}"
    text_surface = font.render(fps_text, True, TEXT_COLOR)
    screen.blit(text_surface, (10, 10))

    # 翻轉畫面
    pygame.display.flip()
    
    # --- D. 控制時間 (Clock Tick) ---
    # 這行是關鍵！它會強制讓迴圈暫停一下，確保 FPS 不會超過 60
    # 如果不加這行，迴圈會跑得飛快 (依賴 CPU 速度)，導致遊戲忽快忽慢
    clock.tick(FPS)

# --- 3. 結束程式 ---
pygame.quit()
sys.exit()
