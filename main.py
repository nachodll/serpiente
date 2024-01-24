import turtle
import time

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]

# Crear la ventana
ventana = turtle.Screen()
ventana.setup(600, 600)
ventana.bgcolor("red")

ventana.tracer(0)

# Crear la serpiente
segmentos = []
for posicion in POSICIONES_INICIALES:
  nuevo_segmento = turtle.Turtle("square")
  nuevo_segmento.penup()
  nuevo_segmento.goto(posicion)
  segmentos.append(nuevo_segmento)

# Bucle principal (main loop)
jugando = True

while jugando:
  ventana.update()
  time.sleep(0.1)

  # Mover la serpiente
  for seg in segmentos:
    seg.forward(20)


ventana.exitonclick()

