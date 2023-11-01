import turtle
import random
class Enemy():
    def __init__(self, dict_enemy_1, dict_enemy_2, dict_enemy_3):
        self.config_enemy_1 = dict_enemy_1 
        self.config_enemy_2 = dict_enemy_2 
        self.config_enemy_3 = dict_enemy_3 
        
        self.enemyspeed = 5
        self.enemies1 = []
        self.enemies2 = []
        self.enemies3 = []
        
        self.number_of_enemies()
        self.enemyListAppend()
        self.enemyConfig()
        self.enemyMove()
        
    def number_of_enemies(self):
        self.number_of_enemies1 = self.config_enemy_1["quantidade"]
        self.number_of_enemies2 = self.config_enemy_2["quantidade"]
        self.number_of_enemies3 = self.config_enemy_3["quantidade"]
        
    def enemyListAppend(self):
        # Adicionar inimigos à lista
        for i in range(self.number_of_enemies1):
            self.enemies1.append(turtle.Turtle())
        for i in range(self.number_of_enemies2):
            self.enemies2.append(turtle.Turtle())
        for i in range(self.number_of_enemies3):
            self.enemies3.append(turtle.Turtle())
    
    def enemyConfig(self):
        # Registrar as formas
        turtle.register_shape(self.config_enemy_1["caminho_shape"])
        turtle.register_shape(self.config_enemy_2["caminho_shape"])
        turtle.register_shape(self.config_enemy_3["caminho_shape"])
        
        # Configuração dos inimigos
        for enemy1 in self.enemies1:
            enemy1.shape(self.config_enemy_1["caminho_shape"])
            enemy1.penup()
            enemy1.speed(0)
            x = random.randint(self.config_enemy_1["x_random_1"], self.config_enemy_1["x_random_2"])
            y = random.randint(self.config_enemy_1["y_random_1"], self.config_enemy_1["y_random_2"])
            enemy1.setposition(x, y)
            
        for enemy2 in self.enemies2:
            enemy2.shape(self.config_enemy_2["caminho_shape"])
            enemy2.penup()
            enemy2.speed(0)
            x = random.randint(self.config_enemy_2["x_random_1"], self.config_enemy_2["x_random_2"])
            y = random.randint(self.config_enemy_2["y_random_1"], self.config_enemy_2["y_random_2"])
            enemy2.setposition(x, y)
        
        for enemy3 in self.enemies3:
            enemy3.shape(self.config_enemy_3["caminho_shape"])
            enemy3.penup()
            enemy3.speed(0)
            x = random.randint(self.config_enemy_3["x_random_1"], self.config_enemy_3["x_random_2"])
            y = random.randint(self.config_enemy_3["y_random_1"], self.config_enemy_3["y_random_2"])
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