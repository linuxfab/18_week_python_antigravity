# 第 01 週 | Vibe Coding 覺醒：Hello Pygame！

> **給教練的戰術板 (Coach's Corner)**：
> 這週不是要教「程式語法」，而是要點燃「創造的神火」。
> 別管什麼變數型別了，重點是讓學生感受到 **「因為我敲了鍵盤，螢幕就聽話了」** 的絕對掌控感。
> 我們要的是 **視覺回饋 (Visual Feedback)**，我們要的是 **信心 (Confidence)**。
> 讓他們覺得自己像個駭客，而不只是個學生。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **環境解鎖**：確認 `uv` 運作正常，Python 蓄勢待發。
2.  **掌握核心**：參透遊戲靈魂三元素 —— **Setup (佈局)**、**Game Loop (心跳)**、**Event (感官)**。
3.  **Vibe Check**：第一次用程式碼控制視窗顏色，感受那種「我就是神」的快感。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: Welcome to Vibe Coding (喚醒你的遊戲靈魂)
*   **靈魂拷問**：為什麼要學程式？為了考試？還是為了創造世界？
*   **拒絕無聊**：`print("Hello World")` 這種老掉牙的東西我們先放一邊。我們要直接在這個漆黑的螢幕上，開天闢地。
*   **終極願景**：18 週後，你將擁有一款獨一無二、自帶 BGM 的「貪食蛇」大作。

### Slide 2: 你的武器庫 (The Arsenal)
*   **Python**：你的魔法咒語書。
*   **Pygame-ce**：最強大的 2D 遊戲引擎 (Community Edition) —— 這是你的畫布。
*   **Antigravity IDE**：你的 AI 副駕駛 (Copilot)，隨時準備救援。
*   **戰鬥指令**：
    ```bash
    uv init           # 召喚專案
    uv add pygame-ce  # 裝備引擎
    ```

### Slide 3: 遊戲的解剖學 (Anatomy of a Game)
*   **神比喻**：遊戲就像一本永遠翻不完的動畫書。
    1.  **Setup (大腦)**：設定視窗多大？載入什麼圖片？這是遊戲的「出生設定」。
    2.  **Game Loop (心臟)**：`while True` —— 只要心臟還在跳 (True)，遊戲就活著。
    3.  **Event (感官)**：按了空白鍵？動了滑鼠？遊戲必須「感覺」到玩家的操作。
    4.  **Render (臉面)**：`flip()` —— 把畫好的下一頁翻出來給你看。

### Slide 4: Mission 01 - 第一次接觸
*   **任務**：召喚一個黑色視窗，證明你已經控制了電腦。
*   **Vibe Check**：試試看按下 **空白鍵**，能不能讓整個世界變色？

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `while True`：為什麼要無限迴圈？
新手常問：「為什麼視窗出來一下就不見了？」
*   **因為程式跑完了啊！** 程式預設是由上往下跑，跑完就下班。
*   **Vibe Solution**：我們用 `while True` 設下一個「時間結界」，把程式困在裡面，直到我們允許它離開 (玩家按關閉)。這就是遊戲的**命**。

### 2. `pygame.event.get()`：甚至連視窗都需要關愛
新手常問：「為什麼視窗卡死轉圈圈 (Not Responding)？」
*   **因為它自閉了。** Windows 作業系統會一直問視窗：「欸你還活著嗎？」，如果程式只顧著跑迴圈不理人，就會被當作當機。
*   **Vibe Solution**：每一幀 (Frame) `pygame.event.get()` 都要出來「社交」一下，回應作業系統的確認，並檢查有沒有人按鍵盤。

### 3. 鍵盤邏輯：輸入 -> 輸出
在 `demo.py` 裡，我們寫下了第一行互動邏輯：
```python
if event.key == pygame.K_SPACE:
    # 變色吧！世界！
```
這就是遊戲設計的原子模型：**Input (按鍵) -> Process (判斷) -> Output (變色)**。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Basic Vibe)
1.  **成功啟動**：執行 `demo.py`，看到視窗跳出來的那一刻，深吸一口氣 —— 你做到了。
2.  **優雅退場**：試著按 `ESC` 鍵或視窗右上角的 `X`，確認你能優雅地結束程式，而不是讓它當掉。

### 🟡 進階題 (Hacker Vibe)
1.  **色彩大師 (Color Master)**：
    *   打開 [Google Color Picker](https://g.co/kgs/colorpicker)，挑一個最騷包的顏色 (例如 `Neon Pink` #FF6EC7)。
    *   修改程式碼中的 `pixel_color`，讓按下空白鍵時，視窗炸出你的專屬色。
2.  **鍵盤駭客 (Keyboard Hacker)**：
    *   目前只有 `UP` 鍵有反應？太遜了。
    *   **挑戰**：加入 `K_LEFT`, `K_RIGHT` 的偵測，並讓它印出 "Turning Left!" 或 "Drifting Right!"。讓終端機 (Terminal) 變身你的儀表板。

---

## 📚 寶藏連結 (References)
*   [Pygame-ce 官方聖經](https://pyga.me/docs/)
*   [RGB 顏色代碼表](https://www.rapidtables.com/web/color/RGB_Color.html) —— 設計師的調色盤
