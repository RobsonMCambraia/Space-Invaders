import turtle
class Display():
    def __init__ (self, border_settings, placar_score):
        self.border_settings = border_settings
        self.placar_setup = placar_score
        
        self.desenharBorda()
        self.placarScore()
        
    def desenharBorda(self):
        # Desenhar a borda
        border_pen = turtle.Turtle()
        border_pen.speed(self.border_settings["speed"])
        border_pen.color(self.border_settings["color"])
        border_pen.penup()
        border_pen.setposition(self.border_settings["position_x"], self.border_settings["position_y"])
        border_pen.pendown()
        border_pen.pensize(self.border_settings["size"])

        for side in range(4):
            border_pen.fd(600)
            border_pen.lt(90)
            
        border_pen.hideturtle()

    def placarScore(self):
        score_pen = turtle.Turtle()
        score = 0
        score_pen.speed(self.placar_setup["speed"])
        score_pen.color(self.placar_setup["color"])
        score_pen.penup()   
        score_pen.setposition(self.placar_setup["position_x"], self.placar_setup["position_y"])
        scorestring = "SCORE: %s" % score
        score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
        score_pen.hideturtle()