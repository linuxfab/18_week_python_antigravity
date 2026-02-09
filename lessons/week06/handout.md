# 第 06 週 | 光速戰記：貪食蛇的身體結構

> **給老師的備課筆記 (Lesson Notes)**：
> 這是程式設計中最痛苦的轉折點之一：**從單一變數 (Primitive) 到陣列清單 (List/Array)**。
> 請務必用「火車車廂」或「排隊買票」來比喻：
> 1.  新的人來排隊 (Append) -> 加到最後面。
> 2.  票賣完了，第一個人離開 (Pop) -> 刪掉最前面。
> 3.  如果不刪掉舊的，隊伍就會無限變長 (記憶體爆炸)。

---

## 🎯 本週教學目標 (Learning Objectives)

1.  **List (清單)**：理解 `[]` 是可以裝很多東西的容器。
2.  **Tuple (元組)**：理解 `(x, y)` 是一組不可分割的座標。
3.  **Queue Logic (隊列)**：先進先出 (First-In, First-Out)，這是貪食蛇移動的核心原理。
4.  **For Loop Rendering**：如何把清單裡的 100 個座標全部畫出來？

---

## 📊 教學投影片大綱 (Slides Outline)

### Slide 1: 變身術 (Transformation)
*   **過去**：`x, y` 只能記住現在的位置。
*   **現在**：我們需要記住「過去 50 步」的位置。
*   **工具**：List `snake_body = [(x1,y1), (x2,y2), ...]`

### Slide 2: 貪食蛇移動原理 (The Caterpillar Method)
*   **迷思**：蛇移動時，並不是整條蛇每一節都往前跑。
*   **真相**：
    1.  **頭**：往前長出一節新的。
    2.  **尾**：縮回去一節舊的。
    3.  **身體**：其實完全沒動！(視覺暫留造成的錯覺)

### Slide 3: 程式碼怎麼寫？ (Code Logic)
```python
# 1. 紀錄現在的頭 (Append)
snake_body.append((new_x, new_y))

# 2. 如果太長了，切掉尾巴 (Pop)
if len(snake_body) > 50:
    snake_body.pop(0)
```
*   `append()`：加到清單的**最後面** [-1]。
*   `pop(0)`：刪除清單的**最前面** [0]。

### Slide 4: Vibe Coding - 光速軌跡 (Tron Trail)
*   **挑戰**：我們能不能讓蛇的尾巴有顏色變化？
*   **解法**：利用 `index` (索引值)。
    *   索引 0 (尾巴)：顏色最暗、最小。
    *   索引 50 (頭部)：顏色最亮、最大。
*   **效果**：這就是你在 Cyberpunk 電影裡看到的光束機車效果！

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `enumerate` 是什麼？
在 `demo.py` 中，我們用了這個高級寫法：
```python
for i, segment in enumerate(snake_body):
```
*   `i`：目前是第幾節 (0, 1, 2...)。
*   `segment`：那節身體的座標 `(x, y)`。
如果不寫 `enumerate`，我們就必須自己用一個變數計數，會很麻煩。

### 2. 彩虹漸層怎麼做的？ (Rainbow Logic)
我們使用了一個叫 HSV 的色彩模型。
*   **Hue (色相)**：0~360 度代表紅橙黃綠藍靛紫。
*   我們把 `i / len` 當作 Hue 的比例，這樣蛇頭到蛇尾就會剛好跑完一圈色相環。

### 3. 動態大小 (Dynamic Size)
為了讓視覺效果像「彗星」，我們把每一節的大小跟它的索引值綁定：
```python
size = block_size * (i / total_length)
```
這樣尾巴 (i=0) 就會變成一個小點，頭部 (i=50) 則是正常大小。

---

## 🏋️‍♂️ 動手試試看 (Hands-on Exercises)

### 🟢 基礎題 (List Master)
1.  **改變長度**：將 `target_length` 改成 100 或 200，看看蛇會變多長？
2.  **定 格**：試著把 `snake_body.pop(0)` 那行註解掉 (前面加 #)，看看會發生什麼事？(提示：無限生長模式 / 貪食蛇變成了 Tron 光牆)。

### 🟡 進階題 (Creative Trail)
1.  **斷尾求生**：
    *   寫一個 `if` 判斷：按下空白鍵時，把 `snake_body` 清空一半。
    *   提示：`del snake_body[:25]`
2.  **閃爍特效**：
    *   利用 `random.randint`，讓每一節的顏色都在一定範圍內隨機跳動，創造出「故障藝術 (Glitch Art)」風格的蛇。

---

## 📚 參考資源 (References)
*   [Python Lists Visualized](https://pythontutor.com/visualize.html) (強烈推薦用這個網站看 append/pop 的過程)
*   [Tron (1982) Light Cycle Scene](https://www.youtube.com/watch?v=-3ODe9mqoDE) (本週的 Vibe 靈感來源)
