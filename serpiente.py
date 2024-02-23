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
    self.puede_girar = True

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
    self.puede_girar = True

  def derecha(self):
    if self.cabeza.heading() != IZQUIERDA and self.puede_girar:
      self.cabeza.setheading(DERECHA)
    self.puede_girar = False

  def arriba(self): 
    if self.cabeza.heading() != ABAJO and self.puede_girar:
      self.cabeza.setheading(ARRIBA)
    self.puede_girar = False

  def izquierda(self):
    if self.cabeza.heading() != DERECHA and self.puede_girar:
      self.cabeza.setheading(IZQUIERDA)
    self.puede_girar = False

  def abajo(self):
    if self.cabeza.heading() != ARRIBA and self.puede_girar:
      self.cabeza.setheading(ABAJO)
    self.puede_girar = False
      