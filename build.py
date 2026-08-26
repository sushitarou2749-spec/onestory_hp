# -*- coding: utf-8 -*-
"""One Story 静的サイト ビルドスクリプト（共通パーツを差し込んで各HTMLを生成）"""
import os, io

OUT = os.path.dirname(os.path.abspath(__file__))

NAV = [
    ("index.html",    "HOME"),
    ("about.html",    "私たちについて"),
    ("business.html", "企業・組織を整える"),
    ("program.html",  "プログラム"),
    ("human.html",    "人を整える"),
    ("wisdom.html",   "日本の智慧"),
    ("future.html",   "次世代へ"),
    ("column.html",   "コラム"),
    ("contact.html",  "お問い合わせ"),
]

HEAD = u"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.png" type="image/png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@300;400;500;600&family=Noto+Sans+JP:wght@300;400&family=Pinyon+Script&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
"""

def header(current):
    items = u"\n".join(
        u'      <li><a href="{h}"{cls}>{label}</a></li>'.format(
            h=h, label=label, cls=u' class="current"' if h == current else u"")
        for h, label in NAV)
    return u"""<header class="site-header">
  <div class="header-top">
    <a class="logo" href="index.html">
      <img src="assets/logo.png" alt="One Story">
      <span class="name">株式会社ワン・ストーリー</span>
    </a>
    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="gnav" aria-label="メニューを開く">
      <span></span><span></span><span></span>
    </button>
  </div>
  <nav class="gnav" id="gnav">
    <ul>
%s
    </ul>
  </nav>
</header>
""" % items

FOOTER = u"""<footer class="site-footer">
  <div class="wrap">
    <ul class="footer-nav">
      <li><a href="index.html">HOME</a></li>
      <li><a href="about.html">私たちについて</a></li>
      <li><a href="business.html">企業・組織を整える</a></li>
      <li><a href="program.html">プログラム</a></li>
      <li><a href="human.html">人を整える</a></li>
      <li><a href="wisdom.html">日本の智慧</a></li>
      <li><a href="future.html">次世代へ</a></li>
      <li><a href="column.html">コラム</a></li>
      <li><a href="contact.html">お問い合わせ</a></li>
      <li><a href="docs/onestory-service.pdf" target="_blank" rel="noopener">サービス資料（PDF）</a></li>
    </ul>
    <p class="copyright">&copy; 2026 株式会社ワン・ストーリー &nbsp;/&nbsp; <a href="tokushoho.html">特定商取引法に基づく表記</a></p>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
"""

def page_head(script_en, h1, tagline=u""):
    tag = u'\n      <p class="tagline">%s</p>' % tagline if tagline else u""
    return u"""<div class="page-head">
  <img class="botanical" src="assets/botanical.svg" alt="">
  <div class="wrap">
    <div class="inner">
      <span class="script">%s</span>
      <h1>%s</h1>%s
    </div>
  </div>
</div>
""" % (script_en, h1, tag)

CTA_BAND = u"""<section class="cta-band">
  <div class="wrap-narrow">
    <h2>まずは、今感じている「困った」を聞かせてください。</h2>
    <p>「何をお願いすればいいのか分からない」「システムが必要なのかも分からない」<br>
    そんな状態でも大丈夫です。お話を伺いながら、一緒に整理していきます。</p>
    <p style="margin-top:28px;"><a class="btn" href="contact.html">会社の課題を相談する</a></p>
  </div>
</section>
"""

def build(filename, title, desc, body):
    html = HEAD.format(title=title, desc=desc) + header(filename) + body + FOOTER
    with io.open(os.path.join(OUT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("built:", filename)


# =======================================================================
# TOP
# =======================================================================
index_body = u"""<div class="page-head">
  <img class="botanical" src="assets/botanical.svg" alt="">
  <div class="wrap">
    <div class="inner">
      <img class="hero-logo" src="assets/logo-wide.png" alt="One Story">
      <h1>人を整える。仕組みを整える。未来を整える。</h1>
    </div>
  </div>
</div>

<div class="hero">
  <div class="hero-visual">
    <div class="hero-copy">
      <p class="catch">人が笑顔で働ける会社を、<br>仕組みから。</p>
      <p class="sub">IT・AI・業務改善・人と組織へのアプローチを通して、<br>
      人が安心して働き、本来の力を発揮できる会社づくりを支援します。</p>
    </div>
  </div>
  <!-- 横長のメインビジュアル写真ができたら images/hero.jpg として置き、
       上の div に class="hero-visual has-photo" を付けると背景に表示されます -->
</div>

<section class="tight center">
  <div class="wrap-narrow">
    <p><a class="btn" href="contact.html">会社の課題を相談する</a>
    <span class="btn-note">何が問題なのか分からない段階でも大丈夫です。</span></p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="script">About</span>
      <h2>One Story について</h2>
    </div>
    <div class="about-intro reveal">
      <div class="about-text">
        <p class="intro-catch">人を整える。仕組みを整える。</p>
        <p class="intro-role">代表取締役　平澤 利佳（RiKA.）</p>
        <p>1982年生まれ、愛知県出身。保育士として9年間勤めたのち、いくつかの事業を経て、
        人の心と向き合うカウンセラーとして独立しました。</p>
        <p>以来18年以上にわたり、人の心や潜在意識、身体、自律神経を整える仕事に携わってきました。
        延べ数え切れないほどの方と向き合うなかで見えてきたのは、
        個人の悩みの多くが、その人が身を置く「会社」や「働き方」とつながっているということでした。</p>
        <p>どれだけ本人が整っても、職場の仕組みが人を追い詰めていれば、また同じところに戻ってしまう。
        そこから私は、人だけでなく、会社や社会の仕組みそのものに目を向けるようになりました。</p>
        <p>人を整えるだけでも足りない。仕組みを整えるだけでも足りない。<br>
        その両方を一緒に整えてはじめて、会社は自然に回りはじめます。</p>
        <p>見える世界（業務・仕組み・IT・AI）と、見えない世界（人・心・信頼・職場の空気）。
        その両方をつなぎながら、人が笑顔で働ける会社づくりをお手伝いしています。</p>
        <p style="margin-top:30px;"><a class="more" href="about.html">私たちについて、もっと見る →</a></p>
      </div>
      <div class="about-photo">
        <img src="images/rika.jpg" alt="代表 平澤利佳">
      </div>
    </div>
  </div>
