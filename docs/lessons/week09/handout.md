# 第 09 週 | 碰撞檢測：First Blood (首殺)

> **給教練的戰術板 (Coach's Corner)**：
> 這是遊戲從「動畫」轉向「模擬」的關鍵。
> 之前蛇只是在練習折返跑，現在它有了 **獵物**。
> 國中生最常搞混的是：為什麼座標要 **完全相等** 才算吃到？
> 因為我們是在 **Grid System (網格系統)** 上移動。
> 如果你的蛇移動速度是 3.5 像素，它們可能永遠不會「相遇」，那就要改用高深的 `AABB` 碰撞演算法了。但我們今天保持簡單。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **碰撞邏輯 (Collision Detection)**：電腦如何判斷兩個物體「撞在一起」？
2.  **成長機制 (Growth Mechanism)**：理解 List 的 `pop(0)` 與 `append()` 組合技。
3.  **條件旗標 (Flag)**：使用 `bool` 變數來傳遞訊號。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 碰撞箱 (Hitbox) 的奧義
*   **比喻**：想像特戰英豪 (Valorant) 的角色外面都有一層看不見的盒子。
*   **判定**：當蛇頭的盒子 (Hitbox) 與食物的盒子 **重疊** 時，就是「命中」。
*   **程式碼**：`if head == food:`
    *   在 Python 裡，List/Tuple 的比較是 **Deep Comparison** (比內容)，所以 `(40, 40) == (40, 40)` 是成立的。

### Slide 2: 貪食蛇的生長痛 (Growing Pains)
*   **平時**：火車每往前開一節，車尾就拿掉一節。長度保持不變。
*   **吃到食物**：火車往前開一節，但我們先 **不叫車尾的人走開**。
*   **結果**：火車變長了！Magic!
*   **程式翻譯**：
    *   `pop(0)` = 叫車尾的人滾蛋。
    *   `should_grow = True` = 這次暫時不要滾蛋。

### Slide 3: Vibe Coding - 打擊感 (Juiciness)
*   讓遊戲變好玩的祕訣在於 **反饋 (Feedback)**。
*   如果吃到食物靜悄悄的，那跟寫作業有什麼兩樣？
*   **螢幕閃爍**：吃到食物的瞬間，背景顏色變白 0.1 秒，會有「閃光彈」的爽快感。
*   **吃掉特效**：
    ```python
    if flash_timer > 0:
        screen.fill((255, 255, 255)) # 亮瞎你的眼
        flash_timer -= 1
    ```

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. 座標重疊檢查
```python
if head_x == food_x and head_y == food_y:
    score += 1
    spawn_food() 
```
這段程式碼必須寫在 **移動邏輯之後**，**繪圖邏輯之前**。
這是 **Game Loop** 的黃金順序。

### 2. 生食防呆 (Spawn Safety)
```python
while True:
    # 隨機選座標...
    if (food_x, food_y) not in snake_body:
        break # 只有當食物不在蛇肚子裡，才准離開迴圈
```
這叫 **防呆設計 (Foolproof)**。
如果沒有這段，玩家會覺得遊戲有 Bug，怎麼食物一出來就被吃掉了？

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Growth Spurt)
1.  **大胃王挑戰**：試著修改程式，讓蛇每吃一顆食物就一次長大 **3 節**。
    *   提示：你需要一個計數器 `growth_pending = 3`。
2.  **音效腦補**：雖然还没教音效，但試著用 `print("Yummy!")` 來模擬音效。

### 🟡 進階題 (Loot Box)
1.  **黃金蘋果 (Golden Apple)**：
    *   改寫 `spawn_food`，讓食物也有 10% 機率生成「黃金蘋果」(也就是 `YELLOW` 色的)。
    *   吃到黃金蘋果，分數 `+5`。
2.  **腐爛機制 (Rotting)**：
    *   給食物一個 `timer`，如果在 5 秒內沒吃到，它就會消失並重新生成在別的地方。
    *   這會逼迫玩家 **主動出擊**，而不是龜縮。

---

## 📚 寶藏連結 (Reference)
*   [Pygame Rect Collision](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect) (如果你想做跑酷遊戲，就要看這個)
*   [Game Feel: The Secret Sauce](https://www.youtube.com/watch?v=216_5nu7a8o) (為什麼馬力歐這麼好玩？這影片解釋了一切)
