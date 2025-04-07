import pygame as pg
from random import randint
from time import sleep

pg.init()

#створ вікна
window_width = 1600
window_height = 900
backgraund = pg.transform.scale(pg.image.load("istockphoto-470309868-612x612.png"), (window_width, window_height))
window = pg.display.set_mode((window_width, window_height))
window.blit(backgraund, (0, 0))

class Apple(pg.sprite.Sprite):
    def __init__(self, filename, x, y, width, height):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(filename), (width, height))
        # створ хітбоксу і мал на нїому  
        self.rect = self.image.get_rect()
        self.rect.x = x    
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x , self.rect.y))

    def teleport(self):
        self.rect.x = randint(0,(window_width - self.rect.width))
        self.rect.y = randint(0,(window_height - self.rect.height))

#створення змії
class Snake:
    def __init__(self, x, y, size, color=(50, 255, 50)):
        self.rect = pg.Rect(x, y, size, size)
        self.size = size
        self.color = color
        self.direction = "right"
        self.step = 3
        self.last_pos = [x, y]

    def draw(self):
        pg.draw.rect(window, self.color, self.rect)

    def goto(self, x, y,):
        self.last_pos = [self.rect.x, self.rect.y]
        self.rect.x = x
        self.rect.y = y

def move(x, y):
    lx, ly =x, y
    for s in snakes:
        s.goto(lx, ly)
        lx, ly = s.last_pos[0], s.last_pos[1]

def level2():
    return pg.transform.scale(pg.image.load("phon2.jpg"), (window_width, window_height))

def level3():
    return pg.transform.scale(pg.image.load("satan.jpg"), (window_width, window_height))

def level4():
    return pg.transform.scale(pg.image.load("phon4.png"), (window_width, window_height))

SIZE = 40
apple = Apple("apple2.png", 0, 0, SIZE, SIZE)
apple.teleport()

apple2 = Apple("apple2.png", 0, 0, SIZE, SIZE)
apple2.teleport()

apple3 = Apple("apple2.png", 0, 0, SIZE, SIZE)
apple3.teleport()

apple4 = Apple("apple2.png", 0, 0, SIZE, SIZE)
apple4.teleport()

bomb = Apple("bomb.png", 0, 0, SIZE, SIZE)
bomb.teleport()

bomb2 = Apple("bomb.png", 0, 0, SIZE, SIZE)
bomb2.teleport()

snakes = []
head = Snake(100, 100, SIZE, (100, 255, 255))
snakes.append(head)

score = 0
f = pg.font.SysFont("Arial", 30)
score_label = f.render("Кредити:", True, (0, 100, 75))
score_text = f.render(str(score), True, (0, 100, 75))


#ігровий цикл
exit = False
while not exit:
    pg.time.delay(5)

    window.blit(backgraund, (0, 0))



#підключення клавіш і перевірка в яку сторону вона йде
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                if head.direction != "down":
                     head.direction = "up"

            if event.key == pg.K_d:
                if head.direction != "left":
                     head.direction = "right"

            if event.key == pg.K_a:
                if head.direction != "right":
                     head.direction = "left"

            if event.key == pg.K_s:
                if head.direction != "up":
                     head.direction = "down"
                     #break

    if apple.rect.colliderect(head.rect):
        score += 1
        apple.teleport()
        score_text = f.render(str(score), True, (100, 100, 100))

    if apple2.rect.colliderect(head.rect):
        score += 1
        apple2.teleport()
        score_text = f.render(str(score), True, (100, 100, 100))

    if apple3.rect.colliderect(head.rect):
        score += 1
        apple3.teleport()
        score_text = f.render(str(score), True, (100, 100, 100))

    if apple4.rect.colliderect(head.rect):
        score += 1
        apple4.teleport()
        score_text = f.render(str(score), True, (100, 100, 100))

        for _ in range(20):
            last_pos = snakes[-1].last_pos
            snakes.append(Snake(last_pos[0], last_pos[1], SIZE))

    if bomb.rect.colliderect(head.rect):
        score -= 1
        bomb.teleport()
        score_text = f.render(str(score), True, (100, 100, 100))



    if bomb2.rect.colliderect(head.rect):
        score -= 1
        bomb.teleport()
        score_text = f.render(str(score), True, (100, 100, 100))

    
    for snake in snakes:
        if head.rect.colliderect(snake.rect) and snakes.index(snake) >= head.size * 10:
            text = pg.font.SysFont("Arial", 100).render("You lose!", True, (0, 0, 0))
            window.blit(text, (800, 800))
            snake.color = (255, 100, 100)
            exit = True
        snake.draw()

    if score >= 4 and score < 5:
        backgraund = level2()
        head.step = 5

    if score >= 9 and score < 10:
        backgraund = level3()
        head.step = 10
        
    if score >= 14 and score < 15:
        backgraund = level4()
        head.step = 10






    if head.direction == "up":
        move(head.rect.x, head.rect.y - head.step)
    elif head.direction == "down":
        move(head.rect.x, head.rect.y + head.step)
    elif head.direction == "left":
        move(head.rect.x - head.step, head.rect.y)
    elif head.direction == "right":
        move(head.rect.x + head.step, head.rect.y)  

    window.blit(score_text, (100, 0))
    window.blit(score_label, (0, 0)) 

    if head.rect.y + head.rect.height > window_height or head.rect.y < 0 or head.rect.x + head.rect.width > window_width or head.rect.x < 0:
        text = pg.font.SysFont("Arial", 200).render("You lose!", True, (0, 0, 0))
        window.blit(text, (500, 350))
        exit = True


    head.draw()
    
    apple.draw()

    bomb.draw()

    apple2.draw()

    bomb2.draw()

    apple3.draw()

    apple4.draw()


    if randint(0, 50) == 0:
        bomb2.teleport()

    if randint(0, 50) == 0:
        bomb.teleport()

    pg.display.update()
sleep(3)
                                                                                                                                                                                                                