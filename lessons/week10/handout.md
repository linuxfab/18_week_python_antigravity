# 第 10 週 | 分數顯示：讓你的成就被世界看見

> **給老師的備課筆記**：
> 文字是遊戲與玩家溝通的橋樑。
> 國中生可能不理解為什麼顯示文字要這麼多行程式碼。
> 關鍵在於：電腦其實並不認識「文字」，它只認識「像素 (Pixels)」。

---

## 🎯 本週教學目標

1.  **字型系統 (Font System)**：如何讓電腦把文字「畫」成圖片？
2.  **UI 平面設計**：圖層 (Layers) 的概念與 Blit。
3.  **變數累加**：記錄與顯示遊戲狀態。

---

## 💡 深度比喻：透明賽璐璐片 (Layering)

想像遊戲畫面有很多層透明的色片疊在一。
*   **最底層**：黑色背景。
*   **中間層**：網格、蛇、食物。
*   **最上層**：分數 (UI)。
如果你把分數畫在最底層，蛇經過時就會把分數遮住。
**所以，在程式碼裡，「最後畫的東西，會出現在最上面」。**

---

## 📝 程式碼拆解 (關鍵步驟)

### 1. 建立「印章」 (Font Object)
```python
font = pygame.font.SysFont("Arial", 36, bold=True)
```
*   這就像是去刻一顆印章。`36` 是大小，`bold=True` 是粗體。

### 2. 沾墨水、蓋章 (Render)
```python
score_surf = font.render(f"Score: {score}", True, (255, 255, 255))
```
*   `render` 就是把文字轉成一張「圖片」(Surface)。
*   `True` 代表「反鋸齒」(Anti-aliasing)，讓文字邊緣變順滑，不毛躁。

### 3. 貼到牆上 (Blit)
```python
screen.blit(score_surf, (10, 10))
```

---

## ✨ Vibe Coding 小撇步：Arcade 復古感

*   **字體選擇**：雖然 Arial 很好用，但在 Vibe Coding 中，試著搜尋 `Press Start 2P` 這種像素字體，遊戲質感立馬從「學生作業」變成「Steam 獨立遊戲」。
*   **影子效果**：先在 (12, 12) 畫黑色的分數，再在 (10, 10) 畫白色的分數。文字就會有酷炫的陰影立體感！

---

## ⚠️ 重大效能陷阱 (Performance Bug)

**千萬不要在 `while True` 迴圈裡面寫 `font = pygame.font.SysFont(...)`！**
*   **為什麼**：這就像是每秒鐘都去買一顆新印章，蓋一次就丟掉。電腦的記憶體很快就會被這些「印章屍體」塞爆，導致遊戲越來越卡。
*   **正確做法**：在迴圈外面定義一次就好。

---

## 🏋️‍♂️ 課後練習

1.  **破紀錄特效**：當目前分數 `score` 超過 `high_score` 時，讓分數的顏色變成「金黃色」。
2.  **動態分數**：讓分數不要只是靜態的，每當吃到食物，文字稍微變大再縮回 (提示：利用變數控制 font size，或者簡單點，畫一張大的再畫回小的)。

---

## 📚 參考來源
*   [Pygame Font Docs](https://www.pygame.org/docs/ref/font.html)
*   [Anti-aliasing Explained](https://en.wikipedia.org/wiki/Spatial_anti-aliasing) (為什麼邊緣會糊糊的？)
