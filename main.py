import pygame as pg
from HC_SR04 import ping
pg.init()
pg.display.set_caption('Ultrasonic Pong')
WIN_X, WIN_Y = 800, 800
window = pg.display.set_mode((WIN_X, WIN_Y))
clock = pg.time.Clock()

class Paddle:
    def __init__(self, player):
        self.rects = []
        self.speed = 12
        for i in range(4):
            if player == "left":
                self.rects.append(pg.Rect(32, (int(WIN_Y / 2)) - 64 + (i * 32), 32, 32))
            elif player == "right":
                self.rects.append(pg.Rect(WIN_X - 64, (int(WIN_Y / 2)) - 64 + (i * 32), 32, 32))
    def setY(self, y):
        for i in range(len(self.rects)):
            self.rects[i].y = (WIN_Y - (y*16 + (i * 32))) % WIN_Y

class Ball:
    def __init__(self):
        self.rect = pg.Rect(int(WIN_X / 2), int(WIN_Y / 2), 32, 32)
        self.dir = [1, -1]
        self.speed = 2
    def move(self):
        self.rect.x += self.dir[0] * self.speed
        self.rect.y += self.dir[1] * self.speed
    def checkCollide(self, paddles):
        for i in range(len(paddles)):
            for j in range(len(paddles[i].rects)):
                collides = self.rect.colliderect(paddles[i].rects[j])
                #bottom collision weird things happen
                if collides and self.dir == [1, -1]:
                    self.dir = [-1, -1]
                    self.rect.x -= self.speed
                elif collides and self.dir == [-1, -1]:
                    self.dir = [1, -1]
                    self.rect.x += self.speed
                elif collides and self.dir == [1, 1]:
                    self.dir = [-1, 1]
                    self.rect.x -= self.speed
                elif collides and self.dir == [-1, 1]:
                    self.dir = [1, 1]
                    self.rect.x += self.speed
                if self.rect.right > WIN_X or self.rect.x < 0:
                    quit()
                if self.rect.bottom > WIN_Y or self.rect.y < 0:
                    self.dir[1] *= -1
                    self.rect.y += self.speed * self.dir[1]
                if collides:
                    self.speed += 1

def draw(paddles, balls):
    window.fill([0,0,0])
    for i in range(len(paddles)):
        for j in range(len(paddles[i].rects)):
            pg.draw.rect(window, (255,255,255), paddles[i].rects[j])
    for i in range(len(balls)):
        pg.draw.rect(window, (255,255,255), balls[i].rect)
    pg.display.update()

def main():
    paddleP1 = Paddle("left")
    paddleP2 = Paddle("right")
    paddles = [paddleP1, paddleP2]
    ball = Ball()
    balls = [ball]
    while 1:
        draw(paddles, balls)
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                quit()
        paddleP1.setY(ping(True))
        paddleP2.setY(ping(False))
	for ball in balls:
	    ball.move()
            ball.checkCollide(paddles)
        clock.tick(60)
	if pg.time.get_ticks() % 600 == 0:
	    balls.append(Ball())

if __name__ == '__main__':
    main()
