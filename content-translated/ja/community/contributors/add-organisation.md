---
HasBanner: false
draft: false
sidebar: true
title: あなたの組織をQGIS貢献者に追加しましょう
type: page

---
{{<content-start >}}
# あなたの組織をQGIS貢献者に追加しましょう
ようこそ! あなたの組織がQGISに貢献している場合、私たちの [貢献者ページ](/community/contributors/) で紹介することができます。以下の簡単な手順に従ってくださいs:
____
## ステップ 1: 自分の組織の詳細を用意する
### 必要なもの
- 組織の名称、スローガン、ウェブサイトURL
- QGISとのかかわり合いの簡潔な説明
- QGISに貢献するチームメンバー達のGitHubユーザー名
- 組織のロゴ（web用に最適化されたPNG又はSVG）

____
## ステップ 2: テンプレートに入力する
このテンプレートをコピーし、自分の組織の情報でカスタマイズしてください:
```
{
  "name": "Your Organization Name",
  "subtitle": "Your tagline or motto",
  "image": "img/contributors/your-logo.png",
  "width": "200px",
  "url": "https://your-website.com",
  "description": "Brief description of your organization and how you contribute to QGIS.",
  "members": [
    {
      "username": "github_username",
      "author_names": "Full Name",
      "from": "2020-01-15",
      "to": null
    }
  ],
  "contributions": {
    "documentation": { "commits": 0, "last_contribution": null },
    "qgis_core": { "commits": 0, "last_contribution": null },
    "web_sites": { "commits": 0, "last_contribution": null }
  }
}
```
### フィールドの説明:
| フィールド | 説明 | 例 |
| --- | --- | --- |
| **name** | 組織の正式名称 | `"Kartoza"` |
| **subtitle** | 短めのスローガンか標語 | `"Mapping the Future"` |
| **image** | ロゴのファイル名（`static/img/contributors/` に加えてください） | `"img/contributors/kartoza-logo.png"` |
| **width** | ロゴの表示幅 | `"200px"` （そのままにしてください） |
| **url** | 自分のウェブサイト | `"https://kartoza.com"` |
| **description** | 簡潔な説明（２～３文） | `"Kartoza provides open-source GIS solutions..."` |
| **members** | チームメンバー達のGitHubユーザー名 | 下記参照 |
| **contributions** | そのまま残してください － スクリプトによって自動的に更新されます | ゼロやnull値のままにしてください |

### メンバー配列の説明:
- **username**: GitHubのユーザー名（完全に一致すること）
- **author_names**: Git コメントに現れる氏名。 "Jean Luc"` 又は複数の氏名は `"Jean Luc,Jean Lucas"` 。
- **from**: この人が自分の組織のための貢献を始めた日付 (YYYY-MM-DD)
- **to**: 活動中のときは `null` のまま残し、そうでなければ終了日を入れます (YYYY-MM-DD)

💡 **Tip:** 複数のメンバーを追加できます—各人用にメンバーオブジェクトを複製するだけです。
____
## ステップ 3: GitHub のプルリクエスト経由で提出します
### 選択肢 A: GitHub のウェブエディタを使う（最も簡単）
1. **ここをクリックしてファイルを直接編集してください:** [Edit organizations.json](https://github.com/qgis/QGIS-Website/edit/main/data/contributors/organizations.json)
   - GitHubがリポジトリを自動的にフォークしてくれます
2. ファイルの **末尾までスクロールしてください**
3. 直前のエントリの最後の `}` の後に **コンマを追加してください**
4. （ステップ 2から） **自分の組織のエントリを貼り付けてください**
5. **「変更をコミットする」をクリックし** 、次のような説明を与えてください: *"Add [自分の組織名称] to contributors"*
6. 緑のボタンをクリックして **プルリクエストを生成してください**

### 選択肢 B: フォークしてクローンする（上級ユーザー向け）
1. [QGIS-Website リポジトリ] (https://github.com/qgis/QGIS-Website/) をフォークしてください
2. 自分のフォークをローカルでクローンしてください
3. 自分のエントリを `data/contributors/organizations.json` に追加してください
4. 自分のロゴを `static/img/contributors/` に追加してください（ファイルサイズを最適化すること！）
5. コミットして変更をプッシュしてください
6. [プルリクエストを開く](https://github.com/qgis/QGIS-Website/pulls)

⚠️ **重要:** 自分の JSON が有効であることを確認してください！必要なら [JSON バリデーター](https://jsonlint.com/) を使ってください。
____
## ステップ 4: ロゴを追加する
自分のロゴを `static/img/contributors/` フォルダにアップロードしてください:
- **形式:** PNGまたはSVG
- **サイズ:** webに最適化してください（目標は100KB以下）
- **大きさ:** 幅は約 400-600px がよいです
- **命名法:** 小文字とハイフンを使ってください（例 `acme-geospatial.png` ）

____
## ステップ 5: 調査と承認
✨ プルリクエストを提出すると:
1. QGIS ウェブサイトチームはあなたの提出物を調査します
2. 私たちは小さな修正をお願いすることがあります
3. 承認されマージされると、あなたの組織が [貢献者のページ](/community/contributors/) に現れます！

____
あなたのQGISへの貢献に感謝します！ 🎉

{{<content-end >}}
