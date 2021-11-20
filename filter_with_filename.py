from PIL import Image
import numpy as np

def get_shade_grey(pixel_array,x,y,mosaic_size):

    grey_color=np.sum(pixel_array[y: y + mosaic_size,x: x + mosaic_size])/3
    grey_color = int(grey_color // pow(mosaic_size,2))
    return grey_color;

def change_pixels(pixel_array,mosaic_size,grayscale):
    height = len(pixel_array)
    width = len(pixel_array[1])
    for y in range(0,height,mosaic_size):
        for x in range(0,width,mosaic_size):
            shade_grey=get_shade_grey(pixel_array,x,y,mosaic_size);
            pixel_array[y: y + mosaic_size,x: x + mosaic_size]=int(shade_grey // grayscale) * grayscale

def get_pixel_array_image(name_file):
    img = Image.open(name_file)
    temp_pixel_array = np.array(img)
    return np.clip(temp_pixel_array, 0, 255)

def save_pixel_image(pixel_array,name_file):
    changed_image = Image.fromarray(pixel_array)
    changed_image.save(name_file)

def change_image(name_image,name_save_file,mosaic_size,grayscale):
    pixel_array = get_pixel_array_image(name_image);
    change_pixels(pixel_array,mosaic_size,grayscale)
    save_pixel_image(pixel_array,name_save_file)
    print("Изменения прошли успешно")

name_image="img2.jpg"
name_save_file="new_img.jpg"
mosaic_size=10
grayscale=50

change_image(name_image,name_save_file,mosaic_size,grayscale)
