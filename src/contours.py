import cv2
from numpy import ndarray
class Contours:
    """
    This class founds the contours.
    """
    def __init__(self, image:ndarray) -> None:
        """
        Rceiving the image from when object creats.
        Args:
            image(numpy.ndarray):
                Source image from the user.
        """
        global help_image
        help_image = image.copy()
    def find_contours(self, thresh:ndarray) -> None:
        """
        Find contours and show them and return contours
        Args:
            image: BGR image
            tresh: tresholded image(binary image)
        Returns:
            (numpy.ndarray):
                Source image with applied contours.
        """
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(help_image, contours, -1, (255, 0, 255), 2)
        return help_image