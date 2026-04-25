import cv2
from numpy import ndarray
class Edges:
    """
    Find the edges from the image.
    """
    def __init__(self, image:ndarray) -> None:
        """
        Receive image from the user with created object and convert it to the grayscale.
        Args:
            image(numpy.ndarray):
                BGR image from the user.
        """
        self.image = image
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    def find_edges(self, threshold1:int, threshold2:int, apertureSize:int, L2gradient:bool) -> ndarray:
        """
        Find the grayscale image edges.
        Args:
            threshold1(int):
                Value of th1.
            threshold2(int):
                Value of th2.
            apertureSize(int):
                Value of apertureSize(3, 5 , 7)
            L2gradient(bool):
                with this parametr you can enable or disable the L2_gradient operatuion.
        Returns:
            (1D array):
                Edges from the gray image.
        """
        result = cv2.Canny(self.gray_image, threshold1=threshold1, threshold2=threshold2,
                           L2gradient=L2gradient, apertureSize=apertureSize)
        return result