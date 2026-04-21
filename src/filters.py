import cv2
from numpy import ndarray
class Filters:
    """
    Apply normal filter, median filter and gaussian filter to the image.
    Attrebutes:
        image(numpy.ndarray):
            An image received from the user.
    """
    def __init__(self, image:ndarray):
        """
        Define and create attrebute
        Args:
            image(numpy.ndarray):
                The source image
        """
        self.image = image
    def gaussian_blur(self, kernel_size:int) -> ndarray:
        """
        Apply gaussian filter to the received image.
        Args:
            kernel_size(int):
                The size of kernel for apply gaussian blur.
        Returns:
            (numpy.ndarray):
                blured image with gaussian filter.
        """
        blured_image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), sigmaX=0, sigmaY=0)
        return blured_image
    def blur(self, kernel_size:int) -> ndarray:
        """
        Apply normal filter to the received image
                Args:
            kernel_size(int):
                The size of kernel for apply normal blur.
        Returns:
            (numpy.ndarray):
                blured image with Normal filter.
        """
        blured = cv2.blur(self.image, (kernel_size, kernel_size))
        return blured
    def median_blur(self, kernel_size:int) -> ndarray:
        """
        Apply median filter to the received image
        Args:
            kernel_size(int):
                The size of kernel for apply median blur.
        Returns:
            (numpy.ndarray):
                blured image with Median filter.
        """
        blured = cv2.medianBlur(self.image, kernel_size)
        return blured