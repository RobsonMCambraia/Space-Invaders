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
    "speed": 0,
    "color": "red",
    "position_x": -290,
    "position_y": 280}

display = Display(border_settings, placar_score)

window = turtle.Screen()
window.title("Space Invaders - Robson")
window.bgpic("src/background.gif")

fogo = {
    "speed": 0.1,
    "color": "dark orange",
    "position_x": 0,
    "position_y": -235,
    "shape": "triangle",
    "shape_size_x": 0.5,
    "shape_size_y": 0.5,
    "heading": 90}
player = {
    "speed": 0,
    "position_x": 0,
    "position_y": -250,
    "caminho_shape": "src/nave-player.gif",
    "heading": 90}
    
jogador = Player(fogo, player)


inimigo = Enemy()

turtle.listen()

#Inicialização dos inimigos
inimigo.enemyListAppend()
inimigo.enemyConfig("src/inimigo-1.gif", "src/inimigo-2.gif")
inimigo.enemyMove()

# Configurar os ouvintes de eventos do teclado
turtle.onkey(jogador.mover_esquerda(), "Left")
turtle.onkey(jogador.mover_direita(), "Right")
turtle.onkey(jogador.mover_fogo(), "space")

turtle.done()