# 第 03 週 | 讓心跳響起：Game Loop 的奧義

> **給教練的戰術板 (Coach's Corner)**：
> 這是從「靜態圖片」進化到「動態影像」的關鍵時刻。
> 學生會問：「為什麼要 `while True` 一直跑？電腦不累嗎？」
> 給他們一個比喻：**心跳**。
> 遊戲是活的物件，它需要心跳來維持生命。如果不限制心跳速度 (FPS)，它會心律不整甚至心臟病發。
> 這週我們要學會控制時間。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **FPS (Frames Per Second)**：理解「幀數」—— 為什麼 60 FPS 是黃金標準？(太快會過勞，太慢會卡頓)。
2.  **節拍器 (Clock)**：掌握 `Clock.tick()`，做時間的主人。
3.  **狀態分離 (State vs Render)**：腦袋想的 (Update) 跟眼睛看的 (Draw) 要分開處理。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 遊戲的心臟 (The Heartbeat)
*   **思考一下**：電影每秒鐘換 24 張圖，你的眼睛就以為它在動。
*   **遊戲標準**：我們通常追求 **60 FPS** (每秒 60 次更新)。
*   **如果不控制 FPS 會怎樣？**
    *   在 RTX 4090 上，你的蛇會以光速撞牆 (或是你的 CPU 會燒起來)。
    *   在阿公級電腦上，你的蛇會像蝸牛。
    *   **公平性**：我們要確保無論在哪台電腦上，時間流動的速度是一樣的。

### Slide 2: Pygame 的時間魔法師 (`pygame.time.Clock`)
*   **神器**：`clock = pygame.time.Clock()`
*   **咒語**：`clock.tick(60)`
*   **效果**：這行程式碼會對 Pygame 說：「嘿，如果這圈跑太快，請你喝杯茶休息一下 (Sleep)，直到滿 1/60 秒再繼續。」
*   **Vibe**：這就是 **節奏感**。

### Slide 3: 遊戲迴圈三位一體 (The Holy Trinity)
1.  **Event (聽)**：有人按鍵盤嗎？視窗被關掉了嗎？(Input)
2.  **Update (想)**：根據輸入，計算蛇頭要去哪？有沒有吃到蘋果？(Logic)
3.  **Draw (畫)**：把計算好的結果畫在畫布上，然後 `flip()` 翻頁給玩家看。(Render)

### Slide 4: Vibe Coding - 讓它呼吸
*   **視覺化心跳**：我們用數學課最討厭的 `sin` (正弦波) 來做特效。
*   **觀察**：看著那個紅色方塊像心臟一樣跳動，注意 FPS 數值穩定在 60。這就是 **穩定 (Stability)** 的美感。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `import math` 與 `sin` 函數：數學是有用的！
我知道你們討厭三角函數，但它是做特效的神器。
*   `math.sin(time)` 會永遠乖乖地在 `-1` 到 `1` 之間擺盪。
*   我們用它來做「呼吸效果 (Breathing Effect)」，完全不需要寫一堆 `if 太大 then 變小` 的醜程式碼。
*   這就是 **Math Logic** 的優雅。

### 2. `pygame.time.Clock()`
這個物件是全域唯一的，通常在遊戲一創世 (Setup) 就建立。
*   `tick(FPS)`：這是 **阻塞式 (Blocking)** 的。意思是它會真的「暫停世界」直到時間到。
*   `get_fps()`：這是 **非阻塞式** 的。它只是看看現在跑多快，適合拿來做 Debug 顯示。

### 3. 事件處理的最佳手勢 (Best Practice)
```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
```
這段程式碼是Pygame 界的 **Hello World**。
沒有它，你的遊戲就會變成一個關不掉的惡意軟體 (只能用工作管理員強制撲殺)。
**請把它刻在腦海裡。**

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Pulse Check)
1.  **變速測試**：動手把 `FPS` 變數改成 `10`，再改成 `120`。
    *   感覺到了嗎？那種卡頓感 vs 滑順感。這就是職業玩家在乎 FPS 的原因。
2.  **心臟移植**：把心跳的顏色改成你喜歡的樣子。

### 🟡 進階題 (Rhythm Master)
1.  **心律不整 (Arrhythmia)**：
    *   試著讓 `FPS` 變成一個隨機數 (使用 `random.randint(5, 60)`)。
    *   體驗一下這混亂的世界。
2.  **雙核運作 (Dual Core)**：
    *   在畫面上創造第二個心臟。
    *   **挑戰**：讓它跟第一個心臟跳動的節奏 **相反** (反相)。
    *   *提示：`sin` 函數裡面加個負號，或者加個 `pi` 會有什麼效果？*

---

## 📚 寶藏連結 (Reference)
*   [Pygame Time 官方文檔](https://pyga.me/docs/ref/time.html)
*   [Desmos 圖形計算機](https://www.desmos.com/calculator) (強烈推薦去玩玩看 sin 波，視覺化超療癒)
