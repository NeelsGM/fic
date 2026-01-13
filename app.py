import streamlit as st

st.set_page_config(page_title="F.I.C Scan Converter", layout="wide", page_icon="favicon.png")  # Add your favicon if in folder

# Inject custom CSS based on your site
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Rajdhani:wght@400;700&display=swap" rel="stylesheet">
    <style>
        /* Core dark carbon bg */
        .stApp {
            background-color: #0a0a0a;
            color: #d1d5db;  /* light gray text */
            font-family: 'Rajdhani', sans-serif;
        }

        /* Headings - Orbitron futuristic */
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif;
            font-weight: 700;
            color: white;
            text-transform: uppercase;
            letter-spacing: 0.2em;
            tracking-tighter;
        }

        /* Accent cyan */
        .cyan-text { color: #00f3ff; }
        .neon-text { 
            color: #d1d5db;
            text-shadow: 0 0 15px rgba(0, 243, 255, 0.7);
        }

        /* Glass panel style */
        .glass {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(255,255,255,0.1);
            backdrop-filter: blur(10px);
            border-radius: 0;  /* sharp edges like yours */
            padding: 2rem;
            transition: all 0.3s ease;
        }
        .glass:hover {
            border-color: #00f3ff;
        }

        /* Buttons - cyan, skew, uppercase */
        .stButton > button {
            background-color: #00f3ff;
            color: black;
            font-family: 'Orbitron', sans-serif;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.3em;
            padding: 1rem 2rem;
            border: none;
            border-radius: 0;
            transform: skewX(-10deg);
            transition: all 0.3s;
        }
        .stButton > button:hover {
            background-color: white;
            transform: skewX(-10deg) scale(1.05);
        }

        /* Input fields */
        .stTextInput > div > div > input,
        .stFileUploader > div {
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.1);
            color: white;
            padding: 1rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }
        .stTextInput > div > div > input:focus {
            border-color: #00f3ff;
        }

        /* Sidebar if we use later */
        section[data-testid="stSidebar"] {
            background: #000000;
            border-right: 1px solid rgba(255,255,255,0.1);
        }

        /* Remove Streamlit header/footer padding */
        .st-emotion-cache-1y4p8pa {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Header like your hero
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 1.2rem; color: #00f3ff; border: 1px solid rgba(0,243,255,0.3); display: inline-block; padding: 0.5rem 1rem; border-radius: 9999px; background: rgba(0,243,255,0.05);">
            Westville • Durban • South Africa
        </div>
        <h1 style="font-size: 4rem; margin: 1rem 0;">
            FORGED IN <span class="neon-text">CARBON</span>
        </h1>
        <p style="font-size: 1.5rem; color: #9ca3af; text-transform: uppercase; letter-spacing: 0.2em;">
            Scan Converter • Reverse Engineering Ready
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div class='glass'>", unsafe_allow_html=True)
st.header("Upload Your Scan")
uploaded_file = st.file_uploader("Drag & drop STL / Point Cloud here", type=["stl", "ply", "obj", "pts"])

if uploaded_file:
    st.success(f"File received: {uploaded_file.name}")
    # Placeholder for processing
    if st.button("Convert to Editable STEP / BREP"):
        st.info("Processing... (mesh repair + AI styling in progress)")

st.markdown("</div>", unsafe_allow_html=True)

# Footer snippet
st.markdown("""
    <hr style="border-color: rgba(255,255,255,0.1);">
    <div style="text-align: center; color: #4b5563; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.5em;">
        © 2026 FORGED IN CARBON | WESTVILLE, DURBAN, SA
    </div>
""", unsafe_allow_html=True)