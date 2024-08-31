import ctypes
import os

def set_wallpaper(image_path):

    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)


set_wallpaper(r'C:\Users\Home_PC\Desktop\kys\kys.jpg')
