import pygame as pg
pg.init()

W, H = 1280, 720
sc = pg.display.set_mode((W, H))
pg.display.set_caption('MADE BY KLYMENKO & (А КУЦЕЛА ШО? СПИТЬ НАХУЙ ПРОСПАВ ВСІ ПАРИ)')
pg.display.set_icon(pg.image.load('logo/logo.png'))
bg = pg.image.load("sprites/bg.png")
ground = pg.image.load("sprites/ground.png")
idle = pg.image.load('sprites/idle.png')

pg.mixer.music.load('sounds/bgMountains1.mp3')
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)

running = True

clock = pg.time.Clock()
x = W // 2
y = 494
speed = 5
width = 60
height = 40

isJump = False
isJumping = False
standing = False
jumpCount = 10

walkRight = [pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png'), pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png'), pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png'), pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png')]
walkLeft = [pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png'), pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png'), pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png'), pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png')]
jumpUp = [pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png')]

left = False
right = True
animCount = 0


class Player:
    def __init__(self):
        self.body = walkRight
        self.hp = 100
        self.attack = 20

    def getDamage(self, damage):
        self.hp -= damage

    def giveDamage(self, who):
        who.hp -= self.attack


player = Player()


def drawWindow():
    global animCount
    sc.blit(bg, (0, 0))
    sc.blit(ground, (0, 650))

    if animCount + 1 >= 30:
        animCount = 0

    if right:
        player.body = walkRight
        sc.blit(player.body[animCount // 5], (x, y))
        animCount += 1
    elif left:
        player.body = walkLeft
        sc.blit(player.body[animCount // 5], (x, y))
        animCount += 1
    elif isJumping:
        player.body = jumpUp
        sc.blit(player.body[animCount // 5], (x, y))
        animCount += 1
    elif standing:
        player.body = idle
        sc.blit(player.body, (x, y))
        animCount += 1

    pg.display.update()


while running:
    clock.tick(30)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    if keys[pg.K_a] and x > 5:
        x -= speed
        left = True
        right = False
    elif keys[pg.K_d] and x < W - width - 5:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        standing = True
        animCount = 0

    if not isJump:
        if keys[pg.K_SPACE]:
            isJump = True
            isJumping = True
            left = False
            right = False
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
                isJumping = False
                left = False
                right = False
                standing = True
            else:
                y -= (jumpCount ** 2) / 2
                isJumping = True
                left = False
                right = False
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    drawWindow()

pg.quit()