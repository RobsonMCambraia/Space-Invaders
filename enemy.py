import turtle
import random
class Enemy():
    def __init__(self):
        self.number_of_enemies1 = 3
        self.number_of_enemies2 = 6
        self.number_of_enemies3 = 1

        self.enemyspeed = 5
        self.enemies1 = []
        self.enemies2 = []
        self.enemies3 = []

                
    def enemyListAppend(self):
        # Adicionar inimigos à lista
        for i in range(self.number_of_enemies1):
            self.enemies1.append(turtle.Turtle())
        for i in range(self.number_of_enemies2):
            self.enemies2.append(turtle.Turtle())
        for i in range(self.number_of_enemies3):
            self.enemies3.append(turtle.Turtle())
    
    def enemyConfig(self, inimigo1, inimigo2, inimigo3):
        # Registrar as formas
        turtle.register_shape(inimigo1)
        turtle.register_shape(inimigo2)
        turtle.register_shape(inimigo3)
        
        # Configuração dos inimigos
        for enemy1 in self.enemies1:
            enemy1.shape(inimigo1)
            enemy1.penup()
            enemy1.speed(0)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy1.setposition(x, y)
            
        for enemy2 in self.enemies2:
            enemy2.shape(inimigo2)
            enemy2.penup()
            enemy2.speed(0)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy2.setposition(x, y)
        
        for enemy3 in self.enemies3:
            enemy3.shape(inimigo3)
            enemy3.penup()
            enemy3.speed(0)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy3.setposition(x, y)
        
    def enemyMove(self):
        for enemy1 in self.enemies1:
            x = enemy1.xcor()
            x += self.enemyspeed
            enemy1.setx(x)

            # Verifique se o inimigo atingiu a borda
            if x > 280:
                y = enemy1.ycor()
                y -= 20
                enemy1.sety(y)
                self.enemyspeed *= -1
            if x < -280:
                y = enemy1.ycor()
                y -= 20
                enemy1.sety(y)
                self.enemyspeed *= -1
                
        for enemy2 in self.enemies2:
            x = enemy2.xcor()
            x -= self.enemyspeed
            enemy2.setx(x)

            # Verifique se o inimigo atingiu a borda
            if x > 280:
                y = enemy2.ycor()
                y -= 20
                enemy2.sety(y)
                self.enemyspeed *= -1
            if x < -280:
                y = enemy2.ycor()
                y -= 20
                enemy2.sety(y)
                self.enemyspeed *= -1
                
        for enemy3 in self.enemies3:
            x = enemy3.xcor()
            x -= self.enemyspeed
            enemy3.setx(x)

            # Verifique se o inimigo atingiu a borda
            if x > 280:
                y = enemy3.ycor()
                y -= 20
                enemy3.sety(y)
                self.enemyspeed *= -1
            if x < -280:
                y = enemy3.ycor()
                y -= 20
                enemy3.sety(y)
                self.enemyspeed *= -1