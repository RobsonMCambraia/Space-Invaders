import turtle
import random
import time
from player import Player
from display import Display
from enemy import Enemy
from fire import Fire

# Instancia das classes
jogador = Player()
visor = Display()
fogo = Fire()
inimigo = Enemy()

#Inicialização do visor
visor.telaConfig()
visor.desenharBorda()
visor.placarScore()

# Configurar os ouvintes de eventos do teclado
turtle.listen()
turtle.onkey(jogador.mover_esquerda(), "Left")
turtle.onkey(jogador.mover_direita(), "Right")
turtle.onkey(mover_fogo, "space")

turtle.done()