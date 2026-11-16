# 株式会社ワン・ストーリー Webサイト（rika-hirasawa.com）

中小企業・個人事業主向けのWeb制作（ホームページ制作・LP制作・SEO・Webシステム開発）のサイトです。
ビルド不要の静的サイトで、GitHub Pages で公開しています。

## ファイル構成

```
index.html            トップ
service.html          サービス
price.html            料金プラン
works.html            制作実績（一覧）
works-detail.html     制作実績（詳細テンプレート）
about.html            私たちについて（想い／代表メッセージ／チーム／会社概要）
column.html           コラム一覧
column-article.html   コラム記事テンプレート
contact.html          お問い合わせ
privacy.html          プライバシーポリシー
tokushoho.html        特定商取引法に基づく表記
business.html ほか    旧ページ（トップへ転送）
sitemap.xml / robots.txt   サーチコンソール用
assets/site.css       共通スタイル・アニメーション
assets/site.js        メニュー／FAQ／絞り込み／フォーム送信
assets/logo-header.png  ヘッダー・フッターのロゴ
assets/favicon.png    タブのアイコン
images/rika.jpg       代表写真
gas-form.gs           お問い合わせ受信用 Google Apps Script（控え）
```

## 消さないファイル

- `CNAME` … 独自ドメイン（rika-hirasawa.com）の設定
- `.nojekyll` … GitHub Pages の変換処理を止める設定

## お問い合わせフォーム

`assets/site.js` の `FORM_ENDPOINT`（Google Apps Script のURL）に送信します。項目名は旧サイトと同じです。

## 【要確認】の箇所

料金、実績、制作期間、特商法の「お支払い方法・時期」「キャンセル・返品」などは仮置きです。HTML内の「【要確認】」を検索して差し替えてください。