</section>

<section class="bg-mint">
  <div class="wrap-narrow center">
    <span class="script">Concept</span>
    <h2>私たちが考える「会社を整える」</h2>
    <hr class="rule">
    <p class="lead-copy">会社の問題は、システムだけでは解決できません。<br>
    業務、仕組み、人、コミュニケーション、経営者の状態。<br>
    それぞれは、すべてつながっています。</p>
    <p class="lead-copy" style="margin-top:1.5em;">だから私たちは、目に見える課題だけではなく、<br>
    その奥にある原因まで丁寧に見ていきます。</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="script">Business</span>
      <h2>私たちの3つの領域</h2>
    </div>
    <div class="cards reveal">
      <article class="card">
        <div class="thumb"></div>
        <p class="en">BUSINESS</p>
        <h3>企業・組織を整える</h3>
        <p class="tags">業務改善／IT／AI／システム開発／組織づくり</p>
        <p>人が頑張り続ける会社から、<br>仕組みが人を支える会社へ。</p>
        <a class="more" href="business.html">詳しく見る →</a>
      </article>
      <article class="card">
        <div class="thumb"></div>
        <p class="en">HUMAN</p>
        <h3>人を整える</h3>
        <p class="tags">経営者・リーダーの心身のコンディショニング／対話／本質回帰</p>
        <p>会社を整える人自身にも、余白を。</p>
        <a class="more" href="human.html">詳しく見る →</a>
      </article>
      <article class="card">
        <div class="thumb"></div>
        <p class="en">FUTURE</p>
        <h3>未来へつなぐ</h3>
        <p class="tags">日本の智慧／自然／文化／家族／次世代への教育</p>
        <p>新しい技術と、受け継いできた智慧を、次の世代へ。</p>
        <a class="more" href="wisdom.html">私たちの想い →</a>
      </article>
    </div>
  </div>
</section>

<section class="bg-blush">
  <div class="wrap-narrow center">
    <span class="script">Our Thought</span>
    <h2>想い</h2>
    <hr class="rule">
    <div class="statement">
      <p>目指しているのは、<br>便利なシステムを増やすことではありません。</p>
    </div>
    <hr class="rule">
    <p class="lead-copy">人が迷わず働けること。<br>
    引き継ぎがスムーズにできること。<br>
    そして、現場にも経営者にも心の余白が生まれること。</p>
    <p class="lead-copy" style="margin-top:1.5em;">そのために、会社に本当に合った仕組みを、<br>一緒につくり育てていきます。</p>
    <p style="margin-top:34px;"><a class="more" href="about.html">私たちについて →</a></p>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Check</span>
      <h2>こんなお悩みはありませんか？</h2>
    </div>
    <ul class="check-list reveal">
      <li>特定の人にしか分からない仕事がある</li>
      <li>社長がいないと判断できない</li>
      <li>Excel、LINE、紙、複数のアプリに情報が散らばっている</li>
      <li>「あの資料どこ？」が日常になっている</li>
      <li>同じ情報を何度も入力している</li>
      <li>システムを導入したけれど、使いこなせていない</li>
      <li>経営者自身が現場の仕事から抜けられない</li>
    </ul>
    <p class="center" style="margin-top:34px;"><a class="more" href="business.html">課題の見つけ方をもっと見る →</a></p>
  </div>
</section>

<section class="bg-gray">
  <div class="wrap">
    <div class="sec-head">
      <span class="script">Program</span>
      <h2>3つのステップでご一緒します</h2>
    </div>
    <div class="steps reveal">
      <article class="step">
        <span class="step-no">1</span>
        <h3>気づく</h3>
        <p>「会社の課題は何か」を見える化する。<br>経営者が現状を客観的に把握する。</p>
        <p class="price">1Day講座</p>
      </article>
      <article class="step">
        <span class="step-no">2</span>
        <h3>設計する</h3>
        <p>理念・人・業務・IT・AIを一体でデザインする。<br>「どういう会社を目指すのか」を明確にする。</p>
        <p class="price">2日間合宿</p>
      </article>
      <article class="step">
        <span class="step-no">3</span>
        <h3>定着させる</h3>
        <p>ヒアリング、業務改善、システム構築、AI活用、社員教育、経営者サポートまで継続的に支援する。</p>
        <p class="price">伴走サポート</p>
      </article>
    </div>
    <p class="center" style="margin-top:40px;"><a class="btn ghost" href="program.html">プログラムを見る</a></p>
    <p class="center" style="margin-top:22px;"><a class="more" href="docs/onestory-service.pdf" target="_blank" rel="noopener">サービス資料（PDF）を見る →</a></p>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Column</span>
      <h2>お知らせ・コラム</h2>
    </div>
    <ul class="post-list">
      <li><a href="column.html"><p class="meta">2026.00.00<span class="cat">会社を整える</span></p><h3>記事タイトルがここに入ります</h3></a></li>
      <li><a href="column.html"><p class="meta">2026.00.00<span class="cat">人を整える</span></p><h3>記事タイトルがここに入ります</h3></a></li>
      <li><a href="column.html"><p class="meta">2026.00.00<span class="cat">日本の智慧</span></p><h3>記事タイトルがここに入ります</h3></a></li>
    </ul>
    <p class="center" style="margin-top:34px;"><a class="more" href="column.html">一覧を見る →</a></p>
  </div>
