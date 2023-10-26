import turtle
class Display():
    def telaConfig(self, background):
        window = turtle.Screen()
        window.title("Space Invaders - Robson")
        window.bgpic(background)

    def desenharBorda(self):
        # Desenhar a borda
        border_pen = turtle.Turtle()
        border_pen.speed(10)
        border_pen.color("white")
        border_pen.penup()
        border_pen.setposition(-300, -300)
        border_pen.pendown()
        border_pen.pensize(3)

        for side in range(4):
            border_pen.fd(600)
            border_pen.lt(90)
        border_pen.hideturtle()

    def placarScore(self):
        score = 0
        # Desenhar a pontuação
        score_pen = turtle.Turtle()
        score_pen.speed(0)
        score_pen.color("red")
        score_pen.penup()   
        score_pen.setposition(-290, 280)
        scorestring = "SCORE: %s" % score
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        score_pen.hideturtle()