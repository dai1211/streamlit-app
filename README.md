# Streamlit TODO App

Streamlitで作成したシンプルなTODOアプリです。Pythonコードのみで基本UIと操作を実装しています。

## 現在の機能（Issue #1）

- タスク追加（テキスト入力 + 追加ボタン）
- チェックボックスによる完了/未完了の切り替え
- タスク削除（🗑️ボタン）
- 表示フィルター（すべて / 未完了 / 完了）

> この時点ではデータ永続化（ファイル保存）は未実装です。

## セットアップ手順

1. 仮想環境を作成・有効化します。

   **Windows (コマンドプロンプト):**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS / Linux:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. 依存関係をインストールします。

   ```bash
   pip install -r requirements.txt
   ```

3. アプリを起動します。

   ```bash
   streamlit run app.py
   ```

4. ブラウザで `http://localhost:8501` を開きます。

## ディレクトリ構成

```text
streamlit-app/
├── app.py
├── requirements.txt
└── README.md
```