</section>
""" + CTA_BAND


# =======================================================================
# 私たちについて
# =======================================================================
about_body = page_head(u"About", u"私たちについて",
    u"私たちがつくりたいのは、便利な社会ではなく、人が幸せに生きられる社会です。") + u"""
<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Why</span>
      <h2>なぜこの会社をやるのか</h2>
    </div>
    <p class="lead-copy narrow">現代は便利になった一方で、多くの人が時間に追われています。<br>
    ITやAIが進化しても、人が幸せにならなければ意味がない。</p>
    <p class="lead-copy narrow" style="margin-top:1.5em;">だから私たちは、テクノロジーを、<br>
    人を忙しくするためではなく、人を人らしくするために使いたい。</p>
  </div>
</section>

<section class="bg-mint">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Two Worlds</span>
      <h2>見える世界と、見えない世界</h2>
    </div>
    <p class="lead-copy narrow">数字、業務、IT、AI、仕組み。<br>そして、心、信頼、人間関係、直感、職場の空気。</p>
    <p class="lead-copy narrow" style="margin-top:1.5em;">会社には、目に見えるものと、目には見えないものがあります。<br>
    私たちは、その両方を大切にしています。</p>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Harmony</span>
      <h2>新しいものと、古いもの</h2>
      <p class="ja-sub">最先端の技術 × 古くから受け継がれてきた智慧</p>
    </div>
    <p class="lead-copy narrow">AIやITだけに偏らない。精神論だけにも偏らない。<br>
    西洋的な合理性と、東洋・日本的な人間観。<br>
    どちらも否定せず、必要なものをつなぐ。</p>
  </div>
</section>

<section class="bg-blush">
  <div class="wrap">
    <div class="sec-head">
      <span class="script">Message</span>
      <h2>代表メッセージ</h2>
    </div>
    <div class="two-col media-narrow reveal">
      <img src="images/rika.jpg" alt="代表 平澤利佳">
      <div>
        <p class="tag beige">代表取締役 ／ 平澤 利佳</p>
        <p>私は18年以上、人の心や潜在意識、身体、自律神経を整える仕事に携わってきました。
        カウンセリングを通して多くの方と向き合うなかで、見える部分だけでは解決しない人の問題を、たくさん見てきました。</p>
        <p>やがて、個人の悩みの多くが、その人が身を置く「会社」や「働き方」とつながっていることに気づきます。
        そこから私は、人だけでなく、会社や社会の仕組みそのものに目を向けるようになりました。</p>
        <p>人を整えるだけでも足りない。仕組みを整えるだけでも足りない。<br>
        その両方を一緒に整えてはじめて、会社は自然に回りはじめる。<br>
        それが、今の事業にたどり着いた理由です。</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="script">Team</span>
      <h2>チーム紹介</h2>
    </div>
    <div class="cards members reveal">
      <article class="card">
        <div class="thumb portrait"></div>
        <h3>平澤 利佳</h3>
        <p class="tags">代表取締役</p>
      </article>
      <article class="card">
        <div class="thumb portrait"></div>
        <h3>渡邊 剛志</h3>
        <p class="tags">CTO ／ 業務改革責任者</p>
      </article>
      <article class="card">
        <div class="thumb portrait"></div>
        <h3>坂本 秀昭</h3>
        <p class="tags">IT戦略責任者</p>
      </article>
      <article class="card">
        <div class="thumb portrait"></div>
        <h3>渡邊 武真</h3>
        <p class="tags">AI担当</p>
      </article>
      <article class="card">
        <div class="thumb portrait"></div>
        <h3>渡邊 勇真</h3>
        <p class="tags">セキュリティ担当</p>
      </article>
      <article class="card">
        <div class="thumb portrait"></div>
        <h3>平澤 林汰朗</h3>
        <p class="tags">web担当</p>
      </article>
    </div>
  </div>
</section>

<section class="bg-gray">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Vision</span>
      <h2>私たちが目指す未来</h2>
    </div>
    <div class="statement">
      <p>人が本来の姿に戻り、<br>日本の良さを次の世代へつないでいくこと。</p>
    </div>
    <hr class="rule wide">
    <div class="pillar reveal" style="margin-top:40px;">
      <div>
        <span class="no">1</span>
        <h3>人が笑顔で働ける会社を増やす</h3>
        <p>業務改善／IT・AI活用／システム開発／組織づくり／経営者のコンディショニングを通して「働く環境」を整えます。</p>
      </div>
      <div>
        <span class="no">2</span>
        <h3>人そのものを整える</h3>
        <p>会社が整うと「もっと自分らしく生きたい」「心や身体も整えたい」という声が生まれます。本質回帰セッション、呼吸・瞑想、心身のコンディショニングへ。</p>
      </div>
      <div>
        <span class="no">3</span>
        <h3>日本人としての土台を取り戻す</h3>
        <p>お墓参りの意味、ご先祖供養、真言密教の智慧、自然との共生、子どもへの教育。受け継いできたものを、次の世代へ。</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Value</span>
      <h2>大切にしていること</h2>
    </div>
    <p class="lead-copy narrow">日本には、古くから「三方よし」という近江商人の考え方があります。<br>
    「売り手よし、買い手よし、世間よし」<br>
    自社だけが良くなるのではなく、関わるすべての人が幸せになることを目指す考え方です。</p>
    <hr class="rule">
    <p class="lead-copy narrow">また、稲盛和夫氏は「人として何が正しいかを判断基準にする」という言葉を大切にされていました。
    私たちも、この考え方に深く共感しています。</p>
    <hr class="rule">
    <p class="lead-copy narrow">効率だけを追い求める西洋的な経営ではなく、<br>
    人とのつながりや思いやりを大切にする東洋的な価値観も取り入れながら、<br>
    ITやAIという新しい技術を、人がより人らしく働くために活かしていく。</p>
    <p class="lead-copy narrow" style="margin-top:1.5em;">それが私たちの考える、これからの会社づくりです。</p>
    <hr class="rule">
    <div class="statement">
      <p>私たちが本当に残したいのは、システムではありません。<br>
      人が笑顔で働ける会社。<br>
      次の世代にも受け継がれていく、強くてあたたかい組織。</p>
    </div>
  </div>
