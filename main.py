import pygame
import math
import os
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)
over=0
jumps=10
j=False
import random
score=0
q=1000
t=random.randint(10,11)
t2=random.randint(10,13)
pygame.init()
screen = pygame.display.set_mode((q, q))
done = False
is_blue = True
x = 400
y = 400
GRAVITY=2
cooldown=15
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
walls=[]
lc=[1,1,1]
go=False
johnm="jf.png"
points=0
spawn=300
up=0
eni=[]
while not done:
        up+=1
        if cooldown!=15:
          cooldown+=1
        bg = pygame.image.load("grass.png")
        text_surface = my_font.render(str(points), True, (200, 200, 200))
        text_surface2 = my_font.render('Score: ', True, (200, 200, 200))
        text_surface3 = my_font.render('GAME OVER', True, (255, 0, 0))
        
        j=0
        px=x
        py=y
        rect1 = pygame.Rect((t,t2,52,52))
        rect2 = pygame.Rect(x+10, y, 50, 190)
        nrec=pygame.Rect((t,t2,52,52))
        yoyo=pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1], 12, 12)
        goscree = pygame.Rect(0, 0, 1000, 1000)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: 
          py-=5
          johnm="jb.png"
        if pressed[pygame.K_s]:
          py += 5
          johnm="jf.png"
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
        if pressed[pygame.K_a]:
          px-=5
          johnm="jl.png"
        if pressed[pygame.K_d]:
          px += 5
          johnm="jr.png"
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
        screen.blit(get_image('grass.png'),(0,0))
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        screen.blit(get_image(johnm), (x, y))
        for i in range(len(lc)):
          if lc[i] == 1:
            screen.blit(get_image('life.png'),(i*25,0))
          else:
            screen.blit(get_image('nolife.png'),(i*25,0))
        screen.blit(get_image('yoyo.png'),pygame.mouse.get_pos())
        yyh = yoyo.colliderect(rect1)
        collide = rect1.colliderect(rect2)
        if collide:
          for i in range(len(lc)-1,-1,-1):
            if lc[i]==1:
              lc[i]=0
              break
          if lc[0]!=1:
            go=True
          c=nrec.colliderect(rect2)
          while c:
            t=random.randint(10,300)
            t2=random.randint(10,200)
            nrec=pygame.Rect((t,t2,52,52))
            c=nrec.colliderect(rect2)
        color = (255, 0, 0) if collide else (255, 255, 255)
        if yyh and cooldown==15:
          points+=1
          print(points)
          color=(0,255,0)
          spzc=random.randint(1,4)
          if spzc==1:
            t=random.randint(10,990)
            t2=random.randint(10,100)
          elif spzc==2:
            t2=random.randint(10,990)
            t=random.randint(10,200)
          elif spzc==3:
            t2=random.randint(10,990)
            t=random.randint(790,990)
          elif spzc==4:
            t=random.randint(10,990)
            t2=random.randint(790,990)
          nrec=pygame.Rect((t,t2,52,52))
          c=nrec.colliderect(rect2)
          while c:
            if spzc==1:
              t=random.randint(10,990)
              t2=random.randint(10,100)
            elif spzc==2:
              t2=random.randint(10,990)
              t=random.randint(10,200)
            elif spzc==3:
              t2=random.randint(10,990)
              t=random.randint(790,990)
            elif spzc==4:
              t=random.randint(10,990)
              t2=random.randint(790,990)
            nrec=pygame.Rect((t,t2,52,52))
            c=nrec.colliderect(rect2)
            cooldown=0
        m=math.sqrt((y-t2)*(y-t2)+(x-t+10)*(x-t+10))
        m2=m/10
        my=(y-t2)/m2
        mx=(x-t+10)/m2
        t+=mx
        t2+=my
        print(mx,my)
        pygame.draw.rect(screen, color, rect1)
        screen.blit(text_surface2, (0,20))
        screen.blit(text_surface, (70,20))
        if go==True:
          pygame.draw.rect(screen, (255, 255, 255), goscree, 10000)
          screen.blit(text_surface3,(400,400))
        for i in range(len(walls)):
          pygame.draw.rect(screen, "blue", walls[i])
          
        pygame.display.flip()
        clock.tick(60)