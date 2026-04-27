import cv2
import streamlit as st
import numpy as np
from histogram import Histogram
from transforms import Transform
from filters import Filters
from blending import Blend
from color_space import ColorSpace
from threshold import Threshold
from edges import Edges
from contours import Contours
def download_image_button(label:str, img_array:np.ndarray, filename:str):
    """
    Convert ndarray to jpeg and create the download button.
    Args:
        label(str):
            label for button download.
        img_array(numpy.ndarray):
            the source image in numpy array format.
        filename(str):
            selected name for downloaded file.
    """
    ok, buf = cv2.imencode(".jpg", img_array)
    st.download_button(label=label,
                       data=buf.tobytes(),
                       file_name=filename,
                       mime="image/jpeg")
class WebApp:
    """
        Main web-based interface for the Mini Photo Editor application.

            This class is responsible for building the Streamlit UI, handling
            user interactions, receiving uploaded images, and delegating
            processing tasks (filters, transforms, color conversions, edges, etc.)
            to corresponding image‑processing modules.

            Attributes:
                option (str | None):
                    The operation selected by the user from the sidebar.
                image (UploadedFile | None):
                    Raw uploaded image file received from Streamlit uploader.
                source_image (numpy.ndarray | None):
                    Decoded BGR image loaded with OpenCV (cv2.imdecode).
    """
    def __init__(self):
        """
        Initialize the Streamlit UI components.

        This method sets up the main layout of the page, sidebar navigation,
        and the file uploader. It also decodes the uploaded image (if any)
        into a NumPy BGR array for further processing.

        Attributes initialized:
            option:
                Selected feature such as Histogram, Threshold, Filters, etc.
            image:
                Uploaded image (Streamlit UploadedFile object).
            source_image:
                Converted BGR image as numpy.ndarray, or None if no image uploaded.
        """
        st.set_page_config(layout="wide")
        st.title("Mini Photo Editor")
        st.divider()
        st.subheader("You can edit your image with select option!")
        st.sidebar.header("From here you can choose the option!")
        self.option = st.sidebar.selectbox("Select the option:", options=["Histogram", "Threshold",
                                                                   "Transforms", "Filters", "Contours",
                                                                   "Color Spaces", "Blending",
                                                                   "Edges"]
                    ,index=None,
                    placeholder="option")
        st.divider()
        self.image = st.file_uploader("Please upload image from here:", max_upload_size=10)
        self.source_image = None
        if self.image is not None:
            file_bytes = np.asarray(bytearray(self.image.read()), dtype=np.uint8)
            self.source_image = cv2.imdecode(file_bytes, 1)



    def option_handling(self):
        """
        Execute and display the action selected by the user.

        Based on the value of `self.option`, this method routes the image to the
        appropriate processing module and displays the result using Streamlit.

        Supported operations:
            Histogram:
                Computes and displays the color histogram of the uploaded image.
            Transforms:
                Resize, rotate, or flip the image based on sidebar options.
            Filters:
                Apply Gaussian, median, or normal blur filters.
            Blending:
                Blend two uploaded images using alpha compositing.
            Threshold:
                Apply binary, Otsu, or adaptive thresholding.
            Contours:
                Detect and draw contours on the image.
            Color Spaces:
                Convert image between RGB, HSV, LAB, YCrCb, GRAY, etc.
            Edges:
                Detect edges using the Canny operator with configurable thresholds.

        Notes:
            • All display output is handled directly through Streamlit.
            • Most operations require an uploaded image; if missing, a sidebar error is shown.
        """
        if self.option == "Histogram":
            if self.image is not None:     
                hist = Histogram(self.source_image)
                plot = hist.calc_hist()
                col1, col2 = st.columns(2)
                with col1:
                    st.header("Your image")
                    st.image(self.image)
                with col2:
                    st.header("Histogram")
                    st.image(plot)
                    st.download_button(label="Download Histogram",data=plot,
                                       file_name="histogram.jpg", mime="image/jpeg",)
                st.divider()
            else:
                st.sidebar.error("There is not any image for processing!")


        elif self.option == "Transforms":
            if self.image is not None:
                cnv = st.sidebar.selectbox("Select your affine transform:", options=["Resize", "Rotate",
                                                                                     "Flip"]
                    # default :
                    ,index=None,
                    placeholder="Select the transform")
                transeformed_image = Transform(self.source_image)

                if cnv == "Resize":
                    ratio = st.sidebar.slider("Ratio of width and height", min_value=0.1,
                                            max_value=1.5, step=0.1, value=0.5)
                    resized_image = transeformed_image.resize(ratio)
                    col = st.columns(1)
                    with col[0]:
                        st.header("Resized image")
                        st.image(resized_image, channels="BGR")
                        download_image_button("Download Resized image", resized_image, "resized.jpg")
                if cnv == "Flip":
                    flip = st.sidebar.radio("Select flip type", options=["0", "1", "-1"])
                    if flip == "0":
                        flipped_image = transeformed_image.flip(int(flip))
                        col = st.columns(1)
                        with col[0]:
                            st.header(f"Flipped image with {int(flip)}")
                            st.image(flipped_image, channels="BGR")
                            download_image_button("Download Flipped image", flipped_image, "flipped.jpg")

                    if flip == "1":
                        flipped_image = transeformed_image.flip(int(flip))
                        col = st.columns(1)
                        with col[0]:
                            st.header(f"Flipped image with {int(flip)}")
                            st.image(flipped_image, channels="BGR")
                            download_image_button("Download Flipped image", flipped_image, "flipped.jpg")

                    if flip == "-1":
                        flipped_image = transeformed_image.flip(int(flip))
                        col = st.columns(1)
                        with col[0]:
                            st.header(f"Flipped image with {int(flip)}")
                            st.image(flipped_image, channels="BGR")
                            download_image_button("Download Flipped image", flipped_image, "flipped.jpg")
                if cnv == "Rotate":
                    Degree = st.sidebar.slider("Degree to rotate:", min_value=0,
                                            max_value=360, step=1)
                    scale = st.sidebar.slider("Scale:", min_value=0.5, max_value=1.5,
                                              value=1.0)
                    rotated_image = transeformed_image.rotate(angle=Degree, scale=scale)
                    col = st.columns(1)
                    with col[0]:
                        st.header(f"Rotated image with {Degree} and scale {scale}")
                        st.image(rotated_image, channels="BGR")
                        download_image_button("Download Rotated image", rotated_image, "rotated.jpg")
            else:
                st.sidebar.error("There is not any image for processing!")
        elif self.option == "Filters":
            if self.image is not None:
                filter_ = st.sidebar.selectbox("Select the blur type to apply :", options=["Normal filter", "Gaussian filter",
                                                                                     "Median filter"]
                    # default :
                    ,index=None,
                    placeholder="Select the transform")
                filtered_image = Filters(self.source_image)
                if filter_ == "Gaussian filter":
                    kernel = st.sidebar.slider("Kernel size :", min_value=1, max_value=49,
                                              value=1, step=2)
                    # Gaussian Blur
                    GB_image = filtered_image.gaussian_blur(kernel_size=kernel)
                    col = st.columns(1)
                    
                    with col[0]:
                        st.header(f"Filtered image with kernel size{kernel} use Gaussian filter.")
                        st.image(GB_image, channels="BGR")
                        download_image_button("Dowload Filtered image", GB_image, "gaussianblur.jpg")
                if filter_ == "Normal filter":
                    kernel = st.sidebar.slider("Kernel size :", min_value=1, max_value=49,
                                               value=1, step=2)
                    # Normal Blur
                    NB_image = filtered_image.blur(kernel_size=kernel)
                    col = st.columns(1)
                    with col[0]:
                        st.header(f"Filtered image with kernel size {kernel} use Normal filter")
                        st.image(NB_image, channels="BGR")
                        download_image_button("Download Filtered image", NB_image, "normalblur.jpg")
                if filter_ == "Median filter":
                    kernel = st.sidebar.slider("Kernel size :", min_value=1, max_value=49,
                                               value=1, step=2)
                    # Median blur
                    MB_image = filtered_image.median_blur(kernel_size=kernel)
                    col = st.columns(1)
                    with col[0]:
                        st.header(f"Filtered image with kernel size {kernel} use Median filter")
                        st.image(MB_image, channels="BGR")
                        download_image_button("Download Filtered image", MB_image, "medianblur.jpg")
            else:
                st.sidebar.error("There is not any image for processing!")
        elif self.option == "Blending":
            self.access = True
            st.sidebar.warning("You must select other image from here!")
            self.image_2 = st.sidebar.file_uploader("Please upload image from here:", max_upload_size=10)
            if self.image_2 and self.image is not None:
                file_bytes = np.asarray(bytearray(self.image_2.read()), dtype=np.uint8)
                self.source_image_2 = cv2.imdecode(file_bytes, 1)
                col = st.columns(1)
                with col[0]:
                    alpha = st.sidebar.slider("Alpha :", max_value=1.0, min_value=0.0, value=0.0)
                    blend_obj = Blend(self.source_image, self.source_image_2, alpha)
                    blended_image = blend_obj.blending()
                    st.header("Blending images")
                    st.image(blended_image, channels="BGR")
                    download_image_button("Download Blended image", blended_image, "blended.jpg")
            else:
                st.sidebar.error("There is not any image for processing!")
        elif self.option == "Color Spaces":
            if self.image is not None:
                # color space
                CS = st.sidebar.selectbox("Select the color space:",options=["RGB","LAB", "HSV", "YCrCb",
                                                                            "GRAY", "HLS", "LUV"])
                obj_CS = ColorSpace(self.source_image)
                new_image = obj_CS.chane_space(CS)
                col = st.columns(1)
                with col[0]:
                    st.header(f"Converted image to {CS}")
                    if CS != "GRAY":
                        st.image(new_image, channels="BGR")
                        download_image_button("Download", new_image, "image.jpg")
                    else:
                        st.image(new_image)
                        download_image_button("Download", new_image, "image.jpg")
            else:
                st.sidebar.error("There is not any image for processing!")
        elif self.option == "Threshold":
            if self.image is not None:
                th = st.sidebar.selectbox("Select the type of treshold:", options=["Binary TH", "Otsu TH",
                                                                              "Adaptive TH"])
                obj_th = Threshold(self.source_image)
                col = st.columns(1)
                if th == "Binary TH":
                    value = st.sidebar.slider("Choose value for thrshold", min_value=0, max_value=255,
                                      value=127)
                    th_image = obj_th.apply_th(th_type=th, value=value)
                    with col[0]:
                        st.header(f"Binary Thrshold bitween {value} and 255")
                        st.image(th_image)
                        download_image_button("Download Threshold image", th_image, "threshold.jpg")
                else:
                    th_image = obj_th.apply_th(th_type=th)
                    with col[0]:
                        st.header(f"{th}")
                        st.image(th_image)
                        download_image_button("Download Threshold image", th_image, "threshold.jpg")
            else:
                st.sidebar.error("There is not any image for processing!")
        elif self.option == "Edges":
            if self.image is not None:
                l2_gradient = st.sidebar.checkbox("L2 Gradiend", value=False)
                apertureSize = st.sidebar.slider("Aperture Size:", max_value=7, min_value=3, 
                                                 value=3, step=2)
                th1 = st.sidebar.slider("Threshold1:", max_value=1000, min_value=1,
                                        value=100)
                th2 = st.sidebar.slider("Threshold2:", max_value=1000, min_value=1,
                                        value=150)
                st.sidebar.info("It is preferable that the ratio of Threshold2 to Threshold1 be close to 1.5.")
                st.sidebar.write(f"`Threshold2 / Threshold1` : `{th2/th1}`")
                eg = Edges(self.source_image)
                edges = eg.find_edges(threshold1=th1, threshold2=th2, L2gradient=l2_gradient,
                                      apertureSize=apertureSize)
                col = st.columns(2)
                with col[0]:
                    st.header("Edges")
                    st.image(edges)
                    download_image_button("Download Edges", edges, "edges.jpg")
                with col[1]:
                    st.header("Image")
                    st.image(self.image, channels="BGR")
            else:
                st.sidebar.error("There is not any image for processing!")
        elif self.option == "Contours":
            if self.image is not None:
                th = st.sidebar.selectbox("Select the type of treshold:", options=["Binary TH", "Otsu TH",
                                                                              "Adaptive TH"])
                obj_th = Threshold(self.source_image)
                th_image = None
                cnt_obj = Contours(self.source_image)
                if th == "Binary TH":
                    value = st.sidebar.slider("Choose value for thrshold", min_value=0, max_value=255,
                                      value=127)
                    th_image = obj_th.apply_th(th_type=th, value=value)
                else:
                    th_image = obj_th.apply_th(th_type=th)
                image_contour = cnt_obj.find_contours(th_image)
                col = st.columns(2)
                with col[0]:
                    st.header("Original image")
                    st.image(self.source_image, channels="BGR")
                with col[1]:
                    st.header("Contours")
                    st.image(image_contour, channels="BGR")
                    download_image_button("Download Contours", image_contour, "contours.jpg")

            else:
                st.sidebar.error("There is not any image for processing!")
app = WebApp()
app.option_handling()