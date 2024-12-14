import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image, ImageEnhance
import numpy as np
import base64

# Konfigurasi halaman
st.set_page_config(page_title="Kelompok Project", layout="centered")

# Fungsi untuk mengubah file gambar lokal menjadi Base64
def set_background_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
        st.markdown(
            f"""
            <style>
            [data-testid="stAppViewContainer"] {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
            }}
            [data-testid="stSidebar"] {{
                background-color: rgba(255, 255, 255, 0.8);
            }}
            .title {{
                font-size: 50px !important;
                color: black;
                text-align: center;
                font-weight: bold;
            }}
            .subheader {{
                font-size: 35px !important;
                color: black;
                text-align: center;
                font-weight: bold;
                margin-top: 50px;  /* Menambahkan jarak antar subheader */
            }}
            .content {{
                font-size: 100px;
                color: black;
                text-align: center;
            }}
            .logo {{
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 300px;
                padding-bottom: 40px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error(f"File background tidak ditemukan. Periksa path gambar Anda.")

# Atur path file lokal untuk gambar latar belakang
background_image_path = (r"C:\Users\Lenovo\OneDrive\Gambar\Presiden t1.jpg")
set_background_image(background_image_path)

# Navigasi sidebar
with st.sidebar:
    select = option_menu(
        'Project Final Exam',
        ['Introduction', 'Application'],
        default_index=0
    )

if select == 'Introduction':
    # Header dan logo
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<p class='title'>INTRODUCTION</p>", unsafe_allow_html=True)
    st.markdown("<img src='data:image/png;base64,{}' class='logo'>".format(
        base64.b64encode(open('./Gambar/Presiden t1.jpg', "rb").read()).decode()),
        unsafe_allow_html=True)

    # Informasi kelompok
    st.markdown("<p class='subheader'>Group 3 IEN 1 2024</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Chyntia Adinda Ramadani (004202305053)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Ratu Enjelita (004202305032)</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Salsabilla Clarysa Putri (004202305016)</p>", unsafe_allow_html=True)

    st.markdown("<p class='subheader'>Program Study</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Industrial Engineering</p>", unsafe_allow_html=True)

    st.markdown("<p class='subheader'>Faculty</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>Engineering</p>", unsafe_allow_html=True)

    # Foto anggota
    st.markdown("<p class='subheader'>Member Photo</p>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(r"C:\\Users\\Lenovo\\OneDrive\\Gambar\\cinta2.jpg", caption="Chyntia Adinda", use_container_width=True)
    with col2:
        st.image(r"C:\\Users\\Lenovo\\OneDrive\\Gambar\\ratu2.jpg", caption="Ratu Engelita", use_container_width=True)
    with col3:
        st.image(r"C:\\Users\\Lenovo\\OneDrive\\Gambar\\salsa2.jpg", caption="Salsabilla Clarysa", use_container_width=True)

elif select == 'Application':
    # Deskripsi aplikasi
    st.markdown("<p class='title'>APPLICATION DESCRIPTION</p>", unsafe_allow_html=True)
    st.markdown("<p class='content'>This application allows users to perform various transformations on images, such as rotation, skew, zoom, scale, resize, brightness adjustment, and transparency. Users can choose the type of transformation and adjust parameters as desired, as well as see the results of image changes directly, making it easier to edit images as needed.</p>", unsafe_allow_html=True)

    # Deskripsi aplikasi
    st.markdown("<p class='subheader'>Image Transformation</p>", unsafe_allow_html=True)
    
    # Upload gambar
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Transformasi gambar
        transformation = st.selectbox("Select Transformation", ["Select", "Rotate", "Skew", "Zoom", "Scale", "Resize", "Brightness", "Transparency"])

        if transformation == "Rotate":
            angle = st.number_input("Enter Rotation Angle (degrees)", min_value=0, max_value=360, value=90, step=1)
            rotated_image = image.rotate(angle)
            st.image(rotated_image, caption="Rotated Image", use_container_width=True)

        elif transformation == "Skew":
            skew_factor = st.number_input("Enter Skew Factor", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            img_array = np.array(image)
            # Apply skew by transforming the image matrix
            rows, cols = img_array.shape[:2]
            M = np.float32([[1, skew_factor, 0], [0, 1, 0]])  # Using a transformation matrix
            skewed_image = Image.fromarray(np.asarray(cv2.warpAffine(img_array, M, (cols, rows))))
            st.image(skewed_image, caption="Skewed Image", use_container_width=True)

        elif transformation == "Zoom":
            zoom_factor = st.number_input("Enter Zoom Factor", min_value=1.0, max_value=10.0, value=1.5, step=0.1)
            img_array = np.array(image)
            height, width = img_array.shape[:2]
            new_height = int(height * zoom_factor)
            new_width = int(width * zoom_factor)
            zoomed_image = image.resize((new_width, new_height))
            st.image(zoomed_image, caption="Zoomed Image", use_container_width=True)

        elif transformation == "Scale":
            scale_factor = st.number_input("Enter Scale Factor", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            width, height = image.size
            scaled_image = image.resize((int(width * scale_factor), int(height * scale_factor)))
            st.image(scaled_image, caption="Scaled Image", use_container_width=True)

        elif transformation == "Resize":
            new_width = st.number_input("Enter New Width", min_value=100, max_value=2000, value=image.width, step=10)
            new_height = st.number_input("Enter New Height", min_value=100, max_value=2000, value=image.height, step=10)
            resized_image = image.resize((new_width, new_height))
            st.image(resized_image, caption="Resized Image", use_container_width=True)

        elif transformation == "Brightness":
            brightness = st.slider("Adjust Brightness", min_value=0.1, max_value=10.0, value=1.0, step=0.1)
            enhancer = ImageEnhance.Brightness(image)
            bright_image = enhancer.enhance(brightness)
            st.image(bright_image, caption="Brightness Adjusted Image", use_container_width=True)

        elif transformation == "Transparency":
            transparency = st.slider("Adjust Transparency", min_value=0.0, max_value=1.0, value=1.0, step=0.1)
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            data = np.array(image)
            data[..., 3] = (data[..., 3] * transparency).astype(np.uint8)
            transparent_image = Image.fromarray(data, 'RGBA')
            st.image(transparent_image, caption="Transparency Adjusted Image", use_container_width=True)
