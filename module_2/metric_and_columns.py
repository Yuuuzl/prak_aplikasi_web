import streamlit as st

# Metric
st.metric(label="Harga telur", value=26000, delta=1000)
st.metric(label="Harga ayam", value=30000, delta=-1000)
st.metric(label="Harga es teh", value=2000, delta=0, delta_color="off")

st.markdown("---")

# Columns
col1, col2, col3, col4 = st.columns(4)
col1.metric("Temperature", "25°C", "+1°C")
col2.metric("Humidity", "80%", "-5%")
col3.metric("Pressure", "1013hPa", "+2hPa")
col4.metric("Wind", "10km/h", "-1km/h")