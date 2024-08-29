# 各サービスについて

データに関しては、[データの定義](../data/README.md)を参照。
シーケンス図に関しては、[シーケンス図](../sequence/RAEDME.md)を参照。

## 概要

本プロジェクトは、大まかに Kizuna(Backend) と Polka(Visualizer) と Koyo(koyo Cluster) の 3 つの部分に分かれる。
詳細は、[アーキテクチャ](../../architecture/README.md)及び、[データの定義](./data.md)を参照。

## 目次

- [Koyo](./koyo/README.md)
  - 入力データを処理し、各種データを抽出する機能
- [Kizuna](./kizuna/README.md)
  - 各種データを検索し、指定のフォーマットで返す機能
- [ビジュアライザー](./polka/README.md)
  - マップにヒートマップを表示する機能
