# 第 07 週 | 程式風水學：重構與函數

> **給教練的戰術板 (Coach's Corner)**：
> 隨著遊戲變大，程式碼會開始變得像是「義大利麵」一樣糾纏不清。
> 本週不學新語法 (List 我們上週學過了)，而是學 **「整理房間」** 的藝術。
> 請示範：把一大塊程式碼剪下，貼到一個 `def` 裡面，然後在原來的地方呼叫它。
> 這就是 **封裝 (Encapsulation)**，讓程式碼讀起來像在讀故事書，而不是讀天書。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **函數 (Functions)**：理解 `def` 關鍵字，如何創造自己的咒語。
2.  **程式碼重構 (Refactoring)**：不改變功能，只改變結構。這是為了走更長遠的路。
3.  **迴圈進階**：利用 `range()` 函數繪製 **Synthwave 風格** 的網格背景。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 程式碼大掃除 (Code Feng Shui)
*   **現狀**：我們的主迴圈 (`while True`) 已經長達 100 行，裡面塞滿了按鍵判斷、移動邏輯、邊界檢查、繪圖指令...
*   **問題**：如果你想修改蛇的顏色，要在幾百行程式碼裡找半天，這就是「技術債」。
*   **解法**：雇用專門的工人 (Functions) 來負責特定的工作。

### Slide 2: 函數工廠 (The Function Factory)
*   **定義 (Define)**：
    ```python
    def draw_grid():
        # 把畫線的髒活全部塞在這裡
        # 主管(Main Loop)不想看細節
    ```
*   **呼叫 (Call)**：
    ```python
    draw_grid()  # 嘿！去畫格子！
    ```
*   **好處**：主程式變得超乾淨，變成了指揮官。

### Slide 3: 網格系統 (The Grid System)
*   **Vibe Coding**：所有經典的復古遊戲都有網格背景。這是 80 年代的浪漫。
*   **數學原理**：
    *   垂直線 (Vertical)：x = 0, 40, 80, 120...
    *   水平線 (Horizontal)：y = 0, 40, 80, 120...
*   **工具**：`range(start, stop, step)`，讓電腦幫你算這些數字。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `def` 關鍵字：自創咒語
這週的範例中，您會發現 `while True` 迴圈變得非常乾淨，簡直賞心悅目：
```python
# 主迴圈只負責指揮
screen.fill((0,0,0))
draw_grid()   # 第一層：畫背景
draw_snake()  # 第二層：畫主角
flip()        # 翻頁
```
這就是專業程式設計師的寫法。**Abstraction (抽象化)** 是人類大腦處理複雜問題的唯一方法。

### 2. 網格繪製 (Grid Logic)
```python
for x in range(0, WINDOW_WIDTH, block_size):
    pygame.draw.line(...)
```
*   `range(0, 800, 40)` 會產生 `[0, 40, 80, ..., 760]`。
*   它省去了我們手寫 20 行 `draw.line` 的麻煩。
*   **Vibe Check**：把線條顏色設為深灰色 `(40, 40, 40)`，不要用全白，那樣會瞎掉。我们要的是 **低調奢華**。

### 3. 參數傳遞 (Passing Arguments)
函數不只是笨笨的執行，它還可以接受指令：
```python
def draw_rect(color, x, y):
    # ...
```
這就像是告訴畫家：「用 **紅色** 在 **(100, 100)** 畫一個方塊」。靈活性 MAX。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (The Grid Master)
1.  **改變網格顏色**：目前的網格是深灰色，試著把它改成充滿科技感的 **螢光綠 (Neon Green)** 或 **賽博紫 (Cyber Purple)**。
2.  **改變密度**：修改 `block_size` 變數 (例如改成 20)，看看網格變密之後的視覺效果。

### 🟡 進階題 (Advanced Function)
1.  **自定義蛇頭 (Custom Head)**：
    *   目前 `draw_snake()` 是用一個簡單的迴圈畫完所有身體。
    *   **挑戰**：定義一個新函數 `def draw_head(x, y)`，專門負責畫蛇頭。
    *   可以嘗試畫出眼睛 (兩個小黑點) 或是用 `draw.polygon` 畫一個三角形代表蛇頭。
    *   然後在 `draw_snake()` 的迴圈裡，利用 `if i == len(snake_body) - 1:` 判斷如果是最後一節 (Head)，就改呼叫 `draw_head()`。

---

## 📚 寶藏連結 (Reference)
*   [Python Functions](https://www.w3schools.com/python/python_functions.asp) (W3Schools 永遠是你的好朋友)
*   [Synthwave Grid Tutorial](https://www.youtube.com/watch?v=k3Y0fG4eBf4) (網格背景的藝術靈感，看這影片會懷孕)
