import turtle
import random
import time
from player import Player
from display import Display
from enemy import Enemy

# Instancia das classes
jogador = Player()
visor = Display()
inimigo = Enemy()

#Inicialização do visor
visor.telaConfig()
visor.desenharBorda()
visor.placarScore()

turtle.listen()
jogador.configFogo()

#Inicialização dos inimigos
inimigo.enemyListAppend()
inimigo.enemyConfig()
inimigo.enemyMove()

# Configurar os ouvintes de eventos do teclado
turtle.onkey(jogador.mover_esquerda(), "Left")
turtle.onkey(jogador.mover_direita(), "Right")
turtle.onkey(jogador.mover_fogo(), "space")

turtle.mainloop()
turtle.done()