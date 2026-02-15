# Week 01 | 隨堂測驗 (Quiz)：Hello Pygame！

> **測驗目標**：檢測學生是否理解遊戲引擎的基本初始化與「遊戲迴圈」的概念。
> **測驗時間**：10 分鐘

---

## 🟢 第一部分：是非題 (True/False)

1.  (  ) `pygame.init()` 是啟動 Pygame 引擎的開關，必須放在所有 Pygame 指令之前。
2.  (  ) 遊戲視窗之所以不會消失，是因為我們寫了一個無限迴圈 (Game Loop) 把程式困住。
3.  (  ) 在 Pygame 中，座標 (0, 0) 是在視窗的正中央。
4.  (  ) `pygame.display.flip()` 的功能是將畫好的內容「翻轉」到螢幕上，讓玩家看見。
5.  (  ) 如果沒有寫 `pygame.event.get()`，視窗可能會呈現「沒有回應」的卡死狀態。

---

## 🟡 第二部分：程式碼填空 (Code Completion)

請填入正確的關鍵字，讓最簡單的遊戲架構能跑起來。

```python
import pygame

# 1. 引擎初始化
pygame.______

screen = pygame.display.set_mode((800, 600))
running = True

# 2. 進入核心迴圈
while ______:
    for event in pygame.event.get():
        if event.type == pygame.______:
            running = False
            
    # 3. 畫面更新
    pygame.display.______
    
pygame.quit()
```

---

## 🔴 第三部分：腦力激盪 (Logic Challenge)

1.  **時間結界**：如果我們把 `while True` 字樣刪掉，只留下裡面的程式碼，執行後會發生什麼事？
    *   答案：____________________

2.  **色彩密碼**：在 RGB 系統中，`(255, 255, 255)` 代表什麼顏色？
    *   答案：____________________

---

## 💡 解答與解析

### 是非題
1. **True**
2. **True**
3. **False** (左上角)
4. **True**
5. **True** (必須處理 OS 的事件訊號)

### 程式碼填空
1. `init()`
2. `running` (或 `True`)
3. `QUIT`
4. `flip()`

### 腦力激盪
1. 視窗會閃一下就關閉（程式執行完畢）。
2. 白色。
