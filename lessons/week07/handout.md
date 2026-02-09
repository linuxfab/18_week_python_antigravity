# 第 07 週 | 程式美學：重構與函數

> **給老師的備課筆記 (Lesson Notes)**：
> 隨著遊戲變大，程式碼會開始變得亂七八糟。
> 本週不學新語法 (List 我們上週學過了)，而是學「**整理房間**」的藝術。
> 請示範：把一大塊程式碼剪下，貼到一個 `def` 裡面，然後在原來的地方呼叫它。這就是「**封裝 (Encapsulation)**」的第一步。

---

## 🎯 本週教學目標 (Learning Objectives)

1.  **函數 (Functions)**：理解 `def` 關鍵字，如何定義與呼叫。
2.  **程式碼重構 (Refactoring)**：不改變功能，只改變寫法，讓程式更好讀。
3.  **For 迴圈進階**：利用 `range()` 函數繪製等距網格。

---

## 📊 教學投影片大綱 (Slides Outline)

### Slide 1: 程式碼大掃除 (Code Cleanup)
*   **現狀**：我們的主迴圈越來越長，裡面塞滿了按鍵判斷、邊界檢查、繪圖邏輯...
*   **問題**：如果你想修改蛇的顏色，要在幾百行程式碼裡找半天。
*   **解法**：雇用專門的工人 (Functions) 來負責特定的工作。

### Slide 2: 函數工廠 (The Function Factory)
*   **定義 (Define)**：
    ```python
    def draw_grid():
        # 把畫線的程式碼全部塞在這裡
        # ...
    ```
*   **呼叫 (Call)**：
    ```python
    draw_grid()  # 只要喊一聲，工人就會去執行任務
    ```

### Slide 3: 網格系統 (The Grid System)
*   **Vibe Coding**：所有經典的復古遊戲都有網格背景。
*   **數學原理**：
    *   垂直線：x = 0, 40, 80, 120...
    *   水平線：y = 0, 40, 80, 120...
*   **工具**：`range(start, stop, step)`

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `def` 關鍵字
這週的範例中，您會發現 `while True` 迴圈變得非常乾淨：
```python
# 主迴圈只負責指揮
screen.fill((0,0,0))
draw_grid()   # 第一層：背景
draw_snake()  # 第二層：主角
flip()        # 讓觀眾看
```
這就是專業程式設計師的寫法。

### 2. 網格繪製 (Grid Logic)
```python
for x in range(0, WINDOW_WIDTH, block_size):
    pygame.draw.line(...)
```
*   `range(0, 800, 40)` 會產生 `[0, 40, 80, ..., 760]`
*   這省去了我們手寫 20 行 `draw.line` 的麻煩。

---

## 🏋️‍♂️ 動手試試看 (Hands-on Exercises)

### 🟢 基礎題 (The Grid Master)
1.  **改變網格顏色**：目前的網格是深灰色，試著把它改成充滿科技感的螢光綠 (Neon Green)。
2.  **改變網格密度**：修改 `block_size` 變數 (例如改成 20)，看看網格變密之後有什麼效果？

### 🟡 進階題 (Advanced Function)
1.  **自定義蛇頭 (Custom Head)**：
    *   目前 `draw_snake()` 是用一個簡單的迴圈畫完所有身體。
    *   **挑戰**：定義一個新函數 `def draw_head(x, y)`，專門負責畫蛇頭。可以嘗試畫出眼睛 (兩個小黑點) 或是用三角形代表蛇頭。
    *   然後在 `draw_snake()` 的迴圈裡，如果是最後一節 (Head)，就改呼叫 `draw_head()`。

---

## 📚 參考資源 (References)
*   [Python Functions](https://www.w3schools.com/python/python_functions.asp)
*   [Synthwave Grid Tutorial](https://www.youtube.com/watch?v=k3Y0fG4eBf4) (網格背景的藝術靈感)
