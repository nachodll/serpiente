import turtle
import random

SEGMENT_SIZE = 40
POSICIONES_INICIALES = [(0, 0), (-SEGMENT_SIZE, 0), (-SEGMENT_SIZE*2, 0)]
DERECHA = 0
ARRIBA = 90
IZQUIERDA = 180
ABAJO = 270 
SPRITE_CABEZA_IZQUIERDA = 'gifs/cabeza_izquierda.gif'
SPRITE_CABEZA_DERECHA = 'gifs/cabeza_derecha.gif'
SPRITE_CABEZA_ARRIBA = 'gifs/cabeza_arriba.gif'
SPRITE_CABEZA_ABAJO = 'gifs/cabeza_abajo.gif'
SPRITE_COLA_IZQUIERDA = 'gifs/cola_izquierda.gif'
SPRITE_COLA_DERECHA = 'gifs/cola_derecha.gif'
SPRITE_COLA_ARRIBA = 'gifs/cola_arriba.gif'
SPRITE_COLA_ABAJO = 'gifs/cola_abajo.gif'
SPRITE_TRONCO_HORIZONTAL = 'gifs/tronco_horizontal.gif'
SPRITE_TRONCO_VERTICAL = 'gifs/tronco_vertical.gif'
SPRITE_GIRO1 = 'gifs/giro1.gif'
SPRITE_GIRO2 = 'gifs/giro2.gif'
SPRITE_GIRO3 = 'gifs/giro3.gif'
SPRITE_GIRO4 = 'gifs/giro4.gif'

class Serpiente:

  def __init__(self):
    self.segmentos = []
    for posicion in POSICIONES_INICIALES:
      self.aniadir_segmento(posicion)

    self.cabeza = self.segmentos[0]
    self.cuello = self.segmentos[1]
    self.cola = self.segmentos[-1]
    self.actualizar_sprites()

  def extender(self):
    self.aniadir_segmento(self.segmentos[-1].position())
    self.cola = self.segmentos[-1]
    self.cola.hideturtle()

  def aniadir_segmento(self, posicion):
    nuevo_segmento = turtle.Turtle("square")
    nuevo_segmento.penup()
    nuevo_segmento.goto(posicion)
    self.segmentos.append(nuevo_segmento)

  def mover(self):
    for seg_num in range(len(self.segmentos)-1, 0, -1):
      nueva_pos = self.segmentos[seg_num-1].pos()
      self.segmentos[seg_num].goto(nueva_pos)
    self.cabeza.forward(SEGMENT_SIZE)
    self.actualizar_sprites()
    self.cola.showturtle()

  def actualizar_sprites(self):
    # Cola
    precola = self.segmentos[len(self.segmentos)-2]
    if round(self.cola.xcor()) == round(precola.xcor()):
      if self.cola.ycor() < precola.ycor():
        self.cola.shape(SPRITE_COLA_ARRIBA)
      else:
        self.cola.shape(SPRITE_COLA_ABAJO)
    else:
      if round(self.cola.xcor()) < round(precola.xcor()):
        self.cola.shape(SPRITE_COLA_DERECHA)
      else:
        self.cola.shape(SPRITE_COLA_IZQUIERDA)

    # Resto del cuerpo
    for seg_num in range(len(self.segmentos)-2, 1, -1):
      self.segmentos[seg_num].shape(self.segmentos[seg_num-1].shape())

    # Cabeza
    if self.cabeza.heading() == ARRIBA:
      self.cabeza.shape(SPRITE_CABEZA_ARRIBA)
    elif self.cabeza.heading() == ABAJO:
      self.cabeza.shape(SPRITE_CABEZA_ABAJO)
    elif self.cabeza.heading() == DERECHA:
      self.cabeza.shape(SPRITE_CABEZA_DERECHA)
    elif self.cabeza.heading() == IZQUIERDA:
      self.cabeza.shape(SPRITE_CABEZA_IZQUIERDA)

    # Cuello
    precuello = self.segmentos[2]
    if (round(self.cuello.xcor()) == round(self.cabeza.xcor())
        and round(self.cuello.xcor()) == round(precuello.xcor())):
      self.cuello.shape(SPRITE_TRONCO_VERTICAL)
    elif (round(self.cuello.ycor()) == round(self.cabeza.ycor())
        and round(self.cuello.ycor()) == round(precuello.ycor())):
      self.cuello.shape(SPRITE_TRONCO_HORIZONTAL)
    elif round(self.cuello.xcor()) > round(self.cabeza.xcor()):
      if round(self.cuello.ycor()) > round(precuello.ycor()):
        self.cuello.shape(SPRITE_GIRO1)
      else:
        self.cuello.shape(SPRITE_GIRO2)
    elif round(self.cuello.xcor()) < round(self.cabeza.xcor()):
      if round(self.cuello.ycor()) > round(precuello.ycor()):
        self.cuello.shape(SPRITE_GIRO4)
      else:
        self.cuello.shape(SPRITE_GIRO3)
    elif round(self.cuello.ycor()) > round(self.cabeza.ycor()):
      if round(self.cuello.xcor()) > round(precuello.xcor()):
        self.cuello.shape(SPRITE_GIRO1)
      else:
        self.cuello.shape(SPRITE_GIRO4)
    elif round(self.cuello.ycor()) < round(self.cabeza.ycor()):
      if round(self.cuello.xcor()) > round(precuello.xcor()):
        self.cuello.shape(SPRITE_GIRO2)
      else:
        self.cuello.shape(SPRITE_GIRO3)

          
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
      