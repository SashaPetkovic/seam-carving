import cv2
import matplotlib.pyplot as plt
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


def show_image(img, title="Image", figsize=(10, 6)):
    """
    Helper function to display an image using Matplotlib with axes turned off.

    Args:
        img (numpy.ndarray): The RGB image to display.
        title (str): The title of the plot.
        figsize (tuple): The size of the figure (width, height).
    """
    plt.figure(figsize=figsize)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off') # Hide the axes for a cleaner view
    plt.show()