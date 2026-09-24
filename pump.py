# ganesh
Pump Performance Calculator
import streamlit as st

# Page configuration
st.set_page_config(page_title="Thermodynamics Calculator", page_icon="⚡", layout="centered")

st.title("⚡ Thermodynamics Calculator")
st.write("Select a calculation from the sidebar menu to compute thermodynamic values.")

# Sidebar Navigation
option = st.sidebar.selectbox(
    "Choose Calculation",
    (
        "1. Work Done During Expansion",
        "2. Heat Supplied",
        "3. Change in Internal Energy",
        "4. Efficiency of Heat Engine",
    )
)

# ---------------------------------------------------------
# 1. Work Done During Expansion
# ---------------------------------------------------------
if option == "1. Work Done During Expansion":
    st.header("Work Done During Expansion")
    st.latex(r"W = P \times (V_2 - V_1)")
    
    col1, col2 = st.columns(2)
    with col1:
        p = st.number_input("Enter pressure (P) in Pa", value=0.0, format="%.2f")
        v1 = st.number_input("Enter initial volume (V₁) in m³", value=0.0, format="%.2f")
    with col2:
        v2 = st.number_input("Enter final volume (V₂) in m³", value=0.0, format="%.2f")
    
    if st.button("Calculate Work Done"):
        work = p * (v2 - v1)
        st.success(f"**Work Done (W):** {work:.2f} J")

# ---------------------------------------------------------
# 2. Heat Supplied
# ---------------------------------------------------------
elif option == "2. Heat Supplied":
    st.header("Heat Supplied")
    st.latex(r"Q = m \times c \times (T_2 - T_1)")
    
    col1, col2 = st.columns(2)
    with col1:
        m = st.number_input("Enter mass (m) in kg", value=0.0, format="%.2f")
        c = st.number_input("Enter specific heat capacity (c) in J/kg·K", value=0.0, format="%.2f")
    with col2:
        t1 = st.number_input("Enter initial temperature (T₁) in K", value=0.0, format="%.2f")
        t2 = st.number_input("Enter final temperature (T₂) in K", value=0.0, format="%.2f")
    
    if st.button("Calculate Heat Supplied"):
        q = m * c * (t2 - t1)
        st.success(f"**Heat Supplied (Q):** {q:.2f} J")

# ---------------------------------------------------------
# 3. Change in Internal Energy
# ---------------------------------------------------------
elif option == "3. Change in Internal Energy":
    st.header("Change in Internal Energy")
    st.latex(r"\Delta U = Q - W")
    
    col1, col2 = st.columns(2)
    with col1:
        q = st.number_input("Enter heat supplied (Q) in J", value=0.0, format="%.2f")
    with col2:
        w = st.number_input("Enter work done by system (W) in J", value=0.0, format="%.2f")
    
    if st.button("Calculate Change in Internal Energy"):
        delta_u = q - w
        st.success(f"**Change in Internal Energy (ΔU):** {delta_u:.2f} J")

# ---------------------------------------------------------
# 4. Efficiency of Heat Engine
# ---------------------------------------------------------
elif option == "4. Efficiency of Heat Engine":
    st.header("Efficiency of Heat Engine")
    st.latex(r"\eta = \left( \frac{Q_{in} - Q_{out}}{Q_{in}} \right) \times 100")
    
    col1, col2 = st.columns(2)
    with col1:
        q_in = st.number_input("Enter heat supplied (Q_in) in J", value=0.0, format="%.2f")
    with col2:
        q_out = st.number_input("Enter heat rejected (Q_out) in J", value=0.0, format="%.2f")
    
    if st.button("Calculate Efficiency"):
        if q_in <= 0:
            st.error("Heat input (Q_in) must be greater than zero.")
        else:
            efficiency = ((q_in - q_out) / q_in) * 100
            st.success(f"**Efficiency (η):** {efficiency:.2f}%")
