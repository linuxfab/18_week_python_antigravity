# 第 05 週 | 鍵盤車神：賦予蛇靈魂

> **給教練的戰術板 (Coach's Corner)**：
> 從這週開始，學生不再是 **觀眾**，而是 **駕駛員**。
> `pygame.KEYDOWN` 是一個「瞬間動作」的偵測 (Click)，這跟「按住不放」 (Hold) 不一樣。
> 學生最容易犯的錯是把 X 軸與 Y 軸搞混 (按上卻往右跑)，這時候不要直接給答案，請他們當個偵探，用 `print` 把變數印出來抓兇手。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **邏輯分流 (If-Elif)**：理解「人生有很多條路，但你只能選一條走」。
2.  **物理慣性 (Inertia)**：一旦改變了速度，物體就會一直動，直到下一次改變。這就是牛頓第一運動定律。
3.  **穿越邊界 (Warp Drive)**：像 Pac-Man (小精靈) 一樣穿越邊界，這比「撞牆反彈」更有外太空的感覺。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 誰是老大？ (Taking Control)
*   **回顧**：上週方塊像喝醉一樣亂撞，今天我們要馴服它。
*   **武器**：鍵盤 (Keyboard)。
*   **戰術**：監聽 `KEYDOWN` 事件 -> 修改 `speed` 向量。
*   **Vibe**：這就是 **Drive-by-Wire (線傳飛控)**。

### Slide 2: If-Elif-Else 的決策樹 (The Decision Tree)
*   **情境**：你開車到十字路口。
    *   **If** 紅燈：踩煞車。
    *   **Elif** 綠燈：油門催下去。
    *   **Elif** 警察攔檢：靠邊停 (並祈禱你沒超速)。
    *   **Else** (其他情況)：保持現狀。
*   **重點**：電腦只會執行其中一條路，因為這些情況是 **互斥 (Exclusive)** 的。

### Slide 3: 貪食蛇移動學 (Snake Physics)
*   **關鍵**：貪食蛇不會「煞車」。一旦按下「右」，它就會永遠向右衝，直到你命令它轉彎。
*   **程式美學**：
    ```python
    if event.key == K_RIGHT:
        speed_x = 5
        speed_y = 0  # 重點！要先把 Y 軸歸零，不然蛇會變成斜著飄移 (Drift)
    ```

### Slide 4: Vibe Coding - 傳送門 (Teleport)
*   **問題**：跑出畫面外就迷路了。
*   **解法**：如果 `x > 800` (太右邊)，就把 `x` 設為 `0` (瞬間傳送回左邊)。
*   **效果**：這是一個無限循環的環形宇宙 (Toroidal World)。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `elif` 的效率 (Efficiency)
試試看把所有 `elif` 都改成 `if` 會發生什麼事？
如果在同一幀 (1/60秒) 同時按下「上」與「下」：
*   **使用 if**：電腦會先執行「上」，再執行「下」，結果互相抵消，蛇原地抽搐。
*   **使用 elif**：電腦一旦確認了「上」，後面的一概不看。這就是 **決策的果斷**。

### 2. 禁止斜向移動 (No Diagonal)
在很多 RPG 遊戲中，同時按「右」與「下」可以往右下移動。
但在貪食蛇遊戲中，這是 **違法** 的。
所以在 `demo.py` 中，當我設定 `speed_x = 5` 時，我強制 `speed_y = 0`。
這叫做 **Mutual Exclusion (互斥鎖)** 的概念。

### 3. Turbo 模式 (Shift Key) - 隱藏大招
```python
keys = pygame.key.get_pressed()
if keys[pygame.K_LSHIFT]:
    speed_x *= 2  # 兩倍速！
```
這是進階技巧！利用 `get_pressed()` 檢查修飾鍵。
加上這行，你的貪食蛇就有了 **NOS 氮氣加速** 功能。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Daily Life Logic)
1.  **紅綠燈模擬器**：寫一個簡單的 Python 腳本 (不是 Pygame)，讓使用者輸入顏色：
    *   `Input: Red` -> Print "Stop"
    *   `Input: Green` -> Print "Go"
    *   `Input: Yellow` -> Print "Faster!" (誤...是 "Slow Down")
2.  **極限測試**：修改 `demo.py`，把速度改成 `20`，試試看你能多快控制方塊轉彎而不撞牆？這是在訓練你的動態視力。

### 🟡 進階題 (Advanced Driver)
1.  **倒退檔防呆 (Reverse Gear Safety)**：
    *   目前的程式允許你在「向右」跑的時候直接按下「左」。
    *   但在貪食蛇世界，這是不允許的 (蛇不能吃自己的脖子)。
    *   **挑戰**：加入一個 `if` 判斷，如果目前的 `speed_x > 0` (向右)，則忽略 `K_LEFT` 的按鍵。
2.  **氮氣加速 (Nitrous Boost)**：
    *   目前只有 Shift 可以加速。試著把「空白鍵」改成超級加速鍵，按下去的一瞬間速度變成 **50**，體驗什麼叫 **Warp Speed**。

---

## 📚 寶藏連結 (Reference)
*   [Pygame Key Codes](https://www.pygame.org/docs/ref/key.html) (所有按鍵代碼表)
*   [Logic Gates Simulator](https://logic.ly/demo) (視覺化邏輯閘，像玩積木一樣學邏輯)
