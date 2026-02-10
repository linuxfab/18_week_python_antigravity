# 第 10 週 | 榮耀榜：分數顯示系統 (UI)

> **給教練的戰術板 (Coach's Corner)**：
> 文字是遊戲與玩家溝通的橋樑。
> 國中生可能不理解為什麼顯示個文字要寫 5 行程式碼。
> 關鍵在於：**電腦其實並不認識「文字」**。它只認識「像素 (Pixels)」。
> 我們必須當個書法家，把文字「畫」在紙上，然後再把紙貼到螢幕上。這就是 `render` 與 `blit` 的真諦。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **字型系統 (Font System)**：如何讓電腦把文字「render」成圖片？
2.  **圖層概念 (Layering)**：UI 必須永遠在最上層，不然會被蛇遮住。
3.  **狀態同步 (HUD)**：Heads-Up Display，隨時告訴玩家現在拿了幾分。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 透明賽璐璐片 (Layers)
*   **想像一下**：遊戲畫面有很多層透明的投影片疊在一起。
*   **最底層**：黑色背景 (Background)。
*   **中間層**：網格、蛇、食物 (Game World)。
*   **最上層**：分數、血條 (UI / HUD)。
*   **規則**：程式碼裡 **越晚畫** 的東西，會蓋住前面的。所以 UI 要最後畫！

### Slide 2: 文字繪製三部曲 (Text Rendering)
1.  **刻印章 (Font Object)**：
    ```python
    font = pygame.font.Font("Pixel.ttf", 36)
    ```
2.  **沾墨水蓋章 (Render)**：
    ```python
    text_surf = font.render(f"Score: {score}", True, WHITE)
    ```
    *   這時候它變成了一張 **圖片 (Surface)**。
3.  **貼上螢幕 (Blit)**：
    ```python
    screen.blit(text_surf, (10, 10))
    ```

### Slide 3: Vibe Coding - 復古美學
*   **字體選擇**：雖然 Arial 很好用，但在 Vibe Coding 中，請死都要用 **Pixel Font**。
*   **陰影效果 (Drop Shadow)**：
    *   先在 (12, 12) 畫黑色的分數。
    *   再在 (10, 10) 畫白色的分數。
    *   文字瞬間立體起來！這就是 **CSS** 裡的 `text-shadow` 原理。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `render` 的神祕參數 `True`
```python
font.render("Text", True, Color)
```
*   這個 `True` 代表 **Anti-aliasing (反鋸齒)**。
*   開：文字邊緣平滑 (適合現代風格)。
*   關：文字邊緣鋸齒狀 (適合 Pixel Art 風格)。
*   **Vibe Tip**：如果是像素遊戲，建議設為 `False`，更有味道。

### 2. 重大效能陷阱 (Performance Trap)
**警告：千萬不要在 `while True` 迴圈裡面寫 `pygame.font.Font(...)`！**
*   **為什麼**：這就像是每秒鐘都去刻一顆新印章，蓋一次就丟到垃圾桶。
*   **後果**：你的電腦記憶體會被這些「印章屍體」塞爆，遊戲在 30 秒後會變成 PPT。
*   **正確做法**：`font` 變數在迴圈外面宣告一次就好 (Global 或是 Init 階段)。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Scoreboard)
1.  **破紀錄特效**：當目前分數 `score` 超過 `high_score` 時，讓分數的顏色變成 **金黃色 (GOLD)**。
2.  **置中對齊**：試著把 "GAME OVER" 文字顯示在螢幕 **正中央**。
    *   提示：使用 `text_rect = text_surf.get_rect(center=(400, 300))`。

### 🟡 進階題 (Dynamic UI)
1.  **心跳文字 (Pulsing Text)**：
    *   讓 "Press Space to Start" 這行字忽大忽小。
    *   這有點難，因為不能直接改 font size。
    *   **變通解法**：讓文字 **忽明忽暗** (利用 RGB 的變化) 或者 **上下浮動** (利用 sin 波修改 y 座標)。
2.  **連擊系統 (Combo)**：
    *   如果你在 2 秒內連續吃到食物，顯示 "COMBO x2!"。

---

## 📚 寶藏連結 (Reference)
*   [DaFont - Pixel Fonts](https://www.dafont.com/bitmap.php) (去這裡找免費的像素字體，讓你的遊戲顏值翻倍)
*   [Anti-aliasing Explained](https://en.wikipedia.org/wiki/Spatial_anti-aliasing) (為什麼邊緣會糊糊的？)
