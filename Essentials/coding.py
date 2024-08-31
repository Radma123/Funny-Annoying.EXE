import base64

with open('C:/Users/Home_PC/Desktop/kys/kys.mp3', 'rb') as image_file:
    # Кодируем изображение в base64 и получаем байтовую строку
    encoded_bytes = base64.b64encode(image_file.read())
    
    # Выводим байтовую строку (это будет не очень читабельно)
    print(encoded_bytes)
