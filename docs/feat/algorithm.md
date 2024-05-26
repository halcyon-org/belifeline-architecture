# データ分析・抽出

## 主な機能・責務

- 情報を入力する
  - algorithm backend api -> algorithm cluster
- データを分析・抽出する
  - algorithm cluster が担当
- データを返す
  - algorithm cluster -> algorithm backend api

## 概要

各アルゴリズムの詳細については、[各アルゴリズム](./algorithm/README.md)を参照してください。

データの処理フェーズであるこの機能には、Backend ServerとAlgorithm Clusterの間での通信のみで成り立ちます。Algorithm ClusterはGCP内部以外にはアクセスできません。
Algorithm Clusterに属する、各Algorithm Functionは、自らが必要とする情報をあらかじめBackend Serverに登録します。Backend Serverは、その情報(その情報に関連付けられた外部API)が更新された時に、各Algorithm Functionに通知します。
これによって、各Algorithm Functionは最新の情報でデータを処理し、結果をBackend Serverに返します。

上記の理由により、Algorithm Functionはイベント駆動型となっています。
