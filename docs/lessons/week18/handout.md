# 第 18 週 | 此刻即永恆：專案發表與打包 (Release)

> **給教練的戰術板 (Coach's Corner)**：
> 這是最後一哩路。
> 重點不在於寫出多少行程式，而在於如何 **「呈現 (Present)」** 你的作品。
> 教會學生如何打包、寫一份簡單的 README，這會讓他們覺得自己像個 **專業的開發者 (Professional Developer)**。
> 告訴他們：這個檔案，就是你這 18 週的青春結晶。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **專案整合 (Integration)**：把這 18 週學到的所有東西 (音效、圖像、OOP) 全部塞進去。
2.  **狀態機 (Final State Machine)**：要有完整的 Start Menu -> Game Loop -> Game Over -> Restart 循環。
3.  **作品包裝 (Packaging)**：寫一個 README，並把遊戲打包成人家可以執行的樣子。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 導演的視角 (The Director)
*   你現在不再只是一個「修水管的工頭」(Coder)。你是一個 **設計師**。
*   **分鏡 (Flow)**：
    *   **開場**：大字體標題、閃爍的 "PRESS START"。背景音樂要有氣勢。
    *   **高潮**：緊張的配樂、不斷加快的速度、螢幕晃動。
    *   **結尾**：最終分數、重新挑戰的機會。
*   你如何安排這些鏡頭，決定了玩家對你作品的評價。

### Slide 2: 關於 README
*   打開 GitHub，每一個受歡迎的專案都有一個漂亮的 README。
*   **它是什麼**：遊戲的說明書、你的名片。
*   **寫什麼**：
    *   **Title**: 遊戲名稱 (要夠酷)。
    *   **How to Play**: 上下左右？空白鍵？
    *   **Credits**: 作者是誰？音樂哪裡來的？(尊重智慧財產權)。

### Slide 3: 未來的路
*   Python 不只能寫貪食蛇。
*   **爬蟲**：抓取網路資料。
*   **AI**：訓練電腦玩貪食蛇。
*   **網站**：用 Django 寫一個貪食蛇對戰平台。
*   這 18 週只是起點，你的超能力才剛覺醒。

---

## 📝 程式碼拆解 (The Final Architecture)

### 1. 狀態控制中心 (Game State Machine)
```python
while True:
    if state == "MENU":
        draw_menu()
        check_start_input()
    elif state == "PLAYING":
        snake.update()
        snake.draw()
        check_collisions()
    elif state == "GAMEOVER":
        draw_gameover()
        check_restart_input()
```
*   這就是 **架構 (Architecture)**。
*   乾淨、易讀、好維護。

### 2. 資料夾結構 (Project Structure)
```
MySnakeGame/
├── main.py        (入口)
├── assets/        (資源)
│   ├── sound/
│   └── image/
├── src/           (原始碼)
│   ├── snake.py
│   └── food.py
└── README.md      (說明書)
```
不要把所有檔案都丟在桌面！專業一點！

---

## ✨ Vibe Coding 小撇步：你的個人簽名 (Signature)

*   **視覺簽名**：你的蛇長得跟別人的不一樣嗎？是星星形狀？還是由文字組成的？
*   **彩蛋 (Easter Eggs)**：
    *   如果你取名叫 `LINUXFAB`，會不會觸發什麼隱藏關卡？
    *   在角落藏一個小小的簽名檔。
    *   加入這個小驚喜，玩家會感受到你的 **靈魂**。

---

## ⚠️ 最後的叮嚀 (Final Advice)

*   **KISS 原則**：**Keep It Simple, Stupid.**
    *   與其做出 100 個會當機的功能，不如做 3 個完美運作的亮點。
*   **備份 (Backup)**：
    *   在最後修改前，複製整份資料夾。
    *   相信我，你會感謝我的。

---

## 🏋️‍♂️ 課後練習

### 🎓 畢業考 (The Final Showcase)
1.  **你的第一份 README**：
    *   寫一個 `README.md`，用 Markdown 語法排版。
    *   放一張你遊戲的截圖 (Screenshot)。
2.  **慶功宴 (Demo Day)**：
    *   按下 F5 執行你的最終版遊戲。
    *   邀請旁邊的同學來玩。
    *   享受他們的尖叫聲與讚美。

---

## 📚 寶藏連結 (Reference)
*   [Awesome README](https://github.com/matiassingers/awesome-readme) (看看別人怎麼寫出漂亮的說明書)
*   [PyInstaller](https://pyinstaller.org/) (想把 Python 變成 .exe 檔給朋友玩？看這裡)
