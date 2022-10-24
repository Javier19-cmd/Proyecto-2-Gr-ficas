from code import interact
from ray import *
from utilidades import *
from math import *
from vector import *
from sphere import *
from material import *
from light import *
from color import *
from plane import *

c1 = Raytracer() #Instancia de la clase Raytracer.


def glCreateWindow(width, height): #Función para crear la ventana.
    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Creando las dimensiones de la pantalla.

            c1.width = width #Ancho de la pantalla.
            c1.height = height #Alto de la pantalla.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    #except: #Si en caso se escribió una letra en vez de número, entonces se imprime esta excepción.
     #   print("Se ingresó una letra en vez de número.")

def glClearColor(r, g, b): #Función para el color de fondo.
    c1.color_fondo = color(r, g, b) #Se le asigna el color.

def glClear(): #Función para limpiar la pantalla.
    c1.framebuffer = [
            [c1.color_fondo for x in range(c1.width)] 
            for y in range(c1.height)
        ] #Se crea el framebuffer.

def glColor(r, g, b): #Función para el color de la figura.
    #c1.colorPunto = color(r, g, b).toBytes() #Se le asigna el color.
    c1.colorPunto = color(r, g, b) #Se le asigna el color.

#Defininiendo el point.
def point(x, y, c): 
    if x < c1.width and y < c1.height and x >= 0 and y >= 0:
        c1.framebuffer[y][x] = c

def glSphere(): #Método para crear las esferas.

    #c1.spheres.append(Sphere(V3(x, y, z), r, col)) #Guardando la esfera en el array de esferas.
    #c1.colors.append(col) #Guardando el color de la esfera.
    
    #Crenado el material de las esferas que tienen los osos en medio.
    al = Material(diffuse=color(128, 128, 128), albedo=[0.61, 0.25], spec=10) #Aluminio. 
    al2 = Material(diffuse=color(255, 0, 0), albedo=[0.61, 0.25], spec=10) #Aluminio.
    
    sil = Material(diffuse=color(0, 128, 0), albedo=[0.6, 0.3], spec=50) #Silicón.

    #Colores para los osos.
    brown = Material(diffuse=color(139, 69, 19), albedo=[1, 0, 0.4], spec=5) #Marrón.
    #brown = Material(diffuse=color(139, 69, 19)) #Marrón.
    white = Material(diffuse=color(255, 250, 250), albedo=[1, 0, 0.3], spec=5) #Blanco.

    #Creando esferas.
    c1.scene = [

        #Esferas de aluminio.
        Sphere(V3(-3, -2.2,-12), 0.8, al),
        Sphere(V3(2, -2.2,-12), 0.8, al2),

        #Creando esfera en el centro para probar la luz.
        #Sphere(V3(0, 0,-12), 3, brown),

    ]

    c1.light = Light(V3(0, 3, 0), 1, color(255, 255, 255)) #Creando la luz.

    #c1.light = Light(V3(0, 0, 0), 1, color(255, 255, 255)) #Creando la luz.

def glPlane(): #Método para crear el plano.

    mat = Material(diffuse=color(212, 175, 55), albedo=[0.5, 0.1], spec=10)

    c1.scene = [
        Plane(V3(0, 2, -6), 2, 2, mat)
    ]


    c1.light = Light(V3(0, 3, 0), 1, color(255, 255, 255)) #Creando la luz.

