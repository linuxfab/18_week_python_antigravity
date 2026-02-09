# 第 18 週 | 此刻即永恆：專案發表與打包

> **給老師的備課筆記**：
> 這是最後一哩路。
> 重點不在於寫出多少行程式，而在於如何「呈現」你的作品。
> 教會學生如何將資料夾打包、寫一份簡單的 README，這會讓他們覺得自己像個專業的開發者。

---

## 🎯 本週教學目標

1.  **專案整合**：把這 18 週學到的所有東西塞進去。
2.  **狀態切換 (Menu System)**：主選單、遊戲中、結算畫面。
3.  **作品包裝**：README 與展示。

---

## 💡 深度比喻：導演的角色 (The Director)

你現在不再只是一個「修水管的工頭」(Coder)。你是一個設計師。
*   **分鏡 (States)**：
    *   **開場**：大字體標題、閃爍的 Press Start。
    *   **高潮**：緊張的配樂、不斷加快的速度。
    *   **結尾**：最終分數、重新挑戰的機會。
你如何安排這些鏡頭，決定了玩家對你作品的評價。

---

## 📝 程式碼拆解 (整合邏輯)

### 1. 狀態控制中心 (Game State)
```python
if state == "MENU":
    draw_menu()
elif state == "PLAYING":
    game_logic()
    draw_game()
elif state == "GAMEOVER":
    draw_over_screen()
```
*   這就是**狀態機**。它是所有現代遊戲的核心。

---

## ✨ Vibe Coding 小撇步：你的個人風格 (The Signature)

*   **視覺簽名**：你的蛇長得跟別人的不一樣嗎？是星星形狀？還是由文字組成的？
*   **彩蛋 (Easter Eggs)**：如果你取名叫 `LINUXFAB`，會不會觸發什麼隱藏關卡？加入這個小驚喜，玩家會感受到你的用心。

---

## ⚠️ 最後的叮嚀 (Final Advice)

*   **KISS 原則**：Keep It Simple, Stupid. 與其做出 100 個會當機的功能，不如做 3 個完美運作的亮點。
*   **備份**：在最後修改前，複製整份資料夾。這是救命用的。

---

## 🏋️‍♂️ 課後練習

1.  **你的第一份 README**：寫一個簡單的文字檔，告訴別人：
    *   這是什麼遊戲？
    *   怎麼執行？
    *   是用什麼語言寫的？
2.  **慶功宴**：按下 F5 執行你的最終版遊戲，邀請同學來玩，並觀察他們在什麼地方感到最有樂趣！

---

## 📚 參考來源
*   [How to Write a Great README](https://github.com/matiassingers/awesome-readme)
*   [Showcasing Your Work to the World](https://dev.to/shadowtime2000/how-to-showcase-your-projects-effectively-4f24)
