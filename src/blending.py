import cv2
from numpy import ndarray
class Blend:
    """
    Combine (blend) two images.
    """
    def __init__(self, image1:ndarray, image2:ndarray, alpha:int):
        """
        Receives two images and blend them base on alpha.
        Args: 
            image1(numpy.ndarray):
                the source image received from the user.
            image2(numpy.ndarray):
                the source image received from the user.
            alpha(int):
                a value bitween 0 and 1.
        """
        self.image1 = image1
        self.image2 = image2
        self.alpha = alpha
    def blending(self):
        """
        Resizing the received images from user to (500, 800), then blend it.
        Args:
            None
        Returns:
            (numpy.ndarray):
                Blended image.

        """
        self.resized_image_1 = cv2.resize(self.image1, (500, 800))
        self.resized_image_2 = cv2.resize(self.image2, (500, 800))
        blended_image = cv2.addWeighted(self.resized_image_1, self.alpha,
                                        self.resized_image_2, 1-self.alpha, gamma=0)
        return blended_image