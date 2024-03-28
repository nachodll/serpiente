import turtle
import time
import os
from serpiente import Serpiente 
from comida import Comida
from puntuacion import Puntuacion

# Crear la ventana
ventana = turtle.Screen()
ventana.setup(600, 600)
ventana.bgpic('gifs/dirt.gif')

# Registrar todos los sprites
for filename in os.listdir('gifs/'):
  ventana.addshape('gifs/' + filename)

ventana.tracer(0)

# Crear los objetos
serpiente = Serpiente()
comida = Comida()
puntuacion = Puntuacion()

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
    puntuacion.incrementar_puntuacion()
    serpiente.crecer()

  # Detectar colision con las paredes
  if serpiente.cabeza.xcor() > 290 or serpiente.cabeza.xcor() < -290 or serpiente.cabeza.ycor() > 290 or serpiente.cabeza.ycor() < -290:
    puntuacion.game_over()
    jugando = False

  # Detectar colision con el cuerpo 
  for segmento in serpiente.segmentos:
     if segmento != serpiente.cabeza:
      if serpiente.cabeza.distance(segmento) < 10:
          jugando = False
          puntuacion = puntuacion.game_over()

ventana.exitonclick()

