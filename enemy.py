from settings import*
from images import*
from display import *
from sounds import *

pg.init()


class Enemy:
    def __init__(self):
        self.body = idleEnemy
        self.hp = 100
        self.attack = 20
        self.x = screenWidth // 2
        self.y = 494
        self.speed = PLAYER_SPEED
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.isJump = False
        self.isJumping = False
        self.standing = True
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.animCount = 0

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.x > 5:
            self.x -= self.speed
            self.left = True
            self.right = False
        elif keys[pg.K_RIGHT] and self.x < screenWidth - self.width - 5:
            self.x += self.speed
            self.left = False
            self.right = True
        else:
            self.left = False
            self.right = False
            self.standing = True
            self.animCount = 0

        if not self.isJump:
            if keys[pg.K_UP]:
                self.isJump = True
                self.isJumping = True
                self.left = False
                self.right = False
        else:
            if self.jumpCount >= -10:
                if self.jumpCount < 0:
                    self.y += (self.jumpCount ** 2) / 2
                    self.isJumping = False
                    self.left = False
                    self.right = False
                    self.standing = True
                else:
                    self.y -= (self.jumpCount ** 2) / 2
                    self.isJumping = True
                    self.left = False
                    self.right = False
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

        if self.animCount + 1 >= 30:
            self.animCount = 0

        if self.right:
            self.body = walkRightEnemy
            sc.blit(self.body[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
        elif self.left:
            self.body = walkLeftEnemy
            sc.blit(self.body[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
        elif self.isJumping:
            self.body = jumpUpEnemy
            sc.blit(self.body[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
        elif self.standing:
            self.body = idleEnemy
            sc.blit(self.body[self.animCount // 5], (self.x, self.y))
            self.animCount += 1
