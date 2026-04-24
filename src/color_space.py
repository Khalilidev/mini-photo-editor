import cv2
from numpy import ndarray
class ColorSpace:
    """
    Convert image to received channel.
    """
    def __init__(self, image:ndarray) -> None:
        """
        create object and receive the image from the user.
        Args:
            image(numpy.ndarray):
                image in BGR channel
        """
        self.image = image
    def chane_space(self, space:str) -> ndarray:
        """
        Changing image from BGR to received channel.
        Args:
            space(str):
                Received channel from the user.
        Returns:
            (numpy.ndarray):
                Converted image from BGR to {space}
        """
        code = getattr(cv2, f"COLOR_BGR2{space}")
        new_image = cv2.cvtColor(self.image, code=code)
        return new_image