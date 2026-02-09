
import pygame
import sys
import colorsys

"""
Week 17: 魔鬼剋星 (Ghostbusters) - 除錯與優化
核心概念: 
1. 除錯 (Debugging): print vs. IDE debugging
2. 優化 (Optimization): 減少不必要的計算
3. 異常處理 (Exception Handling): try-except 安全網
"""

# 這是一個故意寫得很爛、甚至有 Bug 的程式碼
# 學生的任務是修好它！

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 17: The Challenge")
clock = pygame.time.Clock()

# [Bug 1: 拼字錯誤與未定義變數]
# NEON_GREEN = (50, 255, 50)
# FOOD_RED = (255, 50, 50) # 修正後應該會有這行
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# [Bug 2: 全域變數污染]
score = 0
def update_score():
    # 這裡如果不加 global score，會發生 UnboundLocalError
    # score += 10
    pass 

# [Optimization Challenge]
# 這裡有個效能殺手
def heavy_calculation():
    # 每一幀都計算一百萬次 sqrt，會導致遊戲卡頓
    for i in range(1000000):
        _ = i * 0.5 

running = True
print("按下 [SPACE] 觸發 Bug！")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("觸發 Bug...")
                try:
                    update_score() # 這行會爆
                except Exception as e:
                    print(f"抓到了！錯誤是: {e}")
                
                # 這裡會卡
                # heavy_calculation() 

    screen.fill((0, 0, 0))
    # 假裝畫一些東西
    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 50, 50))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()

"""
解答 (Answers):
1. 在 update_score 加入 global score
2. 移除 heavy_calculation 的迴圈，或者不要每幀呼叫它
3. 補上顏色定義
"""
