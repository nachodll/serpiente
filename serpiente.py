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
      self.aniadir_segmento(posicion)
    self.cabeza = self.segmentos[0]

  def crecer(self):
    nueva_pos = self.segmentos[-1].pos()
    self.aniadir_segmento(nueva_pos)

  def aniadir_segmento(self, posicion):
    nuevo_segmento = turtle.Turtle("square")
    nuevo_segmento.penup()
    nuevo_segmento.goto(posicion)
    self.segmentos.append(nuevo_segmento)

  def mover(self):
    for seg_num in range(len(self.segmentos)-1, 0, -1):
      nueva_pos = self.segmentos[seg_num-1].pos()
      self.segmentos[seg_num].goto(nueva_pos)
    self.cabeza.forward(20)

  def derecha(self):
    if self.cabeza.heading() != IZQUIERDA:
      self.cabeza.setheading(DERECHA)

  def arriba(self): 
    if self.cabeza.heading() != ABAJO:
      self.cabeza.setheading(ARRIBA)

  def izquierda(self):
    if self.cabeza.heading() != DERECHA:
      self.cabeza.setheading(IZQUIERDA)

  def abajo(self):
    if self.cabeza.heading() != ARRIBA:
      self.cabeza.setheading(ABAJO)
      