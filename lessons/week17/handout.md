# 第 17 週 | 魔鬼剋星：專業工程師的修煉

> **給老師的備課筆記**：
> 這一週我們要教的是「心法」。
> 學生在完成大專案前，一定會遇到很多 Bug。
> 與其幫他們修，不如教他們**如何修**。
> 除錯不是靠「猜」，是靠「邏輯推導」。

---

## 🎯 本週教學目標

1.  **錯誤訊息解讀 (Traceback)**：學會聽電腦說話。
2.  **單元隔離 (Unit Isolation)**：當程式跑不動時，該如何切塊檢查？
3.  **防禦性編程 (Defensive Programming)**：利用 `try...except` 增加韌性。

---

## 💡 深度比喻：醫生的診斷 (Diagnosis)

*   **病徵 (Symptom)**：遊戲崩潰、蛇不動、顏色怪怪的。
*   **診斷 (Diagnostic)**：看報錯畫面。報錯畫面的第幾行，就是受傷的地方。
*   **治療 (Cure)**：修正代碼，重啟測試。
*   **預防 (Prevention)**：思考為什麼這裡會出錯？下次能不能先寫好判斷式？

---

## 📝 程式碼拆解 (除錯三寶)

### 1. `print()` 大法
不要捨不得用印出。
`print(f"Debug: 現在頭的位置是 {head}")`
如果蛇不動，至少你能確認是座標算錯還是繪圖畫錯。

### 2. `try...except` 安全氣囊
```python
try:
    load_image("high_res_snake.png")
except:
    # 就算圖片載入失敗，也要讓遊戲能玩 (畫個方塊代替)
    draw_placeholder_rect()
```

---

## ✨ Vibe Coding 小撇步：程式碼整潔度

*   **有意義的變數名**：不要寫 `a = x + b`。寫 `new_head_pos = old_head_pos + delta`。雖然字比較多，但你的大腦會感謝你。
*   **註解 (Comments)**：註解是寫給「三個月後的你自己」看的。那時候你已經忘記現在在寫什麼了。

---

## ⚠️ 專業工程師的除錯禁忌

*   **盲目修改**：發現錯了就隨便改一個數字試試看。這叫「亂槍打鳥」，只會讓 Bug 越積越多。
*   **忽略警告**：如果終端機出現黃色的 Warning，雖然不影響遊戲跑，但它通常預示著未來會發生的大崩潰。

---

## 🏋️‍♂️ 課後練習

1.  **Bug 獵人**：請故意寫錯一行程式碼，並截圖它的 Traceback，解釋這三行英文各代表什麼意思。
2.  **效能健檢**：你的遊戲跑起來順嗎？試著在迴圈開頭紀錄 `time.time()`，結尾也紀錄一次，算出每一幀到底花了多少毫秒。

---

## 📚 參考來源
*   [How to Read a Python Traceback](https://realpython.com/python-traceback/)
*   [The debugger is your friend](https://code.visualstudio.com/docs/editor/debugging)
