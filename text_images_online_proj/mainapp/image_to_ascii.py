from PIL import Image
from PIL import ImageEnhance

def image_to_ascii(path):
    """Loads image and converts it to string"""
    try:
        # it takas both string and pathlib objects
        img = Image.open(path)
        img_flag = True
    except:
        print(path, "Unable to find image ");
    
    width, height = img.size
    aspect_ratio = height/width
    new_width = 40
    new_height = aspect_ratio * new_width * 0.5
    img = img.resize((new_width, int(new_height)))
    
    img = img.convert('L')
    obj = ImageEnhance.Contrast(img)
    img = obj.enhance(1.4)
    
    chars = ["█", "▓", "▒", "Ø", "╬", "░", "=", "-", ":", ",", "."]
    
    # convert image 
    pixels = img.getdata()
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    # create a 2D array
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    # make a string
    ascii_image = "\n".join(ascii_image)
    
    return ascii_image