# データ分析・抽出

## 主な機能・責務

- 情報を入力する
  - koyo backend api -> koyo cluster
- データを分析・抽出する
  - koyo cluster が担当
- データを返す
  - koyo cluster -> koyo backend api

## 概要

各アルゴリズムの詳細については、[各アルゴリズム](./koyo/README.md)を参照してください。
シーケンス図は、[シーケンス図](../../sequence/koyo/README.md)を参照してください。

Kizunaとの詳細なやり取りについてはKizunaの仕様のページで説明します。[Kizunaの仕様](../kizuna/README.md)

データの処理フェーズであるこの機能には、Backend Server と koyo Cluster の間での通信のみで成り立ちます。
koyo Cluster は GCP 内部以外にはアクセスできません。
koyo Cluster に属する、各 Koyo は、自らが必要とする情報をあらかじめ Backend Server に登録します。
Backend Server は、その情報(その情報に関連付けられた外部 API)が更新された時に、各 Koyo に通知します。
これによって、各 Koyo は最新の情報でデータを処理し、結果を Backend Server に返します。

上記の理由により、Koyo はイベント駆動型となっています。
