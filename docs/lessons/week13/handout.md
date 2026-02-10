# 第 13 週 | 視覺饗宴：當數學愛上藝術

> **給教練的戰術板 (Coach's Corner)**：
> 這一週我們要證明 **「數學不是枯燥的，它是性感的」**。
> 透過簡單的 `sin` 函數和 HSV 顏色空間，我們可以做出百萬音響等級的動態效果。
> 學生通常會對「彩虹色」毫無抵抗力。請善用這一點，讓他們覺得自己是 **Visual Artist**。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **數學動畫 (Math Animation)**：理解週期函式 `sin` 如何轉換為「呼吸」與「心跳」效果。
2.  **HSV 顏色空間**：從 RGB (機器語言) 轉向 HSV (人類直覺)，輕鬆做出 **彩虹流動**。
3.  **渲染優化 (Render Layers)**：加上殘影與光暈，讓畫面從 8-bit 進化到 16-bit。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 呼吸的規律 (The Breath of Code)
*   **想像一下**：你在睡覺時胸口的起伏：規律地上升、下降。
*   **數學翻譯**：這就是 `sin` 函數。
*   **咒語**：`value = sin(time)`
    *   不管時間怎麼變，`value` 永遠乖乖地在 **-1 到 1** 之間來回擺盪。
*   **應用**：`size = 20 + sin(time) * 5` -> 大小就會在 15~25 之間規律呼吸。

### Slide 2: HSV vs RGB
*   **RGB**：紅綠藍。很難調出「亮一點的橘色」。
*   **HSV**：
    *   **H (Hue)**：色相。0=紅, 120=綠, 240=藍 (彩虹圈圈)。
    *   **S (Saturation)**：飽和度。鮮豔 vs 灰階。
    *   **V (Value)**：亮度。明 vs 暗。
*   **Vibe**：想要做彩虹特效？在 `Hue` 上面跑迴圈就對了！

### Slide 3: 殘影特效 (Ghost Trail)
*   **傳統做法**：每一幀都用黑色 `fill((0,0,0))` 把畫面清空。太乾淨了，沒勁。
*   **Vibe 做法**：
    *   畫一個 **半透明** 的黑色遮罩蓋上去。
    *   `s = Surface((W,H), ALPHA); s.fill((0,0,0, 50))`
    *   **結果**：上一幀的蛇還會留下一點點痕跡，看起來就像是有 **動態模糊 (Motion Blur)** 的賽車遊戲。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. 呼吸燈 (Pulsing Effect)
```python
import math
# 利用時間當輸入，sin 會給出 -1~1 的規律起伏
pulse = (math.sin(pygame.time.get_ticks() * 0.005) + 1) / 2 
# pulse 現在是 0~1 的完美比例
current_color = (255 * pulse, 0, 0)
```
這行程式碼能讓你的紅色方塊像是有生命一樣忽明忽暗。

### 2. 彩虹身體 (Rainbow Trail)
```python
import colorsys
# i 是第幾節身體，總長度是 total
hue = (i / total + time_offset) % 1.0 
rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
```
*   這段程式碼是 **Generative Art (生成式藝術)** 的入門。
*   隨著 `time_offset` 增加，整條蛇的顏色會像流水一樣流動。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Disco Snake)
1.  **變色龍**：讓蛇的顏色隨著時間不停自動變換整體的色調 (從紅變綠變藍...)。
2.  **派對燈光**：讓背景網格線也跟著音樂節奏 (或時間) 變色。

### 🟡 進階題 (Cyberpunk Glow)
1.  **偽發光 (Faux Glow)**：
    *   不要只畫一個方塊。
    *   先畫一個 **大一點、透明度低一點** 的同色方塊在下面。
    *   再畫原本的方塊在上面。
    *   你看！它發光了！(這是在沒有 Shader 的年代，老遊戲常用的詐欺術)。
2.  **閃爍星空**：
    *   在背景隨機生 50 個小白點 (星星)。
    *   用 `sin` 函數讓它們以不同的速度「眨眼」。

---

## 📚 寶藏連結 (Reference)
*   [The Beauty of Math in Nature](https://www.youtube.com/watch?v=khitY-K06_8) (原來向日葵早就懂這些數學了)
*   [HSV Color Picker](https://colorpicker.me/#hsv) (玩玩看 HSV，你會愛上它)
