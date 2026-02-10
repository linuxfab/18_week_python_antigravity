# 第 08 週 | 混沌理論：食物的誕生

> **給教練的戰術板 (Coach's Corner)**：
> 這是學生第一次接觸 **「不確定性 (Uncertainty)」**。
> 在此之前的每一個變數都是我們算計好的，但 `random` 讓電腦有了自己的意志。
> 請特別花時間解釋 **Grid Alignment (網格對齊)** 的數學公式，這是很多初學者的痛點（食物出現在兩個格子的中間，導致怎麼撞都吃不到，這是最讓人挫折的 Bug）。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **隨機數 (Randomness)**：使用 `import random` 擲骰子。
2.  **網格鎖定 (Snap to Grid)**：理解 `randint(0, cols) * size` 的公式意義，這就是「棋盤式生成」。
3.  **Global 變數**：理解為什麼在函數內修改外面的變數需要加 `global` 關鍵字，這是 Python 特有的龜毛之處。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 誰在擲骰子？ (Divine Roll)
*   **提問**：如果每次執行遊戲，食物都在同一個位置，這遊戲能玩嗎？
*   **答案**：無聊透頂。我們需要 **驚喜 (Surprise)**。
*   **神器**：`random` 模組。電腦裡住著一個喜歡亂數之神。

### Slide 2: 網格陷阱 (The Grid Trap)
*   **錯誤示範**：`x = random.randint(0, 800)`。
*   **結果**：食物可能出現在 `x=43` 的位置。
*   **悲劇**：蛇每次移動 40 格 (0, 40, 80...)，它永遠不可能走到 43，所以這顆蘋果是 **看得這吃不到的幽靈蘋果**。
*   **正確解法**：先算格子編號 (0~19)，再乘回像素 (Pixel)。
    *   `randint(0, 19) * 40` -> 永遠會是 40 的倍數。

### Slide 3: 函數的權限 (Scope)
*   **全域變數 (Global)**：像是 `food_x`，大家都看得到。
*   **區域變數 (Local)**：函數裡面自己定義的變數，外面看步道。
*   **關鍵字**：如果要在 `spawn_food()` 裡面 **修改** 外面的 `food_x`，必須大聲告訴 Python：「我要用外面那個 Global 的變數！」
    *   `global food_x`

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `import random`
這是一個標準函式庫 (Standard Library)，Python 自帶的軍火庫，不需要安裝。
*   `random.choice(list)`：從清單選一個 (抽獎)。
*   `random.randint(a, b)`：選一個整數 x，使得 a <= x <= b。

### 2. 生成邏輯 (Spawn Logic)
```python
cols = WINDOW_WIDTH // block_size # 800 // 40 = 20 格
rand_col = random.randint(0, 19)  # 隨機選第 0 到第 19 格
food_x = rand_col * 40            # 轉回座標：0, 40, 80...
```
這個公式是本週的精華。它保證了食物永遠乖乖待在格子裡 (Aligned)。
這就是 **Grid-Based Game** 的開發守則。

### 3. 碰撞檢測的前奏
雖然我們這週還沒教碰撞 (Collision)，但你可以想像一下未來：
```python
if head_x == food_x and head_y == food_y:
    # 吃到了！
```
如果沒有網格對齊，`head_x` 是 40，`food_x` 是 43，這個 `==` 永遠不會成立。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Food Master)
1.  **改變食物顏色**：修改 `spawn_food` 函數，讓食物永遠是黃色的 (像 Pac-Man 的豆子)。
2.  **雙倍快樂**：試著創造第二組變數 `food2_x`, `food2_y`，並讓畫面同時出現兩顆食物。

### 🟡 進階題 (The Poison Apple)
1.  **毒蘋果邏輯 (Loot Table)**：
    *   創造一個有 10% 機率生成的「毒蘋果」(紫色)。
    *   提示：`if random.randint(1, 100) <= 10: color = PURPLE`。
    *   這就是 RPG 遊戲掉寶率 (Drop Rate) 的原理。
2.  **防呆機制 (Spawn Safety)**：
    *   目前的程式碼 **沒有** 檢查食物是否生成在蛇的身體上。
    *   這意味著食物可能直接出現在蛇肚子裡！太不講武德了。
    *   **挑戰** (雖然有點難)：思考如何寫一個 `while` 迴圈來檢查？「當食物的位置 == 蛇頭的位置，就重骰一次」。

---

## 📚 寶藏連結 (Reference)
*   [Python Random Module](https://docs.python.org/3/library/random.html)
*   [Alignment in Game Design](https://www.gamedev.net/tutorials/programming/general-and-gameplay-programming/grid-based-collision-detection-and-movement-r2868/) (進階閱讀：為什麼網格系統是 2D 遊戲的基石)
