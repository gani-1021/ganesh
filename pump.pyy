import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Pump Calculator",
    page_icon="⚙️",
    layout="centered"
)

st.title("⚙️ Pump Calculator")
st.write("Select a pump calculation from the sidebar menu to begin.")

# Constant
G = 9.81  # Acceleration due to gravity (m/s²)

# Sidebar Menu
option = st.sidebar.selectbox(
    "Choose Calculation",
    (
        "1. Calculate Hydraulic Power",
        "2. Calculate Shaft Power",
        "3. Calculate Pump Efficiency",
        "4. Calculate Pump Head",
        "5. Calculate Discharge",
    )
)

# ---------------------------------------------------------
# 1. Hydraulic Power
# ---------------------------------------------------------
if option == "1. Calculate Hydraulic Power":
    st.header("Calculate Hydraulic Power")
    st.latex(r"P_{hyd} = \rho \times g \times Q \times H")
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Enter fluid density (ρ) in kg/m³", value=1000.0, format="%.2f")
        Q = st.number_input("Enter discharge (Q) in m³/s", value=0.0, format="%.4f")
    with col2:
        H = st.number_input("Enter pump head (H) in m", value=0.0, format="%.2f")

    if st.button("Calculate Hydraulic Power"):
        hydraulic_power = rho * G * Q * H
        hydraulic_power_kw = hydraulic_power / 1000
        
        st.success(f"**Hydraulic Power:** {hydraulic_power:.2f} W ({hydraulic_power_kw:.2f} kW)")

# ---------------------------------------------------------
# 2. Shaft Power
# ---------------------------------------------------------
elif option == "2. Calculate Shaft Power":
    st.header("Calculate Shaft Power")
    st.latex(r"P_{shaft} = \frac{\rho \times g \times Q \times H}{\eta / 100}")
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Enter fluid density (ρ) in kg/m³", value=1000.0, format="%.2f")
        Q = st.number_input("Enter discharge (Q) in m³/s", value=0.0, format="%.4f")
    with col2:
        H = st.number_input("Enter pump head (H) in m", value=0.0, format="%.2f")
        efficiency = st.number_input("Enter pump efficiency (η) in %", value=80.0, format="%.2f")

    if st.button("Calculate Shaft Power"):
        if efficiency <= 0:
            st.error("Efficiency must be greater than 0.")
        else:
            efficiency_decimal = efficiency / 100
            shaft_power = (rho * G * Q * H) / efficiency_decimal
            shaft_power_kw = shaft_power / 1000
            
            st.success(f"**Shaft Power:** {shaft_power:.2f} W ({shaft_power_kw:.2f} kW)")

# ---------------------------------------------------------
# 3. Pump Efficiency
# ---------------------------------------------------------
elif option == "3. Calculate Pump Efficiency":
    st.header("Calculate Pump Efficiency")
    st.latex(r"\eta = \left( \frac{P_{hyd}}{P_{shaft}} \right) \times 100")
    
    col1, col2 = st.columns(2)
    with col1:
        hydraulic_power = st.number_input("Enter hydraulic power in kW", value=0.0, format="%.2f")
    with col2:
        shaft_power = st.number_input("Enter shaft power in kW", value=0.0, format="%.2f")

    if st.button("Calculate Efficiency"):
        if shaft_power <= 0:
            st.error("Shaft power must be greater than 0.")
        else:
            efficiency = (hydraulic_power / shaft_power) * 100
            st.success(f"**Pump Efficiency (η):** {efficiency:.2f}%")

# ---------------------------------------------------------
# 4. Pump Head
# ---------------------------------------------------------
elif option == "4. Calculate Pump Head":
    st.header("Calculate Pump Head")
    st.latex(r"H = \frac{P_{hyd}}{\rho \times g \times Q}")
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Enter fluid density (ρ) in kg/m³", value=1000.0, format="%.2f")
        hydraulic_power = st.number_input("Enter hydraulic power in kW", value=0.0, format="%.2f")
    with col2:
        Q = st.number_input("Enter discharge (Q) in m³/s", value=0.0, format="%.4f")

    if st.button("Calculate Pump Head"):
        if rho <= 0 or Q <= 0:
            st.error("Density and discharge must be greater than 0.")
        else:
            hydraulic_power_w = hydraulic_power * 1000
            head = hydraulic_power_w / (rho * G * Q)
            st.success(f"**Pump Head (H):** {head:.2f} m")

# ---------------------------------------------------------
# 5. Discharge
# ---------------------------------------------------------
elif option == "5. Calculate Discharge":
    st.header("Calculate Discharge")
    st.latex(r"Q = \frac{P_{hyd}}{\rho \times g \times H}")
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input("Enter fluid density (ρ) in kg/m³", value=1000.0, format="%.2f")
        hydraulic_power = st.number_input("Enter hydraulic power in kW", value=0.0, format="%.2f")
    with col2:
        H = st.number_input("Enter pump head (H) in m", value=0.0, format="%.2f")

    if st.button("Calculate Discharge"):
        if rho <= 0 or H <= 0:
            st.error("Density and head must be greater than 0.")
        else:
            hydraulic_power_w = hydraulic_power * 1000
            discharge = hydraulic_power_w / (rho * G * H)
            st.success(f"**Discharge (Q):** {discharge:.6f} m³/s ({discharge * 1000:.3f} L/s)")
