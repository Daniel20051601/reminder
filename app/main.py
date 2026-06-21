import sys
from pathlib import Path

# Add parent directory to sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
from app.navigation.navigation import build_navigation

st.set_page_config(
    page_title="Reminder",
    layout="wide",
    page_icon=":material/alarm_on:"
)

pg = build_navigation()
pg.run()