import turtle
import time
from serpiente import Serpiente 

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]

# Crear la ventana
ventana = turtle.Screen()
ventana.setup(600, 600)
ventana.bgcolor("red")

ventana.tracer(0)

# Crear la serpiente
serpiente = Serpiente()

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

ventana.exitonclick()

