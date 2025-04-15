import streamlit as st
from datetime import datetime, timedelta, time

st.title("Time Converter with Midpoint Logic")

# Create layout with 3 columns
col1, col2, col3 = st.columns(3)

# Input for A and B (time-like numbers)
with col1:
    val1 = st.text_input("Column A (e.g., 1230)", key="col1")

with col2:
    val2 = st.text_input("Column B (e.g., 1215)", key="col2")

# Function to convert HHMM to datetime.time
def convert_to_time(value):
    try:
        value = int(value)
        if 0 <= value <= 2359:
            hours = value // 100
            minutes = value % 100
            if minutes < 60:
                return time(hour=hours, minute=minutes)
    except ValueError:
        pass
    return None

# Convert inputs
t1 = convert_to_time(val1)
t2 = convert_to_time(val2)

# Helper to convert time -> datetime (today's date)
def to_datetime(t):
    return datetime.combine(datetime.today(), t)

# Midpoint calculation
midpoint = None
if t1 and t2:
    dt1 = to_datetime(t1)
    dt2 = to_datetime(t2)

    # Normalize so dt1 is always after dt2
    if dt1 < dt2:
        dt1, dt2 = dt2, dt1

    delta = dt1 - dt2
    midpoint = dt2 + delta / 2

# Display converted times
with col3:
    st.markdown("**Column C (Midpoint)**")
    if midpoint:
        st.success(midpoint.time().strftime("%H:%M"))
    else:
        st.warning("Enter valid times in A and B")

# Optional: show converted raw times
st.markdown("### Debug Info")
if t1: st.write(f"Column A as time: {t1.strftime('%H:%M')}")
if t2: st.write(f"Column B as time: {t2.strftime('%H:%M')}")
