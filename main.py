import turtle
import time
from serpiente import Serpiente 
from comida import Comida
from puntuacion import Puntuacion

# Crear la ventana
ventana = turtle.Screen()
ventana.setup(600, 600)
ventana.bgcolor("red")

ventana.tracer(0)

# Crear la serpiente
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
  if serpiente.cabeza.xcor() > 280 or serpiente.cabeza.xcor() < -280 or serpiente.cabeza.ycor() > 280 or serpiente.cabeza.ycor() < -280:
    puntuacion.game_over()
    jugando = False

  # Detectar colision con el cuerpo 
  for segmento in serpiente.segmentos:
     if segmento != serpiente.cabeza:
      if serpiente.cabeza.distance(segmento) < 20:
          jugando = False
          puntuacion = puntuacion.game_over()

ventana.exitonclick()

