# 第 02 週 | 顏色與形狀：座標系統入門

> **給老師的備課筆記 (Lesson Notes)**：
> 大多數國中生還在習慣數學座標軸 (右為正、上為正)，但計算機圖形的 Y 軸是「**向下為正**」。這週的挑戰在於打破數學慣性，建立「螢幕像素」的概念。請善用 `demo.py` 中的滑鼠點擊功能，讓學生「看到」實際的 (x, y) 數值。

---

## 🎯 本週教學目標 (Learning Objectives)

1.  **座標理解**：掌握 (0, 0) 是左上角，(800, 600) 是右下角。
2.  **RGB 混色**：理解紅、綠、藍三原色如何混合出任何顏色。
3.  **形狀繪製**：學會使用 `pygame.draw.rect` 定義物體的大小與位置。

---

## 📊 教學投影片大綱 (Slides Outline)

### Slide 1: 歡迎來到像素世界 (Pixel World)
*   **提問**：想像你的螢幕是由無數個小燈泡組成的矩陣。
*   **概念**：我們怎麼告訴電腦要亮哪燈泡？
*   **答案**：座標 (Coordinate) —— (x, y)。

### Slide 2: 顛倒的世界 (Y-Axis Flip)
*   **數學的世界**：Y 軸往上是正數 (增加高度)。
*   **程式的世界**：Y 軸往**下**是正數 (增加深度/行數)。
*   **記憶法**：像看書一樣，從第 1 行讀到第 100 行，數字是越來越大的。

### Slide 3: 顏色的魔法 (RGB Color Model)
*   **三原色**：Red (紅), Green (綠), Blue (藍)。
*   **數值範圍**：0 (全黑/關燈) ~ 255 (全亮/開燈)。
*   **Vibe Coding 挑戰**：
    *   (255, 0, 0) 是紅色。
    *   (0, 255, 0) 是綠色。
    *   (255, 255, 0) 是什麼顏色？(提示：紅光 + 綠光 = 黃光)

### Slide 4: 召喚第一條蛇 (The First Snake Head)
*   **核心指令**：`pygame.draw.rect(screen, color, rect)`
*   **Rect 四寶**：(x, y, width, height)
*   **定位挑戰**：如何把一個方塊剛好放在畫面正中央？
    *   中心點 = (寬/2, 高/2)
    *   左上角 = (中心點 - 方塊寬/2, 中心點 - 方塊高/2)

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `setup` 與 `rect` 物件
程式碼中我們不再硬寫數字，而是定義了一個 `Rect` 物件：
```python
snake_head = pygame.Rect(rect_x, rect_y, BLOCK_SIZE, BLOCK_SIZE)
```
這其實是在記憶體中切出了一塊「隱形的長方形區域」，等到 `pygame.draw` 函數呼叫時，才把它真正塗上顏色。

### 2. `pygame.draw.rect` 的強大
*   `width=0` (預設)：塗滿整個矩形。
*   `width=2`：只畫邊框 (適合用來當作除錯框或裝飾)。
*   本週範例同時使用了這兩種技巧，讓蛇頭看起來更有層次感。

### 3. 滑鼠座標偵測 (Interactive Debugging)
```python
if event.type == pygame.MOUSEBUTTONDOWN:
    print(mouse_pos)
```
這是本週最強大的教學工具！讓學生在畫面的四個角落點擊，觀察終端機輸出的數值變化，能瞬間秒懂座標系的概念。

---

## 🏋️‍♂️ 動手試試看 (Hands-on Exercises)

### 🟢 基礎題 (Basic)
1.  **改變顏色**：將蛇頭從螢光綠改成你喜歡的顏色 (例如紫色)。
2.  **改變大小**：將 `BLOCK_SIZE` 從 40 改成 100，看看蛇頭變多大。

### 🟡 進階題 (Coordinate Challenge)
1.  **四角定位**：試著計算座標，讓蛇頭分別出現在視窗的：
    *   左上角 (0, 0)
    *   右上角 (760, 0) -> 為什麼是 760？(800 - 40)
    *   左下角 (0, 560)
    *   右下角 (760, 560)
2.  **雙胞胎蛇**：在程式碼中新增第二個 `Rect` 物件，並將它畫在第一條蛇的右邊，讓畫面出現兩個方塊。

---

## 📚 參考資源 (References)
*   [Pygame Rect 文檔](https://pyga.me/docs/ref/rect.html)
*   [RGB 色彩混合模擬器](https://www.w3schools.com/colors/colors_rgb.asp)
