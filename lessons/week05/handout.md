# 第 05 週 | 鍵盤車神：賦予蛇靈魂

> **給老師的備課筆記 (Lesson Notes)**：
> 從本週開始，學生不再是**觀眾**，而是**駕駛員**。
> `pygame.KEYDOWN` 是一個「瞬間動作」的偵測，這跟「按住不放」是不一樣的。
> 在這個階段，學生最容易犯的錯是把 X 軸與 Y 軸搞混 (按上卻往右跑)，請利用 `print` 指令幫助他們除錯。

---

## 🎯 本週教學目標 (Learning Objectives)

1.  **If-Elif 結構**：理解「多選一」的邏輯 (這條路走了，另一條路就不會走)。
2.  **連續移動 (Continuous Movement)**：一旦改變了速度，物體就會一直動，直到下一次改變。
3.  **邊界處理 (Wrapping)**：像小精靈 (Pac-Man) 一樣穿越邊界，這比「撞牆反彈」更有趣且適合貪食蛇。

---

## 📊 教學投影片大綱 (Slides Outline)

### Slide 1: 誰是老大？ (Taking Control)
*   **提問**：上週方塊亂跑，今天我們要馴服它。
*   **工具**：鍵盤 (Keyboard)。
*   **原理**：監聽 `KEYDOWN` 事件 -> 修改 `speed` 變數。

### Slide 2: If-Elif-Else 的決策樹 (The Decision Tree)
*   **情境**：你走到十字路口。
    *   **If** 紅燈：停下來。
    *   **Elif** 綠燈：直走。
    *   **Elif** 警察攔檢：靠邊停。
    *   **Else** (其他情況)：保持警戒。
*   **重點**：電腦只會執行其中一條路，因為這些情況是互斥的。

### Slide 3: 貪食蛇移動學 (Snake Physics)
*   **關鍵**：貪食蛇不會「煞車」。一旦按下「右」，它就會永遠向右，直到你叫它轉彎。
*   **程式寫法**：
    ```python
    if event.key == K_RIGHT:
        speed_x = 5
        speed_y = 0  # 重要！要先把 Y 軸歸零，不然會變成斜著跑 (5, 5)
    ```

### Slide 4: Vibe Coding - 小精靈傳送門 (Teleport)
*   **問題**：跑出畫面外就看不到了。
*   **解法**：如果 `x > 800` (太右邊)，就把 `x` 設為 `0` (瞬間回到左邊)。
*   **效果**：無限循環的宇宙。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `elif` 的重要性
試試看把所有 `elif` 都改成 `if` 會發生什麼事？
如果在同一幀同時按下「上」與「下」：
*   **使用 if**：電腦會先執行「上」，再執行「下」，結果互相抵消，原地不動。
*   **使用 elif**：電腦一旦確認了「上」，就會忽略後面的檢查，程式效率更高。

### 2. 斜向移動 (Diagonal Movement)
在很多 RPG 遊戲中，同時按「右」與「下」可以往右下移動。
但在貪食蛇遊戲中，我們**不希望**發生這件事。
所以在 `demo.py` 中，當我設定 `speed_x = 5` 時，我強制 `speed_y = 0`。這就是著名的「單一軸向移動」。

### 3. Turbo 模式 (Shift Key)
```python
is_turbo = pygame.key.get_mods() & pygame.KMOD_SHIFT
```
這是進階技巧！`get_mods()` 會回傳目前所有被按住的修飾鍵 (Ctrl, Shift, Alt)。利用這個技巧，我們可以做出「衝刺 (Sprint)」功能。

---

## 🏋️‍♂️ 動手試試看 (Hands-on Exercises)

### 🟢 基礎題 (Daily Life Logic)
1.  **紅綠燈**：寫一個簡單的 Python 腳本 (不是 Pygame)，讓使用者輸入顏色：
    *   `Input: Red` -> Print "Stop"
    *   `Input: Green` -> Print "Go"
    *   `Input: Yellow` -> Print "Faster!" (誤)
2.  **四向測試**：修改 `demo.py`，把速度改成 20，試試看你能多快控制方塊轉彎而不撞牆？

### 🟡 進階題 (Advanced Driver)
1.  **倒退檔 (Reverse Gear)**：
    *   目前的程式允許你在「向右」跑的時候直接按下「左」。
    *   但在真正的貪食蛇遊戲中，這是不允許的 (蛇不能自己吃自己脖子)。
    *   **挑戰**：加入一個 `if` 判斷，如果目前的 `speed_x` 是正數 (向右)，則忽略 `K_LEFT` 的按鍵。
2.  **加速器**：
    *   目前只有 Shift 可以加速。試著把「空白鍵」改成「Nitrous Boost」，按下去的一瞬間速度變成 50，持續 0.5 秒後恢復正常。(提示：需要用到 `time.time()` 來計時)。

---

## 📚 參考資源 (References)
*   [Pygame Key Codes](https://www.pygame.org/docs/ref/key.html) (所有按鍵的代碼表)
*   [Logic Gates](https://logic.ly/demo) (視覺化邏輯閘，幫助理解 if/else)
