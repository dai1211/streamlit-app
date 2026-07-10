import streamlit as st


st.title("Streamlit TODO App")

if "todos" not in st.session_state:
    st.session_state.todos = []

if "new_task" not in st.session_state:
    st.session_state.new_task = ""

with st.form("add_task_form", clear_on_submit=True):
    st.text_input("タスクを入力", key="new_task")
    add_clicked = st.form_submit_button("追加")

if add_clicked:
    task_text = st.session_state.new_task.strip()
    if task_text:
        st.session_state.todos.append({"text": task_text, "done": False})
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
            st.rerun()
    with col_delete:
        if st.button("🗑️", key=f"delete-{index}"):
            st.session_state.todos.pop(index)
            st.rerun()

if not visible_found:
    st.info("表示するタスクがありません。")
