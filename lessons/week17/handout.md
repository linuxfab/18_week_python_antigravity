# 第 17 週 | 魔鬼剋星：除錯與優化 (Debugging)

> **給教練的戰術板 (Coach's Corner)**：
> 這一週我們要教的是 **「心法」**。
> 學生在完成大專案前，一定會遇到很多 Bug，這時候他們會慌張、會挫折。
> 與其幫他們修，不如教他們 **如何修**。
> 除錯不是靠「猜」的，是靠 **邏輯推導 (Deduction)** 的。
> 告訴他們：每一個 Bug 都是通往大師之路的隨機遇敵。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **錯誤訊息解讀 (Traceback)**：學會聽電腦說話。那堆紅色的英文字不是咒罵，是線索。
2.  **單元隔離 (Isolation)**：當程式跑不動時，該如何切塊檢查？(Divide and Conquer)
3.  **防禦性編程 (Defensive Programming)**：利用 `try...except` 幫程式裝上安全氣囊。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 醫生的診斷 (Diagnosis)
*   **病徵 (Symptom)**：遊戲崩潰、蛇不動、顏色怪怪的。
*   **診斷 (Diagnostic)**：看報錯畫面。
    *   `IndexError`：你存取了清單裡不存在的位子 (通常是 `pop` 過頭了)。
    *   `TypeError`：你試著把文字跟數字相加 (字串沒轉型)。
    *   `AttributeError`：你呼叫了不存在的方法 (拼字錯誤)。
*   **治療 (Cure)**：修正代碼，重啟測試。

### Slide 2: 除錯三寶
1.  **Print 大法**：
    *   不要捨不得用。`print(f"Debug: 現在頭的位置是 {head}")`
    *   如果蛇不動，至少你能確認是「座標算錯」還是「繪圖畫錯」。
2.  **小黃鴨除錯法 (Rubber Ducking)**：
    *   找一個黃色小鴨 (或是你的同學)，一行一行解釋你的程式碼給他聽。
    *   通常講到一半，你自己就會發現盲點了。
3.  **註解掉 (Comment Out)**：
    *   把可疑的程式碼先註解掉，看看遊戲還會不會當機。

### Slide 3: 效能優化 (Optimization)
*   你的遊戲跑起來卡卡的嗎？
*   **兇手 通常是**：
    *   在 `while` 迴圈裡 `load` 圖片。
    *   在 `while` 迴圈裡 `render` 文字。
    *   畫了幾千個看不見的物體。
*   **Vibe Check**：好的程式碼不只要能跑，還要跑得像跑車一樣順。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. `try...except` 安全氣囊
```python
try:
    load_music("bgm.mp3")
except:
    print("⚠️ 音樂檔遺失，但遊戲繼續執行")
    # 就算圖片載入失敗，也要讓遊戲能玩 (Graceful Failure)
```
這就是為什麼專業的軟體很少直接閃退。

### 2. 斷言 (Assert)
```python
assert len(snake_body) > 0, "蛇的身體怎麼可能小於 0？見鬼了！"
```
這行程式碼會在問題發生時 **主動引爆**，防止錯誤蔓延到後面變得更難抓。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Bug Hunter)
1.  **故意犯錯**：
    *   請故意寫錯一行程式碼 (例如把變數名打錯)。
    *   截圖它的 Traceback，解釋這三行英文各代表什麼意思 (File, Line, Error)。
2.  **極限測試**：
    *   試著把 FPS 調到 1000，或是把蛇的長度加到 10000。
    *   看看你的電腦什麼時候會冒煙 (誤)。

### 🟡 進階題 (Profiler)
1.  **效能健檢**：
    *   你的遊戲每一幀到底花了多少時間？
    *   在迴圈開頭紀錄 `start = time.time()`，結尾紀錄 `end = time.time()`。
    *   `print(f"Frame Time: {(end-start)*1000:.2f} ms")`。
    *   如果超過 **16ms** (1000ms/60fps)，你就該緊張了。

---

## 📚 寶藏連結 (Reference)
*   [How to Read a Python Traceback](https://realpython.com/python-traceback/) (必讀！這是你的求生指南)
*   [Rubber Duck Debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging) (為什麼工程師桌上都有一隻鴨子？)
