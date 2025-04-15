import streamlit as st
from datetime import datetime, time
import platform

# App title
st.title("🕒 Time Converter with Midpoint Logic")

# Layout: Three columns
col1, col2, col3 = st.columns(3)

# Inputs
with col1:
    val1 = st.text_input("Column A (e.g., 1230)")

with col2:
    val2 = st.text_input("Column B (e.g., 0930)")

# Function: Convert HHMM string to time object
def convert_to_time(value):
    try:
        value = int(value)
        if 0 <= value <= 2359:
            hour = value // 100
            minute = value % 100
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                return time(hour=hour, minute=minute)
    except:
        return None
    return None

# Convert inputs
t1 = convert_to_time(val1)
t2 = convert_to_time(val2)

# Function: Combine time with today's date
def to_datetime(t):
    return datetime.combine(datetime.today(), t)

# Midpoint logic
midpoint = None
if t1 and t2:
    dt1 = to_datetime(t1)
    dt2 = to_datetime(t2)

    # Ensure dt1 is after dt2
    if dt1 < dt2:
        dt1, dt2 = dt2, dt1

    midpoint_dt = dt2 + (dt1 - dt2) / 2
    midpoint = midpoint_dt.time()

# Format time to H:MM:SS
def format_time(t):
    if platform.system() == "Windows":
        return t.strftime("%#H:%M:%S")
    else:
        return t.strftime("%-H:%M:%S")

# Display result
with col3:
    st.markdown("**Column C (Midpoint)**")
    if midpoint:
        st.success(format_time(midpoint))
    else:
        st.warning("Enter valid times in A and B")

# Debug Info
st.markdown("---")
st.markdown("### 🛠 Debug Info")
if t1:
    st.write(f"Column A as time: {t1.strftime('%H:%M')}")
else:
    st.write("Invalid input in Column A.")

if t2:
    st.write(f"Column B as time: {t2.strftime('%H:%M')}")
else:
    st.write("Invalid input in Column B.")
