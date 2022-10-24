#Clase material.
class Material:
    #Diffuse, albedo y spec.
    def __init__(self, diffuse, albedo, spec, refractive_index = 0): #Constructor de la clase.
        self.diffuse = diffuse #Esto guarda un color.
        self.albedo = albedo #Esto guarda un array.
        self.spec = spec #Esto guarda un número.
        self.refractive_index = refractive_index #Esto guarda un número.