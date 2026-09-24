```python
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pump Calculator",
    page_icon="💧",
    layout="centered"
)

st.title("💧 Pump Calculator")
st.markdown("Calculate hydraulic power, shaft power, pump efficiency, pump head, and discharge.")

st.divider()

# Sidebar menu
st.sidebar.header("Pump Calculations")

choice = st.sidebar.selectbox(
    "Select Calculation",
    [
        "Hydraulic Power",
        "Shaft Power",
        "Pump Efficiency",
        "Pump Head",
        "Discharge"
    ]
)

g = 9.81  # gravitational acceleration

# --------------------------------------------------
# 1. Hydraulic Power
# --------------------------------------------------
if choice == "Hydraulic Power":
    st.header("🔹 Hydraulic Power")

    rho = st.number_input(
        "Fluid Density (kg/m³)",
        min_value=0.0,
        value=1000.0,
        step=1.0
    )

    Q = st.number_input(
        "Discharge (m³/s)",
        min_value=0.0,
        value=0.01,
        step=0.001,
        format="%.6f"
    )

    H = st.number_input(
        "Pump Head (m)",
        min_value=0.0,
        value=10.0,
        step=0.1
    )

    if st.button("Calculate Hydraulic Power"):
        hydraulic_power = rho * g * Q * H
        hydraulic_power_kw = hydraulic_power / 1000

        st.success(f"Hydraulic Power = {hydraulic_power:.2f} W")
        st.success(f"Hydraulic Power = {hydraulic_power_kw:.2f} kW")


# --------------------------------------------------
# 2. Shaft Power
# --------------------------------------------------
elif c
```
