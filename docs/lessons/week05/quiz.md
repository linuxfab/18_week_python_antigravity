# Week 05 | 隨堂測驗 (Quiz)：操控與邊界穿越

> **測驗目標**：檢測對 if-elif 邏輯、鍵盤事件處理與穿越邊界 (Pac-Man) 的掌握。
> **測驗時間**：10 分鐘

---

## 🟢 第一部分：是非題 (True/False)

1.  (  ) `if` 與 `elif` 的區別在於：如果 `if` 條件成立，後面的 `elif` 就不會再被執行。
2.  (  ) 貪食蛇在移動時，可以同時讓 `speed_x` 與 `speed_y` 都有數值（斜向移動）。
3.  (  ) 在 Pygame 中，按下鍵盤的事件類型是 `pygame.KEYUP`。
4.  (  ) 「穿越邊界」的邏輯是當 x 超過邊界時，將 x 重新設定到另一側的起點。
5.  (  ) 修飾鍵（如 Shift、Ctrl）必須使用 `pygame.key.get_mods()` 來偵測。

---

## 🟡 第二部分：程式碼填空 (Code Completion)

```python
for event in pygame.event.get():
    # 1. 偵測按鍵被按下的事件
    if event.type == pygame.______:
        # 2. 如果按下的是左鍵
        if event.key == pygame.K_LEFT:
            speed_x = -5
            speed_y = ______  # 確保不會斜著跑
            
# 3. 穿越邊界 (寬度 800)
if player_x > 800:
    player_x = ______
```

---

## 🔴 第三部分：腦力激盪 (Logic Challenge)

1.  **邏輯陷阱**：為什麼我們不用四個 `if` 來寫上下左右，而要用 `if-elif`？
    *   答案：____________________

2.  **操控性**：如果我們把 `pygame.KEYDOWN` 改成在迴圈裡用 `pygame.key.get_pressed()`，操控方塊的感覺會有什麼不同？
    *   答案：____________________

---

## 💡 解答與解析

### 是非題
1. **True**
2. **False** (傳統貪食蛇只能四向移動)
3. **False** (是 KEYDOWN)
4. **True**
5. **True**

### 程式碼填空
1. `KEYDOWN`
2. `0`
3. `0` (或略小於 0 的位置)

### 腦力激盪
1. 為了效率，且避免同時按下相反方向時產生衝突（或原地抽搐）。
2. `KEYDOWN` 適合「改變狀態」（按一下轉彎）；`get_pressed()` 適合「按住不放」（一直加速）。