</section>
""" + CTA_BAND


# =======================================================================
# 企業・組織を整える
# =======================================================================
business_body = page_head(u"Business", u"企業・組織を整える",
    u"人が笑顔で働ける会社を、仕組みから。") + u"""
<section>
  <div class="wrap-mid center">
    <h2>業務を整える。人を活かす。会社の未来をつくる。</h2>
    <hr class="rule">
    <p class="lead-copy narrow">私たちが目指しているのは、会社を効率化することだけではありません。<br>
    本当に実現したいのは、「人が安心して働ける会社」を増やすこと。<br>
    そして、働く人が、笑顔で家に帰れる会社を増やすこと。</p>
    <p class="lead-copy narrow" style="margin-top:1.5em;">そのために私たちは、現場の声を丁寧に聞き、会社の中にある課題を見える化し、
    業務改善・仕組みづくり・IT・AI・システム開発を組み合わせながら、
    その会社に本当に必要な環境を、一緒につくります。</p>
  </div>
</section>

<section class="bg-blush">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Check</span>
      <h2>こんなお悩みはありませんか？</h2>
      <p class="ja-sub">会社の課題は、経営者から見えているものだけとは限りません。</p>
    </div>
    <ul class="check-list reveal">
      <li>特定の人にしか分からない仕事がある</li>
      <li>社長がいないと判断できない</li>
      <li>Excel、LINE、紙、複数のアプリに情報が散らばっている</li>
      <li>「あの資料どこ？」が日常になっている</li>
      <li>同じ情報を何度も入力している</li>
      <li>手作業や確認作業に時間を取られている</li>
      <li>新しい人が入るたび、一から仕事を教えている</li>
      <li>システムを導入したけれど、使いこなせていない</li>
      <li>スタッフが忙しく、職場に余裕がない</li>
      <li>経営者自身が現場の仕事から抜けられない</li>
    </ul>
    <hr class="rule">
    <p class="lead-copy narrow">一つひとつは小さな問題に見えるかもしれません。<br>
    けれど、それが毎日積み重なることで、時間がなくなり、人に余裕がなくなり、
    コミュニケーションが減り、人間関係までギクシャクしてしまうことがあります。</p>
    <div class="statement" style="margin-top:40px;">
      <p>問題が見えていないことも、<br>会社の課題です。</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="script">Service</span>
      <h2>私たちが企業にできること</h2>
    </div>
    <div class="svc-grid reveal">
      <div class="svc"><span class="num">01</span><h3>業務の見える化</h3>
        <ul class="dot-list"><li>現場への丁寧なヒアリング</li><li>業務フローの整理</li><li>「誰が・何を・どのように」行っているかを可視化</li><li>経営者が気づいていない現場の課題を発見</li></ul></div>
      <div class="svc"><span class="num">02</span><h3>業務改善コンサルティング</h3>
        <ul class="dot-list"><li>無駄な作業の削減</li><li>重複業務の整理</li><li>属人化の解消</li><li>業務フローの改善</li><li>引き継ぎしやすい仕組みづくり</li></ul></div>
      <div class="svc"><span class="num">03</span><h3>会社に合ったIT・AI活用の提案</h3>
        <ul class="dot-list"><li>必要なITツールの選定</li><li>AIを活用した業務効率化</li><li>既存システムとの連携</li><li>新しいシステムの設計・開発</li><li>一社一社に合わせたオーダーメイドの仕組みづくり</li></ul></div>
      <div class="svc"><span class="num">04</span><h3>システム開発</h3>
        <ul class="dot-list"><li>社内管理システム／顧客管理システム</li><li>シフト管理システム／申込・予約システム</li><li>コミュニティ管理システム／業務管理システム</li><li>データベース構築</li><li>AIを活用した自動化</li></ul></div>
      <div class="svc"><span class="num">05</span><h3>システム導入・定着支援</h3>
        <ul class="dot-list"><li>操作説明</li><li>マニュアル作成</li><li>社内研修</li><li>運用サポート</li><li>社員が自分たちで使いこなせるようになるまで伴走</li></ul></div>
      <div class="svc"><span class="num">06</span><h3>情報の一元管理</h3>
        <ul class="dot-list"><li>バラバラになった情報を整理</li><li>複数アプリの乱立を防止</li><li>必要な情報へすぐアクセスできる環境づくり</li><li>「探す時間」を減らす</li></ul></div>
      <div class="svc"><span class="num">07</span><h3>属人化の解消</h3>
        <ul class="dot-list"><li>担当者しか分からない仕事をなくす</li><li>マニュアル化</li><li>チェックリスト作成</li><li>誰でも仕事ができる仕組みづくり</li></ul></div>
      <div class="svc"><span class="num">08</span><h3>コミュニティ・組織運営支援</h3>
        <ul class="dot-list"><li>イベント運営／会員管理／申込管理</li><li>スタッフ管理</li><li>コミュニケーション設計</li><li>運営の仕組み化</li></ul></div>
      <div class="svc"><span class="num">09</span><h3>継続的な改善サポート</h3>
        <ul class="dot-list"><li>定期ミーティング</li><li>業務改善レビュー</li><li>新たな課題の整理</li><li>システム改善</li><li>AI活用のアップデート</li></ul></div>
    </div>
  </div>
</section>

