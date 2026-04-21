import cv2
import io
import numpy as np
import matplotlib.pyplot as plt
class Histogram:
    """
    Class for calculate the histogram
    Attributes:
        image(numpy.ndarray):
            An image from user
        gray(numpy.1D array):
    """
    def __init__(self, image):
        """
        Convert image to from BGR to GRAY
        Args:
            image(numpy.ndarray):
                An image received when using class.
        """
        self.gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    def calc_hist(self):
        """
        Calculate histogram and convert histogram to image.
        Returns:
            buf(io.BytesIO):
                converted plot to image.
        """
        hist = cv2.calcHist([self.gray], [0], None, [256], [0,256])
        # Create the plot
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.plot(hist)
        ax.set_title("Grayscale histogram")
        ax.set_ylabel("Frequency")
        ax.set_xlabel("Intensity")
        ax.grid(True)
        plt.tight_layout()
        fig = plt.gcf() 
        # Convert plot to the image    
        buf = io.BytesIO()
        fig.savefig(buf, format='png') 
        buf.seek(0) 
        plt.close(fig)
        print(type(buf)) 
        return buf