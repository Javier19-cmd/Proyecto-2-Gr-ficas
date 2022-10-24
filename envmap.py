import mmap
import struct
from color import *
from math import *

#Se puede usar lo que se había hecho para abrir bmp's en el proyecto 1.
class Envmap(object):

    def read(self, path): #Archivo que sirve para leer la textura.
        with open(path, 'rb') as image:
            image.seek(10) #Saltando algunos bytes. Estas sumas se pueden quitar y dejarlo como un número.
            header_size = struct.unpack("=l", image.read(4))[0] #El l es formato nativo.
            image.seek(18) #Saltando algunos bytes.
            #Leyendo el ancho y el alto de la textura.
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]

            image.seek(header_size) #Quitando el header.
            self.pixels = [] #Lista de pixeles.
            for y in range(self.height):
                self.pixels.append([]) #Añadiendo una fila de pixeles.
                for x in range(self.width):
                    #Se lee de 1 en 1, porque el color usa 3 bytes.
                    b = ord(image.read(1)) #Leyendo el byte de b.
                    g = ord(image.read(1)) #Leyendo el byte de g.
                    r = ord(image.read(1)) #Leyendo el byte de r.

                    self.pixels[y].append(
                        color(r, g, b)
                    ) #Añadiendo el color a la lista de pixeles.

                #print(self.pixels) #Imprimiendo el color.
    
    def get_color(self, direction):
        direction = direction.normalice()
        x = int(atan2(direction.z, direction.x) / (2 * pi) + 0.5) * self.width
        y = int(acos(-direction.y) / pi) * self.height

        index = ((y * self.width + x) * 3) % len(self.pixels)
        c = self.pixels[index]

        return color(
            c[0],
            c[1],
            c[2]
        )