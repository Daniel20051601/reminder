import streamlit as st

def build_navigation():
    reminders = st.Page("pages/reminders.py", title="Reminders", default=True)
    dashboard = st.Page("pages/dashboard.py", title="Dashboard")
    todo_list = st.Page("pages/todo_list.py", title="To-Do List")

    return st.navigation([reminders, todo_list, dashboard])