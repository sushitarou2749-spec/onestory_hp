/* =========================================================
   お問い合わせフォーム 送信スクリプト
   ---------------------------------------------------------
   ★ 設定するのはこの1行だけです ★

   下の FORM_ENDPOINT に、フォーム送信サービスのURLを入れてください。

   【Formspree を使う場合】
     https://formspree.io/ に onestory310@gmail.com で登録
     → New Form → 発行される "https://formspree.io/f/xxxxxxxx" を貼り付け
     （無料プランは月50件まで。最初の1件目の送信時に確認メールが届きます）

   【Google Apps Script を使う場合（無料・件数制限なし）】
     README の「お問い合わせフォームの設定」を参照してください。
     発行されたウェブアプリのURL（https://script.google.com/macros/s/.../exec）を貼り付け

   未設定のまま送信すると、画面に案内が出るだけで送信されません。
   ========================================================= */

var FORM_ENDPOINT = "https://script.google.com/macros/s/AKfycbzunvDqgoFYsfdsQ8vAn01DWsdtXCBNUC6Lwxafj4rjRZgsqGyTMh6KPC6YAHhp19bthw/exec";

/* --------------------------------------------------------- */

(function () {
  "use strict";

  var form = document.getElementById("contactForm");
  if (!form) return;

  var btn = document.getElementById("formSubmit");
  var msg = document.getElementById("formMsg");

  function setMsg(text, type) {
    msg.textContent = text;
    msg.className = "form-msg show " + type;
  }

  function fieldOf(el) {
    return el.closest ? el.closest(".field") : el.parentNode;
  }

  function validate() {
    var ok = true;
    var required = form.querySelectorAll("[required]");
    for (var i = 0; i < required.length; i++) {
      var el = required[i];
      var wrap = fieldOf(el);
      var valid = el.value.trim() !== "";
      if (valid && el.type === "email") {
        valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim());
      }
      if (valid) {
        wrap.classList.remove("invalid");
      } else {
        wrap.classList.add("invalid");
        ok = false;
      }
    }
    return ok;
  }

  form.addEventListener("input", function (e) {
    var wrap = fieldOf(e.target);
    if (wrap && wrap.classList.contains("invalid")) validate();
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    msg.className = "form-msg";

    if (!validate()) {
      setMsg("未入力の項目があります。ご確認ください。", "ng");
      return;
    }

    if (!FORM_ENDPOINT) {
      setMsg("送信先が未設定です。assets/contact.js の FORM_ENDPOINT にフォームのURLを設定してください。", "ng");
      return;
    }

    /* application/x-www-form-urlencoded で送る（Formspree・Apps Script 両対応） */
    var fd = new FormData(form);
    var params = new URLSearchParams();
    fd.forEach(function (v, k) { params.append(k, v); });
    params.append("_subject", "【サイト】お問い合わせが届きました");

    var isGAS = /script\.google\.com/.test(FORM_ENDPOINT);

    btn.disabled = true;
    btn.textContent = "送信中…";

    fetch(FORM_ENDPOINT, {
      method: "POST",
      body: params,
      mode: isGAS ? "no-cors" : "cors",
      headers: isGAS ? {} : { Accept: "application/json" }
    })
      .then(function (res) {
        if (!isGAS && !res.ok) throw new Error("status " + res.status);
        form.reset();
        setMsg("お問い合わせありがとうございます。\n内容を確認のうえ、担当者よりご連絡いたします。", "ok");
      })
      .catch(function () {
        setMsg("送信に失敗しました。お手数ですが、時間をおいて再度お試しください。", "ng");
      })
      .then(function () {
        btn.disabled = false;
        btn.textContent = "送信する";
      });
  });
})();
