#Clase para crear todos los lados del cuadrado.

from vector import *
from intersect import *
from plane import *
from atras import *
from lado import *

class Square(object):
    def __init__(self, arriba, izquierda, derecha, abajo, atras, material):
        
        self.material = material #Material del cuadrado.
        
        #Parte superior del cuadrado.
        self.center_arriba = arriba[0]
        self.w_arriba = arriba[1]
        self.l_arriba = arriba[2]
        
        #print(arriba[3])

        #Parte izquierda del cuadrado.
        self.center_izquierda = izquierda[0]
        self.w_izquierda = izquierda[1]
        self.l_izquierda = izquierda[2]

        #Parte derecha del cuadrado.
        self.center_derecha = derecha[0]
        self.w_derecha = derecha[1]
        self.l_derecha = derecha[2]

        #Parte inferior del cuadrado.
        self.center_abajo = abajo[0]
        self.w_abajo = abajo[1]
        self.l_abajo = abajo[2]

        #Parte frontal del cuadrado.
        self.center_frente = atras[0]
        self.w_frente = atras[1]
        self.l_frente = atras[2]


        self.arriba = Plane(arriba[0], arriba[1], arriba[2], material)
        self.izquierda = Lado(izquierda[0], izquierda[1], izquierda[2], material)
        self.derecha = Lado(derecha[0], derecha[1], derecha[2], material)
        self.abajo = Plane(abajo[0], abajo[1], abajo[2], material)
        self.atras = Atras(atras[0], atras[1], atras[2], material)

    def ray_intersect(self, orig, direction): #Método para la intersección.
        arriba = self.arriba.ray_intersect(orig, direction)
        izquierda = self.izquierda.ray_intersect(orig, direction)
        derecha = self.derecha.ray_intersect(orig, direction)
        abajo = self.abajo.ray_intersect(orig, direction)
        atras = self.atras.ray_intersect(orig, direction)

        if arriba: #Detectando la colisión de arriba del cuadrado.
            #print("Arriba: ", arriba)
            return arriba
        elif izquierda: #Detectando la colisión de la izquierda del cuadrado.
            #print("Izquierda: ", izquierda)
            return izquierda
        elif derecha: #Detectando la colisión de la derecha del cuadrado.
            #print("Derecha: ", derecha)
            return derecha
        elif abajo: #Detectando la colisión de abajo del cuadrado.
            return abajo
        else: #Detectando la colisión de frente del cuadrado.
            #print("Frente: ", frente)
            return atras
            
        # if izquierda: #Detectando la colisión de la izquierda del cuadrado.
        #     print("Izquierda: ", izquierda)
        #     return izquierda
        # if derecha: #Detectando la colisión de la derecha del cuadrado.
        #     print("Derecha: ", derecha)
        #     return derecha

        # if frente and atras and izquierda and derecha:
        #     return frente
        # elif frente and atras and izquierda:
        #     return frente
        # elif frente and atras and derecha:
        #     return frente
        # elif frente and izquierda and derecha:
        #     return frente
        # elif atras and izquierda and derecha:
        #     return atras
        # elif frente and atras:
        #     return frente
        # elif frente and izquierda:
        #     return frente
        # elif frente and derecha:
        #     return frente
        # elif atras and izquierda:
        #     return atras
        # elif atras and derecha:
        #     return atras
        # elif izquierda and derecha:
        #     return izquierda
        # elif frente:
        #     return frente
        # elif atras:
        #     return atras
        # elif izquierda:
        #     return izquierda
        # elif derecha:
        #     return derecha
