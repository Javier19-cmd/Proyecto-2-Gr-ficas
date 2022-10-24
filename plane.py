#Archivo para otras cosas.
from intersect import *
from vector import *

class Plane(object):
    def __init__(self, center, w, h, material):
        self.center = center
        self.w = w
        self.l = h
        self.material = material

    def ray_intersect(self, orig, direction): #Método para la intersección.
        d = -(orig.y + self.center.y) / direction.y #Calculando la distancia. 
        impact = orig + (direction * d)
        normal = V3(0, 1, 0)


        if d <= 0 or \
            impact.x > (self.center.x + self.w/2) or \
            impact.x < (self.center.x - self.w/2) or \
            impact.z > (self.center.z + self.l/2) or \
            impact.z < (self.center.z - self.l/2): #Detectando la no colisión.
            return None
    
        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )