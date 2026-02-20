import cv2
import os
import numpy as np

def read_image_rgb(file_path):
    """
    Reads an image from the specified file path and converts it from BGR to RGB.
    Alpha channel is stripped if present (e.g. PNG with 4 channels).

    Args:
        file_path (str): The relative or absolute path to the image file.

    Returns:
        numpy.ndarray: The image in RGB format, shape (H, W, 3).

    Raises:
        FileNotFoundError: If the file does not exist at the specified path.
        ValueError: If the file exists but cannot be decoded as an image.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file was not found at {file_path}")

    image_bgr = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

    if image_bgr is None:
        raise ValueError(f"Error: Could not decode the file {file_path}.")

    if image_bgr.shape[2] == 4:
        image_bgr = image_bgr[:, :, :3]

    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

    return image_rgb



def draw_seams(img, seams, color=(255, 0, 0)):
    """
    Draws collected seams on the original image for visualization.
    Fully vectorized — no explicit row loop.
    
    Args:
        img (np.ndarray): Input image of shape (H, W, 3).
        seams (list of np.ndarray): List of seam paths, each of shape (H,).
        color (tuple): RGB color for seam visualization. Default: (255, 0, 0) red.
    
    Returns:
        np.ndarray: Image copy with seams overlaid, shape (H, W, 3).
    """
    viz = img.copy()
    rows = np.arange(img.shape[0])
    for seam in seams:
        viz[rows, seam] = color
    return viz