from pygame import *
from random import randint
from time import time as timer

#фоновая музыка


#шрифты и надписи
font.init()
font1 = font.SysFont("Arial", 36)
Player_L_lose = font1.render('Player_l Lose!', True, (0, 0, 0))
Player_R_lose = font1.render('Player_r Lose!', True, (0, 0, 0))
font2 = font.SysFont("Arial", 36)

# нам нужны такие картинки:

img_back = "fon.jpg" #фон
img_hero_l = "player_l.png"
img_hero_r = "player_r.png" # герой
img_ball = "ball.png"

# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def uprav_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
  # метод "выстрел" (используем место игрока, чтобы создать там пулю)
    def uprav_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

        
        # исчезает, если дойдет до края экрана
        
            

# класс спрайта-врага   


# класс спрайта-пули   


# Создаем окошко
win_width = 700
win_height = 500
display.set_caption("Ping Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# создаем спрайты
player_l = Player(img_hero_l, 15, win_height - 100, 15, 100, 10)
player_r = Player(img_hero_r, 665, win_height - 100, 15, 100, 10)
ball = GameSprite(img_ball, 350, win_height - 250, 75, 100, 15)

# переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
clock = time.Clock()
FPS = 120
# Основной цикл игры:
run = True # флаг сбрасывается кнопкой закрытия окна=
reload = False
speed_x = 5
speed_y = 5
while run:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            run = False
        # событие нажатия на пробел - спрайт стреляет
    if not finish:
        ball.rect.x += speed_x
        if ball.rect.y <0 or ball.rect.y > win_height-100:
            speed_y *= -1
        ball.rect.y += speed_y 
        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1     
       

        window.blit(background, (0,0))        
        if ball.rect.x <=0:
            window.blit(Player_L_lose, (250, 250))
            finish = True
        if ball.rect.x >= 625:
            window.blit(Player_R_lose, (250, 250))  
            finish = True 
        player_l.uprav_l()
        player_r.uprav_r()
        ball.reset()
        player_l.reset()
        player_r.reset()
        display.update()

        





        
    



        
   
         

        # пишем текст на экране


        # производим движения спрайтов
       

        # обновляем их в новом местоположении при каждой итерации цикла


        
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)
    clock.tick(FPS)