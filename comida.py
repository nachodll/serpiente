import random
import turtle

SPRITE_MANZANA = 'gifs/manzana.gif'

class Comida(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.shapesize(0.5, 0.5)
    self.shape(SPRITE_MANZANA)
    self.penup()
    self.color("blue")
    self.actualizar()


  def actualizar (self):
    new_x = random.randint(-300, 300)
    new_y = random.randint(-300, 300)
    self.goto(new_x, new_y)
