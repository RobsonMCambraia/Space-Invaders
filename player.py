import turtle
import time
from enemy import Enemy
import random

class Player():
    def __init__(self, fogo, player, enemy):
        # Inicializa as tartarugas do jogador e do projétil
        self.fogo = turtle.Turtle()
        self.player = turtle.Turtle()
        
        # Velocidades para o jogador e o projétil
        self.playerspeed = 15
        self.fogospeed = 30
        
        # Recebe as configurações para o jogador e o projétil
        self.configuração_fogo = fogo
        self.configuração_player = player
        
        self.enemy = enemy
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
    
    def init_pos(self):
        x_positions = []
        y_positions = []
        for pos_invaders in self.inimigos.enemies1 :
            x_position = pos_invaders.xcor()
            y_position = pos_invaders.ycor()
            x_positions.append(x_position)
            y_positions.append(y_position)

        left_pos = min(x_positions)
        right_pos = max(x_positions)

        down_pos = min(y_positions)

        left_id = x_positions.index(left_pos)
        right_id = x_positions.index(right_pos)
        down_id = y_positions.index(down_pos)

        global left_index, right_index, down_index
        return left_id, right_id, down_id
            
    # Função para mover o projétil disparado pelo jogador
    def mover_fogo(self):
        x_fogo = self.fogo.xcor()
        y_fogo = self.fogo.ycor()
        while y_fogo < 300:
            y_fogo += self.fogospeed
            self.fogo.sety(y_fogo)
            time.sleep(0.01)
            
            for inimigo1 in self.enemy.enemies1:
                x_ini = inimigo1.xcor()
                y_ini = inimigo1.ycor()
                if x_fogo >= x_ini - 20 and x_fogo <= x_ini + 20:
                    if y_fogo >= y_ini:
                        inimigo1.setx(random.randint(-280, 280))
                        inimigo1.sety(random.randint(100, 250))
                        y_fogo = 400
                        break
            for inimigo2 in self.enemy.enemies2:
                x_ini = inimigo2.xcor()
                y_ini = inimigo2.ycor()
                if x_fogo >= x_ini - 20 and x_fogo <= x_ini + 20:
                    if y_fogo >= y_ini:
                        inimigo2.setx(random.randint(-280, 280))
                        inimigo2.sety(random.randint(100, 250))
                        y_fogo = 400
                        break                      
            for inimigo3 in self.enemy.enemies3:
                x_ini = inimigo3.xcor()
                y_ini = inimigo3.ycor()
                if x_fogo >= x_ini - 20 and x_fogo <= x_ini + 20:
                    if y_fogo >= y_ini:
                        inimigo3.setx(random.randint(-280, 280))
                        inimigo3.sety(random.randint(100, 250))
                        y_fogo = 400
                        break
            y_fogo += self.fogospeed
            self.fogo.sety(y_fogo)
                                                                    
        self.fogo.sety(-235)
        
        while y_fogo < 300:
            for inimigo in self.inimigos.enemies1:
                x_ini = inimigo.xcor()
                y_ini = inimigo.ycor()
                if x_fogo >= x_ini -20 and x_fogo <= x_ini + 20:
                    if y_fogo >= y_ini:
                        inimigo.setx(random.randint(-280, 280))
                        inimigo.sety(random.randint(100, 250))
                        y_fogo = 400
                        left_index, right_index, down_index = self.init_pos()
                        break
                
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
