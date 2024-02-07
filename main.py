import turtle
import time
import os
from serpiente import Serpiente 
from comida import Comida

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]

# Crear la ventana
ventana = turtle.Screen()
ventana.setup(600, 600)
ventana.bgcolor("red")

# Registrar todos los sprites
for filename in os.listdir('gifs/'):
  ventana.addshape('gifs/' + filename)

ventana.tracer(0)

# Crear los objetos
serpiente = Serpiente()
comida = Comida()

# Configurar los listeners
ventana.listen()
ventana.onkey(serpiente.derecha,"Right")
ventana.onkey(serpiente.arriba,"Up")
ventana.onkey(serpiente.izquierda,"Left")
ventana.onkey(serpiente.abajo,"Down")


jugando = True

# Bucle principal (main loop)
while jugando:
  ventana.update()
  time.sleep(0.1)

  # Mover la serpiente
  serpiente.mover()

  # Detectar colision con comida
  if serpiente.cabeza.distance(comida) < 25:
    comida.actualizar()

ventana.exitonclick()

