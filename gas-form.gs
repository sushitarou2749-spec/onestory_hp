/**
 * お問い合わせフォーム受信スクリプト（Google Apps Script）
 * ------------------------------------------------------------
 * 無料・件数制限なしで、フォームの内容を onestory310@gmail.com に
 * メールで届けるためのスクリプトです。
 *
 * 【設置手順】
 *  1. onestory310@gmail.com でログインした状態で
 *     https://script.google.com を開き「新しいプロジェクト」
 *  2. 既存のコードをすべて消して、このファイルの中身を貼り付け
 *  3. 右上「デプロイ」→「新しいデプロイ」
 *     ・種類の選択（歯車アイコン）→「ウェブアプリ」
 *     ・次のユーザーとして実行：自分（onestory310@gmail.com）
 *     ・アクセスできるユーザー：全員
 *     →「デプロイ」→ 初回は承認画面が出るので許可
 *  4. 表示される「ウェブアプリのURL」
 *     （https://script.google.com/macros/s/........./exec）をコピー
 *  5. assets/contact.js の FORM_ENDPOINT にそのURLを貼り付け
 *
 * ※ コードを修正したときは「デプロイ」→「デプロイを管理」→
 *    鉛筆アイコン →「新しいバージョン」→「デプロイ」で反映されます。
 */

/** 送信先メールアドレス */
var MAIL_TO = "onestory310@gmail.com";

/** 記録用スプレッドシートに残す場合はIDを入れる（空なら記録しません） */
var SHEET_ID = "";

/** 問い合わせた方へ自動返信するか */
var AUTO_REPLY = true;

/** 自動返信の差出人名 */
var FROM_NAME = "株式会社ワン・ストーリー";


function doPost(e) {
  try {
    var d = (e && e.parameter) || {};

    // 迷惑メール対策（人には見えない項目に入力があれば無視）
    if (d._gotcha) {
      return jsonOut({ result: "ok" });
    }

    var name = d["お名前"] || "（お名前未記入）";
    var email = d["メールアドレス"] || "";

    var lines = [];
    Object.keys(d).forEach(function (k) {
      if (k.charAt(0) === "_") return;
      lines.push("■ " + k + "\n" + (d[k] || "（未記入）"));
    });

    var body =
      "ウェブサイトのお問い合わせフォームから送信がありました。\n\n" +
      lines.join("\n\n") +
      "\n\n--------------------------------\n" +
      "受信日時：" +
      Utilities.formatDate(new Date(), "Asia/Tokyo", "yyyy/MM/dd HH:mm");

    var options = { name: FROM_NAME };
    if (email) options.replyTo = email;

    MailApp.sendEmail({
      to: MAIL_TO,
      subject: "【サイト】お問い合わせ：" + name + " 様",
      body: body,
      name: FROM_NAME,
      replyTo: email || MAIL_TO
    });

    // 自動返信
    if (AUTO_REPLY && email) {
      var reply =
        name + " 様\n\n" +
        "お問い合わせいただき、ありがとうございます。\n" +
        "下記の内容で承りました。内容を確認のうえ、担当者よりご連絡いたします。\n\n" +
        "--------------------------------\n" +
        lines.join("\n\n") +
        "\n--------------------------------\n\n" +
        "※ このメールは自動送信です。ご返信は不要です。\n\n" +
        FROM_NAME;

      MailApp.sendEmail({
        to: email,
        subject: "【" + FROM_NAME + "】お問い合わせありがとうございます",
        body: reply,
        name: FROM_NAME,
        replyTo: MAIL_TO
      });
    }

    // スプレッドシートに記録
    if (SHEET_ID) {
      var sheet = SpreadsheetApp.openById(SHEET_ID).getSheets()[0];
      if (sheet.getLastRow() === 0) {
        sheet.appendRow(["受信日時", "お名前", "会社名", "メールアドレス", "電話番号", "お問合せ内容", "メッセージ"]);
      }
      sheet.appendRow([
        new Date(),
        d["お名前"] || "",
        d["会社名"] || "",
        d["メールアドレス"] || "",
        d["電話番号"] || "",
        d["お問合せ内容"] || "",
        d["メッセージ"] || ""
      ]);
    }

    return jsonOut({ result: "ok" });
  } catch (err) {
    return jsonOut({ result: "error", message: String(err) });
  }
}

function doGet() {
  return ContentService.createTextOutput("OK");
}

function jsonOut(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(
    ContentService.MimeType.JSON
  );
}

/** 動作テスト用：エディタ上でこの関数を実行すると、自分宛にテストメールが届きます */
function testSend() {
  doPost({
    parameter: {
      "お名前": "テスト 太郎",
      "会社名": "テスト株式会社",
      "メールアドレス": MAIL_TO,
      "電話番号": "000-0000-0000",
      "お問合せ内容": "その他",
      "メッセージ": "これはテスト送信です。"
    }
  });
}
