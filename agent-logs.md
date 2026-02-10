### 2026-02-10 08:12:00
*   **重點**: 全面重潤 1-18 週教學講義，轉化為「Vibe Coding」戰術手冊。
*   **影響**:
    *   **深度進化**: 將 `lessons/week01` 到 `lessons/week18` 的 `handout.md` 全數重寫。
    *   **風格定義**: 捨棄機器人語言，導入「教練戰術板 (Coach's Corner)」、「攻略目標 (Mission Objectives)」及「Vibe Coding 小撇步」等專欄位。
    *   **教學法升級**: 強化了視覺化比喻（如變數置物櫃、火車車廂、Minecraft 藍圖），並加入大量關於打擊感 (Juiciness)、心流 (Flow) 與遊戲美學的專業心法。
*   **結果**: 課程教材從「語法手冊」進化為「開發者攻略」，能有效點燃學生的創造熱情，並建立專業的工程思維。
*   **更新者**: Antigravity Agent

### 2026-02-10 02:10:00 (Asset Package Preparation)
*   **重點**: 建立遊戲資產包 (Asset Package) 並實作自動化生成腳本。
*   **影響**:
    *   **音效資產**: 新增 `assets/make_sounds.py`，利用 Python `wave` 模組透過數學運算直接生成 `eat.wav` (高頻嗶嗶聲) 與 `game_over.wav` (雷射下降音)，解決課程專案對外部資源的依賴。
    *   **目錄結構**: 建立 `assets/sounds` 與 `assets/images` 標準化目錄結構。
    *   **開發指南**: 新增 `assets/README.md`，提供 40x40 像素資產規格、Vibe 建議調色盤、以及推薦的第三方免費資源網站 (Kenney.nl 等)。
*   **結果**: 課程專案現在具備完整的音效回饋能力，學員除了寫遊戲邏輯，也能體驗到「程式化音效 (Procedural Audio)」的開發樂趣。
*   **更新者**: antigravity agent

### 2026-02-10 02:00:00 (Week 09-18 Handout Enhancement)
*   **重點**: 大幅強化第 09 週至第 18 週的學生講義 (`handout.md`)，增加視覺化比喻與「Vibe Coding」設計心法。
*   **影響**:
    *   **內容升級**:
        *   導入 **Minecraft 方塊比喻** (W12) 與 **紅綠燈狀態機比喻** (W11)。
        *   加入 **心流理論 (Flow State)** (W15) 與 **音效回饋圈** (W14) 等遊戲設計觀念。
        *   增設 **Vibe Coding 小撇步**：螢幕震動 (Screen Shake)、呼吸燈效果 (Pulse)、彩虹體 (Rainbow Trail) 等視覺特效實作指南。
        *   增加 **⚠️ 常見陷阱**：解決 Font 記憶體洩漏、HSV 轉換、全域變數污染等初學者痛點。
    *   **檔案範圍**: `lessons/week09/handout.md` 到 `lessons/week18/handout.md`。
*   **結果**: 學生讲義從單純的程式筆記進化為全方位的遊戲開發指南，結合了程式邏輯、數學美學與開發者心法。
*   **更新者**: antigravity agent
