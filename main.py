import pygame
import os
over=0
jumps=10
j=False
import random
score=0
q=750
t=random.randint(10,300)
t2=random.randint(10,200)
pygame.init()
screen = pygame.display.set_mode((q, q))
done = False
is_blue = True
x = 100
y = 30
GRAVITY=2
clock = pygame.time.Clock()
_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image
color = (255, 0, 0)

while not done:
        j=0
        px=x
        py=y
        rect1 = pygame.Rect((t,t2,52,52))
        rect2 = pygame.Rect(x, y, 50, 50)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: py-=3
        if pressed[pygame.K_s]: py += 3
        wc= pygame.Rect(px,py,50,50)
        for i in range(len(walls)):
          wall = wc.colliderect(walls[i])
          if wall:
            j+=1
            break
        if j!=0:
          if py<y:
            y=walls[i][1]+walls[i][3]
          else:
            y=walls[i][1]-walls[i][3]
        else:
          y=py
            
            
        j=0
        py=y
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_a]: px-=3
        if pressed[pygame.K_d]: px += 3
        wc= pygame.Rect(px,py,50,50)
        for i in range(len(walls)):
          wall = wc.colliderect(walls[i])
          if wall:
            j+=1
            break
        if j!=0:
          if px<x:
            x=walls[i][0]+walls[i][2]
          else:
            x=walls[i][0]-walls[i][2]
        else:
          x=px
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        screen.blit(get_image('ball.jpeg'), (x, y))
        collide = rect1.colliderect(rect2)
        if collide:
          score+=1
          t=random.randint(10,300)
          t2=random.randint(10,200)
          print(score)
        color = (255, 0, 0) if collide else (255, 255, 255)
        pygame.draw.rect(screen, color, rect1)
        pygame.draw.rect(screen, (0, 255, 0), rect2, 6, 1)
        for i in range(len(walls)):
          pygame.draw.rect(screen, "blue", walls[i])
        pygame.display.flip()
        clock.tick(60)