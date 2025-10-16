from PIL import Image,ImageFont,ImageDraw

image = Image.open('matrix.jpg')
print(image.size)
print(image.mode)
print(image.format)

#convetir imagen a blanco y negro
#image_blackwhite = image.convert('L')
#image_blackwhite.show()

#redimensionar la imagen
width = image.size[0]
height = image.size[1]

new_width = width // 5
new_height = height // 5

new_size = (new_width,new_height)

# image_short = image.resize(new_size)
# image_short.show()
# image_short.save('matrix_short.jpg','JPEG',quality=90)

#incrustar texto en la imagen
font = ImageFont.truetype('Roboto-Bold.ttf',120)
draw = ImageDraw.Draw(image)

draw.text(
    (10,0),
    'CESAR MAYTA EN CODIGO G5',
    (255,255,255),
    font
)
image.show()