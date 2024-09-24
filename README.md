# TechBlog-Baton

**TechBlog-Baton** は、複数の外部ブログの最新記事を自動的に取得・表示するJekyllベースのサイトです。GitHub Actionsを活用して、記事のURLを追加するだけでタイトルとサムネイル画像を自動的に取得し、サイトに反映します。

## 目次

1. [セットアップ](#1-セットアップ)
2. [ブログURLの追加手順](#2-ブログurlの追加手順)
3. [トラブルシューティング](#3-トラブルシューティング)
4. [カスタマイズ](#4-カスタマイズ)
5. [参考情報](#5-参考情報)

---

## 1. セットアップ

初めてリポジトリをクローンする場合やセットアップが必要な場合は、以下の手順に従ってください。

### a. リポジトリのクローン

```bash
git clone https://github.com/あなたのユーザー名/リポジトリ名.git
cd リポジトリ名
```

### b. 必要なファイルの確認

- `_data/external_articles.yml`: 外部ブログのURLを管理するファイル。
- `fetch_opengraph.py`: URLからOpen Graphメタデータを取得するスクリプト。
- `.github/workflows/update_articles.yml`: GitHub Actionsのワークフローファイル。
- `_includes/article_list.html`: 記事一覧を表示するテンプレート。
- `assets/css/style.css`: スタイルシート。
- `index.md`: ホームページのMarkdownファイル。

---

## 2. ブログURLの追加手順

新しいブログ記事をサイトに追加する際の手順を以下に示します。この手順に従うことで、ローカル環境を使用せずにGitHub上で全ての操作を完結できます。

### ステップ1: `_data/external_articles.yml` にURLを追加

1. **GitHubリポジトリにアクセス**し、`_data/external_articles.yml` ファイルを開きます。

2. **新しい記事のURLを追加**します。以下のように、`url` フィールドを追加してください。

   ```yaml
   articles:
     - url: "https://tech.findy.co.jp/entry/2024/09/20/090000"
     - url: "https://engineering.visional.inc/blog/491/soda/"
     - url: "https://example.com/new-article"  # 新しい記事を追加
   ```

   **ポイント:**

   - 各記事はリスト形式で記述します。
   - コメント（`#`）を使用して説明を追加することも可能です。

### ステップ2: 変更をコミットしてプッシュ

1. **ファイルを編集後**、ページ下部の「**Commit changes**」ボタンをクリックします。

2. **コミットメッセージを入力**します。例:

   ```
   Add new article URL: https://example.com/new-article
   ```

3. **「Commit changes」をクリック**して変更を保存します。

### ステップ3: GitHub Actionsが自動的にスクリプトを実行

1. **GitHub Actionsの実行を確認**します。リポジトリの「**Actions**」タブに移動し、「**Update Articles Data**」ワークフローがトリガーされていることを確認します。

2. **ワークフローの進行状況を確認**します。成功すれば、`_data/articles_data.yml` が更新され、サイトが再ビルドされます。

### ステップ4: サイトの確認

1. **数分待って**、GitHub Pagesがサイトを再ビルドします。

2. **サイトにアクセス**し、新しく追加した記事が正しく表示されていることを確認します。

   例: `https://あなたのユーザー名.github.io/リポジトリ名/`

---

## 3. トラブルシューティング

サイトに変更が反映されない場合、以下の点を確認してください。

### a. GitHub Actionsのログ確認

1. **「Actions」タブ**に移動します。

2. **「Update Articles Data」ワークフロー**を選択し、最新の実行ログを確認します。

3. **エラーや警告**がないかチェックし、必要に応じて修正します。

### b. データファイルの内容確認

1. **`_data/articles_data.yml`** が最新の状態に更新されていることを確認します。

2. **YAMLの構文確認**:
   
   - インデントやコロンの後にスペースが必要です。

   ```yaml
   articles:
     - url: "https://example.com/new-article"
       title: "新しい記事のタイトル"
       image: "https://example.com/path/to/eyecatch.jpg"
       published: "2024-04-01"
   ```

### c. テンプレートの確認

1. **`_includes/article_list.html`** が正しく設定されているか確認します。

   ```html
   <div class="article-list">
     {% for article in site.data.articles_data.articles %}
       <div class="article-item">
         <a href="{{ article.url }}" target="_blank" rel="noopener noreferrer">
           <img src="{{ article.image }}" alt="{{ article.title }}" class="thumbnail">
           <h3>{{ article.title }}</h3>
         </a>
       </div>
     {% endfor %}
   </div>
   ```

2. **`index.md`** に `{% include article_list.html %}` が正しく挿入されているか確認します。

   ```markdown
   ---
   layout: default
   title: 企業ブログリンク集
   ---

   <h1>企業ブログリンク集</h1>

   {% include article_list.html %}
   ```

### d. キャッシュのクリア

1. **ブラウザのキャッシュをクリア**して、最新のサイトが表示されているか確認します。

2. **GitHub Pagesのキャッシュ**が原因で表示が遅れる場合があります。時間を置いて再度確認してください。

---

## 4. カスタマイズ

### a. スタイルの調整

`assets/css/style.css` を編集して、サイトのデザインをカスタマイズできます。

```css
/* コンテナ全体のスタイル */
.container {
  display: block; /* フレックスレイアウトを解除 */
  height: auto;
  overflow: visible;
}

/* メインコンテンツのスタイル */
.content {
  width: 100%;
  padding: 20px;
}

/* 記事アイテムのスタイル */
.article-item {
  text-align: center; /* コンテンツを中央揃えにする（任意） */
  margin-bottom: 20px;
}

/* サムネイル画像のスタイル */
.thumbnail {
  width: 100%;             /* 親要素の幅に合わせる */
  max-width: 180px;        /* サムネイルの最大幅を180pxに設定 */
  height: auto;            /* アスペクト比を維持して高さを自動設定 */
  display: block;          /* ブロック要素として扱い、他の要素と独立させる */
  margin: 10px auto;       /* 上下に10pxのマージンを設定し、中央揃え */
  border-radius: 5px;      /* 角を丸くする（任意） */
}

/* 公開日のスタイル */
.published-date {
  font-size: 0.9em;
  color: #666;
  margin-bottom: 5px;
}

/* レスポンシブ対応 */
@media (max-width: 768px) {
  /* サムネイルの最大幅を調整 */
  .thumbnail {
    max-width: 150px;
  }
}

@media (max-width: 600px) {
  /* サムネイルがさらに狭くなる場合 */
  .thumbnail {
    max-width: 120px;
  }
}

/* その他の基本スタイル */
h1, h2, h3 {
  margin-top: 20px;
  margin-bottom: 10px;
  font-weight: bold;
  line-height: 1.2em;
}
```

### b. 追加情報の表示

必要に応じて、記事の公開日や概要などの追加情報を表示できます。

1. **データファイルの更新**:

   ```yaml
   articles:
     - url: "https://example.com/new-article"
       title: "新しい記事のタイトル"
       image: "https://example.com/path/to/eyecatch.jpg"
       published: "2024-04-01"
       summary: "この記事の概要をここに記述します。"
   ```

2. **テンプレートの更新**:

   ```html
   <div class="article-list">
     {% for article in site.data.articles_data.articles %}
       <div class="article-item">
         <a href="{{ article.url }}" target="_blank" rel="noopener noreferrer">
           <img src="{{ article.image }}" alt="{{ article.title }}" class="thumbnail">
           <h3>{{ article.title }}</h3>
           <p class="published">{{ article.published }}</p>
           <p class="summary">{{ article.summary }}</p>
         </a>
       </div>
     {% endfor %}
   </div>
   ```

3. **スタイルの追加**:

   ```css
   .article-item .published {
     font-size: 0.9em;
     color: #666;
   }

   .article-item .summary {
     font-size: 0.9em;
     color: #555;
   }
   ```

---

## 5. 参考情報

- [Jekyll公式ドキュメント](https://jekyllrb.com/docs/)
- [GitHub Actions公式ドキュメント](https://docs.github.com/actions)
- [BeautifulSoup 公式ドキュメント](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests ライブラリの公式ドキュメント](https://docs.python-requests.org/en/latest/)
- [PyYAML公式ドキュメント](https://pyyaml.org/wiki/PyYAMLDocumentation)

---

## 補足情報

### サムネイル画像の調整

サムネイル画像のサイズが適切に反映されない場合、以下の点を確認してください。

1. **CSSの適用確認**:

   ブラウザのデベロッパーツール（右クリック → 「検証」）を使用して、`img.thumbnail` に適用されているCSSスタイルを確認します。特に、`max-width: 180px;` が適用されているかを確認してください。

2. **CSSの優先順位確認**:

   他のスタイルシートやテーマのスタイルが優先されている場合、`max-width` が上書きされている可能性があります。必要に応じて、CSSセレクタの優先順位を高めるか、`!important` を使用します。

   ```css
   .thumbnail {
     max-width: 180px !important;
   }
   ```

   **注意**: `!important` は最後の手段として使用し、他のスタイルとの整合性に注意してください。

3. **画像の元サイズ確認**:

   サムネイル画像自体が非常に大きいサイズで提供されている場合、`max-width` を適用しても期待通りに縮小されない可能性があります。画像の解像度を確認し、必要に応じて適切なサイズにリサイズしてください。

4. **キャッシュのクリア**:

   変更後、ブラウザのキャッシュが古いスタイルを保持している場合があります。ブラウザのキャッシュをクリアして最新のスタイルが反映されるようにしてください。

### サイドバーの削除に伴うテンプレートの修正

サイドバーを削除したため、関連するテンプレートやCSSスタイルも適宜修正しました。以下の点を確認してください。

1. **`_layouts/default.html` の修正**:

   サイドバーとリサイズバーを削除し、シンプルなレイアウトに戻しました。

   ```html
   <!DOCTYPE html>
   <html lang="ja">
   <head>
     <meta charset="UTF-8">
     <title>{{ page.title }}</title>
     <link rel="stylesheet" href="{{ "/assets/css/style.css" | relative_url }}">
   </head>
   <body>
     <div class="container">
       <!-- メインコンテンツ -->
       <main class="content" id="main-content">
         {{ content }}
       </main>
     </div>
   </body>
   </html>
   ```

2. **不要なCSSの削除**:

   サイドバー関連のCSSスタイルを削除し、メインコンテンツとサムネイル画像に関連するスタイルのみを残しました。

   ```css
   /* コンテナ全体のスタイル */
   .container {
     display: block; /* フレックスレイアウトを解除 */
     height: auto;
     overflow: visible;
   }

   /* メインコンテンツのスタイル */
   .content {
     width: 100%;
     padding: 20px;
   }

   /* 記事アイテムのスタイル */
   .article-item {
     text-align: center; /* コンテンツを中央揃えにする（任意） */
     margin-bottom: 20px;
   }

   /* サムネイル画像のスタイル */
   .thumbnail {
     width: 100%;             /* 親要素の幅に合わせる */
     max-width: 180px;        /* サムネイルの最大幅を180pxに設定 */
     height: auto;            /* アスペクト比を維持して高さを自動設定 */
     display: block;          /* ブロック要素として扱い、他の要素と独立させる */
     margin: 10px auto;       /* 上下に10pxのマージンを設定し、中央揃え */
     border-radius: 5px;      /* 角を丸くする（任意） */
   }

   /* 公開日のスタイル */
   .published-date {
     font-size: 0.9em;
     color: #666;
     margin-bottom: 5px;
   }

   /* レスポンシブ対応 */
   @media (max-width: 768px) {
     /* サムネイルの最大幅を調整 */
     .thumbnail {
       max-width: 150px;
     }
   }

   @media (max-width: 600px) {
     /* サムネイルがさらに狭くなる場合 */
     .thumbnail {
       max-width: 120px;
     }
   }

   /* その他の基本スタイル */
   h1, h2, h3 {
     margin-top: 20px;
     margin-bottom: 10px;
     font-weight: bold;
     line-height: 1.2em;
   }
   ```

---

## 最終確認

1. **ファイルの保存**:
   - `_layouts/default.html`
   - `_includes/article_list.html`
   - `assets/css/style.css`
   - `index.md`

2. **ローカルでのビルドと確認**:

   ```bash
   bundle install
   bundle exec jekyll serve
   ```

   ブラウザで `http://localhost:4000` にアクセスし、サイトが正しく表示されていることを確認します。

3. **GitHubへのプッシュ**:

   ```bash
   git add .
   git commit -m "サイドバーを削除し、サムネイルサイズを180pxに調整"
   git push origin main
   ```

   GitHub Actionsが自動でビルドし、サイトがデプロイされます。

4. **GitHub Pagesの確認**:

   リポジトリのGitHub Pages URL（例: `https://あなたのユーザー名.github.io/リポジトリ名/`）にアクセスし、サイトが正しく表示されていることを確認します。
   
