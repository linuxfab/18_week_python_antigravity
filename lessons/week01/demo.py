import pygame
import sys

"""
Week 01: Vibe Coding 體驗 - Hello Pygame
核心概念: 
1. 環境建置 (Setup)
2. 遊戲迴圈 (Game Loop)
3. 事件處理 (Event Handling) - 包含基礎鍵盤控制
4. 畫面渲染 (Rendering)
"""

# --- 1. 初始設定 (Setup) ---
# 啟動 Pygame 引擎，這是所有 Pygame 程式的第一步
pygame.init()

# 設定視窗大小 (寬, 高)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 設定視窗標題
pygame.display.set_caption("Python Vibe Coding - Week 01 Demo")

# --- Vibe Coding: 定義顏色 (Color Palette) ---
# 使用 RGB (Red, Green, Blue) 格式，數值範圍 0-255
CLASSIC_BLACK = (0, 0, 0)       # 經典黑
CYBER_PURPLE = (30, 0, 50)      # 賽博龐克紫
MATRIX_GREEN = (0, 255, 100)    # 駭客矩陣綠 (用於文字或特效)

# 遊戲狀態變數 (Game State)
# 這是一個簡單的「狀態」，記錄目前的背景顏色
current_background = CLASSIC_BLACK

# --- 2. 遊戲主迴圈 (Game Loop) ---
# 這是遊戲的心臟，只要 running 為 True，遊戲就會持續運行
running = True 
print("遊戲引擎啟動！試試看按下 [空白鍵] 或 [ESC]...")

while running:
    # --- 3. 偵測輸入/事件 (Event Handling) ---
    # 這是遊戲的「感官」，負責接收滑鼠、鍵盤等訊號
    for event in pygame.event.get():
        
        # [事件 1] 使用者點擊視窗關閉按鈕 (X)
        if event.type == pygame.QUIT:
            running = False
            
        # [事件 2] 鍵盤控制邏輯 (Keyboard Control)
        elif event.type == pygame.KEYDOWN:
            # 可以在終端機看到按下的按鍵代碼，方便除錯
            print(f"偵測到按鍵: {event.key}")
            
            # 邏輯 A: 按下 ESC 鍵 -> 退出遊戲
            if event.key == pygame.K_ESCAPE:
                print("玩家要求退出 (ESC)")
                running = False
                
            # 邏輯 B: 按下空白鍵 (Space) -> 切換背景氣氛 (Vibe Switch)
            elif event.key == pygame.K_SPACE:
                print("Vibe 切換！")
                if current_background == CLASSIC_BLACK:
                    current_background = CYBER_PURPLE
                else:
                    current_background = CLASSIC_BLACK
            
            # 邏輯 C: 方向鍵偵測 (預告功能)
            elif event.key == pygame.K_UP:
                print("↑ 前進訊號收到")
            elif event.key == pygame.K_DOWN:
                print("↓ 後退訊號收到")
            elif event.key == pygame.K_LEFT:
                print("← 左轉訊號收到")
            elif event.key == pygame.K_RIGHT:
                print("→ 右轉訊號收到")

    # --- 4. 更新畫面 (Rendering/Drawing) ---
    # 這是遊戲的「臉」，負責將狀態畫到螢幕上
    
    # 步驟 A: 塗滿背景顏色 (清除上一幀的畫面)
    screen.fill(current_background)
    
    # (未來週次會在這裡畫上蛇、食物、分數...)
    
    # 步驟 B: 翻轉顯示緩衝區 (Flip)
    # 將繪製好的畫面一次性呈現給玩家，避免閃爍
    pygame.display.flip()

# --- 5. 結束程式 (Quit) ---
# 釋放 Pygame 資源並關閉視窗
print("遊戲結束，下次見！")
pygame.quit()
sys.exit()
