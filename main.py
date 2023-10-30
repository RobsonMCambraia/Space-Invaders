import turtle
import random
import time
from player import Player
from display import Display
from enemy import Enemy


border_settings = {
    "speed": 10,
    "color": "white",
    "position_x": -300,
    "position_y": -300,
    "size": 3}

placar_score = {
    "speed": 10,
    "color": "white",
    "position_x": -300,
    "position_y": -300,
    "size": 3}

display = Display(border_settings)

window = turtle.Screen()
window.title("Space Invaders - Robson")
window.bgpic("src/background.gif")

# Instancia das classes
jogador = Player()
inimigo = Enemy()

turtle.listen()
jogador.configFogo()

#Inicialização dos inimigos
inimigo.enemyListAppend()
inimigo.enemyConfig("src/inimigo-1.gif", "src/inimigo-2.gif")
inimigo.enemyMove()

# Configurar os ouvintes de eventos do teclado
turtle.onkey(jogador.mover_esquerda(), "Left")
turtle.onkey(jogador.mover_direita(), "Right")
turtle.onkey(jogador.mover_fogo(), "space")

turtle.done()