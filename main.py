from gl import * 
from utilidades import * #Archivo de utilidades.
from material import * #Archivo de material.
from ray import * #Archivo de rayo.

def main(): 
    glCreateWindow(1000, 1000)  
    glClearColor(212, 175, 55) 
    glClear() 
    #glColor(255, 0, 0)
    envmap("./Arbol.bmp") #Cargar imagen de fondo.
    #Cargando el fondo.
    #get_background()
    #Creando array para las esferas.
    #glSphere(3, 1, -16, 0.5)
    
    #Creando esferas.
    #glSphere() #Esfera 3 color azul.
    #glPlane() #Plano.
    escena() #Escena.

    finish()

main()