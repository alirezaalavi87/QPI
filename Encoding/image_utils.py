from PIL import Image
import numpy as np

# helped by chatGPT3.5 turbo
# Resize the image to the given width and height
# If only width or height is provided, resize while maintaining ratio
def image_resize(input_image_path, output_image_path, width=None, height=None):
    try:
        input_image = Image.open(input_image_path)
    except:
        print("Error in opening the Image")
    
    if width is None and height is None:
        raise ValueError("Please provide either width or height for resizing.")
    
    if width is not None and height is not None:
        resized_image = input_image.resize((width, height))
    elif width is not None:
        aspect_ratio = float(width) / input_image.size[0]
        height = int(input_image.size[1] * aspect_ratio)
        resized_image = input_image.resize((width, height))
    elif height is not None:
        aspect_ratio = float(height) / input_image.size[1]
        width = int(input_image.size[0] * aspect_ratio)
        resized_image = input_image.resize((width, height))
    
    resized_image.save(output_image_path)

# Convert the image to grayscale
def image_grayscale(input_image_path, output_image_path):
    try:
        img = Image.open(input_image_path)
    except:
        print("Error in opening the Image")

    img_grayscale = img.convert(mode="L")
    img_grayscale.save(output_image_path)

# Return matrix-pixel representation of the image
def image_pixel_matrix(input_image_path):
    img = Image.open(input_image_path)

    #get pixel values as a matrix
    # only get the Red band (all bands have the same value in grayscale)
    # NOTE if you want to work with RGB images, make this an argument
    pixel_matrix = list(img.getdata(band=0))

    # Reshape the matrix to match the image dimensions
    width, height = img.size
    pixel_matrix = [pixel_matrix[i * width:(i + 1) * width] for i in range(height)]

    pixel_matrix = np.array(pixel_matrix)

    return pixel_matrix
    


# image_resize("images/SURF-100px-bw.png", "images/SURF-10px-bw.png", width=10)
# image_pixel_matrix("images/SURF-10px-bw.png")
