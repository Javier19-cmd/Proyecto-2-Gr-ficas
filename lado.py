#Clase para hacer los lados de izquierda y derecha del cuadrado.
from vector import *
from intersect import *

class Lado(object):
    def __init__(self, center, w, h, material):
        self.center = center
        self.w = w
        self.l = h
        self.material = material

    def ray_intersect(self, orig, direction): #Método para la intersección.
        d = -(orig.x + self.center.x) / direction.x #Calculando la distancia. 
        impact = orig + (direction * d)
        normal = V3(0, 0, 1)


        if d <= 0 or \
            impact.y > (self.center.y + self.w/2) or \
            impact.y < (self.center.y - self.w/2) or \
            impact.z > (self.center.z + self.l/2) or \
            impact.z < (self.center.z - self.l/2): #Detectando la no colisión.
            return None
    
        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )