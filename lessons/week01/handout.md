# 第 01 週 | Vibe Coding 體驗：Hello Pygame

> **給老師的備課筆記 (Lesson Notes)**：
> 本週重點在於「**視覺回饋**」與「**建立信心**」。不要過度糾結於 Python 的變數型別或詳細語法，而是讓學生理解「**因為我寫了這行程式，所以視窗出現了**」的因果關係。

---

## 🎯 本週教學目標 (Learning Objectives)

1.  **環境驗證**：確認學生能透過 `uv` 建置專案並執行 Python。
2.  **理解結構**：掌握遊戲開發的三大支柱 —— **Setup (設定)**、**Game Loop (迴圈)**、**Event (事件)**。
3.  **Vibe Coding**：體驗透過程式碼控制視覺（顏色、視窗）的成就感。

---

## 📊 教學投影片大綱 (Slides Outline)

### Slide 1: Welcome to Vibe Coding (喚醒你的遊戲靈魂)
*   **核心提問**：為什麼我們要學程式？
*   **內容**：
    *   拒絕枯燥：我們不從 `print("Hello World")` 開始，我們直接開啟一個世界。
    *   專案目標：18 週後，你將擁有一款自己打造、有聲光效果的「貪食蛇」。
*   **視覺**：展示最終成品的截圖或 GIF。

### Slide 2: 認識你的武器庫 (Tools of the Trade)
*   **Python**：我們的魔法咒語。
*   **Pygame-ce**：最強大的 2D 遊戲引擎 (Community Edition)。
*   **Antigravity IDE**：你的 AI 副駕駛。
*   **指令時間**：
    ```bash
    uv init
    uv add pygame-ce
    ```

### Slide 3: 遊戲的解剖學 (The Anatomy of a Game)
*   **比喻**：遊戲就像一個永遠不會停下來的翻頁動畫書。
    1.  **Setup (大腦)**：設定視窗大小、載入資源。
    2.  **Game Loop (心臟)**：`while True`，只要活著就不斷跳動。
    3.  **Event (感官)**：偵測鍵盤按下、滑鼠移動。
    4.  **Render (臉)**：`flip()`，將畫好的畫面以此呈現。

### Slide 4: 第 01 號任務 (Mission 01)
*   **目標**：讓一個黑色的視窗出現在螢幕上，並且能由你控制關閉。
*   **Vibe Check**：試試看按下空白鍵，能不能改變世界的顏色？

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. 為什麼需要 `while True`？
新手常見疑問：「為什麼遊戲視窗一閃就消失了？」
*   **解釋**：程式碼預設是「由上而下」執行完就結束。
*   **解法**：遊戲需要一直存在，所以我們用一個**無限迴圈 (Infinite Loop)** 把它「困住」，直到玩家說停為止。

### 2. 什麼是 `pygame.event.get()`？
新手常見疑問：「為什麼視窗卡住轉圈圈 (Not Responding)？」
*   **解釋**：作業系統 (Windows) 會一直問視窗：「你還活著嗎？」，如果程式忙著跑迴圈而不回應作業系統的訊號 (Events)，就會被判定為當機。
*   **解法**：必須在迴圈每一幀都檢查並處理事件 (Pump events)。

### 3. 鍵盤控制邏輯 (Keyboard Logic)
在 `demo.py` 中，我們示範了最基礎的控制：
```python
if event.key == pygame.K_SPACE:
    # 切換顏色的邏輯
```
這雖然還沒讓蛇移動，但已經建立了「**輸入 (Input) -> 處理 (Process) -> 輸出 (Output)**」的核心邏輯。

---

## 🏋️‍♂️ 動手試試看 (Hands-on Exercises)

### 🟢 基礎題 (Basic)
1.  **成功執行**：下載並執行 `demo.py`，確認視窗出現。
2.  **安全退出**：試著按 ESC 鍵與視窗右上角的 X，確認都能關閉程式。

### 🟡 進階題 (Advanced Vibe)
1.  **色彩大師**：
    *   打開 [Google Color Picker](https://g.co/kgs/colorpicker)，挑選一個你喜歡的顏色 (例如 `Neon Pink`)。
    *   修改程式碼中的 `pixel_color` 變數，讓按下空白鍵時變成你的專屬色。
2.  **鍵盤駭客**：
    *   目前程式只對 `UP` (上) 有反應。
    *   **挑戰**：加入 `K_LEFT`, `K_RIGHT` 的偵測，並讓它印出不同的訊息 (例如 "Turning Left!")。

---

## 📚 參考資源 (References)
*   [Pygame-ce 官方文檔](https://pyga.me/docs/)
*   [Python 顏色代碼表 (RGB)](https://www.rapidtables.com/web/color/RGB_Color.html)
