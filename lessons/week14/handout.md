# 第 14 週 | 聽覺盛宴：聲音的靈魂與回饋

> **給老師的備課筆記**：
> 聲音是遊戲回饋 (Feedback Loop) 的重要一環。
> 科學研究顯示：有音效的動作，玩家會覺得「反應更靈敏」。
> 重點：理解 Mixer 的非同步特性（呼叫 `play()` 後，程式會繼續往下跑，不會等聲音播完）。

---

## 🎯 本週教學目標

1.  **音頻管理 (Mixer)**：理解同步與異步播放。
2.  **檔案格式**：WAV 與 MP3 的使用時機。
3.  **錯誤防禦 (Error Handling)**：防止因為少了一個音效檔就讓整個遊戲崩潰。

---

## 💡 深度比喻：錄音機 vs 現場駐唱

*   **音效 (Sound)**：像是「按鈕印章」。按一下，發出一次聲音。你可以同時按好幾個印章（吃到食物 + 撞牆）。
*   **音樂 (Music)**：像是「現場駐唱」。你只能有一組樂手在台上。他們可以連續唱很久，但一次只能唱一首。
*   **程式翻譯**：
    *   `pygame.mixer.Sound` = 短音效，支援多聲道。
    *   `pygame.mixer.music` = 背景音樂，串流播放。

---

## 📝 程式碼拆解 (關鍵語法)

### 1. 預防性的載入
```python
try:
    eat_sound = pygame.mixer.Sound("assets/eat.wav")
except:
    print("找不到聲音檔，改用無聲模式")
    eat_sound = None
```
*   **專業提示**：永遠不要假設玩家的電腦裡一定有那些檔案。

### 2. 精準觸發
```python
if head == food:
    if eat_sound: eat_sound.play() # 只有在檔案存在時才播
```

---

## ✨ Vibe Coding 小撇步：音效設計

*   **音調隨機化 (Pitch Variation)**：如果你每次吃到東西的聲音都一模一樣，耳朵會疲勞。雖然 Pygame 調整音調比較麻煩，但你可以準備三個頻率略有不同的 `eat1.wav`, `eat2.wav` 隨機播放。
*   **環境氛圍 (Atmosphere)**：給背景音樂加一點淡淡的 `fadein` 效果。
    `pygame.mixer.music.play(-1, fade_ms=2000)`

---

## ⚠️ 常見陷阱 (Pitfalls)

*   **延遲問題**：如果你覺得按下按鍵後 0.5 秒才聽到聲音，那是緩衝區設定太大的問題。
*   **檔案格式**：Pygame 有時候會討厭某些採樣率的 MP3。如果播不出來，試著轉換成 **Ogg** 或 **WAV**。

---

## 🏋️‍♂️ 課後練習

1.  **節奏大師**：當蛇的長度越長，讓背景音樂的播放速度變快 (如果音樂格式支援)。
2.  **空間感**：根據食物的座標 (左或右)，調整音效的左右聲道平衡 (Panning)。

---

## 📚 參考來源
*   [Pygame Mixer Official Docs](https://www.pygame.org/docs/ref/mixer.html)
*   [How Audio Feedback Improves Gaming](https://www.gamedeveloper.com/audio/the-importance-of-sound-effects-in-video-games)
