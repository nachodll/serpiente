import turtle

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]
DERECHA = 0
ARRIBA = 90
IZQUIERDA = 180
ABAJO = 270 
SPRITE_CABEZA_IZQUIERDA = 'gifs/cabeza_izquierda.gif'
SPRITE_CABEZA_DERECHA = 'gifs/cabeza_derecha.gif'
SPRITE_CABEZA_ARRIBA = 'gifs/cabeza_arriba.gif'
SPRITE_CABEZA_ABAJO = 'gifs/cabeza_abajo.gif'

class Serpiente:

  def __init__(self):
    self.segmentos = []
    for posicion in POSICIONES_INICIALES:
      nuevo_segmento = turtle.Turtle("square")
      nuevo_segmento.penup()
      nuevo_segmento.goto(posicion)
      self.segmentos.append(nuevo_segmento)
    self.cabeza = self.segmentos[0]
    self.cabeza.shape(SPRITE_CABEZA_DERECHA)


  def mover(self):
    for seg_num in range(len(self.segmentos)-1, 0, -1):
      nueva_pos = self.segmentos[seg_num-1].pos()
      self.segmentos[seg_num].goto(nueva_pos)
    self.cabeza.forward(20)

  def derecha(self):
    if self.cabeza.heading() != IZQUIERDA:
      self.cabeza.setheading(DERECHA)
      self.cabeza.shape(SPRITE_CABEZA_DERECHA)

  def arriba(self): 
    if self.cabeza.heading() != ABAJO:
      self.cabeza.setheading(ARRIBA)
      self.cabeza.shape(SPRITE_CABEZA_ARRIBA)

  def izquierda(self):
    if self.cabeza.heading() != DERECHA:
      self.cabeza.setheading(IZQUIERDA)
      self.cabeza.shape(SPRITE_CABEZA_IZQUIERDA)

  def abajo(self):
    if self.cabeza.heading() != ARRIBA:
      self.cabeza.setheading(ABAJO)
      self.cabeza.shape(SPRITE_CABEZA_ABAJO)
      