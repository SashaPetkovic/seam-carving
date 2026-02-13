import cv2
import os

def read_image_rgb(file_path):
    """
    Reads an image from the specified file path and converts it from BGR to RGB.

    Args:
        file_path (str): The relative or absolute path to the image file.

    Returns:
        numpy.ndarray: The image in RGB format.

    Raises:
        FileNotFoundError: If the file does not exist at the specified path.
        ValueError: If the file exists but cannot be decoded as an image.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file was not found at {file_path}")

    image_bgr = cv2.imread(file_path, 1)

    if image_bgr is None:
        raise ValueError(f"Error: Could not decode the file {file_path}.")

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    return image_rgb
