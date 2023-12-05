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
    "score": 0,
    "speed": 0,
    "color": "red",
    "position_x": -290,
    "position_y": 270}

score = placar_score["score"]
text_score_fim = f"Game over!\nScore:\t{score}"

game_over = {
    "speed": 0,
    "color": "red",
    "position_x": 0,
    "position_y": 0,
    "text": text_score_fim}

display = Display(border_settings, placar_score, game_over)

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

config_inimigo_1 = {
    "quantidade": 8,
    "caminho_shape": "src/inimigo-1.gif",
    "x_random_1": -250,
    "x_random_2": 250,
    "y_random_1": 50,
    "y_random_2": 120
}
config_inimigo_2 = {
    "quantidade": 4,
    "caminho_shape": "src/inimigo-2.gif",
    "x_random_1": -250,
    "x_random_2": 250,
    "y_random_1": 150,
    "y_random_2": 220
}
config_inimigo_3 = {
    "quantidade": 2,
    "caminho_shape": "src/inimigo-3.gif",
    "x_random_1": -250,
    "x_random_2": 250,
    "y_random_1": 230,
    "y_random_2": 280
}

inimigo = Enemy(config_inimigo_1, config_inimigo_2, config_inimigo_3)

turtle.listen()

# Configurar os ouvintes de eventos do teclado
turtle.onkey(jogador.mover_esquerda, "Left")
turtle.onkey(jogador.mover_direita, "Right")
turtle.onkey(jogador.mover_fogo, "space")

while True:
    inimigo.enemyMove()


turtle.done()