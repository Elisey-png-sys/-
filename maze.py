#создай игру "Лабиринт"!
# подключение 
import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("jungles.ogg")
pygame.mixer.music.play()


windown = pygame.display.set_mode((700,500))#создание экрана
fps = pygame.time.Clock()#создание фпс

fon = pygame.image.load("background.jpg")
fon = pygame.transform.scale(fon, (700,500))

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, visota, shirina, x,y, speed):
        super().__init__()
        self.img_sprite = pygame.image.load(image)
        self.img_sprite = pygame.transform.scale(self.img_sprite,(visota,shirina))

        self.hitbox = self.img_sprite.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y

        self.move = ""

        self.speed = speed
    def show(self):
        windown.blit(self.img_sprite, self.hitbox)

     
class  GamePlayer(GameObject):
    def ypravlenie(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]  and self.hitbox.y > 0:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s]   and self.hitbox.y < 450:
            self.hitbox.y +=  self.speed
        if keys[pygame.K_d] and self.hitbox.x < 650:
            self.hitbox.x += self.speed
        if keys[pygame.K_a] and self.hitbox.x > 0:
            self.hitbox.x -= self.speed

class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_x,wall_y, wall_shirina,wall_visota, wall_r, wall_g, wall_b):
        super().__init__()
        self.wall_shirina = wall_shirina
        self.wall_visota = wall_visota
        self.wall_r = wall_r
        self.wall_g = wall_g
        self.wall_b = wall_b

        self.wall_image = pygame.Surface((self.wall_shirina, self.wall_visota))
        self.wall_image.fill((self.wall_r,self.wall_g,self.wall_b))

        self.wall_hitdox = self.wall_image.get_rect()
        self.wall_hitdox.x = wall_x
        self.wall_hitdox.y = wall_y


    def show(self):
        windown.blit(self.wall_image, self.wall_hitdox)

class Enemi(GameObject):
    def forward(self):
        if self.hitbox.x <= 470:
            self.move = "parvo"
        if self.hitbox.x > 600:
            self.move = "levo"
    
        if self.move == 'levo':
            self.hitbox.x -= self.speed
        else:
            self.hitbox.x += self.speed
    


player = GamePlayer("hero.png",60, 60, 20, 40, 5)
vrag = Enemi("cyborg.png",60, 60, 600, 300, 5)
gold = GameObject("treasure.png",60, 60, 600, 400, 5)
run = True
w1 = Wall(100,100,200,10,123,123,123)
w2 = Wall(300,100,10,200,123,123,123)
w3 = Wall(300,150,10,200,123,123,123)
w4 = Wall(300,300,10,200,123,123,123)
w5 = Wall(400,100,200,10,123,123,123)
w6 = Wall(500,100,200,10,123,123,123)
w7 = Wall(400,100,10,300,123,123,123)
w8 = Wall(500,400,50,10,123,123,123)
w9 = Wall(500,400,200,10,123,123,123)
w10 = Wall(500,200,10,200,123,123,123)
while run:
    for  i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False


    windown.blit(fon,(0,0))
    player.show()
    vrag.show()
    gold.show()
    player.ypravlenie()
    vrag.forward()
    w1.show()
    w2.show()
    w3.show()
    w4.show()
    w5.show()
    w6.show()
    w7.show()
    w8.show()
    w9.show()
    w10.show()
    
    if player.hitbox.colliderect(w1.wall_hitdox)  or player.hitbox.colliderect(w2.wall_hitdox)  or player.hitbox.colliderect(w3.wall_hitdox)  or player.hitbox.colliderect(w4.wall_hitdox)  or player.hitbox.colliderect(w5.wall_hitdox)  or player.hitbox.colliderect(w6.wall_hitdox)  or player.hitbox.colliderect(w7.wall_hitdox)  or player.hitbox.colliderect(w8.wall_hitdox)  or player.hitbox.colliderect(w9.wall_hitdox)  or player.hitbox.colliderect(w10.wall_hitdox):
        player.hitbox.x = 20 
        player.hitbox.y =  400
    

    if player.hitbox.colliderect(vrag.hitbox):
        run = False


    pygame.display.update()
    fps.tick(60)












