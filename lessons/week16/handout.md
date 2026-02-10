# 第 16 週 | 基因工程：繼承與多型 (Advanced OOP)

> **給教練的戰術板 (Coach's Corner)**：
> 這一週我們要用 OOP 最強大的武器：**繼承 (Inheritance)**。
> 比起從頭寫一個 `class Poison` 和 `class Food`，繼承能讓你少寫 80% 的廢話。
> 重點：強調 **「多型 (Polymorphism)」** —— 讓主程式不用關心對手是誰，只要知道它能「被吃」。
> 這是程式設計師的 **偷懶 (Efficiency)** 美學。

---

## 🎯 本週攻略目標 (Mission Objectives)

1.  **繼承 (Inheritance)**：父與子的關係。如何不勞而獲 (繼承父類的程式碼)。
2.  **覆寫 (Override)**：青出於藍。子類別如何修改父類別的行為。
3.  **多型 (Polymorphism)**：把一堆不同的東西裝在同一個 List 裡，並統一呼叫同一個方法。

---

## 📊 簡報精華 (Slide Highlights)

### Slide 1: 超級英雄的披風 (The Cape)
*   **普通人 (Base Class)**：`Person`。會走路、會說話。
*   **超人 (Sub Class)**：`Class Superman(Person)`。
    *   他 **繼承** 了普通人的一切 (不用重寫走路和說話)。
    *   但他 **多了一個** `fly()` 方法。
    *   他 **覆寫 (Overwrite)** 了 `strength` 屬性 (變得超強)。
*   這就是繼承。你不需要重新發明輪子，你只要幫輪子裝上火箭推進器。

### Slide 2: 貪食蛇的軍火庫 (The Arsenal)
*   **Food (父)**：基礎食物。吃了+1分。
*   **Poison (子)**：毒藥。繼承 Food，但吃了扣分 (或是死掉)。
*   **GoldenApple (子)**：金蘋果。繼承 Food，但吃了+50分。
*   他們 **都是 (is-a)** Food。所以可以放在同一個清單 `items = []` 裡。

### Slide 3: 隨機生成器 (Loot Table)
```python
possible_items = [Food, Poison, GoldenApple]
ItemClass = random.choices(possible_items, weights=[70, 20, 10])[0]
new_item = ItemClass() # 生產！
```
*   這行程式碼讓我們可以像上帝一樣，根據機率創造萬物。

---

## 📝 程式碼邏輯拆解 (Code Breakdown)

### 1. 繼承的語法
```python
class GoldenApple(Food): # 括號裡寫爸爸的名字
    def __init__(self):
        super().__init__() # 記得先呼叫爸爸的初始化！(孝道)
        self.color = GOLD  # 然後再改成自己的顏色
        
    def effect(self, snake):
        return 50 # 覆寫：金蘋果價值連城
```

### 2. 多型的威力 (The Power of Polymorphism)
在主迴圈裡：
```python
# item 可能是毒藥，也可能是蘋果，程式碼完全不用改！
item.draw(screen)
score += item.effect(snake)
```
如果沒有多型，你就要寫：
```python
if type(item) == Food: score += 1
elif type(item) == Poison: score -= 10
elif type(item) == GoldenApple: score += 50
...
```
這就是一般的爛程式碼 (`Spaghetti Code`) 與架構師的差別。

---

## 🏋️‍♂️ 實戰演練 (Hands-on Labs)

### 🟢 基礎題 (Item Factory)
1.  **毒蘑菇**：創造一個 `Mushroom` 類別，繼承自 Food。
    *   顏色：紫色。
    *   效果：吃了之後，蛇的速度變慢一半 (持續 5 秒)。(Debuff)
2.  **幸運草**：創造一個 `Clover` 類別。
    *   顏色：綠色。
    *   效果：吃了之後，下一次撞牆不會死 (無敵護盾)。

### 🟡 進階題 (Polymorphic Boss)
1.  **動態道具**：
    *   讓 `GoldenApple` 不會乖乖待在原地，而是會每秒鐘隨機跳動一次 (繼承 `Food` 的 `update` 方法並改寫它)。
    *   這會讓遊戲變成「打地鼠」。
2.  **時空裂縫 (Portal)**：
    *   這有點難。繼承 Food，但它是一對 (A 和 B)。
    *   當蛇頭碰到 A，直接把蛇頭座標改成 B。
    *   這需要你修改 `effect` 方法，讓它能存取 `snake` 物件並修改其座標。

---

## 📚 寶藏連結 (Reference)
*   [Inheritance vs Composition](https://stackoverflow.com/questions/49002/prefer-composition-over-inheritance) (工程師的經典辯論，以後你會懂的)
*   [Design Patterns: Factory Method](https://refactoring.guru/design-patterns/factory-method) (如何優雅地生產物件)
