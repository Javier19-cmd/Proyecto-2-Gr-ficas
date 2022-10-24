#Clase para hacer el frente del cuadrado.
from vector import *
from intersect import *

class Frente(object):
    def __init__(self, center, w, h, material):
        self.center = center
        self.w = w
        self.l = h
        self.material = material

    def ray_intersect(self, orig, direction): #Método para la intersección.
        d = -(orig.z + self.center.z) / direction.z #Calculando la distancia. 
        impact = orig + (direction * d)
        normal = V3(1, 0, 0)


        if d <= 0 or \
            impact.y > (self.center.y + self.w/2) or \
            impact.y < (self.center.y - self.w/2) or \
            impact.x > (self.center.x + self.l/2) or \
            impact.x < (self.center.x - self.l/2): #Detectando la no colisión.
            return None
    
        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )