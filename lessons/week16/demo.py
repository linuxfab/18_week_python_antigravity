
import pygame
import sys
import colorsys
import random

"""
Week 16: 擴充功能 (Power-Ups) - 繼承與多型
核心概念: 
1. 繼承 (Inheritance): class Poison(Food)
2. 多型 (Polymorphism): draw() override
3. 效果疊加 (Effect Stacking)
"""

pygame.init()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 16: The Poison")
clock = pygame.time.Clock()

NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
POISON_PURPLE = (200, 0, 255) # 毒蘋果顏色
SPEED_YELLOW = (255, 255, 0)
BG_COLOR = (15, 15, 20)
TEXT_COLOR = (255, 255, 255)

# --- 基礎食物類別 ---
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.block_size = 40
        self.color = FOOD_RED
        self.score_value = 10
        self.randomize_position()
        
    def randomize_position(self):
        cols = WINDOW_WIDTH // self.block_size
        rows = WINDOW_HEIGHT // self.block_size
        self.position = (
            random.randint(0, cols-1) * self.block_size,
            random.randint(0, rows-1) * self.block_size
        )

    def effect(self, snake):
        """ 吃到後的效果 """
        snake.should_grow = True
        return self.score_value # 回傳得分

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], self.block_size, self.block_size)
        pygame.draw.rect(surface, self.color, rect, border_radius=10)

# --- [本週核心] 繼承類別 ---

class PoisonInfo(Food):
    """ 毒蘋果: 繼承自 Food，但覆寫掉效果 """
    def __init__(self):
        super().__init__() # 呼叫父類的 init
        self.color = POISON_PURPLE
        self.score_value = -50
    
    def effect(self, snake):
        """ 吃到毒蘋果，不會長大，反而扣分並縮短身體(這裡簡化不縮短) """
        print("哎呀！好毒！")
        snake.should_grow = False # 確保不長大
        # 甚至可以砍掉身體一半？
        if len(snake.body) > 3:
            del snake.body[:len(snake.body)//2] # 砍掉一半身體
        return self.score_value

class SpeedBoost(Food):
    """ 加速道具 """
    def __init__(self):
        super().__init__()
        self.color = SPEED_YELLOW
        self.score_value = 50
    
    def effect(self, snake):
        """ 吃到加速，大量加分 """
        print("Turbo Boost!")
        return self.score_value

# --- 遊戲管理 ---
# 我們不再只有一顆食物，而是一個清單
food_items = []
snake_dummy = None # 省略 snake 實作細節，僅展示 Food 邏輯

# 隨機生成特殊的物品
def spawn_special_item():
    roll = random.randint(1, 100)
    if roll <= 20: # 20% 機率生成毒蘋果
        return PoisonInfo()
    elif roll <= 40: # 20% 機率生成加速
        return SpeedBoost()
    else: # 60% 機率生成普通食物
        return Food()

# Demo 用的簡單生成
current_item = spawn_special_item()

# --- 主迴圈 ---
running = True
print("按 [SPACE] 重新生成物品 (模擬吃到)，觀察控制台輸出類型！")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 模擬吃到
                # 這裡展示 polymorphism 的威力：
                # 不管 current_item 是什麼，我們只呼叫 .effect()，不用寫 if 去判斷類型
                
                # 假設有個假的 snake 物件傳進去
                class DummySnake: 
                    def __init__(self): self.body = [0]*10; self.should_grow = False
                
                dummy = DummySnake()
                score_gain = current_item.effect(dummy)
                print(f"吃到 {type(current_item).__name__}, 得分: {score_gain}")
                
                current_item = spawn_special_item() # 生成下一個

    screen.fill(BG_COLOR)
    
    # Polymorphic Draw
    # 不管是毒蘋果還是普通蘋果，都呼叫 .draw()
    current_item.draw(screen)
    
    # 畫個標籤說明它是什麼
    try:
        font = pygame.font.SysFont("Arial", 24)
        label = font.render(f"Type: {type(current_item).__name__}", True, TEXT_COLOR)
        screen.blit(label, (10, 10))
    except: pass

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
