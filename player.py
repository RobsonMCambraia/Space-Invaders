import turtle
import time

class Player():
    def __init__(self):
        self.playerspeed = 15

        # Configurar o jogador
        turtle.register_shape("src/nave-player.gif")
        self.player = turtle.Turtle()
        self.player.shape("src/nave-player.gif")
        self.player.penup()
        self.player.speed(0)
        self.player.setposition(0, -250)
        self.player.setheading(90)
        
    # Configuração do projétil disparado pelo jogador
    def configFogo(self):
        self.fogo = turtle.Turtle()
        self.fogo.color("dark orange")
        self.fogo.shape("triangle")
        self.fogo.penup()
        self.fogo.speed(0.1)
        self.fogo.setheading(90)
        self.fogo.shapesize(0.5, 0.5)
        self.fogo.setposition(0, -235)
        self.fogospeed = 30
        
    # Função para mover o projétil disparado pelo jogador
    def mover_fogo(self):
        y = self.fogo.ycor()
        while y < 300:
            y += self.fogospeed
            self.fogo.sety(y)
            time.sleep(0.01)
        self.fogo.sety(-235)
        
    # Função para mover o jogador para a esquerda
    def mover_esquerda(self):
        x = self.player.xcor()
        if x >= -250:
            x -= self.playerspeed
        self.player.setx(x)
        self.fogo.setx(x)
        
    # Função para mover o jogador para a direita
    def mover_direita(self):
        x = self.player.xcor()
        if x <= 250:
            x += self.playerspeed
        self.player.setx(x)
        self.fogo.setx(x)