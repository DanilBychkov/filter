from PIL import Image
import numpy as np
import os.path

def get_shade_grey(pixel_array,x,y,mosaic_size):
    """получение оттенков серого цвета"""
    grey_color=np.sum(pixel_array[y: y + mosaic_size,x: x + mosaic_size])/3
    grey_color = int(grey_color // pow(mosaic_size,2))
    return grey_color;

def change_pixels(pixel_array,mosaic_size,grayscale):
    """изменение пикселей"""
    height = len(pixel_array)
    width = len(pixel_array[1])
    for y in range(0,height,mosaic_size):
        for x in range(0,width,mosaic_size):
            shade_grey=get_shade_grey(pixel_array,x,y,mosaic_size);
            pixel_array[y: y + mosaic_size,x: x + mosaic_size]=int(shade_grey // grayscale) * grayscale

def get_pixel_array_image(name_file):
    """получение пикселей из указанного фото"""
    img = Image.open(name_file)
    width, height = img.size
    print("Ширина изображения " + str(width))
    print("Высота изображения " + str(height))
    temp_pixel_array = np.array(img)
    return np.clip(temp_pixel_array, 0, 255)

def save_pixel_image(pixel_array,name_file):
    """сохранение изображения по указанному пути"""
    changed_image = Image.fromarray(pixel_array)
    changed_image.save(name_file)

def change_image(name_image,name_save_file,mosaic_size,grayscale):
    """изменения фотографии """
    pixel_array = get_pixel_array_image(name_image);
    change_pixels(pixel_array,mosaic_size,grayscale)
    save_pixel_image(pixel_array,name_save_file)
    if(os.path.exists(name_save_file)):
        print("Изменения прошли успешно")

name_image=input("Введите название изображения ")
name_save_file=input("Введите название изображение куда сохранить картинку ")
mosaic_size=int(input("Введите размер мозаики "))
grayscale=int(input("Введите шаг градации серого "))

change_image(name_image,name_save_file,mosaic_size,grayscale)
