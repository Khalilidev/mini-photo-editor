import cv2
from numpy import ndarray
class Transform:
    """
    Class for apply affine transforms(resize, flip, rotate)
    Attrebutes:
        image(numpy.ndarray):
            An image received from the user
    """
    def __init__(self, image:ndarray):
        """
        Define the attrebute
        Args:
            image(numpy.ndarray):
                An image selected by user
        """
        self.image = image
    def resize(self, ratio:int):
        """
        Resizing image with ratio of height and width.
        Args:
            ratio(image):
                A number recived from the slidebar.
        Returns:
            (numpy.ndarry):
                resized image with scale : ratio*(w, h)
        """
        h, w = self.image.shape[:2]
        resized_image = cv2.resize(self.image, (int(ratio*w), int(ratio*h)))
        return resized_image
    def flip(self, flipcode:int):
        """
        Flip image with the received args.
        Args:
            flipcode(int):
                0 or 1 or -1
        returns:
            (numpy.ndarry):
                flipped image with the flipcode
        """
        flipped_image = cv2.flip(self.image, flipcode)
        return flipped_image
    def rotate(self, angle:int, scale:int):
        """
        Rotate image with received degree and change scale with received scale using warp Affine.
        
        Args:
            angle(ing):
                Received degree from the slider
            scale(int):
                Received scale from the slider
        Returns:
            (numpy.ndarray):
                rotated image with received degree.
        """
        h, w = self.image.shape[:2]
        center = (int(w/2), int(h/2))
        rotation_matrix = cv2.getRotationMatrix2D(center, angle=angle, scale=scale)
        rotated_image = cv2.warpAffine(self.image, rotation_matrix, (w, h))
        return rotated_image