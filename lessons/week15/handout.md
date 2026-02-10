# 第 15 週 | 難度曲線：心流體驗 (Flow)

> **給教練的戰術板 (Coach's Corner)**：
> 這一週我們要探討「遊戲設計」中最神祕的部分：**平衡 (Balance)**。
> 太簡單會無聊 (Boredom)，太難會焦慮 (Anxiety)。
> 身為遊戲設計師 (也就是你)，你要負責調配這個配方。
> 我們要把冷冰冰的「程式變數」轉換成玩家的「心理壓力」。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **動態難度 (Dynamic Difficulty)**：讓遊戲隨著玩家變強而變難。
2.  **FPS 控制**：除了用 `time.sleep`，我們還能怎麼精準控制節奏？
3.  **心流 (Flow State)**：設計出讓人「停不下來」、「再一次就好」的毒性節奏。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 心流通道 (The Flow Channel)
*   **Mhaly Csikszentmihalyi** (別試著念他的名字) 提出的理論。
*   **左岸**：技能太強，挑戰太弱 -> **無聊**，玩家會睡著。
*   **右岸**：挑戰太強，技能太弱 -> **挫折**，玩家會摔鍵盤 (Rage Quit)。
*   **中間**：挑戰剛好大於你的能力一點點 -> **心流**，時間消失，人劍合一。

### Slide 2: 難度公式設計
我們可以用數學來控制這條河流：
1.  **線性增長 (Linear)**：
    *   `FPS = 初始速度 + (分數 / 5)`
    *   每吃 5 顆，速度 +1。簡單粗暴。
2.  **對數增長 (Logarithmic)**：
    *   一開始變快很快，後面變快很慢。適合競技遊戲。
3.  **階梯式 (Stepped)**：
    *   每 10 分，升級一次 (Level Up)，速度暴增，然後背景變色。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. FPS 封頂 (Capping)
```python
current_speed = BASE_FPS + (score // 5)
if current_speed > MAX_FPS:
    current_speed = MAX_FPS
clock.tick(current_speed)
```
*   **重要**：一定要設 **上限 (Cap)**。
*   如果不設上限，當分數學到 1000 分時，你的蛇會變成量子型態 (瞬間移動)，那是程式 Bug，不是遊戲挑戰。

### 2. 視覺上的速度感
*   純粹加 FPS 玩家可能無感。我們要用 **視覺詐欺**。
*   **殘影 (Trail)**：當速度 > 20 時，啟動殘影繪製。
*   **鏡頭晃動**：速度越快，撞牆時的晃動越劇烈。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Level Up)
1.  **速度階梯**：
    *   Level 1 (0-10分): FPS 10
    *   Level 2 (11-20分): FPS 15
    *   Level 3 (21+分): FPS 20
    *   請用 `if/elif` 實現這個邏輯，並在螢幕上顯示 "LEVEL 2"。
2.  **縮小視野 (Fog of War)**：
    *   分數越高，畫面四個角落的黑色遮罩越大，只剩下中間看得到。增加壓迫感。

### 🟡 進階題 (Boss Fight Mode)
1.  **Boss 戰節奏**：
    *   每當分數達到 10 的倍數 (10, 20, 30...)。
    *   **背景音樂切換** 成快節奏的戰鬥曲。
    *   **背景變紅**。
    *   **FPS 瞬間 x 1.5 倍**。
    *   持續 10 秒後恢復正常。這種「間歇性高潮」是現代遊戲設計的精髓。

---

## 📚 寶藏連結 (Reference)
*   [The Art of Game Design](https://www.amazon.com/Art-Game-Design-Book-Lenses/dp/0123694965) (推薦給想認真做遊戲的人看這本書)
*   [Flow in Games Explained](https://www.youtube.com/watch?v=8hP9D6kGNvI) (影片版的心流解說)
