from intersect import *
from vector import *

class Triangle(object):

    def __init__(self, v0, v1, v2, material):
        self.v0 = v0
        self.v1 = v1
        self.v2 = v2
        self.material = material
    
    def ray_intersect(self, orig, direction):
        edge1 = self.v1 - self.v0
        edge2 = self.v2 - self.v0
        #h = direction.cross(edge2)
        h = direction * edge2
        #print(type(h))
        #a = edge1.dot(h)
        a = edge1 @ h
        if a > -0.00001 and a < 0.00001:
            #print("a: ", a)
            return None
        f = 1/a
        s = orig - self.v0
        #u = f * s.dot(h)
        u = f * (s @ h)
        if u < 0.0 or u > 1.0:
            #print("u: ", u)
            return None
        q = s * edge1
        #v = f * direction.dot(q)
        v = f * (direction @ q)
        if v < 0.0 or u + v > 1.0:
            #print("v: ", v)
            return None
        #t = f * edge2.dot(q)
        t = f * (edge2 @ q)
        if t > 0.00001:
            #print("Hola")
            return Intersect(
                distance=t,
                point=orig + (direction * t),
                normal=V3(0, 1, 0)
            )
        else:
            #print("Adiós")
            return None