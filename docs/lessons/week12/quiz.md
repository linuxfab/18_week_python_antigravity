# Week 12 | 隨堂測驗 (Quiz)：物件導向程式設計 (OOP)

> **測驗目標**：檢測學生對類別 (Class)、實例 (Instance)、初始化函數 (`__init__`) 及 `self` 關鍵字的理解。
> **測驗時間**：10 分鐘

---

## 🟢 第一部分：是非題 (True/False)

1.  (  ) 「類別 (Class)」就像是設計圖，而「實例 (Instance)」是根據設計圖做出來的真實物件。
2.  (  ) 在 Python 類別中定義函數時，第一個參數通常必須是 `self`。
3.  (  ) `__init__` 函數是當我們建立一個新物件時，Python 會自動幫我們執行的初始化函數。
4.  (  ) 如果我們有兩個 Snake 物件 `s1` 和 `s2`，修改 `s1.color` 也會同時改變 `s2.color`。
5.  (  ) 物件導向程式設計 (OOP) 的主要目的之一是提高程式碼的重用性與可讀性，雖然一開始寫起來可能比較繁瑣。

---

## 🟡 第二部分：程式碼填空 (Code Completion)

請將下面的 `Food` 類別補充完整，使其能隨機出現在畫面上。

```python
import random

# 1. 定義類別
class Food:
    # 2. 初始化函數
    def ______(self):
        self.block_size = 40
        self.randomize_position()

    def randomize_position(self):
        # 產生隨機座標與網格對齊
        self.x = random.randint(0, 19) * self.block_size
        self.y = random.randint(0, 14) * self.block_size

    def draw(self, surface):
        # 3. 使用 self 存取自己的屬性
        rect = pygame.Rect(______.x, ______.y, ______.block_size, ______.block_size)
        pygame.draw.rect(surface, (255, 0, 0), rect)

# 主程式中建立物件
my_apple = ______()
```

---

## 🔴 第三部分：腦力激盪 (Logic Challenge)

1.  **擴充思考**：如果我們要新增一種「毒蘋果」物件，它繼承自 `Food` 但顏色是紫色的。你會怎麼設計這個繼承結構？
    *   答案：`class PoisonFood(______):` (提示：括號內要填什麼?)

2.  **多物件管理**：如果我們想在畫面上同時生成 5 顆蘋果，我們應該用什麼資料結構來管理它們？
    *   答案：____________________ (例如：List, Dictionary, Tuple?)

---

## 💡 解答與解析

### 是非題
1. **True**
2. **True**
3. **True**
4. **False** (實例屬性是獨立的)
5. **True**

### 程式碼填空
1. `class`
2. `__init__`
3. `self`, `self`, `self`, `self`
4. `Food`

### 腦力激盪
1. `Food` (繼承自 Food 類別)
2. List (列表，例如 `foods = [Food() for _ in range(5)]`)