def escena():
    #c1.spheres.append(Sphere(V3(x, y, z), r, col)) #Guardando la esfera en el array de esferas.
    #c1.colors.append(col) #Guardando el color de la esfera.
    
    #Crenado el material de las esferas que tienen los osos en medio.
    al = Material(diffuse=color(128, 128, 128), albedo=[0.61, 0.25, 0, 0], spec=10) #Aluminio. 
    al2 = Material(diffuse=color(255, 0, 0), albedo=[0.61, 0.25, 0, 0], spec=10) #Aluminio.
    
    sil = Material(diffuse=color(0, 128, 0), albedo=[0.6, 0.3, 0.1, 0], spec=50) #Silicón.

    #Colores para los osos.
    brown = Material(diffuse=color(139, 69, 19), albedo=[1, 0, 0.6, 0], spec=80) #Marrón.
    #brown = Material(diffuse=color(139, 69, 19)) #Marrón.
    white = Material(diffuse=color(255, 250, 250), albedo=[1, 0, 0, 0], spec=5) #Blanco.
    
    mat = Material(diffuse=color(212, 175, 55), albedo=[0.5, 0.1, 0.4, 0], spec=10)

    mirror = Material(diffuse=color(255, 255, 255), albedo=[0, 1, 0.8, 0], spec=1425) # Espejo.

    glass = Material(diffuse=color(255, 255, 255), albedo=[0, 0.5, 0.1, 0.0], spec=125, refractive_index=1.5) # Vidrio.
    
    #Creando esferas.
    c1.scene = [

        #Esferas de aluminio.
        Sphere(V3(-0.5, -2.2,-12), 0.8, al),
        Sphere(V3(1, -2.2,-12), 0.8, sil),
        Sphere(V3(-2, -2.2,-12), 0.8, mirror),
        Sphere(V3(2.5, -2.2,-12), 0.8, glass),
        Plane(V3(0, 0.5, -6), 2, 2, brown)

    ]

    c1.light = Light(V3(0, 3, 0), 1, color(255, 255, 255)) #Creando la luz.

def envmap(path): #Setter del envmap.
    c1.envmap = path

def get_background(direction):
    if c1.envmap:
        return c1.envmap.get_color(direction)
    else:
        return color(0, 0, 0)

def cast_ray(orig, direction, recursion=0): #Método para el rayo.
    #Revisa contra que chocó y en base a eso regresa un material.

    #Se verifica si no se ha pasado del máximo de recursiones.
    if recursion >= c1.max_recursion_depth:
        return c1.color_fondo #Asigna el color de fondo.
    
    material, intersect = scene_intersect(orig, direction) #Llamando a la función para la intersección.

    if material is None: #Si no hay material, entonces se regresa el color de fondo.
        return c1.color_fondo

    light_dir = (c1.light.position - intersect.point).normalice() #Llamando al método para la luz.

    #print(reflection_color)

    bias = 1.1 #Definiendo el bias.
    shadow_orig = intersect.point + (intersect.normal * bias) #Calculando el origen de la sombra.
    shadowmat, shadowin = scene_intersect(shadow_orig, light_dir) #Calculando la intersección de la sombra.

    shadow_intensity = 0 #Intensidad de la sombra.
    if shadowmat: 
        shadow_intensity = 0.75 #Si hay sombra, entonces la intensidad es 0.6.

    diffuse_intensity = light_dir @ intersect.normal #Calculando la intensidad de la luz.

    #Reflexión.
    if material.albedo[2] > 0: #Si el material tiene reflexión.
        reversion_dir = direction * -1 #Se invierte el rayo.
        reflect_dir = reflect(reversion_dir, intersect.normal) #Se calcula el rayo reflejado.
        reflection_bias = -0.8 if reflect_dir @ intersect.normal < 0 else 0.8 #Se calcula el bias.
        reflect_orig = intersect.point - (intersect.normal * reflection_bias) #Se calcula el origen del rayo reflejado.
        reflect_col = cast_ray(reflect_orig, reflect_dir, recursion + 1) #Se calcula el color del rayo reflejado.
    else: #Si no tiene reflexión.
        reflect_col = color(0, 0, 0)

    #Multiplicar el color de la reflexión por el albedo de la reflexión.
    reflection_color = reflect_col * material.albedo[2] #Se calcula el color de la reflexión.

    #Refracción.
    if material.albedo[3] > 0: #Si el material tiene reflexión.
        refract_dir = refract(direction, intersect.normal, material.refractive_index) #Se calcula el rayo reflejado.
        refract_bias = -0.8 if refract_dir @ intersect.normal < 0 else 0.8 #Se calcula el bias.
        refract_orig = intersect.point - (intersect.normal * refract_bias) #Se calcula el origen del rayo reflejado.
        refract_col = cast_ray(refract_orig, refract_dir, recursion + 1) #Se calcula el color del rayo reflejado.
    else: #Si no tiene reflexión.
        refract_col = color(0, 0, 0)

    #print(reflect_col)
    #Multiplicar el color de la reflexión por el albedo de la reflexión.
    refraction = refract_col * material.albedo[3] #Se calcula el color de la reflexión.

    
    #Calculando el color de la esfera.
    
    # print(material.diffuse)
    # print(diffuse_intensity)
    # print(material.albedo[0])

    diffuse = material.diffuse * diffuse_intensity * material.albedo[0] * (1 - shadow_intensity) #Calculando la reflexión difusa.
    #diffuse = material.diffuse * diffuse_intensity
    #print("Diffuse: ", diffuse)

    #Componente especular.
    light_reflection = reflect(light_dir, intersect.normal) #Calculando la reflexión.
    reflection_intensity = max(0, light_reflection @ direction) #Calculando la intensidad de la reflexión.
    specular_intensity =  (c1.light.intensity * reflection_intensity) ** material.spec #Calculando la intensidad de la luz.
    specular = c1.light.c * specular_intensity * material.albedo[1] #Calculando la reflexión especular.

    #print("Especular: ", specular)

    #print(diffuse + specular)

    # print(light_reflection)
    # print(reflection_intensity)
    # print(specular_intensity)
    #print(diffuse + specular + reflection_color)
    #return (diffuse + specular)
    return (diffuse + specular + reflection_color + refraction) #Regresando el color de la esfera.
    #print(diffuse)
    
    #return (diffuse).toBytes() #Regresando el color de la esfera.