<section class="bg-mint">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Strength</span>
      <h2>私たちの強み</h2>
    </div>
    <ul class="plain-list reveal">
      <li>現場を丁寧にヒアリングし、本当の課題を見つける</li>
      <li>一社一社に合わせたオーダーメイドの仕組みを設計</li>
      <li>システム開発から導入・運用まで一貫してサポート</li>
      <li>「作って終わり」ではなく、自社で運用できる状態まで伴走</li>
      <li>IT・AIと、人を大切にする組織づくりの両方を支援</li>
      <li>西洋的な効率性と、日本が大切にしてきた「人を活かす経営」の考え方を調和させたご提案</li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Our Style</span>
      <h2>目に見えない部分も、一緒に見ていきます</h2>
    </div>
    <p class="lead-copy narrow">業務改善やシステム開発だけでは、本当に良い会社はつくれません。<br>
    会社を動かしているのは「人」です。</p>
    <p class="lead-copy narrow" style="margin-top:1.5em;">だから私たちは、数字や業務フローだけではなく、
    職場の空気、人間関係、コミュニケーション、一人ひとりの強み、経営者の想い。<br>
    といった、目には見えない部分も大切にしています。</p>
    <hr class="rule">
    <p class="lead-copy narrow">現場で起きている問題は、表面上は業務の問題に見えても、
    実際にはコミュニケーションや心理的な負担、組織の空気が原因になっていることも少なくありません。</p>
    <div class="statement" style="margin-top:40px;">
      <p>見える世界（業務・仕組み・IT・AI）と、<br>
      見えない世界（人・心・信頼・組織の空気）。<br>
      その両方をつなぎながら、<br>本当に機能する会社づくりをお手伝いしています。</p>
    </div>
    <p class="center" style="margin-top:44px;"><a class="btn ghost" href="program.html">具体的なプログラムを見る</a></p>
  </div>
</section>


<section class="bg-blush">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Document</span>
      <h2>サービス資料</h2>
      <p class="ja-sub">私たちの支援内容をまとめた資料をご覧いただけます。</p>
    </div>
    <div class="doc-dl reveal">
      <div class="doc-meta">
        <p class="doc-title">株式会社ワン・ストーリー　サービスのご案内</p>
        <p class="doc-note">業務改善・IT・AI活用・システム開発・組織づくりの進め方をまとめています。<br>
        PDF形式／全19ページ</p>
      </div>
      <div class="doc-actions">
        <a class="btn" href="docs/onestory-service.pdf" target="_blank" rel="noopener">資料を見る（PDF）</a>
        <a class="more" href="docs/onestory-service.pdf" download>ダウンロード</a>
      </div>
    </div>
    <p class="center quiet" style="margin-top:28px;">
      内容についてのご質問は、<a class="more" href="contact.html">お問い合わせ</a>からお気軽にどうぞ。</p>
  </div>
</section>

""" + CTA_BAND


# =======================================================================
# プログラム
# =======================================================================
program_body = page_head(u"Program", u"プログラム",
    u"人と仕組みを整え、会社が自然と成長する土台をつくる。") + u"""
<section>
  <div class="wrap-mid center">
    <p class="lead-copy narrow">私たちは、経営者を変えることでも、社員を変えることでもありません。<br>
    人と仕組みの両方を整えることで、会社全体が自然と回り始める状態をつくります。</p>
    <hr class="rule">
    <div class="statement">
      <p>人を整える。<br>仕組みを整える。<br>会社の未来を整える。</p>
    </div>
  </div>
</section>

<section class="bg-gray">
  <div class="wrap">
    <div class="sec-head">
      <span class="script">Step</span>
      <h2>3つのステップ</h2>
    </div>
    <div class="steps reveal">
      <article class="step">
        <span class="step-no">1</span>
        <h3>気づく</h3>
        <p>「会社の課題は何か」を見える化する。<br>経営者が現状を客観的に把握する。</p>
        <p class="price">1Day講座</p>
      </article>
      <article class="step">
        <span class="step-no">2</span>
        <h3>設計する</h3>
        <p>理念・人・業務・IT・AIを一体でデザインする。<br>「どういう会社を目指すのか」を明確にする。</p>
        <p class="price">2日間合宿</p>
      </article>
      <article class="step">
        <span class="step-no">3</span>
        <h3>定着させる</h3>
        <p>現場へのヒアリング、業務改善、システム構築、AI活用、社員教育、経営者サポートまで継続的に支援する。</p>
        <p class="price">伴走サポート</p>
      </article>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Lecture</span>
      <h2>1Day講座</h2>
      <p class="ja-sub">会社の見えないムダ発見講座</p>
    </div>
    <p class="lead-copy narrow">「IT会社」ではなく「業務改善会社」だと知っていただくための一日です。</p>
    <hr class="rule">
    <ul class="flow reveal">
      <li>
        <p class="tag green">第一部</p>
        <h3>会社が成長しない本当の理由</h3>
        <ul class="items">
          <li>なぜ忙しい会社ほど利益が出ないのか</li>
          <li>属人化とは</li>
          <li>人間関係が悪くなる理由</li>
          <li>ストレスが生産性を下げる理由</li>
          <li>AI時代に必要な会社とは</li>
        </ul>
      </li>
      <li>
        <p class="tag green">第二部</p>
        <h3>会社診断ワーク</h3>
        <ul class="items">
          <li>□ 誰しかできない仕事がある</li>
          <li>□ 毎日同じ質問が飛び交う</li>
          <li>□ 社長しか判断できない</li>
          <li>□ LINEが情報共有になっている</li>
          <li>□ 紙が多い</li>
          <li>□ システムがバラバラ</li>
          <li>□ 会議が長い　など</li>
        </ul>
      </li>
      <li>
        <p class="tag green">第三部</p>
        <h3>改善ロードマップ</h3>
        <span class="note">会社がレベル1〜5のどこにいるのかを診断します</span>
      </li>
      <li>
        <p class="tag beige">参加特典</p>
        <h3>30分個別相談</h3>
      </li>
    </ul>
    <div class="center" style="margin-top:40px;">
      <p class="price-block"><span class="amount">受講料：50,000円 〜 100,000円</span><br>
      <span class="quiet">※ 開催形式・人数により異なります。詳細はお問い合わせください。</span></p>
    </div>
  </div>
