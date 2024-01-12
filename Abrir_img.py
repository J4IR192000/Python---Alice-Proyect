from PIL import Image
import sys

try:
    img = Image.open("Hilda.png")
except:
    print("No se pudo cargar la imagen")
    sys.exit(1)
img.show()


#Convertir la imagen en otro formato PNG a JPG
# img.save("Hilda.jpg","jpg")

#Rotar imagen
# img2= img.rotate(45)
# img2.show()

#Ancho y alto de una img
# ancho,alto = img.size
# print("Ancho: ", ancho)
# print("Alto: ",alto)

#Reescalar una imagen
# size =(200,200)
# img3 = img.resize(size) #ajusta la imagen a las medidas
# img4 = img.copy()
# img4.thumbnail(size) #Mantiene el aspecto, esta es la chida pa reescalar
# img3.show()
# img4.show()
