import streamlit as st

# Inject Bootstrap and Custom CSS
st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body {
            background: #121212;
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background: linear-gradient(135deg, #121212 0%, #1f1f1f 100%);
        }
        .card {
            margin-top: 50px;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 15px 30px rgba(0,0,0,0.5);
            background: rgba(33, 33, 33, 0.95);
            border: 1px solid #333;
            backdrop-filter: blur(5px);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.6);
            border: 1px solid #444;
        }
        .btn-custom {
            background: linear-gradient(to right, #8E2DE2, #4A00E0);
            color: white;
            font-weight: 600;
            border-radius: 30px;
            padding: 10px 25px;
            border: none;
            box-shadow: 0 4px 15px rgba(78, 0, 224, 0.3);
            transition: all 0.3s ease;
        }
        .btn-custom:hover {
            background: linear-gradient(to right, #7928CA, #3A0CA3);
            box-shadow: 0 6px 18px rgba(142, 45, 226, 0.4);
            transform: translateY(-2px);
            color: white;
        }
        .result {
            font-size: 22px;
            font-weight: bold;
            color: #6ee7b7;
            margin-top: 25px;
            padding: 15px;
            border-radius: 10px;
            background: rgba(16, 185, 129, 0.1);
            box-shadow: 0 4px 10px rgba(16, 185, 129, 0.15);
            border: 1px solid rgba(16, 185, 129, 0.2);
        }
        .app-title {
            font-weight: 700;
            color: #e2e8f0;
            text-shadow: 0 0 10px rgba(142, 45, 226, 0.5);
            margin-bottom: 20px;
        }
        .input-group {
            margin-bottom: 20px;
        }
        .input-label {
            font-weight: 600;
            margin-bottom: 8px;
            color: #d1d5db;
        }
        .stNumberInput {
            border-radius: 10px !important;
        }
        .footer {
            margin-top: 30px;
            font-size: 14px;
            color: rgba(255,255,255,0.5);
        }
        /* Dark mode overrides for Streamlit elements */
        .stTextInput > div > div {
            background-color: #2d2d2d !important;
            color: #e2e8f0 !important;
        }
        .stNumberInput > div > div {
            background-color: #2d2d2d !important;
            border: 1px solid #3d3d3d !important;
            color: #e2e8f0 !important;
        }
        .stNumberInput > div > div > div > input {
            color: #e2e8f0 !important;
        }
        .stButton > button {
            background: linear-gradient(to right, #8E2DE2, #4A00E0) !important;
            color: white !important;
            font-weight: 600 !important;
            border: none !important;
            box-shadow: 0 4px 15px rgba(78, 0, 224, 0.3) !important;
        }
        .stButton > button:hover {
            background: linear-gradient(to right, #7928CA, #3A0CA3) !important;
            box-shadow: 0 6px 18px rgba(142, 45, 226, 0.4) !important;
            transform: translateY(-2px) !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='text-center app-title'><i class='fas fa-calculator'></i> Dark Mode Calculator</h2>", unsafe_allow_html=True)

# Create a Bootstrap card with improved layout
st.markdown('<div class="container d-flex justify-content-center">', unsafe_allow_html=True)

st.markdown('<h4 class="mb-4 text-center" style="color:#8E2DE2;"><i class="fas fa-plus-circle"></i> Addition Calculator</h4>', unsafe_allow_html=True)

# Input fields with better styling
st.markdown('<div class="input-group">', unsafe_allow_html=True)
st.markdown('<label class="input-label"><i class="fas fa-hashtag"></i> First Number</label>', unsafe_allow_html=True)
a = st.number_input("", key="num1", help="Enter your first number here")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="input-group">', unsafe_allow_html=True)
st.markdown('<label class="input-label"><i class="fas fa-hashtag"></i> Second Number</label>', unsafe_allow_html=True)
b = st.number_input("", key="num2", help="Enter your second number here")
st.markdown('</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('Calculate Sum', key="add_btn", use_container_width=True):
        c = a + b
        st.markdown(f"""
        <div class='result text-center'>
            <i class='fas fa-equals'></i> Result: {a} + {b} = <span style='color:#8E2DE2'>{c}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer text-center mt-4"><i class="fas fa-moon"></i> Dark Mode Calculator | <i class="fas fa-code"></i> Developed with Streamlit & Bootstrap</div>', unsafe_allow_html=True)
