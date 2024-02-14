from turtle import Turtle
ALINEACION = "center"
FUENTE = ("Courier", 24, "normal")

class Puntuacion(Turtle):

    def __init__(self):
        super().__init__()
        self.puntuacion = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.actualizar_puntuacion()

    def actualizar_puntuacion(self):
        self.write(f"Puntuación: {self.puntuacion}", align=ALINEACION, font=FUENTE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALINEACION, font=FUENTE)

    def incrementar_puntuacion(self):
        self.puntuacion += 1
        self.clear()
        self.actualizar_puntuacion()