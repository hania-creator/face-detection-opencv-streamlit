import streamlit as st
import cv2
import numpy as np
from detector import detect_faces

st.set_page_config(
    page_title="Face Detection using OpenCV",
    page_icon="😊",
    layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #07111f 0%, #0f2a4d 40%, #1f3d72 100%);
        color: #f5f7ff;
    }

    .block-container {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 18px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
        backdrop-filter: blur(10px);
    }

    h1, h2, h3, p, label, .stTextInput > label, .stSelectbox > label {
        color: #f5f7ff !important;
    }

    .stButton > button {
        background: linear-gradient(90deg, #4f7cff, #7b61ff);
        color: white;
        border: none;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("😊 Face Detection using OpenCV")
st.write("Upload an image to detect human faces.")

uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, channels="BGR", use_container_width=True)

    detected_image, face_count = detect_faces(image.copy())

    with col2:
        st.subheader("Detected Image")
        st.image(detected_image, channels="BGR", use_container_width=True)

    st.success(f"✅ Faces Detected: {face_count}")

    success, buffer = cv2.imencode(".jpg", detected_image)

    st.download_button(
        label="📥 Download Result",
        data=buffer.tobytes(),
        file_name="detected_faces.jpg",
        mime="image/jpeg"
    )