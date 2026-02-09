# 第 12 週 | 物件導向 (OOP)：打造你的程式樂高

> **給老師的備課筆記**：
> 這是課程中最難跨越的「邏輯之牆」。
> 學生會問：為什麼要把原本好好的程式碼變這麼複雜？
> 答案是：為了「擴張性」。如果未來要加 10 種食物、3 條蛇，OOP 是唯一的活路。

---

## 🎯 本週教學目標

1.  **類別 (Class)**：學會設計藍圖，而不只是手刻零件。
2.  **物件 (Object/Instance)**：學會從藍圖生產出一個個鮮活的個體。
3.  **封裝 (Encapsulation)**：把行為 (Method) 和資料 (Attribute) 裝在一起。

---

## 💡 深度比喻：Minecraft 的方塊 (Blueprint vs Instance)

想像你在玩 Minecraft：
*   **類別 (Class)**：是「泥土方塊」的定義。它定義了這個方塊看起來是什麼顏色、挖碎會掉落什麼。
*   **物件 (Object)**：是你放在地上的那 100 個泥土方塊。每個方塊都有自己的座標 `(x, y, z)`，但它們都共享同一個「藍圖」。
*   **方法 (Method)**：就是方塊被破壞時觸發的動作 `on_break()`。

---

## 📝 程式碼拆解 (核心語法)

### 1. 宣告藍圖：`class` 與 `__init__`
```python
class Snake:
    def __init__(self):
        self.body = [(400, 300)]
        self.color = (0, 255, 0)
```
*   `__init__` 就是「出生證明」。當你寫 `s = Snake()` 時，這個函數會自動執行。
*   `self` 就是「我的」。`self.color` 代表「這條蛇自己的顏色」。

### 2. 行動封裝：把動詞放進類別裡
```python
    def move(self):
        # 移動蛇身體的邏輯全部收進來
```
*   這讓你的主迴圈 `while True` 變得超級漂亮：只要寫 `snake.move()` 就好！

---

## ✨ Vibe Coding 小撇步：模組化之美

*   **程式碼美學**：專業程式設計師不喜歡把所有東西塞在同一個地方。當你把「蛇」的邏輯藏進類別裡，主程式看起來就像是在「讀劇本」一樣流暢。
*   **隨插即用**：想換蛇的顏色？改 `Snake.color` 就好。想讓蛇變快？改 `Snake.speed`。這就是「設計」的層次感。

---

## ⚠️ 國中生常見「self」大亂鬥

*   **死掉的變數**：如果你不加 `self.`，在 `__init__` 裡面定義的變數在離開發生後就會消失。
*   **忘記傳入 self**：定義方法時，第一個括號裡面一定要寫 `self`，否則 Python 會報錯說你給的參數不對。

---

## 🏋️‍♂️ 課後練習

1.  **蛇的個性**：給 `Snake` 增加一個 `name` 屬性，並在 `draw` 的時候把名字畫在頭頂上。
2.  **量產工廠**：在 `while` 迴圈外面一口氣創造 5 條 `snake1, snake2...`，然後讓它們在畫面上亂跑。

---

## 📚 參考來源
*   [Python OOP Beginner's Guide](https://realpython.com/python3-object-oriented-programming/)
*   [Why use OOP in Games?](https://news.ycombinator.com/item?id=30545934)
