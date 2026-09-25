# AI to Agent 漫劇製作流程

把故事拆成可執行鏡頭，用VAD看懂流程、用VAC定義任務與驗收，讓Agent按規格工作，人保留導演決策。

**版本：0.1.0｜日期：2026-09-25｜類型：方法論＋教學教材｜授權：保留所有權利**

AI Coach 益力康陳董 x CGM Coach 血糖教練 | 2026 AI to Agent

![全流程總覽](assets/images/01-overview.png)

## 為什麼需要這套流程

漫劇製作常卡在人物不一致、道具跳位、反覆抽卡與素材難以交接。本專案把工作拆成有輸入、有產物、有驗收的關卡，讓問題可以定位、重做與追溯。

## 內容與範圍

包含四張VAC圖卡、每頁約500字使用介紹、八步驟SOP、任務範本、完整規格案例及驗收表。這是可供人與Agent閱讀的規格套件，**沒有內建自動生圖、生影片、口型同步或剪輯API**。不需要安裝應用程式；若要實際產片，另選具備所需能力的工具與帳號。

## 八步驟與交付

理解劇情 → 拆解腳本 → 設計分鏡 → 鎖定資產 → 生成圖片 → 生成影片 → 粗剪精剪 → 成片驗收。

- 輸入：故事、目標受眾、參考圖、片長、比例與製作限制。
- 輸出：分鏡表、核准資產、鏡頭素材、成片、素材索引及QC紀錄。
- 驗收：角色與場景連貫、動作正確、劇情清楚、影音同步、格式符合用途，最後人工核准。

詳細分工見[架構與SOP](docs/architecture.md)，欄位與例外見[VAC規格](docs/vac-spec.md)。

## 快速開始

1. 依序閱讀下方四頁圖卡介紹。
2. 填寫[資產設定表](templates/asset-bible.md)與[分鏡表](templates/storyboard.csv)。
3. 複製[Shot VAC範本](templates/shot-vac.json)，補齊真實參考、時間與成本限制。
4. 對照[30秒宮殿案例](examples/palace-scene.md)與[單鏡JSON案例](examples/palace-shot-vac.json)。案例尚未渲染。
5. 生成後填[逐鏡QC](templates/shot-qc.csv)，剪輯後完成[成片驗收](templates/final-qc.md)，保存[素材索引](templates/asset-index.csv)。

## 依頁碼使用介紹

每頁各約500字，對應使用者提供的最終圖卡。

| 頁碼 | 主題 | 使用介紹 | 圖片 |
|---|---|---|---|
| 01/04 | 全流程總覽 | [閱讀第1頁](docs/01-usage.md) | [原圖](assets/images/01-overview.png) |
| 02/04 | 前製 VAC | [閱讀第2頁](docs/02-usage.md) | [原圖](assets/images/02-preproduction.png) |
| 03/04 | 生成 VAC | [閱讀第3頁](docs/03-usage.md) | [原圖](assets/images/03-generation.png) |
| 04/04 | 交付 VAC | [閱讀第4頁](docs/04-usage.md) | [原圖](assets/images/04-delivery.png) |

## 適用場景

適合AI漫劇、品牌故事短片、企業教學及跨工具的規格交接。不適用於要求不經人工覆核、零錯誤或保證一致性的全自動大量產片。

## 教學與示例

[90分鐘規格演練](docs/teaching.md)提供先備能力、練習與100分評量。宮殿案例把30秒拆成六鏡；單鏡示例演練皇帝拍桌、茶杯位置與重試上限，沒有聲稱已完成影片實測。

## 目錄

- `docs/`：四頁介紹、閱讀順序、架構、VAC規格、教學與GitHub上傳方式。
- `assets/images/`：四張最終圖卡；`assets/manifest.json`記錄來源與雜湊。
- `templates/`：資產表、分鏡表、Shot VAC、逐鏡與成片QC、素材索引。
- `examples/`：30秒六鏡案例與一份已填寫的Shot VAC示例。
- `scripts/validate_repo.py`：檢查本地路徑、JSON、圖片雜湊與套件完整性。
- `VERSION`：專案版本來源；`project.json` 為中繼資料，版本須與其一致。
- 根目錄其他文件：授權／版權／素材聲明、變更紀錄、貢獻規範、Agent規則、檢查報告與Release草稿。

## 檢查

選用Python 3執行：

```bash
python3 scripts/validate_repo.py
```

此檢查不呼叫付費工具，不生成影片，也不自動判定圖片內容與授權。已完成檢查及未驗證項目見[檢查報告](validation-report.md)。

## 版本與後續計畫

0.1.0為方法論初版；欄位可能依實作經驗調整。[變更紀錄](CHANGELOG.md)記錄已完成內容。[發布說明](RELEASE_NOTES.md)為草稿。

後續可擴充：真實工具adapter、自動記錄成本、驗收證據整理及經授權的端到端實測；以上尚未實作。

## 版權與授權

作者品牌署名不直接推定法律權利人。本專案採保留所有權利，未授予開源授權，不能視為MIT或CC教材；詳見[LICENSE](LICENSE)、[版權聲明](COPYRIGHT.md)與[素材來源](THIRD_PARTY_NOTICES.md)。Logo、人物形象與圖卡的使用範圍尚待權利人確認，未經同意不得使用。

## 上傳與貢獻

完整操作見[GitHub上傳指南](docs/github-publishing.md)。版本以git tag標示。修改方式見[CONTRIBUTING](CONTRIBUTING.md)。
