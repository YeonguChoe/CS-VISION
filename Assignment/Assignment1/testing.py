from PIL import Image, ImageOps, ImageChops
import numpy as np

# Function to compute the low-pass (blurred) image for a given sigma
def compute_low_frequency(image_path, sigma):
    image = Image.open(image_path)
    # Separate the image into RGB channels
    red_channel, green_channel, blue_channel = image.split()
    # Convert channels to arrays
    red_array = np.asarray(red_channel)
    green_array = np.asarray(green_channel)
    blue_array = np.asarray(blue_channel)
    # Apply Gaussian blur to each channel
    red_blurred = gaussconvolve2d_scipy(red_array, sigma)
    green_blurred = gaussconvolve2d_scipy(green_array, sigma)
    blue_blurred = gaussconvolve2d_scipy(blue_array, sigma)
    # Convert back to image
    red_low_freq = Image.fromarray(red_blurred).convert('L')
    green_low_freq = Image.fromarray(green_blurred).convert('L')
    blue_low_freq = Image.fromarray(blue_blurred).convert('L')
    return red_low_freq, green_low_freq, blue_low_freq

# Function to compute the high-pass (detail) image
def compute_high_frequency(image_path, sigma):
    image = Image.open(image_path)
    # Compute the low-frequency image
    red_low_freq, green_low_freq, blue_low_freq = compute_low_frequency(image_path, sigma)
    # Compute the high-frequency image by subtracting the low-frequency image from the original
    red_high_freq = ImageChops.subtract(image, red_low_freq)
    green_high_freq = ImageChops.subtract(image, green_low_freq)
    blue_high_freq = ImageChops.subtract(image, blue_low_freq)
    return red_high_freq, green_high_freq, blue_high_freq

# Function to create a hybrid image by adding low and high-frequency images
def create_hybrid_image(image_path, sigma):
    # Compute low and high-frequency images
    red_low_freq, green_low_freq, blue_low_freq = compute_low_frequency(image_path, sigma)
    red_high_freq, green_high_freq, blue_high_freq = compute_high_frequency(image_path, sigma)
    
    # Add low and high-frequency images without adding 128
    red_hybrid = ImageChops.add(red_low_freq, red_high_freq)
    green_hybrid = ImageChops.add(green_low_freq, green_high_freq)
    blue_hybrid = ImageChops.add(blue_low_freq, blue_high_freq)
    
    # Merge RGB channels to create the final hybrid image
    hybrid_image = Image.merge('RGB', (red_hybrid, green_hybrid, blue_hybrid))
    
    return hybrid_image

image_path = "hw1/0a_cat.bmp"  # Replace with the path to your image


create_hybrid_image("Assignment/Assignment1", 1).show()