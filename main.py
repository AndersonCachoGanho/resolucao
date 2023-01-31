from PIL import Image

img = Image.open('arte.png')
img_resized = img.resize((10000,10000))
img_resized.save('imagem_resized.png')