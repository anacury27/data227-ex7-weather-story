import streamlit as st
from utils.io import load_weather
from charts.charts import chart_dashboard
from charts.charts import chart_interactive_monthly_temp

st.set_page_config(page_title="Explore", layout="wide")
df = load_weather()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—focus on one weather type, then zoom into a time window.")

st.altair_chart(chart_dashboard(df), use_container_width=True)

st.markdown("**Guided prompts:**")
st.write("- Filter to one weather type (e.g., `sun`, `rain`)—does the temperature distribution shift?")
st.write("- Brush a specific year—do extremes cluster in particular periods?")
st.write("- Compare histogram shape across weather types—what changes most: center, spread, or tails?")

st.header("New interactive view: focus on a time window")
st.write("Brush a time range on the top plot. The histogram below updates to only those days.")
st.altair_chart(chart_interactive_monthly_temp(df), use_container_width=True)
st.caption("Takeaway: selecting a window makes it easier to compare temperature distributions across seasons.")
