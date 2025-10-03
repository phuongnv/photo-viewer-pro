import streamlit as st
import cv2 as cv
import numpy as np
from PIL import Image
import io
import matplotlib.pyplot as plt

st.set_page_config(page_title="Photo Viewer Pro"
                   ,page_icon="🔍"
                   , layout="wide"
                   , initial_sidebar_state="expanded"
                   )

def main():
    st.sidebar.title("Photo Viewer Pro Panel")
    app_mode = st.sidebar.selectbox("Choose the app mode",
                                    ["Home page", 
                                     "Basic processing", 
                                     "Image Editor"])
    if app_mode == "Home page":
        show_home()
    elif app_mode == "Basic processing":
        show_basic_processing()
    elif app_mode == "Image Editor":
        # pass for now
        pass

def show_home():
    st.title("🖼️ AI Vision App với Streamlit")
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Chào mừng đến với AI Vision App!")
        st.markdown("""
        Ứng dụng này cung cấp các tính năng:
        - 📷 **Xử lý ảnh cơ bản**: Chuyển đổi grayscale, blur, edge detection
        - 👤 **Phát hiện khuôn mặt**: Sử dụng Haar Cascades
        - 🔍 **Phân tích nâng cao**: Histogram, thresholding, morphological operations
        - 💾 **Xuất kết quả**: Tải về ảnh đã xử lý
        """)
    
    with col2:
        st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
        st.success("Sẵn sàng xử lý ảnh!")

def show_basic_processing():
    st.title("🖼️ Xử lý ảnh cơ bản")

    uploaded_file = st.file_uploader("Tải lên ảnh của bạn", 
                                     type=["jpg", "jpeg", "png"], 
                                     help="Chọn một ảnh để tải lên và xử lý.")
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.success(f"Ảnh đã được tải {uploaded_file.name} lên thành công!")

        opencv_image = cv.cvtColor(np.array(image), cv.COLOR_RGB2BGR)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Ảnh gốc")
            st.image(image, width='stretch')
            st.info(f"Shape: {opencv_image.shape}")

        with col2:
            st.subheader("Ảnh đã xử lý")
            processing_option = st.selectbox("Chọn phương pháp xử lý",
                                             ["Grayscale", "Grayscale 2",
                                              "Gaussian Blur", 
                                              "Canny Edge Detection",
                                              "Thresholding",
                                              "Rotation",
                                              "HSV",
                                              "HLS"
                                              ])
            if processing_option == "Grayscale":
                processed_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2GRAY)
                st.image(processed_image, width='stretch', clamp=True)
                st.info(f"Shape: {processed_image.shape}")
            elif processing_option == "Grayscale 2":
                processed_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2RGBA)
                st.image(processed_image, width='stretch', clamp=True)
                st.info(f"Shape: {processed_image.shape}")
            elif processing_option == "Gaussian Blur":
                kernel_size = st.slider("Chọn kích thước kernel", 3, 31, 15, step=2)
                processed_image = cv.GaussianBlur(opencv_image, (kernel_size, kernel_size), 0)
                st.image(processed_image, width='stretch')
                st.info(f"Shape: {processed_image.shape}")
            elif processing_option == "Canny Edge Detection":
                low_threshold = st.slider("Ngưỡng thấp", 0, 255, 100)
                high_threshold = st.slider("Ngưỡng cao", 0, 255, 200)
                gray_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2GRAY)
                processed_image = cv.Canny(gray_image, low_threshold, high_threshold)
                st.image(processed_image, width='stretch', clamp=True)
                st.info(f"Shape: {processed_image.shape}")
            elif processing_option == "Thresholding":
                threshold_value = st.slider("Giá trị ngưỡng", 0, 255, 127)
                gray_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2GRAY)
                _, processed_image = cv.threshold(gray_image, threshold_value, 255, cv.THRESH_BINARY)
                st.image(processed_image, width='stretch', clamp=True)
                st.info(f"Shape: {processed_image.shape}")
            elif processing_option == "Rotation":
                angle = st.slider("Góc xoay", -180, 180, 0)
                (h, w) = opencv_image.shape[:2]
                center = (w // 2, h // 2)
                M = cv.getRotationMatrix2D(center, angle, 1.0)
                processed_image = cv.warpAffine(opencv_image, M, (w, h))
                st.image(processed_image, width='stretch')
                st.info(f"Shape: {processed_image.shape}")
            elif processing_option == "HSV":
                processed_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2HSV)
                st.image(processed_image, width='stretch')
                st.info(f"Shape: {processed_image.shape}")
            elif processing_option == "HLS":
                processed_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2HLS)
                st.image(processed_image, width='stretch')
                st.info(f"Shape: {processed_image.shape}")


            else: 
                # pass for now
                pass
        
            # Download button
            if st.button("Tải ảnh đã xử lý về"):
                _, png_buffer = cv.imencode(".png", processed_image)
                _, jpg_buffer = cv.imencode(".jpg", processed_image)
                # io_buf = io.BytesIO(buffer)
                st.download_button(label="Ảnh PNG",
                                data=io.BytesIO(png_buffer),
                                file_name="processed_image.png",
                                mime="image/png")
                st.download_button(label="Ảnh JPG",
                                data=io.BytesIO(jpg_buffer),
                                file_name="processed_image.jpg",
                                mime="image/jpeg")

if __name__ == "__main__":
    main()