from intersect import *
from vector import *


class Prueba(object):
    def __init__(self, center, w, h, material):
        self.center = center
        self.w = w
        self.h = h
        self.material = material
    
    def ray_intersect(self, orig, direction):
        d = -(orig.z + self.center.z) / direction.z
        impact = orig + (direction * d)
        normal = V3(0, 0, 1)
        
        if d <= 0 or \
            impact.x > (self.w/2) or \
            impact.x < (-self.w/2) or \
            impact.y > (self.h/2) or \
            impact.y < (-self.h/2):
            return None
        
        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )