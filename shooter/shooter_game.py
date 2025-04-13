from pygame import *  
from random import randint
window = display.set_mode((700, 500))
display.set_caption('Шутер')
galaxy = transform.scale(image.load("galaxy.jpg"), (700, 500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
clock = time.Clock()
x =  200
y = 200

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__() 
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed) 
    def dvish(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= 5
        if keys_pressed[K_RIGHT] and self.rect.x < 595:
            self.rect.x += 5
    def fire(self):
        global pulki
        pulki = sprite.Group()
        bulli = Bullet('bullet.png', self.rect.x, self.rect.y, 5)
        bullets.add(bulli)
  
lost = 0 
class Enemy(GameSprite):
    def update(self):
        if self.rect.y >= 500:   
            self.rect.y = 0
            self.rect.x = randint(0, 500) 
            global number
        elif self.rect.y < 500:  
            self.rect.y += self.speed 
            
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.playerx = player_x
    def update(self):
        if self.rect.y >= 0:
            self.rect.y -= 3
        if self.rect.y < 0:
            self.kill()
font.init()
font1 = font.SysFont('Arial', 36)

bullets = sprite.Group()
monsters = sprite.Group()

plari = Player('rocket.png', 200, 400, 4)
for i in range(5):
    enemi = Enemy('ufo.png', randint(0, 500), 0, 2)
    monsters.add(enemi)

game = True
while game:
    window.blit(galaxy,(0, 0))
    text_lose = font1.render('Счет:' + str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (50, 50))
    text_lose = font1.render('Пропущено:' + str(lost), 1, (255, 255, 255))
    window.blit(text_lose, (50, 90))
    keys_pressed = key.get_pressed()
    if keys_pressed[K_SPACE]:
        plari.fire()

    sprites_list = sprite.groupcollide(monsters, bullets, True, True)
    if len(sprites_list)!= 0:
        enemi = Enemy('ufo.png', randint(0, 500), 0, 2)
        monsters.add(enemi)
    for e in event.get():
        if e.type == QUIT:
            game = False 


    plari.reset()
    plari.dvish()
    monsters.update()
    monsters.draw(window)
    bullets.update()
    bullets.draw(window)
    display.update()
clock.tick(60)