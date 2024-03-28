import turtle
import sprites

SEGMENT_SIZE = 40
POSICIONES_INICIALES = [(0, 0), (-SEGMENT_SIZE, 0), (-SEGMENT_SIZE*2, 0)]
DERECHA = 0
ARRIBA = 90
IZQUIERDA = 180
ABAJO = 270 

class Serpiente:

  def __init__(self):
    self.segmentos = []
    for posicion in POSICIONES_INICIALES:
      self.aniadir_segmento(posicion)
    
    self.puede_girar = True
    self.cabeza = self.segmentos[0]
    self.cuello = self.segmentos[1]
    self.cola = self.segmentos[-1]
    self.actualizar_sprites()

  def crecer(self):
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
    self.puede_girar = True
    self.actualizar_sprites()
    self.cola.showturtle()

  def actualizar_sprites(self):
    # Cola
    precola = self.segmentos[len(self.segmentos)-2]
    if round(self.cola.xcor()) == round(precola.xcor()):
      if self.cola.ycor() < precola.ycor():
        self.cola.shape(sprites.COLA_ARRIBA)
      else:
        self.cola.shape(sprites.COLA_ABAJO)
    else:
      if round(self.cola.xcor()) < round(precola.xcor()):
        self.cola.shape(sprites.COLA_DERECHA)
      else:
        self.cola.shape(sprites.COLA_IZQUIERDA)

    # Resto del cuerpo
    for seg_num in range(len(self.segmentos)-2, 1, -1):
      self.segmentos[seg_num].shape(self.segmentos[seg_num-1].shape())

    # Cabeza
    if self.cabeza.heading() == ARRIBA:
      self.cabeza.shape(sprites.CABEZA_ARRIBA)
    elif self.cabeza.heading() == ABAJO:
      self.cabeza.shape(sprites.CABEZA_ABAJO)
    elif self.cabeza.heading() == DERECHA:
      self.cabeza.shape(sprites.CABEZA_DERECHA)
    elif self.cabeza.heading() == IZQUIERDA:
      self.cabeza.shape(sprites.CABEZA_IZQUIERDA)

    # Cuello
    precuello = self.segmentos[2]
    if (round(self.cuello.xcor()) == round(self.cabeza.xcor())
        and round(self.cuello.xcor()) == round(precuello.xcor())):
      self.cuello.shape(sprites.TRONCO_VERTICAL)
    elif (round(self.cuello.ycor()) == round(self.cabeza.ycor())
        and round(self.cuello.ycor()) == round(precuello.ycor())):
      self.cuello.shape(sprites.TRONCO_HORIZONTAL)
    elif round(self.cuello.xcor()) > round(self.cabeza.xcor()):
      if round(self.cuello.ycor()) > round(precuello.ycor()):
        self.cuello.shape(sprites.GIRO1)
      else:
        self.cuello.shape(sprites.GIRO2)
    elif round(self.cuello.xcor()) < round(self.cabeza.xcor()):
      if round(self.cuello.ycor()) > round(precuello.ycor()):
        self.cuello.shape(sprites.GIRO4)
      else:
        self.cuello.shape(sprites.GIRO3)
    elif round(self.cuello.ycor()) > round(self.cabeza.ycor()):
      if round(self.cuello.xcor()) > round(precuello.xcor()):
        self.cuello.shape(sprites.GIRO1)
      else:
        self.cuello.shape(sprites.GIRO4)
    elif round(self.cuello.ycor()) < round(self.cabeza.ycor()):
      if round(self.cuello.xcor()) > round(precuello.xcor()):
        self.cuello.shape(sprites.GIRO2)
      else:
        self.cuello.shape(sprites.GIRO3)

          
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
      