**TechBlog-Baton** は、複数の外部ブログの最新記事を自動的に取得・表示するJekyllベースのサイトです。GitHub Actionsを活用して、記事のURLを追加するだけでタイトルとサムネイル画像を自動的に取得し、サイトに反映します。

## 目次

1. [セットアップ](#1-セットアップ)
2. [ブログURLの追加手順](#2-ブログurlの追加手順)
3. [ローカル環境の構築手順](#3-ローカル環境の構築手順)
4. [トラブルシューティング](#4-トラブルシューティング)
5. [カスタマイズ](#5-カスタマイズ)
6. [参考情報](#6-参考情報)

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

## 3. ローカル環境の構築手順

ローカルでサイトを確認する場合、以下の手順でJekyll環境を構築してください。

### ステップ1: `Gemfile` の確認または作成

1. プロジェクトディレクトリに移動し、`Gemfile` が存在しない場合は以下のコマンドで作成します。

   ```bash
   touch Gemfile
   ```

2. `Gemfile` に以下の内容を記述します。

   ```ruby
   source "https://rubygems.org"
   
   gem "jekyll", "~> 4.3.4"
   gem "webrick", "~> 1.7"
   ```

   **説明**:
   - `jekyll`: サイト生成に使用するGem。
   - `webrick`: Jekyll 4.x 系ではローカルサーバーに必要です。

### ステップ2: 必要なGemのインストール

1. `bundle install` コマンドを実行して、必要なGemをインストールします。

   ```bash
   bundle install
   ```

### ステップ3: Jekyllのローカルサーバー起動

1. ローカルサーバーを起動するには、以下のコマンドを実行します。

   ```bash
   bundle exec jekyll serve
   ```

2. ローカルサーバーが起動したら、ブラウザで以下のURLにアクセスしてサイトを確認できます。

   ```
   http://localhost:4000
   ```

---

## 4. トラブルシューティング

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

---

## 5. カスタマイズ

### a. スタイルの調整

`assets/css/style.css` を編集して、サイトのデザインをカスタマイズできます。

```css
/* コンテナ全体のスタイル */
.container {
  display: block;
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
  text-align: center;
  margin-bottom: 20px;
}

/* サムネイル画像のスタイル */
.thumbnail {
  width: 100%;
  max-width: 180px;
  height: auto;
  display: block;
  margin: 10px auto;
  border-radius: 5px;
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
```

---

## 6. 参考情報

- [Jekyll公式ドキュメント](https://jekyllrb.com/docs/)
- [GitHub Actions公式ドキュメント](https://docs.github.com/actions)
- [BeautifulSoup 公式ドキュメント](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [requests ライブラリの公式ドキュメント](https://docs.python-requests.org/en/latest/)
- [PyYAML公式ドキュメント](https://pyyaml.org/wiki/PyYAMLDocumentation)