</section>

<section class="bg-mint">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Camp</span>
      <h2>2日間合宿</h2>
      <p class="ja-sub">会社を変える経営デザイン合宿</p>
    </div>
    <div class="statement">
      <p>ここでは知識ではなく、<br>実際に会社を設計します。</p>
    </div>
    <hr class="rule">
    <ul class="flow reveal">
      <li>
        <p class="tag green">Day 1</p>
        <h3>経営者を整える</h3>
        <ul class="items">
          <li>ビジョン／想い</li>
          <li>会社理念／判断軸</li>
          <li>強み／自分しかできない仕事</li>
          <li>瞑想／イメージワーク</li>
        </ul>
      </li>
      <li>
        <p class="tag green">Day 2</p>
        <h3>会社の仕組みを設計する</h3>
        <ul class="items">
          <li>業務の棚卸しと見える化</li>
          <li>人と役割の再設計</li>
          <li>IT・AIをどこに使うかの設計</li>
          <li>今後1年の改善ロードマップ</li>
        </ul>
      </li>
    </ul>
    <div class="center" style="margin-top:40px;">
      <p class="price-block"><span class="amount">価格：300,000円 〜 500,000円</span><br>
      <span class="quiet">※ 参加人数・会場により異なります。</span></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Support</span>
      <h2>伴走サポート</h2>
      <p class="ja-sub">会社全体の継続支援</p>
    </div>
    <p class="lead-copy narrow">現場へのヒアリング、業務改善、システム構築、AI活用、社員教育、経営者サポートまで。<br>
    「作って終わり」ではなく、自社で運用できる状態になるまでご一緒します。</p>
    <table class="spec" style="margin-top:40px;">
      <tr><th>支援内容</th><td>業務の見える化／業務改善／システム開発・導入／AI活用／社員研修／経営者のコンディショニング</td></tr>
      <tr><th>進め方</th><td>定期ミーティング（月1回〜）＋随時のご相談</td></tr>
      <tr><th>期間</th><td>6ヶ月〜（ご状況に合わせてご提案します）</td></tr>
      <tr><th>費用</th><td>内容に応じてお見積り</td></tr>
    </table>
  </div>
</section>
""" + CTA_BAND


# =======================================================================
# 人を整える
# =======================================================================
human_body = page_head(u"Human", u"人を整える",
    u"会社を整える人自身も、整っていること。") + u"""
<section>
  <div class="wrap-mid center">
    <div class="statement">
      <p>良い判断は、<br>余白のあるところから生まれる。</p>
    </div>
    <hr class="rule">
    <p class="lead-copy narrow">経営者は、毎日のように決断しています。<br>
    会社、お金、人、未来。<br>
    考えることが仕事だからこそ、頭が休まらなくなっている人も少なくありません。</p>
  </div>
</section>

<section class="bg-mint">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Conditioning</span>
      <h2>経営者・リーダーを整える</h2>
    </div>
    <p class="lead-copy narrow">思考を止められない状態のままでは、どれだけ良い仕組みをつくっても、判断が濁ってしまいます。<br>
    心と身体、自律神経を整えることで、本来の判断力と直感を取り戻していきます。</p>
    <ul class="plain-list reveal" style="margin-top:36px;">
      <li>対話（カウンセリング）</li>
      <li>心身のコンディショニング</li>
      <li>呼吸・瞑想</li>
      <li>自律神経を整えるアプローチ</li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Essence</span>
      <h2>本質回帰</h2>
      <p class="ja-sub">頑張ることで進む人生から、本来の自分で進む人生へ。</p>
    </div>
    <div class="statement">
      <p>答えを外に探すのではなく、<br>自分の内側へ還る。</p>
    </div>
    <hr class="rule">
    <div class="two-col reveal" style="margin-top:20px;">
      <div class="ph"></div>
      <div>
        <p class="tag beige">セッションで扱うこと</p>
        <ul class="dot-list">
          <li>カウンセリング</li>
          <li>潜在意識</li>
          <li>身体</li>
          <li>呼吸</li>
          <li>瞑想</li>
          <li>エネルギーワーク</li>
        </ul>
        <p class="quiet" style="margin-top:24px;">会社が整うと、「もっと自分らしく生きたい」「心や身体も整えたい」という方が必ず出てきます。
        会社での出会いから、個人の人生へとサポートが広がっていく流れです。</p>
      </div>
    </div>
  </div>
</section>
""" + CTA_BAND


# =======================================================================
# 日本の智慧
# =======================================================================
wisdom_body = page_head(u"Wisdom", u"日本の智慧をつなぐ",
    u"受け継いできたものを、次の世代へ。") + u"""
<section>
  <div class="wrap-mid center">
    <div class="statement">
      <p>古いから残すのではなく、<br>今を生きる私たちに必要だから伝える。</p>
    </div>
  </div>
</section>

<section class="bg-blush">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Theme</span>
      <h2>お伝えしているテーマ</h2>
    </div>
    <ul class="plain-list reveal">
      <li>お墓参りの意味</li>
      <li>ご先祖供養</li>
      <li>祈り</li>
      <li>真言密教から学んだ智慧</li>
      <li>自然との関わり</li>
      <li>日本人が大切にしてきた精神性</li>
    </ul>
    <hr class="rule">
    <p class="lead-copy narrow quiet">「これが唯一正しい作法」と断定するものではありません。<br>
    宗派・地域・家ごとに異なる文化を尊重しながら、<br>
    私たちが学び、受け継いできた考え方をお伝えしています。</p>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="two-col reveal">
      <div class="ph"></div>
      <div>
        <h3>なぜ、会社の話と一緒に伝えるのか</h3>
        <p>効率だけを追い求める西洋的な経営ではなく、人とのつながりや思いやりを大切にする東洋的な価値観も取り入れる。
        その土台にあるのが、日本人が長い時間をかけて育んできた知恵や祈りのかたちです。</p>
        <p>単純作業や繰り返しの業務はAIに任せ、人は「考えること」「創造すること」「人と向き合うこと」に時間を使う。
        その使い方こそが、日本人が昔から大切にしてきた知恵や思いやり、創意工夫を未来へつないでいくことにつながると信じています。</p>
      </div>
    </div>
  </div>
