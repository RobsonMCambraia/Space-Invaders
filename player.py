import turtle
import time
import random

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
        x_fire = self.fogo.xcor()  # Obtém a posição horizontal do fogo
        while y < 300:
            y += self.fogospeed
            self.fogo.sety(y)
            time.sleep(0.01)
            # Verifica se houve colisão entre o fogo e os inimigos
            for inimigo in self.invaders:
                x_ini = inimigo.xcor()
                y_ini = inimigo.ycor()
                if x_fire >= x_ini - 20 and x_fire <= x_ini + 20 and y >= y_ini:
                    # Reposiciona o inimigo e o fogo e atualiza variáveis se houver colisão
                    inimigo.setx(random.randint(-280, 280))
                    inimigo.sety(random.randint(100, 250))
                    y = 400  # Movendo o fogo para fora da tela
                    self.fogospeed = 0  # Ou atribui um valor para parar o fogo
                    break  # Para verificar colisão com apenas um inimigo por vez
        self.fogo.sety(-235)
