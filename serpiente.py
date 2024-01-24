import turtle

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]
DERECHA = 0
ARRIBA = 90
IZQUIERDA = 180
ABAJO = 270 

class Serpiente:

  def __init__(self):
    self.segmentos = []
    for posicion in POSICIONES_INICIALES:
      nuevo_segmento = turtle.Turtle("square")
      nuevo_segmento.penup()
      nuevo_segmento.goto(posicion)
      self.segmentos.append(nuevo_segmento)


  def mover(self):
    for seg_num in range(len(self.segmentos)-1, 0, -1):
      nueva_pos = self.segmentos[seg_num-1].pos()
      self.segmentos[seg_num].goto(nueva_pos)
    self.segmentos[0].forward(20)

  def derecha(self):
    if self.segmentos[0].heading() != IZQUIERDA:
      self.segmentos[0].setheading(DERECHA)

  def arriba(self): 
    if self.segmentos[0].heading() != ABAJO:
      self.segmentos[0].setheading(ARRIBA)

  def izquierda(self):
    if self.segmentos[0].heading() != DERECHA:
      self.segmentos[0].setheading(IZQUIERDA)

  def abajo(self):
    if self.segmentos[0].heading() != ARRIBA:
      self.segmentos[0].setheading(ABAJO)
      