</section>
""" + CTA_BAND


# =======================================================================
# 次世代へ
# =======================================================================
future_body = page_head(u"Future", u"次世代へつなぐ",
    u"私たちは、何を子どもたちに残せるだろう。") + u"""
<section>
  <div class="wrap-mid center">
    <div class="statement">
      <p>未来をつくることは、<br>次の世代に何を手渡すかを考えること。</p>
    </div>
  </div>
</section>

<section class="bg-mint">
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Theme</span>
      <h2>扱っていくテーマ</h2>
    </div>
    <ul class="plain-list reveal">
      <li>若い世代への教育</li>
      <li>働くことについて</li>
      <li>AIとの付き合い方</li>
      <li>自分で考える力</li>
      <li>人とのつながり</li>
      <li>日本文化／自然</li>
      <li>家族／命／感謝</li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap-mid">
    <div class="sec-head">
      <span class="script">Next</span>
      <h2>これからの展開</h2>
    </div>
    <p class="lead-copy narrow">将来的には、講座、学校との連携、企業の次世代教育、親子向け企画などへ発展させていきます。</p>
    <div class="cards reveal" style="margin-top:44px;">
      <article class="card"><div class="thumb"></div><h3>講座</h3><p>働くこと、考える力、AIとの向き合い方を学ぶ場。</p></article>
      <article class="card"><div class="thumb"></div><h3>学校との連携</h3><p>教育現場と一緒に、次世代へ手渡すものを考える。</p></article>
      <article class="card"><div class="thumb"></div><h3>親子向け企画</h3><p>家族・自然・命について、体験から学ぶ機会を。</p></article>
    </div>
  </div>
</section>
""" + CTA_BAND


# =======================================================================
# コラム
# =======================================================================
column_body = page_head(u"Column", u"お知らせ・コラム",
    u"人・会社・未来を整える。") + u"""
<section>
  <div class="wrap-mid">
    <div class="cat-chips">
      <span>会社を整える　業務改善／IT／AI／組織／経営</span>
      <span>人を整える　心／身体／自律神経／経営者のコンディショニング</span>
      <span>日本の智慧　文化／祈り／ご先祖／自然</span>
      <span>未来を考える　AI時代／子ども／教育／働き方</span>
    </div>
    <ul class="post-list">
      <li><a href="#"><p class="meta">2026.00.00<span class="cat">会社を整える</span></p><h3>記事タイトルがここに入ります</h3></a></li>
      <li><a href="#"><p class="meta">2026.00.00<span class="cat">人を整える</span></p><h3>記事タイトルがここに入ります</h3></a></li>
      <li><a href="#"><p class="meta">2026.00.00<span class="cat">日本の智慧</span></p><h3>記事タイトルがここに入ります</h3></a></li>
      <li><a href="#"><p class="meta">2026.00.00<span class="cat">未来を考える</span></p><h3>記事タイトルがここに入ります</h3></a></li>
      <li><a href="#"><p class="meta">2026.00.00<span class="cat">会社を整える</span></p><h3>記事タイトルがここに入ります</h3></a></li>
    </ul>
  </div>
</section>
""" + CTA_BAND


# =======================================================================
# お問い合わせ
# =======================================================================
contact_body = page_head(u"Contact", u"お問い合わせ",
    u"まずは、今感じている「困った」を聞かせてください。") + u"""
<section>
  <div class="wrap-mid center">
    <p class="lead-copy narrow">「何をお願いすればいいのか分からない」<br>
    「システムが必要なのかも分からない」<br>
    そんな状態でも大丈夫です。お話を伺いながら、一緒に整理していきます。</p>
    <hr class="rule">
    <p class="lead-copy narrow quiet">ご相談内容の目安</p>
    <ul class="plain-list" style="max-width:32em;margin-inline:auto;">
      <li>会社について相談する</li>
      <li>講座・合宿について相談する</li>
      <li>個人セッションについて相談する</li>
    </ul>
  </div>
</section>

