#подключение библеотек
from pygame import * 

#класс для создания персонажей
class GameSprite(sprite.Sprite):

#пораметры для персонажей
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#подкласс для передвижения героя
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

#создание окна и его пораметры
back = (250, 231, 181)
win_width = 1200
win_height = 800
window = display.set_mode((win_width, win_height))
window.fill(back)

#флаги, отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

#создание игроков
raketL = Player('bob2.4.png', 10, 200, 15, 120, 170)
raketR = Player('bob1.2.png', 1080, 200, 15, 120, 170)
#создание мяча
ball = GameSprite('boll1.png', 200, 200, 15, 50, 50)

font.init()
font = font.Font(None, 35)
#победа того или иного игрока
lose2 = font.render("Пепельный молодец!", True, (1, 121, 111))
lose1 = font.render('Чёрный молодец!', True, (25, 25, 112))

speed_x = 10
speed_y = 10

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
#вывод на экран всех героев
    if finish != True:

        window.fill(back)
        raketL.update_l()
        raketR.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        
        if sprite.collide_rect(raketL, ball) or sprite.collide_rect(raketR, ball):
            speed_x *= -1
            speed_y *= 1
        
        #если мяч достигает границ экрана, меняем направление его движения
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        
#если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (460, 410))
            game_over = True
        
#если мяч улетел дальше ракетки, выводим условие проигрыша для второго игрока
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (460, 410))
            game_over = True
        
        raketL.reset()
        raketR.reset()
        ball.reset()
        

    display.update()
    clock.tick(FPS)
