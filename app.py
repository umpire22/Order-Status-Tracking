import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Order Status Tracking", layout="wide", initial_sidebar_state="expanded")

# --- TITLE & DESCRIPTION ---
st.title("📦 **Order Status Tracking Agent**")
st.markdown("""
This agent tracks the status of customer orders in real-time. Users can input an order ID and receive instant updates on the shipping and delivery status.
""", unsafe_allow_html=True)

# --- MANUAL INPUT SECTION ---
order_id = st.text_input("Enter Order ID:")

if order_id:
    # Placeholder for actual order status tracking logic
    order_status = "Shipped, in transit"
    
    st.markdown("### 📦 **Order Status**")
    st.write(f"Order ID: **{order_id}**")
    st.write(f"Status: **{order_status}**")
    
    # --- DOWNLOAD ORDER STATUS ---
    st.download_button(
        label="Download Order Status",
        data=f"Order ID: {order_id}\nStatus: {order_status}",
        file_name="order_status.txt",
        mime="text/plain"
    )

# --- STYLING ---
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.5em 1em;
    }
    .stTextInput>div>div>input {
        background-color: #333 !important;
        color: white !important;
        border-radius: 6px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