<section class="bg-gray">
  <div class="wrap">
    <div class="sec-head">
      <h2>お問合せフォーム</h2>
      <p class="ja-sub">ご相談、各種お申込み、講演・セミナー等のご依頼などお気軽にお問合せください。</p>
    </div>
    <div class="contact-cols">
      <!-- ===== フォーム ===== -->
      <form class="contact-form" id="contactForm" novalidate>
        <div class="field">
          <label for="f-name">お名前<span class="req">*</span></label>
          <input type="text" id="f-name" name="お名前" placeholder="お名前" required>
          <span class="err">お名前をご入力ください</span>
        </div>
        <div class="field">
          <label for="f-company">会社名・団体名</label>
          <input type="text" id="f-company" name="会社名" placeholder="会社名・団体名（任意）">
        </div>
        <div class="field">
          <label for="f-email">Email<span class="req">*</span></label>
          <input type="email" id="f-email" name="メールアドレス" placeholder="Email" required>
          <span class="err">メールアドレスをご確認ください</span>
        </div>
        <div class="field">
          <label for="f-tel">お電話番号(任意)</label>
          <input type="tel" id="f-tel" name="電話番号" placeholder="お電話番号(任意)">
        </div>
        <div class="field">
          <label for="f-type">お問合せ内容<span class="req">*</span></label>
          <select id="f-type" name="お問合せ内容" required>
            <option value="">お問合せ内容</option>
            <option>会社について相談する</option>
            <option>講座・合宿について相談する</option>
            <option>個人セッションについて相談する</option>
            <option>取材・講演のご依頼</option>
            <option>その他</option>
          </select>
          <span class="err">お問合せ内容をお選びください</span>
        </div>
        <div class="field">
          <label for="f-msg">メッセージ<span class="req">*</span></label>
          <textarea id="f-msg" name="メッセージ" placeholder="メッセージ" required></textarea>
          <span class="err">メッセージをご入力ください</span>
        </div>

        <!-- 迷惑メール対策（人には見えません。触らないでください） -->
        <div class="hp-field" aria-hidden="true">
          <label for="f-hp">この欄は入力しないでください</label>
          <input type="text" id="f-hp" name="_gotcha" tabindex="-1" autocomplete="off">
        </div>

        <button type="submit" class="form-submit" id="formSubmit">送信する</button>
        <p class="form-msg" id="formMsg"></p>
        <p class="form-privacy">いただいた個人情報は、お問い合わせへのご返信以外の目的では使用いたしません。</p>
      </form>

      <!-- ===== 右側（写真・リンク） ===== -->
      <div class="contact-side">
        <img src="images/rika.jpg" alt="代表 平澤利佳">
        <p class="side-links"><a href="#" target="_blank" rel="noopener">Facebook</a></p>
        <p class="side-note">お返事には数日いただく場合がございます。<br>
        3日以上返信がない場合は、恐れ入りますが再度ご連絡ください。</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap-mid center">
    <span class="script">Company</span>
    <hr class="rule">
    <table class="spec">
      <tr><th>会社名</th><td>株式会社ワン・ストーリー</td></tr>
      <tr><th>代表取締役</th><td>平澤 利佳</td></tr>
      <tr><th>所在地</th><td>〒472-0001　愛知県知立市八橋町山田谷2-15</td></tr>
      <tr><th>メール</th><td>onestory310@gmail.com</td></tr>
      <tr><th>事業内容</th><td>業務改善コンサルティング／システム開発／IT・AI活用支援／組織づくり支援／各種講座・セッション</td></tr>
    </table>
  </div>
</section>

<script src="assets/contact.js"></script>
"""


# =======================================================================
# 特定商取引法に基づく表記
# =======================================================================
tokusho_body = page_head(u"Legal", u"特定商取引法に基づく表記") + u"""
<section>
  <div class="wrap-mid">
    <table class="spec">
      <tr><th>販売業者</th><td>株式会社ワン・ストーリー</td></tr>
      <tr><th>運営責任者</th><td>代表取締役　平澤 利佳</td></tr>
      <tr><th>所在地</th><td>〒472-0001　愛知県知立市八橋町山田谷2-15</td></tr>
      <tr><th>メールアドレス</th><td>onestory310@gmail.com</td></tr>
      <tr><th>事業内容</th><td>業務改善コンサルティング／システム開発／IT・AI活用支援／組織づくり支援／各種講座・セッション</td></tr>
      <tr><th>キャンセル・返品</th><td>（キャンセルポリシーを記載してください）</td></tr>
    </table>
  </div>
</section>
"""


PAGES = [
    ("index.html",    u"人を整える。仕組みを整える。未来を整える。｜株式会社ワン・ストーリー",
     u"人が笑顔で働ける会社を、仕組みから。IT・AI・業務改善・人と組織へのアプローチを通して、人が安心して働き、本来の力を発揮できる会社づくりを支援します。", index_body),
    ("about.html",    u"私たちについて｜株式会社ワン・ストーリー",
     u"私たちがつくりたいのは、便利な社会ではなく、人が幸せに生きられる社会です。ワン・ストーリーの想いと代表メッセージ、目指す未来をご紹介します。", about_body),
    ("business.html", u"企業・組織を整える｜株式会社ワン・ストーリー",
     u"業務改善／IT／AI／システム開発／組織づくり。人が頑張り続ける会社から、仕組みが人を支える会社へ。", business_body),
    ("program.html",  u"プログラム｜株式会社ワン・ストーリー",
     u"1Day講座「会社の見えないムダ発見講座」、2日間合宿「会社を変える経営デザイン合宿」、伴走サポート。人と仕組みを整える3つのステップ。", program_body),
    ("human.html",    u"人を整える｜株式会社ワン・ストーリー",
     u"会社を整える人自身も、整っていること。経営者・リーダーの心身のコンディショニングと本質回帰セッション。", human_body),
    ("wisdom.html",   u"日本の智慧をつなぐ｜株式会社ワン・ストーリー",
     u"受け継いできたものを、次の世代へ。お墓参りの意味、ご先祖供養、祈り、真言密教から学んだ智慧、自然との関わり。", wisdom_body),
    ("future.html",   u"次世代へつなぐ｜株式会社ワン・ストーリー",
     u"私たちは、何を子どもたちに残せるだろう。若い世代への教育、AIとの付き合い方、自分で考える力。", future_body),
    ("column.html",   u"お知らせ・コラム｜株式会社ワン・ストーリー",
     u"会社を整える／人を整える／日本の智慧／未来を考える。人・会社・未来を整えるためのコラムをお届けします。", column_body),
    ("contact.html",  u"お問い合わせ｜株式会社ワン・ストーリー",
     u"まずは、今感じている「困った」を聞かせてください。何をお願いすればいいのか分からない段階でも大丈夫です。", contact_body),
    ("tokushoho.html", u"特定商取引法に基づく表記｜株式会社ワン・ストーリー",
     u"特定商取引法に基づく表記", tokusho_body),
]

for fn, t, d, b in PAGES:
    build(fn, t, d, b)

print("done")
