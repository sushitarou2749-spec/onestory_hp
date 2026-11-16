(function () {
  'use strict';
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.documentElement.classList.add('js');

  // ===== ヒーロー：見出しを行に分けてマスク表示 =====
  var hero = document.getElementById('top');
  if (hero) {
    var splitLines = function (el, base) {
      var lines = el.innerHTML.split(/<br\s*\/?>/i);
      el.innerHTML = lines.map(function (h, i) {
        return '<span class="os-line"><span class="os-line__in" style="transition-delay:' + (base + i * 0.12).toFixed(2) + 's">' + h + '</span></span>';
      }).join('');
    };
    var en = hero.querySelector('.hero-en'); if (en) splitLines(en, 0.25);
    var h1 = hero.querySelector('h1'); if (h1) splitLines(h1, 0.55);
    var col = en ? en.parentElement : null;
    if (col) {
      var d = 0.1;
      Array.prototype.forEach.call(col.children, function (c) {
        if (c === en || c === h1) { d = 0.85; return; }
        c.classList.add('os-fade'); c.style.transitionDelay = d.toFixed(2) + 's'; d += 0.12;
      });
    }
    var blobs = document.createElement('div');
    blobs.className = 'os-blobs'; blobs.setAttribute('aria-hidden', 'true');
    blobs.innerHTML = '<span class="os-blob os-blob--1"></span><span class="os-blob os-blob--2"></span><span class="os-blob os-blob--3"></span>';
    hero.insertBefore(blobs, hero.firstChild);
    requestAnimationFrame(function () { requestAnimationFrame(function () { hero.classList.add('is-ready'); }); });
  }

  // ===== ヘッダー：スクロールで少し縮む =====
  var hdr = document.querySelector('header[style*="sticky"]');
  if (hdr) {
    var onHdr = function () { hdr.classList.toggle('is-scrolled', window.scrollY > 40); };
    onHdr(); window.addEventListener('scroll', onHdr, { passive: true });
  }

  // ===== スクロールでフェードアップ =====
  if (!reduce && 'IntersectionObserver' in window) {
    var targets = [];
    var isGrid = function (el) { var d = getComputedStyle(el).display; return d === 'grid' || d === 'inline-grid'; };
    document.querySelectorAll('section:not(#top) .wrap, article .wrap, header .wrap').forEach(function (wrap) {
      if (wrap.closest('header[style*="sticky"]') || wrap.closest('#top')) return;
      Array.prototype.forEach.call(wrap.children, function (c) {
        var grid = isGrid(c) ? c : c.querySelector(':scope > [style*="display: grid"], :scope > ul, :scope > ol');
        if (isGrid(c)) {
          Array.prototype.forEach.call(c.children, function (g, i) { g.style.setProperty('--d', Math.min(i, 6) * 0.08 + 's'); targets.push(g); });
        } else {
          targets.push(c);
        }
      });
    });
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    targets.forEach(function (t) {
      if (t.getBoundingClientRect().top < vh * 0.9) return; // 最初から見えているものは隠さない
      t.classList.add('os-reveal'); io.observe(t);
    });
  }

  // 全画面メニュー
  var menu = document.getElementById('sp-menu');
  var openBtn = document.querySelector('[data-menu-open]');
  function setMenu(open) {
    if (!menu) return;
    if (open) {
      menu.hidden = false;
      requestAnimationFrame(function () { requestAnimationFrame(function () { menu.classList.add('is-open'); }); });
      menu.querySelectorAll('.sp-menu__nav a, .sp-menu__cta').forEach(function (a, i) { a.style.transitionDelay = (0.15 + i * 0.05) + 's'; });
    } else {
      menu.classList.remove('is-open');
      setTimeout(function () { if (!menu.classList.contains('is-open')) menu.hidden = true; }, reduce ? 0 : 600);
    }
    document.body.classList.toggle('menu-open', open);
    if (openBtn) openBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    if (open) { var c = menu.querySelector('[data-menu-close]'); if (c) c.focus(); }
    else if (openBtn) openBtn.focus();
  }
  if (openBtn) openBtn.addEventListener('click', function () { setMenu(true); });
  if (menu) {
    menu.querySelector('[data-menu-close]').addEventListener('click', function () { setMenu(false); });
    menu.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  // FAQ アコーディオン
  document.querySelectorAll('.faq-q').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var ans = document.getElementById(btn.getAttribute('aria-controls'));
      var open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (ans) ans.hidden = !open;
      var icon = btn.querySelector('.faq-icon');
      if (icon) icon.style.transform = open ? 'rotate(45deg)' : 'rotate(0deg)';
    });
  });

  // 実績・コラムの絞り込み
  var filters = document.querySelectorAll('[data-filter]');
  if (filters.length) {
    var items = document.querySelectorAll('[data-tag]');
    var count = document.querySelector('[data-count]');
    filters.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var f = btn.getAttribute('data-filter');
        filters.forEach(function (b) { b.setAttribute('aria-pressed', b === btn ? 'true' : 'false'); });
        var n = 0;
        items.forEach(function (it) {
          var show = f === 'all' || it.getAttribute('data-tag') === f;
          it.hidden = !show;
          if (show) n++;
        });
        if (count) count.textContent = n + '件の実績';
      });
    });
  }

  // スマホ固定CTA：ファーストビューを過ぎたら表示
  var spCta = document.querySelector('.sp-cta');
  if (spCta) {
    var onScroll = function () {
      spCta.classList.toggle('is-away', window.scrollY < window.innerHeight * 0.6);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // お問い合わせフォーム
  var form = document.getElementById('contact-form');
  if (form) {
    var alertBox = document.getElementById('form-alert');
    var alertText = alertBox ? alertBox.textContent : '';
    var sent = document.getElementById('form-sent');
    var fields = {
      name: { el: document.getElementById('f-name'), check: function (v) { return v.trim() !== ''; } },
      email: { el: document.getElementById('f-email'), check: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); } },
      type: { el: document.getElementById('f-type'), check: function (v) { return v !== ''; } },
      msg: { el: document.getElementById('f-msg'), check: function (v) { return v.trim() !== ''; } },
      agree: { el: document.getElementById('f-agree'), check: function () { return document.getElementById('f-agree').checked; } }
    };
    var tried = false;
    function validate() {
      var ok = true, first = null;
      Object.keys(fields).forEach(function (k) {
        var f = fields[k];
        var good = f.check(f.el.value || '');
        var err = document.getElementById('e-' + k);
        if (k === 'email' && err) err.textContent = f.el.value ? 'メールアドレスの形式で入力してください' : 'メールアドレスを入力してください';
        if (err) err.hidden = good;
        f.el.setAttribute('aria-invalid', good ? 'false' : 'true');
        if (k !== 'agree') f.el.style.border = good ? '1px solid #1a1a1a' : '2px solid #b3261e';
        if (!good) { ok = false; if (!first) first = f.el; }
      });
      if (alertBox) { if (!ok) alertBox.textContent = alertText; alertBox.hidden = ok; }
      return { ok: ok, first: first };
    }
    Object.keys(fields).forEach(function (k) {
      var ev = k === 'agree' || k === 'type' ? 'change' : 'input';
      fields[k].el.addEventListener(ev, function () { if (tried) validate(); });
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      tried = true;
      var r = validate();
      if (!r.ok) { if (r.first) r.first.focus(); return; }
      // 送信先：今のサイトと同じ Google Apps Script（項目名も今のサイトに合わせる）
      var FORM_ENDPOINT = 'https://script.google.com/macros/s/AKfycbzunvDqgoFYsfdsQ8vAn01DWsdtXCBNUC6Lwxafj4rjRZgsqGyTMh6KPC6YAHhp19bthw/exec';
      var val = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; };
      var typeEl = document.getElementById('f-type');
      var typeText = typeEl && typeEl.selectedIndex > 0 ? typeEl.options[typeEl.selectedIndex].text : '';
      var extra = [];
      if (val('f-budget')) extra.push('ご予算：' + val('f-budget'));
      if (val('f-when')) extra.push('ご希望の時期：' + val('f-when'));
      var params = new URLSearchParams();
      params.append('お名前', val('f-name'));
      params.append('会社名', val('f-company'));
      params.append('メールアドレス', val('f-email'));
      params.append('電話番号', val('f-tel'));
      params.append('お問合せ内容', typeText);
      params.append('メッセージ', val('f-msg') + (extra.length ? '\n\n' + extra.join('\n') : ''));
      params.append('_gotcha', val('f-hp'));
      params.append('_subject', '【サイト】お問い合わせが届きました');
      var btn = form.querySelector('button[type="submit"]');
      var btnText = btn ? btn.innerHTML : '';
      if (btn) { btn.disabled = true; btn.textContent = '送信中…'; }
      fetch(FORM_ENDPOINT, { method: 'POST', body: params, mode: 'no-cors' })
        .then(function () {
          form.reset();
          form.hidden = true;
          if (sent) { sent.hidden = false; sent.setAttribute('tabindex', '-1'); sent.focus(); }
        })
        .catch(function () {
          if (alertBox) { alertBox.textContent = '送信できませんでした。時間をおいて、もう一度お試しください。'; alertBox.hidden = false; }
        })
        .then(function () { if (btn) { btn.disabled = false; btn.innerHTML = btnText; } });
    });
    var reset = document.getElementById('form-reset');
    if (reset) reset.addEventListener('click', function () {
      form.reset(); tried = false; validate();
      if (alertBox) alertBox.hidden = true;
      Object.keys(fields).forEach(function (k) {
        var err = document.getElementById('e-' + k); if (err) err.hidden = true;
        if (k !== 'agree') fields[k].el.style.border = '1px solid #1a1a1a';
        fields[k].el.setAttribute('aria-invalid', 'false');
      });
      sent.hidden = true; form.hidden = false;
    });
  }
})();
