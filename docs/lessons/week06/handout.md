# 第 06 週 | 光速戰記：蛇的身體結構 (List)

> **給教練的戰術板 (Coach's Corner)**：
> 這是程式設計中最痛苦的轉折點之一：**從單一變數 (Primitive) 到清單 (List)**。
> 請把 `variable` 比喻成一個「口袋」，把 `list` 比喻成「火車」。
> 1.  新的乘客來了 (Append) -> 加到最後一節車廂。
> 2.  到站了，第一節車廂脫離 (Pop) -> 刪掉最前面。
> 3.  如果不刪掉舊的，火車就會無限變長，直到塞爆你的記憶體。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **清單 (List)**：理解 `[]` 是可以裝很多東西的容器，就像多啦A夢的百寶袋。
2.  **元組 (Tuple)**：理解 `(x, y)` 是一組不可分割的座標，它們是連體嬰。
3.  **隊列邏輯 (Queue Logic)**：先進先出 (FIFO)，這是貪食蛇移動的核心原理。
4.  **迴圈渲染 (Loop Rendering)**：如何把清單裡的 100 個座標全部畫出來？除了 `for` 迴圈別無他法。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 變身術 (Transformation)
*   **過去**：`x, y` 只能記住 **現在** 的位置 (金魚腦)。
*   **現在**：我們需要記住 **過去 50 步** 的位置 (大象腦)。
*   **神器**：List `snake_body = [(x1,y1), (x2,y2), ...]`

### Slide 2: 毛毛蟲移動法 (The Caterpillar Method)
*   **迷思**：蛇移動時，並不是整條蛇每一節都在往前跑。
*   **真相**：
    1.  **頭**：往前長出一節新的 (New Head)。
    2.  **尾**：縮回去一節舊的 (Remove Tail)。
    3.  **身體**：其實完全沒動！(這就是視覺暫留造成的錯覺)。
*   **Vibe**：這就像是你在排隊，前面多了一個人，後面走了一個人，隊伍看起來就在移動。

### Slide 3: 程式碼怎麼寫？ (Code Logic)
```python
# 1. 紀錄現在的頭 (Append)
snake_body.append((new_x, new_y))

# 2. 如果太長了，切掉尾巴 (Pop)
if len(snake_body) > 50:
    snake_body.pop(0)
```
*   `append()`：加到清單的 **最後面** `[-1]`。
*   `pop(0)`：刪除清單的 **最前面** `[0]`。

### Slide 4: Vibe Coding - 光速軌跡 (Tron Trail)
*   **挑戰**：我們能不能讓蛇的尾巴有顏色變化？
*   **解法**：利用 `index` (索引值)。
    *   索引 0 (尾巴)：顏色最暗、最小。
    *   索引 50 (頭部)：顏色最亮、最大。
*   **效果**：這就是你在 《Tron: Legacy (光速戰記)》 電影裡看到的光束機車效果！

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `enumerate` 是什麼神仙語法？
在 `demo.py` 中，我們用了這個高級寫法：
```python
for i, segment in enumerate(snake_body):
    # i 是編號 (0, 1, 2...)
    # segment 是內容 (座標)
```
*   如果不寫 `enumerate`，我們就必須自己用一個變數計數 `count += 1`，那太原始人了。
*   Python就是要寫得像英文一樣優雅。

### 2. 彩虹漸層 (Rainbow Logic)
我們使用了一個叫 **HSV** 的色彩模型。
*   **Hue (色相)**：0~360 度代表紅橙黃綠藍靛紫。
*   我們把 `i / len` 當作 Hue 的比例，這樣蛇頭到蛇尾就會剛好跑完一圈色相環。
*   這讓你的蛇看起來像是吃了無敵星星一樣閃耀。

### 3. 動態大小 (Dynamic Size)
為了讓視覺效果像「彗星」，我們把每一節的大小跟它的索引值綁定：
```python
size = block_size * (i / total_length)
```
這樣尾巴 (i=0) 就會變成一個小點，頭部 (i=50) 則是正常大小。
這就是 **Procedural Animation (程式化動畫)** 的入門。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (List Master)
1.  **長度控制**：將 `target_length` 改成 `100` 或 `200`，看看蛇會變多長？
2.  **時間暫停**：試著把 `snake_body.pop(0)` 那行註解掉 (前面加 #)，看看會發生什麼事？
    *   **結果**：無限生長模式 / 貪食蛇變成了 Tron 光牆。這其實也是一種遊戲玩法！

### 🟡 進階題 (Creative Trail)
1.  **斷尾求生 (Quick Escape)**：
    *   寫一個 `if` 判斷：按下空白鍵時，把 `snake_body` 清空一半。
    *   提示：利用 List Slicing `del snake_body[:25]`。
2.  **故障藝術 (Glitch Art)**：
    *   利用 `random.randint`，讓每一節的顏色都在一定範圍內隨機跳動。
    *   創造出一條看起來像是 **訊號接觸不良** 的 Cyberpunk 蛇。

---

## 📚 寶藏連結 (Reference)
*   [Python Tutor](https://pythontutor.com/visualize.html) (強烈推薦用這個網站看 append/pop 的過程，不要憑空想像！)
*   [Tron Light Cycle Scene](https://www.youtube.com/watch?v=-3ODe9mqoDE) (本週的 Vibe 靈感來源)
