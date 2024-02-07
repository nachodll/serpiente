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
    self.cabeza.shape(SPRITE_CABEZA_DERECHA)
    self.segmentos[1].shape(SPRITE_TRONCO_HORIZONTAL)
    self.segmentos[-1].shape(SPRITE_COLA_DERECHA)

  def extender(self):
    self.aniadir_segmento(self.segmentos[-1].position())

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

  def actualizar_sprites(self):
    for seg_num in range(len(self.segmentos)-1, 0, -1):
      # Primero despues de la cabeza
      if seg_num == 1:
        if (round(self.segmentos[seg_num].xcor()) == round(self.cabeza.xcor())
            and round(self.segmentos[seg_num].xcor()) == round(self.segmentos[seg_num+1].xcor())):
          self.segmentos[seg_num].shape(SPRITE_TRONCO_VERTICAL)
        elif (round(self.segmentos[seg_num].ycor()) == round(self.cabeza.ycor())
            and round(self.segmentos[seg_num].ycor()) == round(self.segmentos[seg_num+1].ycor())):
          self.segmentos[seg_num].shape(SPRITE_TRONCO_HORIZONTAL)
        elif round(self.segmentos[seg_num].xcor()) > round(self.cabeza.xcor()):
          if round(self.segmentos[seg_num].ycor()) > round(self.segmentos[seg_num+1].ycor()):
            self.segmentos[seg_num].shape(SPRITE_GIRO1)
          else:
            self.segmentos[seg_num].shape(SPRITE_GIRO2)
        elif round(self.segmentos[seg_num].xcor()) < round(self.cabeza.xcor()):
          if round(self.segmentos[seg_num].ycor()) > round(self.segmentos[seg_num+1].ycor()):
            self.segmentos[seg_num].shape(SPRITE_GIRO4)
          else:
            self.segmentos[seg_num].shape(SPRITE_GIRO3)
        elif round(self.segmentos[seg_num].ycor()) > round(self.cabeza.ycor()):
          if round(self.segmentos[seg_num].xcor()) > round(self.segmentos[seg_num+1].xcor()):
            self.segmentos[seg_num].shape(SPRITE_GIRO1)
          else:
            self.segmentos[seg_num].shape(SPRITE_GIRO4)
        elif round(self.segmentos[seg_num].ycor()) < round(self.cabeza.ycor()):
          if round(self.segmentos[seg_num].xcor()) > round(self.segmentos[seg_num+1].xcor()):
            self.segmentos[seg_num].shape(SPRITE_GIRO2)
          else:
            self.segmentos[seg_num].shape(SPRITE_GIRO3)

      # Cola
      if seg_num == len(self.segmentos)-1:
        if round(self.segmentos[seg_num].xcor()) == round(self.segmentos[seg_num-1].xcor()):
          if self.segmentos[seg_num].ycor() < self.segmentos[seg_num-1].ycor():
            self.segmentos[seg_num].shape(SPRITE_COLA_ARRIBA)
          else:
            self.segmentos[seg_num].shape(SPRITE_COLA_ABAJO)
        else:
          if round(self.segmentos[seg_num].xcor()) < round(self.segmentos[seg_num-1].xcor()):
            self.segmentos[seg_num].shape(SPRITE_COLA_DERECHA)
          else:
            self.segmentos[seg_num].shape(SPRITE_COLA_IZQUIERDA)

      # Resto del cuerpo
      if seg_num != 1 and seg_num != len(self.segmentos)-1 and seg_num != 0:
        self.segmentos[seg_num].shape(self.segmentos[seg_num-1].shape())

          
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
      