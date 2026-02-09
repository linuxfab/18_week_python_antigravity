
import pygame
import sys
import colorsys

"""
Week 13: 視覺饗宴 (Visual Polish) - 色彩與圖像
核心概念: 
1. 影像載入 (Image Loading): pygame.image.load
2. 漸層渲染 (Gradient Rendering): 利用 body index
3. 動態效果 (Effects): 呼吸燈與閃爍
"""

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 13: The Glamour")
clock = pygame.time.Clock()

# --- Vibe colors ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (15, 15, 20)

class Snake:
    def __init__(self):
        # 初始化蛇的身體 (30x30, 稍微小一點比較可愛)
        self.body = [(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)]
        self.direction = (0, 0)
        self.block_size = 40
        self.color = NEON_GREEN
        self.length = 3
        
    def draw(self, surface):
        """ 這裡演示『彩虹漸層』的 Vibe 效果 """
        for i, segment in enumerate(self.body):
            # 漸層色邏輯：利用 i / len 計算 Hue
            hue = (i / len(self.body)) * 0.7  # 限制 hue 範圍 (只在綠色到藍色間變換)
            r, g, b = colorsys.hsv_to_rgb(hue, 0.8, 1.0)
            rainbow_color = (int(r*255), int(g*255), int(b*255))
            
            # 使用稍微圓角的矩形，產生科技感
            rect = pygame.Rect(segment[0], segment[1], self.block_size-2, self.block_size-2)
            pygame.draw.rect(surface, rainbow_color, rect, border_radius=8)
            
            # 如果是頭部，畫個眼睛
            if i == len(self.body) - 1:
                eye_radius = 4
                eye_offset_x = 10 if self.direction[0] > 0 else -10
                eye_offset_y = 10 if self.direction[1] > 0 else -10
                
                # 簡單的眼睛位置計算 (這需要一點幾何 logic，這裡簡化)
                eye_pos = (segment[0] + self.block_size//2, segment[1] + self.block_size//2)
                pygame.draw.circle(surface, (255, 255, 255), eye_pos, eye_radius)

class Food:
    def __init__(self):
        self.position = (200, 200)
        self.block_size = 40
        self.pulse_val = 0
        
    def draw(self, surface):
        """ 這裡演示『呼吸燈』效果 """
        self.pulse_val += 0.1
        pulse_size = 20 + abs(int(5 * math.sin(self.pulse_val))) # 20~25 縮放
        
        # 畫在格子的中心點
        center_x = self.position[0] + self.block_size // 2
        center_y = self.position[1] + self.block_size // 2
        
        # 使用圓形代表食物 (因為我們沒有載入 PNG 圖片)
        # 如果要載入圖片： self.image = pygame.image.load("apple.png")
        pygame.draw.circle(surface, FOOD_RED, (center_x, center_y), pulse_size)
    
import math # 用於呼吸燈計算

# --- 遊戲主流程 ---
# 注意：為了簡化，這裡省略了 Handle Input / Move Logic
# 這週重點是 Draw() 方法的改進

snake = Snake()
food = Food()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # 這裡省略蛇的移動邏輯，專注於靜態展示效果
    # 實際運作時，請將 Week 12 的 Move Logic 複製過來！
    
    screen.fill(BG_COLOR)
    snake.draw(screen)
    food.draw(screen)
    
    pygame.display.flip()
    clock.tick(60) # 為了動畫流暢，調回 60 FPS

pygame.quit()
sys.exit()
