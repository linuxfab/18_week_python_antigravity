# 第 11 週 | 死亡宣告：失敗的藝術與重生

> **給老師的備課筆記**：
> 死亡在遊戲中不是終結，而是學習循環的關鍵。
> 學生會在這裡學到**狀態管理**，這對未來寫大型 App 或網頁非常重要。
> 貪食蛇最經典的死法是「咬到自己」，這需要判斷「頭座標是否在身體清單中」。

---

## 🎯 本週教學目標

1.  **狀態旗標 (State Management)**：學會切換遊戲模式 (`Menu` / `Play` / `Game Over`)。
2.  **清單搜尋 (List Lookup)**：利用 `if x in list` 語法快速抓到碰撞。
3.  **封裝重置 (Reset Function)**：如何讓遊戲重來而不需要關掉視窗。

---

## 💡 深度比喻：紅綠燈交通管制

想像你的遊戲是一個紅綠燈：
*   **綠燈 (Play)**：蛇一直在動，你可以控制方向。
*   **紅燈 (Game Over)**：蛇死掉了，畫面停住，只有按下「重播」按鈕才會變回綠燈。
*   **關鍵**：我們需要一個變數來記錄現在是「紅燈」還是「綠燈」。在程式碼裡，我們用 `game_over = True`。

---

## 📝 程式碼拆解 (關鍵邏輯)

### 1. 如何發現「我咬到我自己」？
```python
new_head = (head_x, head_y)
if new_head in snake_body:
    game_over = True
```
*   這行程式超強！它會瞬間掃描整條蛇的身體，看看你有沒有撞上一節。

### 2. 停住蛇的腳步
```python
if not game_over:
    # 這裡放移動、生長等邏輯
    # 當 game_over 變成 True，這裡就會被「跳過」，蛇就不動了
```

---

## ✨ Vibe Coding 小撇步：死亡震撼 (Impact)

當玩家失敗時，不要只是顯示一行冷冰冰的字。
*   **螢幕變色**：整個背景瞬間轉成暗紅色 `(50, 0, 0)`。
*   **慢動作**：死掉的那一瞬間，把 `clock.tick(10)` 降到 `clock.tick(2)`，創造出一種戲劇性的緩慢感。
*   **倒退嚕**：讓蛇死掉後，身體一節一節慢慢消失。

---

## ⚠️ 常見陷阱 (Pitfalls)

*   **重置不完全**：按下重啟後，蛇的長度竟然沒變短？那是因為你忘記清空 `snake_body`。
*   **死掉還能動**：有些同學忘了在 `event` 處理那邊加上判斷，導致 Game Over 選單出來了，蛇還在背景偷偷跑。

---

## 🏋️‍♂️ 課後練習

1.  **無敵護身符**：設定一個變數 `invincible_frames = 60`。當蛇重生後，這 60 幀內就算撞到自己也不會死。
2.  **排行榜預熱**：雖然還沒教儲存檔案，但你能讓程式記錄這一次執行期間的「最高分」嗎？(即使重刷也不會消失)。

---

## 📚 參考來源
*   [Game State Management](https://gameprogrammingpatters.com/state.html)
*   [Finite State Machines for Beginners](https://brilliant.org/wiki/finite-state-machines/)
