from pygame import *
from random import *
from time import sleep
init()

#######################################
                                      #
font.init()                           #
font = font.SysFont('Arial', 27)      #
                                      #
#######################################

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sizex, sizey, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (sizex, sizey)) 
        self.speed = player_speed


        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):

    def update(self):

        keys=key.get_pressed()
        if keys[K_a]:
            self.rect.x=self.rect.x - self.speed
        if keys[K_d]:
            self.rect.x=self.rect.x + self.speed
        if keys[K_SPACE]:
            self.rect.y=self.rect.y - self.speed
        if keys[K_s]:
            self.rect.y=self.rect.y + self.speed

        if self.rect.x >= win_width-75:
            self.rect.x = win_width - 80

        if self.rect.x <= -5:
            self.rect.x = 0

        if self.rect.y >= win_heigth-75:
            self.rect.y = win_heigth-80

        if self.rect.y <= 0:
            self.rect.y = win_heigth-75


    def fire(self):
        bul = Pulya('Pulya.png', self.rect.x, self.rect.y, 17, 17, sila) #ПУЛЬКА
        buli.add(bul)



class Enemy(GameSprite):
    def update(self):
        self.rect.y += randint(-12, 12)
        self.rect.x += randint(-12, 12)
        global lost
        if self.rect.y >= (win_heigth-50):
            self.rect.y = randint(40, win_width-100)
        if self.rect.y <= (50):
            self.rect.y = randint(40, win_width-100)
        if self.rect.x >= (win_width-50):
            self.rect.x = randint(40, win_width-100)
        if self.rect.x <= (50):
            self.rect.x = randint(40, win_width-100)
            


class Pulya(GameSprite):
    def update (self):
        self.rect.x = self.rect.x + self.speed
        if (self.rect.x > win_width):
            self.kill()



class Walls(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        
        sprite.Sprite.__init__(self)
        self.color_1=color_1
        self.color_2=color_2
        self.color_3=color_3
        self.width = wall_width
        self.height = wall_height
        
        self.image = Surface([self.width,self.height])
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        draw.rect(window,(self.color_1,self.color_2,self.color_3),(self.rect.x,self.rect.y,self.width, self.height))


########################################################################################################


speed = 5
x_speed = 5
y_speed = 5
sila = 10
imgl = 'Bgck.png'

win_width = 1125
win_heigth = 675
window = display.set_mode((win_width,win_heigth))
background = transform.scale(image.load(imgl), (win_width*2, win_heigth))



display.set_caption("Аркадо!")



heigth = 60
width = 40
x = 5
y = 500 - heigth - 5


draw.rect(window, (0, 0, 255), (x, y, width, heigth))

me = Player('iui.png', 5, win_heigth - 80, 80, 85, speed)

bulya = Pulya('Pulya.png', 80, 80, 80, 80, 2)

sprites = sprite.Group()

health = 3
lost = 0
score = 0 


for i in range(0, 4):
    vrag = Enemy('vrg.png', randint(50, win_width-75), randint(100, win_heigth-100), 80, 80, randint(1, 3))
    sprites.add(vrag)

buli = sprite.Group()
tpshki = sprite.Group()
ships = sprite.Group()
hilka = sprite.Group()

w1 = Walls(0, 175, 255, 200, 550, 150, 25)
tpshki.add(w1)
s2 = Walls(255, 50, 50, 550, 425, 200, 35)
ships.add(s2)
w3 = Walls(0, 175, 255, 850, 475, 125, 50)
tpshki.add(w3)
w4 = Walls(0, 175, 255, 700, 250, 250, 75)
tpshki.add(w4)
w5 = Walls(0, 175, 255, 275, 325, 100, 100)
tpshki.add(w5)
w6 = Walls(0, 175, 255, 100, 100, 70, 250)
tpshki.add(w6)
s1 = Walls(255, 50, 50, 300, 175, 275, 35)
ships.add(s1)
w8 = Walls(0, 175, 255, 700, 95, 100, 35)
tpshki.add(w8)
w9 = Walls(0, 175, 255, 575, 550, 175, 35)
tpshki.add(w9)
h1 = Walls(0, 255, 50, randint(20, win_width-20), randint(20, win_heigth-20), 25, 25)
hilka.add(h1)



#################################################################################################################


run = True
while run:

    window.fill((200, 200, 255))
    window.blit(background, (0, 0))



    me.update()
    buli.update()
    sprites.update()


    me.reset()
    buli.draw(window)
    sprites.draw(window)
    tpshki.draw(window)
    ships.draw(window)
    hilka.draw(window)


###ТЕКСТ###
    text = font.render("Счет: " + str(score), 1, (0, 255, 0))
    window.blit(text, (7, 17))# - здесь два числа это координаты

#    text_lose = font.render("Пропущено: " + str(lost), 1, (255, 0, 0))
#    window.blit(text_lose, (10, 50))

    text_hp = font.render("Осталось Hp: " + str(health), 1, (255, 0, 115))
    window.blit(text_hp, (13, 83))
###ТЕКСТ###


    collides = sprite.groupcollide(sprites, buli, True, True)

    scale = randint(75, 125)


    for i in collides:

        vrag = Enemy('vrg.png', randint(100, win_width-100), randint(100, win_heigth-100), scale, scale, randint(1, 3))
        sprites.add(vrag)
       
        score = score + 1

    if sprite.spritecollide(me, sprites, True):
        health = health - 1
        vrag = Enemy('vrg.png', randint(100, win_width-100), randint(100, win_heigth-100), scale, scale, randint(1, 3))
        sprites.add(vrag)


    platforms_touched = sprite.spritecollide(me, tpshki, False)
    for p in platforms_touched:
        s = [p.rect.right, p.rect.left - 80] #эта и следующие строчки, для того, чтобы телепортироваться на другую 
        me.rect.x = s[randint(0,1)]      #строну платформы
        #me.rect.x = me.rect.x + randint(-2,2) # вот это для того, чтобы смещаться на случайное число 
        #                                       от -2 до 2 относительно текущей координаты


    if sprite.spritecollide(me, hilka, True):
        h1 = Walls(0, 255, 50, randint(20, win_width-20), randint(20, win_heigth-20), 25, 25)
        hilka.add(h1)
        health += 1

    if sprite.spritecollide(me, ships, False):
        health -= 0.1


    timer = 0
    if health <= 0:
        background = transform.scale(image.load('dize.png'), (win_width, win_heigth))
        window.blit(background, (0, 0))
        sleep (5)
        run = False


    if health >= 7:
        background = transform.scale(image.load('volo.png'), (win_width, win_heigth))
        window.blit(background, (0, 0))
        sleep (5)
        run = False

    if score >= 25:
        background = transform.scale(image.load('volo.png'), (win_width, win_heigth))
        window.blit(background, (0, 0))

    if score >= 30:
        run = False



    time.delay(3)
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                sila = 10
                me.fire()
                sila = 11
                me.fire()
            if e.button == 3:       
                sila = -10
                me.fire()
                sila = -11
                me.fire()

        if e.type == QUIT:
            run = False



    display.update()



































##_типа_недопасхалка_##
a = 255
b = 0
c = 115
mandarinka = (a,b,c)
##_недолайфхак_с_цветами_ ;) _##