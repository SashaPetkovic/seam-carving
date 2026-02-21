import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

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

def plot_energy_maps_with_image(image, en_map1, en_map2, en_map1_title, en_map2_title):
    """
    Displays original image alongside two energy maps with colorbars.
    
    Args:
        image (np.ndarray): Original image of shape (H, W, 3).
        en_map1 (np.ndarray): First energy map of shape (H, W).
        en_map2 (np.ndarray): Second energy map of shape (H, W).
        en_map1_title (str): Title for the first energy map.
        en_map2_title (str): Title for the second energy map.
    """
    fig, axes = plt.subplots(1, 3, figsize=(22, 8), layout='tight')

    axes[0].imshow(image)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    heatmap_e1 = axes[1].imshow(en_map1, cmap='inferno')
    axes[1].set_title(en_map1_title)
    axes[1].axis('off')
    fig.colorbar(heatmap_e1, ax=axes[1], fraction=0.046, pad=0.04)

    heatmap_entropy = axes[2].imshow(en_map2, cmap='inferno')
    axes[2].set_title(en_map2_title)
    axes[2].axis('off')
    fig.colorbar(heatmap_entropy, ax=axes[2], fraction=0.046, pad=0.04)

    plt.show()

def plot_three_images(image1, title1, image2, title2, image3, title3):
    """
    Displays three images side by side with titles.
    
    Args:
        image1 (np.ndarray): First image.
        title1 (str): Title for the first image.
        image2 (np.ndarray): Second image.
        title2 (str): Title for the second image.
        image3 (np.ndarray): Third image.
        title3 (str): Title for the third image.
    """
    _, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 7), layout='tight')

    ax1.imshow(image1)
    ax1.set_title(title1)
    ax1.axis('off')

    ax2.imshow(image2)
    ax2.set_title(title2)
    ax2.axis('off')

    ax3.imshow(image3)
    ax3.set_title(title3)
    ax3.axis('off')

    plt.show()

def plot_two_images(image1, title1, image2, title2):
    """
    Displays two images side by side with titles.
    
    Args:
        image1 (np.ndarray): First image.
        title1 (str): Title for the first image.
        image2 (np.ndarray): Second image.
        title2 (str): Title for the second image.
    """
    _, (ax_original, ax_carved) = plt.subplots(1, 2, figsize=(15, 8))

    ax_original.imshow(image1)
    ax_original.set_title(title1)
    ax_original.axis('off')

    ax_carved.imshow(image2)
    ax_carved.set_title(title2)
    ax_carved.axis('off')

    plt.show()