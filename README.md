# 株式会社ワン・ストーリー 新サイト（静的サイト）

現サイト（rika-hirasawa.com）の雰囲気 — 白基調・明朝体・中央揃え・筆記体の英字見出し・
淡いグリーン／ベージュの帯・植物イラスト — を踏襲したまま、内容を新しい事業内容に入れ替えた静的サイトです。

## ファイル構成

```
index.html        TOP
about.html        私たちについて（想い／代表メッセージ／チーム／ビジョン）
business.html     企業・組織を整える（メイン事業）
program.html      プログラム（1Day講座／2日間合宿／伴走サポート）
human.html        人を整える
wisdom.html       日本の智慧をつなぐ
future.html       次世代へつなぐ
column.html       お知らせ・コラム
contact.html      お問い合わせ
tokushoho.html    特定商取引法に基づく表記（雛形）
assets/
  style.css       全ページ共通のデザイン
  main.js         スマホメニュー／スクロール表示
  contact.js      お問い合わせフォームの送信処理（★送信先URLをここに設定）
  logo.png        ロゴ（縦組み・ヘッダー用）
  logo-wide.png   ロゴ（横組み・予備）
  favicon.png     ブラウザタブのアイコン
  botanical.svg   各ページ左上の植物イラスト
images/rika.jpg   代表写真（TOPの自己紹介／私たちについて／お問い合わせで使用）
docs/onestory-service.pdf   サービス資料（営業提案書）
gas-form.gs       Google Apps Script用（送信スクリプトの控え）
build.py          各HTMLを生成したスクリプト（納品後は不要／文言一括修正に使えます）
```

## 公開方法（GitHub Pages）

このフォルダの中身をそのままリポジトリの直下に置けば公開できます。

- `CNAME` … 独自ドメイン（rika-hirasawa.com）の設定ファイル。**消さないでください**
- `.nojekyll` … GitHub Pages の変換処理を止めるための空ファイル。**消さないでください**

DNS設定（ドメイン管理会社側）

| 種別 | ホスト名 | 値 |
|---|---|---|
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | （GitHubユーザー名）.github.io |

※ Wixを指していた既存のAレコード・CNAMEは削除してください。

他のサーバー（エックスサーバー等、Netlify、Cloudflare Pages）でも、
フォルダの中身をアップロードするだけで公開できます。

## 差し替えが必要な箇所

### 1. お問い合わせフォーム（送信先：onestory310@gmail.com）

フォーム本体は contact.html に組み込み済みで、送信先も **設定済み** です。
（Google Apps Script のウェブアプリURLを `assets/contact.js` の `FORM_ENDPOINT` に設定）

変更したい場合は `assets/contact.js` の `FORM_ENDPOINT` を書き換えてください。

送信されると onestory310@gmail.com に通知メールが届き、問い合わせた方には自動返信が送られます。
スクリプト本体は同梱の `gas-form.gs` と同じ内容で、Apps Script 側で編集できます。

> **ローカル（file:// でHTMLを直接開いた状態）では送信テストができません。**
> サーバーにアップロードしてからテストしてください。

#### フォームの項目を変えたいとき

contact.html の `<form class="contact-form">` の中を編集してください。
`name="..."` に入れた日本語が、そのままメールの見出しになります。

### 2. 写真

`images/` フォルダに写真を入れ、各ページのグレーの枠（`<div class="ph">…</div>` や
`<div class="thumb">…</div>`）を `<img src="images/○○.jpg" alt="">` に置き換えてください。

想定している写真:

| ファイル名 | 使う場所 | 状態 |
|---|---|---|
| images/rika.jpg | TOP自己紹介／about.html／contact.html | **設置済み** |
| images/hero.jpg | TOP メインビジュアル（横長） | 未設置（任意） |
| images/member01〜03.jpg | about.html チーム紹介 | 未設置 |
| images/team.jpg | about.html チーム全体写真 | 未設置 |
| images/human.jpg | human.html | 未設置 |
| images/wisdom.jpg | wisdom.html | 未設置 |

### 3. メインビジュアル（任意）

TOPの一番上は現在、余白とキャッチコピーだけのデザインです。
横長の写真を使いたい場合は `images/hero.jpg` として置き、index.html の
`<div class="hero-visual">` を `<div class="hero-visual has-photo">` に変えてください。
（縦長の写真だと顔が切れてしまうため、横位置で撮った写真がおすすめです）

### 4. 会社情報

contact.html と tokushoho.html の「（住所を入力してください）」等を実際の情報に置き換えてください。
メールアドレスは onestory310@gmail.com を記載済みです。
contact.html 右側の Facebook リンク（`href="#"`）も実際のURLに変えてください。
特定商取引法の表記は雛形ですので、必ず内容をご確認ください。

### 5. サービス資料（PDF）

`docs/onestory-service.pdf` に置いてあります。差し替えるときは同じファイル名で上書きしてください。
リンクは「企業・組織を整える」ページ／TOP／フッターの3か所から張っています。

### 6. 料金表示

program.html の受講料（50,000〜100,000円／300,000〜500,000円）は、
いただいた企画書の金額をそのまま記載しています。
非公開にする場合は該当の `<p class="price-block">…</p>` を削除してください。

## フォントについて

見出しの筆記体（Pinyon Script）と明朝体（Noto Serif JP）は Google Fonts を読み込んでいます。
インターネット接続のあるサーバーで公開すれば自動的に適用されます。

## 文言をまとめて直したいとき

`build.py` の中に全ページの文章が入っています。編集後に

```
python3 build.py
```

を実行すると、全HTMLが再生成されます（ヘッダー・フッターも自動で揃います）。
1ページだけ直す場合は、そのHTMLを直接編集していただいて問題ありません。
