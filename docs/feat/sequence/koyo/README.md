# アルゴリズムクラスターシーケンス図

アルゴリズムクラスター(Koyo)はイベント駆動型である。
イベントは、初回起動時(情報登録)と、外部情報更新時、パラメータ別要求の 3 つがある。

それぞれ、

- 初回起動時
  - Koyo のリリースの際にアルゴリズム情報を登録する
  - その時点の情報でデータを分析する
- 外部情報更新時
  - 外部情報(外部 API 等)が更新された際に、データを更新する
- パラメータ別要求時
  - プロバイダー経由で現在保存されていないデータが要求された際に、データを生成する

## 初回起動時

アルゴリズム情報については、[データの定義#アルゴリズム情報](../data.md#アルゴリズム情報)を参照

```mermaid
sequenceDiagram
    participant server as アルゴリズムバックエンド
    participant db as データベース
    participant func as Koyo
    server ->> func: 初回起動イベントをコール
    func ->> server: アルゴリズム情報を登録
    server ->> db: 情報を保存
    func ->> server: 外部情報を要求
    server ->> func: 外部情報を返却
    func ->> func: データ分析・抽出
    func ->> server: データを返却
    server ->> db: データを保存

```

## 外部情報更新時・パラメータ別要求時

```mermaid
sequenceDiagram
    participant server as アルゴリズムバックエンド
    participant db as データベース
    participant func as Koyo
    server ->> func: 外部情報更新イベントをコール
    func ->> server: 情報を要求
    server ->> func: 要求に基づき、外部情報を返却
    func ->> func: データ分析・抽出
    func ->> server: データを返却

```
