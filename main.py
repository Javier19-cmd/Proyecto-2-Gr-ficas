from gl import * 
from utilidades import * #Archivo de utilidades.
from material import * #Archivo de material.
from ray import * #Archivo de rayo.

def main(): 
    glCreateWindow(1920, 1280)  
    glClearColor(212, 175, 55) 
    glClear() 
    envmap("Fondo.bmp") #Cargar imagen de fondo.
    #carga("Fondo.bmp")
    #Creando array para las esferas.
    glColor(255, 0, 0)
    #glSphere(3, 1, -16, 0.5)
    
    #Creando esferas.
    #glSphere() #Esfera 3 color azul.
    #glPlane() #Plano.
    escena() #Escena.

    finish()

main()