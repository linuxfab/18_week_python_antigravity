# 第 03 週 | 遊戲迴圈 (Game Loop) 的心跳

> **給老師的備課筆記 (Lesson Notes)**：
> 這是整個遊戲開發中最關鍵的一課。學生要學會控制時間，而不只是寫靜態程式。`while True` 是一個很容易讓初學者困惑的概念（為什麼要一直跑？），建議用「心跳」的比喻：遊戲是活著的生物，它每一秒鐘都要呼吸 60 次。

---

## 🎯 本週教學目標 (Learning Objectives)

1.  **FPS (Frames Per Second)**：理解為什麼要限制幀率？(穩定性 > 速度)。
2.  **Clock.tick()**：學會使用 Pygame 的節拍器。
3.  **遊戲狀態更新 (State Update)**：將「邏輯計算」與「畫面繪製」分開思考。

---

## 📊 教學投影片大綱 (Slides Outline)

### Slide 1: 遊戲的心臟 (The Heartbeat)
*   **提問**：電影每秒播放幾張圖片？(約 24 張)。那遊戲呢？(通常 60 張)。
*   **概念**：FPS = 每一秒鐘跑這段 `while` 迴圈多少次。
*   **如果不控制 FPS 會怎樣？**
    *   在超級電腦上，蛇跑太快撞牆。
    *   在舊電腦上，蛇跑太慢。
    *   這不公平！

### Slide 2: Pygame 的節拍器 (`pygame.time.Clock`)
*   **工具**：`clock = pygame.time.Clock()`
*   **關鍵指令**：`clock.tick(60)`
*   **魔法**：這行程式碼會叫 Pygame 說：「嘿，如果這圈跑太快，請你休息一下 (Sleep)，直到滿 1/60 秒再繼續。」

### Slide 3: 遊戲迴圈的三部曲 (The Holy Trinity)
1.  **Event (聽)**：有人按鍵盤嗎？視窗被關掉了嗎？
2.  **Update (想)**：根據輸入，計算新的蛇頭位置、分數。
3.  **Draw (畫)**：把計算結果畫在白色畫布上，最後翻開給玩家看。

### Slide 4: Vibe Coding - 讓它活起來
*   **心跳視覺化**：我們利用數學函數 `sin` (正弦波) 來模擬呼吸。
*   **觀察**：注意視窗左上角的 FPS 數字，它應該穩定在 60 附近。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `import math` 與 `sin` 函數
這雖然是數學課，但在這裡我們用它來做特效。`sin` 函數的值會永遠在 -1 到 1 之間平滑擺盪，這非常適合用來做「變大、變小」的持續動畫，而不需要寫複雜的 `if` 判斷 (如果太大就變小，如果太小就變大)。

### 2. `pygame.time.Clock()`
這個物件是全域唯一的，我們通常在遊戲一開始就建立它。
*   `tick(FPS)`：這是**阻塞式 (Blocking)** 的函數，意味著它會真的暫停程式執行。
*   `get_fps()`：這是**非阻塞式** 的函數，只是單純告訴你目前的效能。

### 3. 事件處理的最佳實踐
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```
這是每一款 Pygame 遊戲都必須具備的標準起手式。如果沒有這段，你的視窗會關不掉，只能強制結束工作管理員。

---

## 🏋️‍♂️ 動手試試看 (Hands-on Exercises)

### 🟢 基礎題 (Basic)
1.  **改變心跳速度**：嘗試修改 `FPS` 變數 (例如改成 10 或 120)，觀察心跳變快或變慢，以及畫面的流暢度差異。
2.  **改變心跳顏色**：讓心臟變成你喜歡的顏色。

### 🟡 進階題 (Rhythm Master)
1.  **心律不整**：試著讓 `FPS` 變成一個隨機數 (使用 `random.randint`)，體驗不穩定的遊戲迴圈是什麼感覺。
2.  **雙心跳**：在畫面上創造第二個心臟，但讓它的跳動節奏跟第一個相反 (提示：使用 `math.cos` 或是在 `sin` 裡面加一個相位差)。

---

## 📚 參考資源 (References)
*   [Pygame Time 文檔](https://pyga.me/docs/ref/time.html)
*   [Visualizing Sine Waves](https://www.desmos.com/calculator) (推薦用圖形計算機展示 sin 波)
