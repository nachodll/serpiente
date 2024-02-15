from turtle import Turtle
ALINEACION = "center"
FUENTE = ("Courier", 24, "normal")

class Puntuacion(Turtle):

    def __init__(self):
      super().__init__()
      self.puntuacion = 0
      self.highscore = self.leer_highscore()
      self.color("white")
      self.penup()
      self.goto(0, 260)
      self.hideturtle()
      self.actualizar_puntuacion()

    def leer_highscore(self):
      try:
        with open('highscore.txt') as file:
          highscore = int(file.read())
          return highscore or 0
      except:
        return 0
      
    def actualizar_highscore(self):
      with open('highscore.txt', 'w') as file:
        file.write(str(self.puntuacion))

    def actualizar_puntuacion(self):
      self.write(
        f"Record: {self.highscore}\t Puntuación: {self.puntuacion}", 
        align=ALINEACION, font=FUENTE)

    def game_over(self):
      self.goto(0, 0)
      self.write("GAME OVER", align=ALINEACION, font=FUENTE)
      if self.puntuacion > self.highscore:
        self.goto(0, -40)
        self.write('NUEVO RECORD!', align=ALINEACION, font=FUENTE)
        self.actualizar_highscore()

    def incrementar_puntuacion(self):
      self.puntuacion += 1
      self.clear()
      self.actualizar_puntuacion()
        