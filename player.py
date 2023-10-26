class Player:
    # Função que inicializa e configura o player
    def configPlayer():
        turtle.register_shape("player (1).gif")

        # Criar a tartaruga do jogador
        player = turtle.Turtle()
        player.shape("player (1).gif")
        player.penup()
        player.speed(0)
        player.setposition(0, -250)
        player.setheading(90)

        playerspeed = 15
    # Função para mover o jogador para a esquerda
    def mover_esquerda():
        x = player.xcor()
        if x >= -250:
            x -= playerspeed
        player.setx(x)
        fogo.setx(x)
        
    # Função para mover o jogador para a direita
    def mover_direita():
        x = player.xcor()
        if x <= 250:
            x += playerspeed
        player.setx(x)
        fogo.setx(x)