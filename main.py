import turtle
import random
import time
import player
import display
import enemy
import fire

# Configurar a janela do jogo
window = turtle.Screen()

# Instancia das classes
jogador = player()



# Configurar os ouvintes de eventos do teclado
turtle.listen()
turtle.onkey(jogador.mover_esquerda(), "Left")
turtle.onkey(jogador.mover_direita(), "Right")
turtle.onkey(mover_fogo, "space")

turtle.done()