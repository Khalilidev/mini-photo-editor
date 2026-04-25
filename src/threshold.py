import cv2
from numpy import ndarray
class Threshold:
    """
    Thresholding received image.
    """
    def __init__(self, image:ndarray) -> None:
        """
        Receive image from created object and convert it to graysclae.
        Args:
            image(numpy.ndarray):
                The source image from user.
        """
        self.image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    def apply_th(self, th_type:str, value=127) -> ndarray:
        """
        Apply the threshold operations on the gray image.
        Args:
            th_type(str):
                type of thresholding.
            value(int):
                value of thresholding.                
        """
        if th_type == "Binary TH":
            _, bin_th = cv2.threshold(self.image, value, 255, cv2.THRESH_BINARY)
            return bin_th
        elif th_type == "Otsu TH":
            _, otsu_th = cv2.threshold(self.image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
            return otsu_th
        elif th_type == "Adaptive TH":
            adapt_th = cv2.adaptiveThreshold(self.image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)
            return adapt_th