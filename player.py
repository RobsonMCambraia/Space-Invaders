import turtle
import time

class Player():
    def __init__(self, fogo, player):
        # Inicializa as tartarugas do jogador e do projétil
        self.fogo = turtle.Turtle()
        self.player = turtle.Turtle()
        
        # Velocidades para o jogador e o projétil
        self.playerspeed = 15
        self.fogospeed = 30
        
        # Recebe as configurações para o jogador e o projétil
        self.configuração_fogo = fogo
        self.configuração_player = player
        
        # Configura a aparência do jogador
        self.configPlayer()
        # Configura a aparência e posição inicial do projétil
        self.configFogo()
        
    def configPlayer(self):
        # Configura a aparência do jogador
        player = self.player
        # Registra a forma do jogador no Turtle
        turtle.register_shape(self.configuração_player["caminho_shape"])
        player.shape(self.configuração_player["caminho_shape"])
        player.penup()
        player.speed(self.configuração_player["speed"])
        player.setposition(self.configuração_player["position_x"], self.configuração_player["position_y"])
        player.setheading(self.configuração_player["heading"])
        
    # Configuração do projétil disparado pelo jogador
    def configFogo(self):
        # Configura a aparência do projétil
        fogo = self.fogo
        fogo.color(self.configuração_fogo["color"])
        fogo.shape(self.configuração_fogo["shape"])
        fogo.penup()
        fogo.speed(self.configuração_fogo["speed"])
        fogo.setheading(self.configuração_fogo["heading"])
        fogo.shapesize(self.configuração_fogo["shape_size_x"], self.configuração_fogo["shape_size_y"])
        fogo.setposition(self.configuração_fogo["position_x"], self.configuração_fogo["position_y"])
            
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
