
import pygame
import sys
import colorsys

"""
Week 14: 聽覺盛宴 (Audio Experience) - 音效與背景音樂
核心概念: 
1. 聲音載入 (SFX Loading): pygame.mixer.Sound
2. 背景音樂 (Background Music): pygame.mixer.music
3. 事件觸發音效 (Event-based Audio)
"""

pygame.init()
pygame.mixer.init() # 記得初始化 Mixer！

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Python Vibe Coding - Week 14: The Sound")
clock = pygame.time.Clock()

# --- 載入音效 (模擬) ---
# 因為我們沒有實際的 .wav 檔案，這裡使用了 Pygame 的 Synthesizer (Synth) 功能？
# 不，Pygame 沒有內建 Synth。
# 所以這週的 demo 必須依賴外部檔案。
# 但為了讓程式碼能跑，我們會用 try-except 包起來，如果找不到檔案就不播放。

try:
    eat_sound = pygame.mixer.Sound("eat.wav")
    game_over_sound = pygame.mixer.Sound("game_over.wav")
    pygame.mixer.music.load("bgm.mp3")
    pygame.mixer.music.play(-1) # -1 代表無限循環播放
    print("音效載入成功！")
except:
    print("注意：找不到音效檔案 (eat.wav, bgm.mp3)。請自行準備這些檔案放在同目錄下！")
    # 這裡我們可以生成一個簡單的 Beep 聲替代嗎？
    # Windows 系統可以用 winsound，但跨平台不建議。
    # 這裡僅展示架構。

# --- Vibe colors ---
NEON_GREEN = (50, 255, 50)
FOOD_RED = (255, 50, 50)
BG_COLOR = (15, 15, 20)
TEXT_COLOR = (255, 255, 255)

# --- 變數 ---
snake_body = [(400, 300)]
should_grow = False 
food_x, food_y = 200, 200

# --- 函數 ---
def play_eat_sound():
    try:
        eat_sound.play()
    except:
        print("Beep! (模擬吃到聲音)")

# --- 主迴圈 (簡化版) ---
running = True
print("按下 [SPACE] 模擬吃到食物並播放音效！")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Yummy!")
                play_eat_sound() # 這是本週重點

    screen.fill(BG_COLOR)
    
    # 畫個簡單的蛇和食物示意
    pygame.draw.rect(screen, FOOD_RED, (food_x, food_y, 40, 40), border_radius=10)
    pygame.draw.rect(screen, NEON_GREEN, (400, 300, 40, 40), border_radius=4)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
