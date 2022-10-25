import mmap
import struct
from color import *
from math import *

#Se puede usar lo que se había hecho para abrir bmp's en el proyecto 1.

class Envmap(object):

    def read(self, path):
        with open(path, "rb") as image:
            image.seek(10)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(18)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size)

            self.pixels = []
            for y in range(self.height):
                self.pixels.append([])
                for x in range(self.width):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    self.pixels[y].append(
                        color(r, g, b)
                    )

    def load(self, path): #Función que carga la textura.
        self.read(path)

        #Obteniendo el ancho y el alto de la textura.
        self.width = self.width
        self.height = self.height

        #print(self.width, self.height) #Imprimiendo el ancho y el alto de la textura.

        #print("Tipo de textura: ", type(self.pixels)) #Imprimiendo el tipo de textura.
    
        #Devolviendo el color de la textura en rgb.
        return self.pixels

    def get_color(self, direction):
        direction = direction.normalice()
        x = int(((atan2(direction.z, direction.x) / (2 * pi)) + 0.5) * self.width)
        y = int((acos(direction.y) / pi) * self.height)

        return self.pixels[y][x]

        #print(self.pixels) #Imprimiendo el color.
    