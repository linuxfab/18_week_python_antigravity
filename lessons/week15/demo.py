
import pygame
import sys
import colorsys

"""
Week 15: 難度曲線 (Difficulty Curve) - 這是挑戰，也是樂趣
核心概念: 
1. 速度調整 (Speed Scaling): Base Speed + Score Factor
2. FPS 驅動 vs. Timer 驅動
3. 平衡性 (Balancing)
"""

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 15: The Pressure")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (15, 15, 20)
TEXT_COLOR = (255, 255, 255)

# --- 變數 ---
block_size = 40
snake_body = [(400, 300)]
head_x, head_y = 400, 300
speed_x, speed_y = 0, 0
score = 0

# 基礎變數
BASE_FPS = 5
MAX_FPS = 30
difficulty_factor = 0 # 每吃一顆食物增加多少 FPS

try:
    font = pygame.font.SysFont("Arial", 36, bold=True)
except:
    font = pygame.font.Font(None, 36)

# --- 函數 ---
def calculate_fps(score):
    """ 本週核心函數：根據分數回傳目標 FPS """
    # 公式：5 + (分數 / 50) -> 每得 50 分增加 1 FPS
    # 或者稍微快一點：5 + (分數 / 10)
    
    current_fps = BASE_FPS + (score // 10) # 這是難度曲線公式
    
    # 限制最大速度 (以免人類無法反應)
    return min(current_fps, MAX_FPS)

# --- 主迴圈 (含簡單移動) ---
running = True
print("試著按 [SPACE] 增加分數，體驗速度變化！")

while running:
    # 這裡的邏輯幾乎與 Week 12 相同，省略重複部分
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and speed_y == 0: speed_x, speed_y = 0, -block_size 
            elif event.key == pygame.K_DOWN and speed_y == 0: speed_x, speed_y = 0, block_size
            elif event.key == pygame.K_LEFT and speed_x == 0: speed_x, speed_y = -block_size, 0
            elif event.key == pygame.K_RIGHT and speed_x == 0: speed_x, speed_y = block_size, 0
            
            # 測試：按空白鍵加分
            elif event.key == pygame.K_SPACE:
                score += 10
                print(f"分數: {score}, 目標 FPS: {calculate_fps(score)}")

    # 簡單移動 (注意，這只是為了展示效果)
    head_x += speed_x
    head_y += speed_y
    # ... 省略邊界處理 ...

    snake_body.append((head_x, head_y))
    snake_body.pop(0) # 這裡假設沒吃到食物

    screen.fill(BG_COLOR)
    
    # 畫蛇
    for segment in snake_body:
        pygame.draw.rect(screen, NEON_GREEN, (segment[0], segment[1], block_size, block_size), border_radius=4)

    # 顯示目前 FPS 狀態
    target_fps = calculate_fps(score)
    actual_fps = clock.get_fps()
    
    status_text = f"Score: {score} | Target FPS: {target_fps} | Real FPS: {actual_fps:.1f}"
    text_surf = font.render(status_text, True, TEXT_COLOR)
    screen.blit(text_surf, (10, 10))

    pygame.display.flip()
    
    # [本週核心] 使用動態的 FPS
    clock.tick(target_fps)

pygame.quit()
sys.exit()
