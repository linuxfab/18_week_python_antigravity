# Week 11 | 隨堂測驗 (Quiz)：死亡機制與狀態管理

> **測驗目標**：檢測學生對自我碰撞檢測、遊戲狀態切換及重置函數的理解。
> **測驗時間**：10 分鐘

---

## 🟢 第一部分：是非題 (True/False)

1.  (  ) 在 Python 中，判斷一個元素是否在清單裡，可以使用 `in` 關鍵字。
2.  (  ) 咬到自己身體的條件是：蛇頭的新座標 `new_head` 已經出現在 `snake_body` 清單中。
3.  (  ) 為了讓遊戲重來，最好的方式是讓 Python 程式直接崩潰並關閉視窗。
4.  (  ) 狀態管理 (State Management) 可以幫助我們分開處理「遊戲進行中」與「遊戲結束」的畫面。
5.  (  ) `reset_game()` 函數應該包含將分數歸零、重設蛇的位置與長度等初始化代碼。

---

## 🟡 第二部分：程式碼填空 (Code Completion)

請根據邏輯填入正確的代碼片段。

```python
# 1. 判斷自我碰撞
if new_head ______ snake_body:
    game_over = ______  # 進入死亡狀態

# 2. 處理 Game Over 模式下的事件
if game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # 偵測按下空白鍵重來
            if event.key == pygame.______:
                reset_game()

# 3. 定義重置函數
def reset_game():
    ______ game_over, score, snake_body
    game_over = False
    score = 0
    snake_body = [(400, 300)]
```

---

## 🔴 第三部分：腦力激盪 (Logic Challenge)

1.  **狀態機應用**：除了 `PLAY` 和 `GAME_OVER`，你覺得一個完整的遊戲還需要哪種狀態？
    *   答案：____________________ (例如：MENU 開頭選單、PAUSE 暫停、LEVEL_UP 升級等)

2.  **死亡特效**：如果要讓玩家感到震撼，你覺得「死掉的那一瞬間」除了顯示文字，還可以加入什麼視覺或操作上的變化？
    *   答案：____________________ (例如：畫面變黑白、蛇身爆炸噴散、背景顏色閃動等)

---

## 💡 解答與解析

### 是非題
1. **True**
2. **True**
3. **False** (這種設計非常不優雅，會讓玩家失去興致)
4. **True**
5. **True**

### 程式碼填空
1. `in`, `True`
2. `K_SPACE`
3. `global` (因為要修改全域變數)

### 腦力激盪
1. 開放性建議：START_MENU (開始選單)、PAUSE (暫停)、SETTINGS (設定)。
2. 開放性建議：背景閃紅光、把 FPS 瞬間降到極低來強調衝擊感、播放死亡慘叫聲。