#Método para calcular la reflexión.
def reflect(I, N):
    return (I - N * (2 * (I @ N))).normalice()

#Método para calcular la refracción.
def refract(I, N, roi):
    #I = dirección del rayo.
    #N = normal de la superficie.
    #roi = rayo de salida.
    etai = 1
    etat = roi

    cosi = (I @ N) * -1 #Calculando el coseno.

    if cosi < 0: #Si el coseno es menor a 0.
        cosi = -cosi
        eati = -eati
        etat = -etat
        N = N * -1

    eta = etai/etat #Calculando la razón de eta.

    k = 1 - eta**2 * (1 - cosi**2) #Calculando k.

    if k < 0: #Si k es menor a 0.
        return V3(0, 0, 0)

    cost = k ** 0.5 #Calculando el coseno de t.

    return ((I * eta) + (N * (eta * cosi - cost))).normalice() #Regresando el vector de la reflexión.

    #return (I - (N * 2 * (N @ I))).normalice()

#Función para la intersección.
def scene_intersect(orig, direction):
    #Revisa todos los objetos de la escena y regresa el material del objeto con el que chocó.
    zBuffer = 999999 #Se crea el zBuffer. 
    material = None #Se crea el material.
    intersect = None #Se crea la intersección.

    for o in c1.scene: #Recorriendo el array de esferas.
        object_intersect = o.ray_intersect(orig, direction) #Llamando al método para el rayo.
        if object_intersect: #Si hay intersección, entonces se regresa el material.
            if object_intersect.distance < zBuffer:
                #Se actualiza el zBuffer y se regresa el material actualizado.
                zBuffer = object_intersect.distance
                material = o.material
                intersect = object_intersect
    
    return material, intersect #Regresando el color de la esfera.


def finish():
    fov = int(pi/2)
    aspectRatio = c1.width / c1.height #Relación de aspecto.
    tana = tan(fov/2) #Tangente del ángulo.

    for y in range(c1.height):
        for x in range(c1.width):
            i = ((2 * (x + 0.5) / c1.width) - 1) * aspectRatio * tana
            j = (1 - ( 2 * (y + 0.5) / c1.height)) * tana
            origin = V3(0, 0, 0)
            direction = (V3(i, j, -1)).normalice()

            c = cast_ray(origin, direction) #Llamando al método para el rayo.
        
            point(x, y, c) #Pintando un punto con el color que se recibe después del cast_ray.
    c1.write()