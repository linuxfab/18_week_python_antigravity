
import pygame
import sys
import colorsys
import random

"""
Week 11: 死亡宣告 (Game Over) - 遊戲結束狀態
核心概念: 
1. 自我碰撞 (Self-Collision): 吃到自己的身體
2. 狀態管理 (State Management): Running vs. Game Over
3. 遊戲重置 (Reset/Restart Mechanism)
"""

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 11: The End")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (15, 15, 20)
TEXT_COLOR = (255, 255, 255)
GAME_OVER_COLOR = (255, 50, 50) # 紅色

# --- 變數定義 ---
block_size = 40
snake_body = [(400, 300)]
head_x, head_y = 400, 300
speed_x, speed_y = 0, 0
should_grow = False 
food_x, food_y = 0, 0
score = 0
game_over = False # 這是本週的重點變數

# 字型
try:
    font_large = pygame.font.SysFont("Arial", 80, bold=True)
    font_small = pygame.font.SysFont("Arial", 36)
except:
    pass

def spawn_food():
    global food_x, food_y
    cols = WINDOW_WIDTH // block_size
    rows = WINDOW_HEIGHT // block_size
    while True:
        food_x = random.randint(0, cols - 1) * block_size
        food_y = random.randint(0, rows - 1) * block_size
        if (food_x, food_y) not in snake_body:
            break

def reset_game():
    """
    重置所有遊戲狀態，讓玩家可以重新開始
    """
    global head_x, head_y, snake_body, speed_x, speed_y, score, game_over
    head_x, head_y = 400, 300
    snake_body = [(400, 300)]
    speed_x, speed_y = 0, 0
    score = 0
    game_over = False
    spawn_food()

spawn_food()

running = True
# --- 遊戲主迴圈 ---
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 如果 Game Over 狀態，按任何鍵重新開始
            if game_over:
                if event.key == pygame.K_SPACE:
                    reset_game()
            else:
                if event.key == pygame.K_UP and speed_y == 0: speed_x, speed_y = 0, -block_size 
                elif event.key == pygame.K_DOWN and speed_y == 0: speed_x, speed_y = 0, block_size
                elif event.key == pygame.K_LEFT and speed_x == 0: speed_x, speed_y = -block_size, 0
                elif event.key == pygame.K_RIGHT and speed_x == 0: speed_x, speed_y = block_size, 0

    if not game_over:
        # --- 正常遊戲邏輯 ---
        head_x += speed_x
        head_y += speed_y
        
        # 邊界傳送 (Pac-Man Style)
        # 本週可以選擇：想做「撞牆死」還是「穿越」？這裡維持穿越比較好玩
        if head_x >= WINDOW_WIDTH: head_x = 0
        elif head_x < 0: head_x = WINDOW_WIDTH - block_size
        if head_y >= WINDOW_HEIGHT: head_y = 0
        elif head_y < 0: head_y = WINDOW_HEIGHT - block_size
        
        # [核心] 自我碰撞檢測 (Self Collision)
        # 如果新的頭部位置，已經存在於舊的身體清單中 -> 咬到自己了！
        # snake_body[:-1] 排除最後一節 (因為如果是剛剛長出來的可能會有誤判? 其實直接檢查 body 就好，因為頭還沒加進去)
        
        new_head = (head_x, head_y)
        if new_head in snake_body:
            print("Game Over! 咬到尾巴了")
            game_over = True
        
        # 食物碰撞
        if head_x == food_x and head_y == food_y:
            should_grow = True 
            score += 10
            spawn_food()       
        
        snake_body.append(new_head)
        
        if should_grow:
            should_grow = False 
        else:
            snake_body.pop(0) 

    # --- 畫面渲染 ---
    screen.fill(BG_COLOR)
        
    if game_over:
        # 繪製 Game Over 畫面
        text_go = font_large.render("GAME OVER", True, GAME_OVER_COLOR)
        text_restart = font_small.render("Press SPACE to Restart", True, TEXT_COLOR)
        
        # 置中顯示
        rect_go = text_go.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50))
        rect_restart = text_restart.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50))
        
        screen.blit(text_go, rect_go)
        screen.blit(text_restart, rect_restart)
        
    else:
        # 繪製正常遊戲畫面
        pygame.draw.rect(screen, FOOD_RED, (food_x, food_y, block_size, block_size), border_radius=10)
        
        for i, segment in enumerate(snake_body):
            color_val = max(50, 255 - i * 5)
            pygame.draw.rect(screen, (50, color_val, 50), (segment[0], segment[1], block_size, block_size), border_radius=4)
        
        # 分數
        score_surf = font_small.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_surf, (10, 10))
        
    pygame.display.flip()
    clock.tick(10) 

pygame.quit()
sys.exit()
