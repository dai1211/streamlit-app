import json
from pathlib import Path

import streamlit as st


st.title("Streamlit TODO App")

TODOS_FILE_PATH = Path(__file__).resolve().parent / "todos.json"


def load_todos() -> list[dict]:
    if not TODOS_FILE_PATH.exists():
        return []

    try:
        raw = TODOS_FILE_PATH.read_text(encoding="utf-8")
        data = json.loads(raw)
    except json.JSONDecodeError:
        st.warning("todos.json の読み込みに失敗したため、空のリストで起動しました。")
        return []
    except OSError as exc:
        st.error(f"todos.json の読み込み中にエラーが発生しました: {exc}")
        return []

    if not isinstance(data, list):
        st.warning("todos.json の形式が不正なため、空のリストで起動しました。")
        return []

    todos: list[dict] = []
    for item in data:
        if not isinstance(item, dict):
            continue
        text = item.get("text")
        done = item.get("done")
        if isinstance(text, str) and isinstance(done, bool):
            todos.append({"text": text, "done": done})

    return todos


def save_todos(todos: list[dict]) -> None:
    try:
        TODOS_FILE_PATH.write_text(
            json.dumps(todos, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError as exc:
        st.error(f"todos.json の保存中にエラーが発生しました: {exc}")


if "todos" not in st.session_state:
    st.session_state.todos = load_todos()

if "new_task" not in st.session_state:
    st.session_state.new_task = ""

with st.form("add_task_form", clear_on_submit=True):
    st.text_input("タスクを入力", key="new_task")
    add_clicked = st.form_submit_button("追加")

if add_clicked:
    task_text = st.session_state.new_task.strip()
    if task_text:
        st.session_state.todos.append({"text": task_text, "done": False})
        save_todos(st.session_state.todos)
        st.rerun()
    else:
        st.warning("タスクを入力してください。")

filter_option = st.radio(
    "表示フィルター",
    ("すべて", "未完了", "完了"),
    horizontal=True,
)


def is_visible(todo: dict) -> bool:
    if filter_option == "未完了":
        return not todo["done"]
    if filter_option == "完了":
        return todo["done"]
    return True


visible_found = False
for index, todo in enumerate(st.session_state.todos):
    if not is_visible(todo):
        continue

    visible_found = True
    col_task, col_delete = st.columns([6, 1])
    with col_task:
        checked = st.checkbox(todo["text"], value=todo["done"], key=f"todo-{index}")
        if checked != todo["done"]:
            st.session_state.todos[index]["done"] = checked
            save_todos(st.session_state.todos)
            st.rerun()
    with col_delete:
        if st.button("🗑️", key=f"delete-{index}"):
            st.session_state.todos.pop(index)
            save_todos(st.session_state.todos)
            st.rerun()

if not visible_found:
    st.info("表示するタスクがありません。")
