# 第 16 週 | 擴充功能：超能力與基因工程

> **給老師的備課筆記**：
> 這一週我們要玩轉 OOP 的進階技巧：**繼承 (Inheritance)**。
> 比起從頭寫一個新類別，繼承能讓你少寫 80% 的廢話。
> 重點：強調「多型 (Polymorphism)」—— 讓主程式不用關心對手是誰，只要知道它能「被吃」。

---

## 🎯 本週教學目標

1.  **繼承 (Inheritance)**：父與子的關係，如何子承父業。
2.  **多型 (Polymorphism)**：同一個方法名稱，根據物件不同而有不同行為。
3.  **創意擴充**：如何快速增加多樣化的遊戲道具。

---

## 💡 深度比喻：超級英雄的披風 (Inheritance)

*   **普通人 (Food)**：有生命、能移動、有名字。
*   **超能者 (PowerUp)**：繼承了普通人的所有特徵，但**多了一個**「飛翔」或「隱形」的能力。
*   **程式翻譯**：
    *   `class Food`: 基礎
    *   `class Poison(Food)`: 它繼承了座標、繪圖方法，但修改了「被吃掉後的得分邏輯」。

---

## 📝 程式碼拆解 (繼承的魔法)

### 1. 覆寫方法 (Override)
```python
class GoldenApple(Food):
    def effect(self, snake):
        # 普通蘋果加 10，金蘋果加 50！
        return 50
```

### 2. 隨機生成器
```python
items = [Food(), Poison(), GoldenApple()]
item = random.choice(items)
# 這裡最神：不管是哪種 item，我們都只要執行這兩行
item.draw(screen)
score += item.effect(snake)
```
這就是**多型**！主程式不需要寫 `if item == poison... else if apple...`。

---

## ✨ Vibe Coding 小撇步：浮空文字 (Floating Text)

*   **即時反饋**：吃到好東西時，在食物的位置出現一個「+50」的文字並緩緩飄上去消失。這會讓玩家覺得自己「賺大了」。
*   **顏色對比**：毒蘋果用紫色、加速用黃色、普通蘋果用紅色。利用顏色心理學指引玩家。

---

## ⚠️ 常見陷阱 (Pitfalls)

*   **忘記呼叫 super()**：如果你在子類別自定義了 `__init__` 卻忘了寫 `super().__init__()`，爸爸預設好的屬性（比如座標）就不會幫你設定好。
*   **過度繼承**：不要繼承太多層（爺爺、老爺爺...），這會讓你的程式碼變得很難找 Bug。

---

## 🏋️‍♂️ 課後練習

1.  **磁鐵道具 (Magnet)**：繼承 Food，吃到後讓蛇在接下來 10 秒內可以自動「吸」附近的食物。
2.  **時空裂縫 (Portal)**：生一組傳送門食物，吃到 A 從 B 出現。

---

## 📚 參考來源
*   [Inheritance vs Composition](https://stackoverflow.com/questions/49002/prefer-composition-over-inheritance) (工程師的經典辯論)
*   [The power of Polymorphism in Games](https://www.toptal.com/game/video-game-design-patterns)
