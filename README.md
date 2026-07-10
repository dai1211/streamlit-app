# Streamlit TODO App

Streamlitで作成したシンプルなTODOアプリです。Pythonコードのみで基本UIと操作を実装しています。

## 現在の機能（Issue #4）

- `st.session_state` を使ったタスクの一時保持
- タスク追加（テキスト入力 + 追加ボタン、追加後は入力欄クリア）
- チェックボックスによる完了/未完了の切り替え
- タスク削除（🗑️ボタン）
- 表示フィルター（すべて / 未完了 / 完了）
- `todos.json` への自動保存と起動時の自動読み込み（ローカル永続化）

> `todos.json` が破損している場合は、空のリストで起動し、アプリ上に警告を表示します。

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
├── todos.json  # 初回保存時に自動生成
├── requirements.txt
└── README.md
```
