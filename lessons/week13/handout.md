# 第 13 週 | 視覺饗宴：當數學愛上藝術

> **給老師的備課筆記**：
> 這一週我們要證明「數學不是枯燥的」。
> 透過簡單的 `sin` 函數和顏色坐標系轉換，我們可以做出百萬音響等級的動態效果。
> 請特別解釋 HSV 顏色空間，這對做視覺設計的同學非常震撼。

---

## 🎯 本週教學目標

1.  **數學動畫 (Math Animation)**：理解週期函式 `sin` 如何轉換為縮放效果。
2.  **HSV 顏色空間**：從 RGB 轉向更直覺的「彩虹色」操作。
3.  **渲染優化 (Render Layers)**：增加層次感。

---

## 💡 深度比喻：呼吸的規律 (Sine waves)

想像你在睡覺時胸口的起伏：規律地上升、下降。
這在數學裡就是 `sin` 函數。
*   值域在 **-1 到 1** 之間來回。
透過這組神奇的數字，我們可以讓食物「縮放」：
`size = 20 + sin(time) * 5` -> 大小就會在 15~25 之間規律呼吸。

---

## 📝 程式碼拆解 (關鍵視覺邏輯)

### 1. 呼吸燈 (Pulsing Food)
```python
import math
# 利用時間當輸入，sin 會給出 -1~1 的規律起伏
pulse = abs(math.sin(pygame.time.get_ticks() * 0.005))
size = base_size + pulse * 10
```

### 2. 彩虹身體 (Rainbow Trail)
```python
import colorsys
# 把 0~1 的 Hue 值轉成 RGB
hue = (i / len(snake_body))
rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
```
*   **HSV 解密**：
    *   **H (Hue)**：色相。0=紅, 0.3=綠, 0.6=藍... 就像是在彩虹圈圈上面指位置。

---

## ✨ Vibe Coding 小撇步：賽博龐克光暈 (Glow)

*   **物件發光**：不要只畫一個方塊。先畫一個大一點、透明度低一點的方塊在下面。這叫「偽發光」(Faux Glow)。
*   **粒子殘影 (Ghosting)**：不要每一幀都執行 `screen.fill((0,0,0))`。試著畫一個半透明的黑色大矩形蓋住全螢幕，這會讓蛇移動時留下一條淡淡的幻影。

---

## ⚠️ 常見陷阱 (Pitfalls)

*   **HSV 轉 RGB 的比例**：`colorsys` 回傳的值是 **0~1**，但 Pygame 需要 **0~255**。記得要乘上 255 (例如：`int(r * 255)`)。
*   **Sin 的輸入**：如果你輸入的是常數，它就不會動。記得要傳入 `pygame.time.get_ticks()` 這種會隨時間變化的值。

---

## 🏋️‍♂️ 課後練習

1.  **閃爍星空**：在背景隨機生一些點（星星），並用 `sin` 函數讓它們以不同的速度「眨眼」。
2.  **變色龍蛇**：讓蛇的顏色隨著時間不停自動變換整體的色調。

---

## 📚 參考來源
*   [The Beauty of Math in Nature](https://www.youtube.com/watch?v=khitY-K06_8)
*   [HSV vs RGB: Which to use?](https://www.canva.com/colors/color-meanings/hsv/)
