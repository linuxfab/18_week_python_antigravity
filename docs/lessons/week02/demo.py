
import pygame
import sys

"""
Week 02: 顏色與形狀 (Colors & Shapes) - The First Snake Head
核心概念: 
1. 座標系統 (Coordinate System): (0,0) 在左上角
2. RGB 色彩模型 (Red, Green, Blue)
3. 繪製矩形 (Drawing Rectangles)
"""

# --- 1. 初始設定 (Setup) ---
pygame.init()

# 定義視窗大小
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 02: Coordinate Mastery")

# --- Vibe Coding: 色彩調色盤 (Color Palette) ---
# 試著修改這些數值，創造你的專屬配色！
# 格式: (R, G, B) -> 範圍 0-255
DEEP_SPACE_BLUE = (10, 10, 50)    # 深空藍背景
NEON_GREEN = (57, 255, 20)        # 螢光綠 (經典蛇色)
HOT_PINK = (255, 20, 147)         # 熱粉紅 (標記點)
GRID_GRAY = (50, 50, 60)          # 網格灰

# --- 蛇頭設定 (Snake Head Config) ---
# 我們將蛇頭定義為一個 40x40 的正方形
BLOCK_SIZE = 40

# 計算畫面中心點 (Center Calculation)
# 寬度的一半, 高度的一半 -> (400, 300)
center_x = WINDOW_WIDTH // 2
center_y = WINDOW_HEIGHT // 2

# 注意：pygame.Rect 的 (x, y) 是指「左上角」的座標
# 為了讓方塊真正置中，我們需要將座標往左上修正一半的方塊大小
rect_x = center_x - (BLOCK_SIZE // 2)
rect_y = center_y - (BLOCK_SIZE // 2)

# 建立蛇頭矩形物件 (Rect Object)
# 參數: (x, y, width, height)
snake_head = pygame.Rect(rect_x, rect_y, BLOCK_SIZE, BLOCK_SIZE)

# --- 2. 遊戲主迴圈 (Game Loop) ---
running = True
print(f"視窗中心點: ({center_x}, {center_y})")
print(f"蛇頭繪製位置 (左上角): ({rect_x}, {rect_y})")

while running:
    # --- 3. 事件處理 (Event Handling) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # [Vibe Feature] 點擊滑鼠，在終端機顯示座標
        # 這是理解座標系統最直觀的方式！
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(f"👆 你點擊了座標: {mouse_pos}")

    # --- 4. 畫面渲染 (Rendering) ---
    
    # A. 塗滿背景
    screen.fill(DEEP_SPACE_BLUE)
    
    # B. [輔助線] 繪製中心十字線 (Visual Guide)
    # 畫一條橫線 (從左到右)
    pygame.draw.line(screen, GRID_GRAY, (0, center_y), (WINDOW_WIDTH, center_y), 1)
    # 畫一條直線 (從上到下)
    pygame.draw.line(screen, GRID_GRAY, (center_x, 0), (center_x, WINDOW_HEIGHT), 1)

    # C. 繪製蛇頭 (The Hero)
    # pygame.draw.rect(畫布, 顏色, 矩形物件)
    pygame.draw.rect(screen, NEON_GREEN, snake_head)
    
    # D. [Vibe Check] 繪製邊框 (讓蛇頭更立體)
    # width=2 表示只畫邊框，不填滿
    pygame.draw.rect(screen, HOT_PINK, snake_head, width=2)

    # E. 更新畫面
    pygame.display.flip()

# --- 5. 結束程式 ---
pygame.quit()
sys.exit()
