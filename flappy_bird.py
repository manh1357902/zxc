import pygame
import random


pygame.init()
#bắt đầu
start = 0
start2 =0
start_1=0
check_1=0
check_2= 0
check_3=0
check_4=0
game_over = 0
game_over_2 = 0
game_over_3=0
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks() - pipe_frequency
last_pipe_2 = pygame.time.get_ticks() - pipe_frequency
p_pass = 0
p_pass_2 = 0
score = 0
score2 = 0
#màn hình
width = 1200
height = 900
displaysurf = pygame.display.set_mode((width,height))
font = pygame.font.SysFont('Bauhaus 93', 60)
#set up tên cửa sổ
pygame.display.set_caption('Flappy Bird')
#background + sàn
floor = pygame.image.load('img/ground.png')
floor = pygame.transform.scale(floor,(width+70,168))
floor_1 = pygame.transform.scale(floor,(width//2+70,168))
floor_move =0
floor_move_2=width//2
background = pygame.image.load('img/bg.png')
background = pygame.transform.scale(background,(width,height)) 
botton_load = pygame.image.load('img/restart.png')
botton_1 = pygame.image.load('img/1player.png')
botton_1 = pygame.transform.scale(botton_1,(160,100))
botton_2 = pygame.image.load('img/2player.png')
botton_2 = pygame.transform.scale(botton_2,(160,100))
#âm thanh
bird_wing = pygame.mixer.Sound('sound/sfx_wing.wav')
bird_point = pygame.mixer.Sound('sound/sfx_point.wav')
bird_point_2 = pygame.mixer.Sound('sound/sfx_point.wav')
bird_hit = pygame.mixer.Sound('sound/sfx_hit.wav')
bird_hit_2 = pygame.mixer.Sound('sound/sfx_hit.wav')
#Chim
class Bird(pygame.sprite.Sprite) :
    def __init__(self,x,y,z,k):
        super(Bird, self).__init__()
        self.imgs = []
        self.count = 0
        self.index = 0
        self.v=0
        self.z=z
        self.k=k
        for i in range(1,4):
            if z==0 and k==0:
                self.imgs.append(pygame.transform.scale(pygame.image.load(f'img/bird{i}.png'),(51,36)))  
            elif z == 1 and k==0:
                self.imgs.append(pygame.transform.scale(pygame.image.load(f'img/bird_{i}.png'),(51,36)))    
            elif k==1 and z==0:
                self.imgs.append(pygame.transform.scale(pygame.image.load(f'img/bird{i}.png'),(70,50)))   
            elif k==1 and z==1:
                self.imgs.append(pygame.transform.scale(pygame.image.load(f'img/bird1_{i}.png'),(70,50)))      
        self.image = self.imgs[0]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    #chuyển động chim
    def update(self):
        #rơi
        if self.k==0:
            if start == 1:
                self.v += 0.7
                if self.rect.bottom < height-132:
                    self.rect.y += int(self.v)  
                if self.v == 8:
                    self.v = 8  
            #bay
            if game_over == 0 and self.z ==0:
                if pygame.key.get_pressed()[pygame.K_SPACE]==1:
                    bird_wing.play()
                    self.v = 0
                    self.v -= 10    
                self.count += 1
                if self.index == len(self.imgs):
                    self.index = 0
                self.image = self.imgs[self.index]
                self.image  = pygame.transform.rotate(self.image,self.v*-1)
                if self.count > 11:
                    self.index += 1
                    self.count = 0    
            elif game_over_2 == 0 and self.z == 1:
                if pygame.mouse.get_pressed()[2]==1:
                    bird_wing.play()
                    self.v = 0
                    self.v -= 10    
                self.count += 1
                if self.index == len(self.imgs):
                    self.index = 0
                self.image = self.imgs[self.index]
                self.image  = pygame.transform.rotate(self.image,self.v*-1)
                if self.count > 11:
                    self.index += 1
                    self.count = 0   
            else:        
                self.image  = pygame.transform.rotate(self.imgs[0],-90)
        elif self.k==1:
            if self.z == 0:
                if pygame.key.get_pressed()[pygame.K_a] and self.rect.x>0:  # LEFT
                    self.rect.x -= v
                if pygame.key.get_pressed()[pygame.K_d] and self.rect.x < (width-50)//2-75:  # RIGHT
                    self.rect.x += v
                if pygame.key.get_pressed()[pygame.K_w] and self.rect.y>0:  # UP
                    self.rect.y -= v
                if pygame.key.get_pressed()[pygame.K_s] and self.rect.y < height-80:  # DOWN
                    self.rect.y += v   
                self.count += 1
                if self.index == len(self.imgs):
                    self.index = 0
                self.image = self.imgs[self.index]
                self.image  = pygame.transform.rotate(self.image,self.v*-1)
                if self.count > 11:
                    self.index += 1
                    self.count = 0  
            else:
                if pygame.key.get_pressed()[pygame.K_LEFT] and self.rect.x > (width-50)//2+35:  # LEFT
                        self.rect.x -= v
                if pygame.key.get_pressed()[pygame.K_RIGHT] and self.rect.x < width-100:  # RIGHT
                    self.rect.x += v
                if pygame.key.get_pressed()[pygame.K_UP] and self.rect.y > 0:  # UP
                    self.rect.y -= v
                if pygame.key.get_pressed()[pygame.K_DOWN] and self.rect.y < height-80:  # DOWN
                    self.rect.y += v   
                self.count += 1
                if self.index == len(self.imgs):
                    self.index = 0
                self.image = self.imgs[self.index]
                self.image  = pygame.transform.rotate(self.image,self.v*-1)
                if self.count > 11:
                    self.index += 1
                    self.count = 0       
          
#ống nước
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x,y,pos,t):
        super(Pipe,self).__init__()
        self.image = pygame.image.load('img/pipe.png')
        self.rect = self.image.get_rect()
        self.t = t
        if pos == -1:
            self.rect.topleft = (x,y+100)
        if pos == 1:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.bottomleft = (x,y-100)
    def update(self):
        self.rect.x -=4
        if self.rect.right < self.t:
            self.kill() 
       
#nút             
class Botton:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.x = x
        self.y = y
    def draw(self):
        displaysurf.blit(self.image,(self.x,self.y))    
    def check(self):
        action = 0
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = 1 
        return action    
class Shotgun(pygame.sprite.Sprite): #đạn
    def __init__(self,x,y,o):
        super(Shotgun, self).__init__()
        self.x=x
        self.y=y
        self.o = o
        if o == 0:
            self.image = pygame.transform.scale(pygame.image.load('img/red.png'),(20,5))
        else :
            self.image = pygame.transform.scale(pygame.image.load('img/yellow.png'),(20,5))    
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def update(self) :
        if self.o==0:
            self.rect.x +=6
            if(self.rect.left > width):
                self.kill()
        else:
            self.rect.x -=10
            if(self.rect.left < 0):
                self.kill()           

bird = Bird(100,height//2,0,0)
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
bird_group.add(bird)
botton = Botton(int(width/2)-60,int(height/2)+200,botton_load)
bird1 = Bird(width//2+100,height//2,1,0)
bird_group_2 = pygame.sprite.Group()
bird_group_2.add(bird1)
pipe_group_2 = pygame.sprite.Group()
floor_2 = pygame.transform.scale(floor,(20,168))

#vẽ chữ
def draw_text(text,font,color,x,y):
    img = font.render(text,True, color)
    displaysurf.blit(img,(x- img.get_width() /2,y- img.get_height()/2))
botton1 = Botton(int(width/2)-260,int(height/2)-200,botton_1)   
botton2 = Botton(int(width/2)+100,int(height/2)-200,botton_2)    
seperate = pygame.image.load('img/ngancach.png')
seperate = pygame.transform.scale(seperate,(10,height))
floor_3 = pygame.image.load('img/aa.png')
floor_3 = pygame.transform.scale(floor_3,(20,168))
#pk
bird_3 = Bird(100,int(height/2),0,1)
bird_group_3 = pygame.sprite.Group()
bird_group_3.add(bird_3) 
bird_4 = Bird(width-100,int(height/2),1,1)
bird_group_4 = pygame.sprite.Group()
bird_group_4.add(bird_4) 
red_health = 5
yellow_health = 5
red_bullet = pygame.sprite.Group() 
yellow_bullet = pygame.sprite.Group()
botton3 = pygame.image.load('img/1vs1.png')
botton3 = pygame.transform.scale(botton3,(160,100))
botton_3 = Botton(int(width/2)-80,int(height/2),botton3)    
home = pygame.image.load('img/home.png')
home = pygame.transform.scale(home,(100,100))
home_1 = Botton(50,50,home) 
#âm thanh
gun_hit = pygame.mixer.Sound('sound/GunHit.wav')     
gun_fire = pygame.mixer.Sound('sound/GunFire.mp3')  
v=5
check = False
clock = pygame.time.Clock()

run =1
while run:         
    clock.tick(60)   
    displaysurf.blit(background,(0,0))  
    if start_1 == 0:   
        background = pygame.transform.scale(background,(width,height))
        if start == 1 and game_over ==0  :
            if check_3 == 0:
                displaysurf.blit(pygame.transform.scale(pygame.image.load('img/bird1.png'),(51,36)),(100,height//2))
            if pygame.key.get_pressed()[pygame.K_SPACE]==1:
                check_3 = 1 
            if check_3:
                bird_group.draw(displaysurf) 
                bird_group.update()  
                pipe_group.draw(displaysurf)
        #kiem tra va cham
        if check_3:
            if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or bird.rect.top < 0 or bird.rect.bottom >=height-132:
                if game_over== 0:
                    bird_hit.play()
                game_over = 1 

            displaysurf.blit(floor,(floor_move,height -132))  
            #di chuyển ống + sàn
            if game_over == 0 and start == 1 :
                pipe_now = pygame.time.get_ticks()
                if pipe_now - last_pipe > pipe_frequency and start ==1:
                    pipe_h = random.randint(-200,200)
                    top_pipe = Pipe(width,int(height/2)+pipe_h-20,1,0)
                    bottom_pipe = Pipe(width,int(height/2)+pipe_h-40,-1,0)
                    pipe_group.add(bottom_pipe)
                    pipe_group.add(top_pipe)
                    last_pipe = pipe_now
                if floor_move <= -40:
                    floor_move = 0    
                floor_move -=4
                pipe_group.update() 
            #điểm    
            if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and  bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and p_pass == 0:
                    p_pass = 1  
                if p_pass == 1 and bird_group.sprites()[0].rect.right > pipe_group.sprites()[0].rect.right:    
                    bird_point.play()
                    score += 1
                    p_pass = 0
            if start ==1:
                draw_text(str(score),font,(255,255,255,255),int(width/2),50)
            #restart
            if game_over == 1 and start == 1:
                displaysurf.blit(background,(0,0))  
                draw_text("SCORE: "+str(score),font,(255,255,255,255),int(width/2),height//2)
                botton.draw() 
                if botton.check():
                    start = 0
                    pipe_group.empty()
                    bird.rect.x = 100
                    bird.rect.y = int(height / 2)
                    score = 0
                    game_over = 0
                    bird.v=0
    elif start_1 == 1:
        # player 1
        displaysurf.blit(background,(0,0))
        if start == 1:
            if check_1 == 0:
                displaysurf.blit(pygame.transform.scale(pygame.image.load('img/bird1.png'),(51,36)),(100,height//2))
            if pygame.key.get_pressed()[pygame.K_SPACE]==1:
                check_1 = 1 
            if check_1:
                check_4 = 1
                bird_group.draw(displaysurf)
                bird_group.update()  
                pipe_group.draw(displaysurf)
            #kiem tra va cham
        if check_1:    
            if pygame.sprite.groupcollide(bird_group,pipe_group,False,False) or bird.rect.top < 0 or bird.rect.bottom >=height-132:
                if game_over == 0:
                    bird_hit.play()
                game_over = 1 
            displaysurf.blit(floor_1,(floor_move,height -132))  
            #di chuyển ống + sàn
            if game_over == 0 and start == 1:
                pipe_now = pygame.time.get_ticks()
                if pipe_now - last_pipe > pipe_frequency and start ==1:
                    pipe_h = random.randint(-200,200)
                    top_pipe = Pipe(width//2,int(height/2)+pipe_h,1,0)
                    bottom_pipe = Pipe(width//2,int(height/2)+pipe_h-20,-1,0)
                    pipe_group.add(bottom_pipe)
                    pipe_group.add(top_pipe)
                    last_pipe = pipe_now
                if floor_move <= -40:
                    floor_move = 0    
                floor_move -=4
                pipe_group.update() 
            if game_over == 1:
                displaysurf.blit(floor,(floor_move,height -132))       
            #điểm    
            if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and  bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and p_pass == 0:
                    p_pass = 1  
                if p_pass == 1 and bird_group.sprites()[0].rect.right > pipe_group.sprites()[0].rect.right:  
                    bird_point.play()  
                    score += 1
                    p_pass = 0
            if start ==1:
                draw_text(str(score),font,(255,255,255,255),int(width/4),100)  
        # player2        
        displaysurf.blit(background,(width//2,0)) 
        if start2 == 1:
            if check_2 == 0 :
                displaysurf.blit(pygame.transform.scale(pygame.image.load('img/bird_1.png'),(51,36)),(width//2+100,height//2))
            if  pygame.mouse.get_pressed()[2]==1:
                check_2=1 
            if check_2==1:   
                bird_group_2.draw(displaysurf) 
                bird_group_2.update()  
                pipe_group_2.draw(displaysurf)  
            #kiem tra va cham
                if pygame.sprite.groupcollide(bird_group_2,pipe_group_2,False,False) or bird1.rect.top < 0 or bird1.rect.bottom >= height-132:
                    if game_over_2 == 0:
                        bird_hit_2.play()
                    game_over_2 = 1 

                displaysurf.blit(floor_1,(floor_move_2,height-132))  
                #di chuyển ống + sàn
                if game_over_2 == 0 and start2 == 1:
                    pipe_now_2 = pygame.time.get_ticks()
                    if pipe_now_2 - last_pipe_2 > pipe_frequency and start2 ==1:
                        pipe_h = random.randint(-200,200)
                        top_pipe_2 = Pipe(width,int(height/2)+pipe_h,1,width//2+78)
                        bottom_pipe_2 = Pipe(width,int(height/2)+pipe_h-20,-1,width//2+78)
                        pipe_group_2.add(bottom_pipe_2)
                        pipe_group_2.add(top_pipe_2)
                        last_pipe_2 = pipe_now_2
                    if floor_move_2 <= width//2-20:
                        floor_move_2 = width//2  
                    floor_move_2 -=4
                    pipe_group_2.update() 

                if len(pipe_group_2):
                    if bird_group_2.sprites()[0].rect.left > pipe_group_2.sprites()[0].rect.left and  bird_group_2.sprites()[0].rect.right < pipe_group_2.sprites()[0].rect.right and p_pass_2 == 0:
                        p_pass_2 = 1  
                    if p_pass_2 == 1 and bird_group_2.sprites()[0].rect.right > pipe_group_2.sprites()[0].rect.right:    
                        bird_point.play()
                        score2 += 1
                        p_pass_2 = 0
                if start2 ==1:
                    draw_text(str(score2),font,(255,255,255,255),int(width*3/4),100)  
            if check_1 and check_2:        
                displaysurf.blit(floor_2,(width//2-20,height-132))    
            if check_4 == 0 and check_2 ==1:
                displaysurf.blit(floor_3,(width//2-20,height-132))            
            displaysurf.blit(seperate,(width//2,0)) 
            #restart
            if game_over == 1 and start ==1 and game_over_2==1 and start2==1:
                displaysurf.blit(pygame.transform.scale(background,(width,height)),(0,0))
                if score > score2 :
                    draw_text("PLAYER 1 WIN ",font,(255,255,255,255),width//2,height//2-100)
                    draw_text("SCORE: "+str(score),font,(255,255,255,255),width//2,height//2)
                elif score < score2: 
                    draw_text("PLAYER 2 WIN",font,(255,255,255,255),width//2,height//2-100)    
                    draw_text("SCORE: "+str(score2),font,(255,255,255,255),width//2,height//2)
                else: 
                    draw_text("HÒA",font,(255,255,255,255),width//2,height//2)    
                botton.draw() 
                if botton.check():
                    start = 0
                    start2=0
                    pipe_group.empty()
                    pipe_group_2.empty()
                    bird.rect.x = 100
                    bird.rect.y = int(height / 2)
                    bird1.rect.x = width//2+100
                    bird1.rect.y = int(height / 2)
                    bird1.v=0
                    bird.v = 0
                    score = 0
                    score2 = 0
                    game_over = 0
                    game_over_2 = 0  
                    background = pygame.transform.scale(background,(width//2,height))  
    # 1 vs 1                
    else: 
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                run = 0 
                pygame.quit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j and len(red_bullet)<4:
                    t = int(bird_3.rect.topleft[0])+10
                    t1 = int(bird_3.rect.topleft[1])+20
                    shogun = Shotgun(t,t1,0)
                    gun_hit.play()
                    red_bullet.add(shogun)  
                if event.key == pygame.K_KP0 and len(yellow_bullet)<4:
                    t = int(bird_4.rect.topleft[0])+10
                    t1 = int(bird_4.rect.topleft[1])+20
                    shogun = Shotgun(t,t1,1)
                    gun_hit.play()
                    yellow_bullet.add(shogun)   
        #vẽ background + bird            
        background = pygame.transform.scale(background,(width,height))                 
        displaysurf.blit(background,(0,0))    
        red_bullet.draw(displaysurf) #đạn
        yellow_bullet.draw(displaysurf)   # đạn    
        bird_group_3.draw(displaysurf)        
        bird_group_3.update()
        bird_group_4.draw(displaysurf)   
        red_bullet.update()     
        yellow_bullet.update()
        bird_group_4.update()
        draw_text("HEALTH:"+str(red_health),font,(255,255,255,255),width//4,30)
        draw_text("HEALTH:"+str(yellow_health),font,(255,255,255,255),width*3//4,30)
        #va chạm
        if pygame.sprite.groupcollide(bird_group_4,red_bullet,False,True) and yellow_health>0:
            gun_fire.play()
            yellow_health -=1
        if pygame.sprite.groupcollide(bird_group_3,yellow_bullet,False,True) and red_health>0:
            gun_fire.play()    
            red_health-=1
        displaysurf.blit(seperate,(width//2,0))     
        if red_health==0: 
            displaysurf.blit(pygame.transform.scale(background,(width,height)),(0,0))
            draw_text(str("PLAYER 2 WIN:"),font,(255,255,255,255),width//2,height//4+100)
            draw_text("HEALTH:"+str(yellow_health),font,(255,255,255,255),width//2,height//4+200)
            botton.draw() 
            if botton.check():
                start = 0
                bird_3.rect.x = 100
                bird_3.rect.y = height//2
                bird_4.rect.x = width-130
                bird_4.rect.y = height//2
        if yellow_health==0: 
            displaysurf.blit(pygame.transform.scale(background,(width,height)),(0,0))
            draw_text(str("PLAYER 1 WIN:"),font,(255,255,255,255),width//2 ,height//4+100)
            draw_text("HEALTH:"+str(red_health),font,(255,255,255,255),width//2,height//4+200)
            botton.draw() 
            if botton.check() :
                start = 0 
                bird_3.rect.x = 100
                bird_3.rect.y = height//2
                bird_4.rect.x = width-130
                bird_4.rect.y = height//2

    if start == 0 :
        displaysurf.blit(pygame.transform.scale(background,(width,height)) ,(0,0))
        botton1.draw()
        botton2.draw() 
        botton_3.draw()
        if botton1.check() and start == 0 and game_over == 0:
            start_1 = 0
            start = 1  
            check_1=0 
            check_3=0 
            game_over = 0

        if botton2.check() and start == 0 and game_over == 0 and start2 ==0 and game_over_2 == 0:
            start_1 = 1
            start = 1
            start2 = 1     
            check_2=0
            check_1=0  
            check_3 = 0
            check_4=0
            game_over_2=0
            game_over = 0
        if botton_3.check() :
            start_1 = 2
            start = 1     
            red_health=5
            yellow_health = 5    
    if start == 1:
        home_1.draw()
        if home_1.check():
            start = 0 
            game_over = 0
            game_over_2 =0
            start2=0
            pipe_group.empty()
            pipe_group_2.empty()
            bird_3.rect.x = 100
            bird_3.rect.y = height//2
            bird_4.rect.x = width-130
            bird_4.rect.y = height//2
            bird.rect.x = 100
            bird.rect.y = int(height / 2)
            bird1.rect.x = width//2+100
            bird1.rect.y = int(height / 2)
            bird1.v=0
            bird.v = 0
            score = 0
            score2 = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0   
            pygame.quit() 
  

    pygame.display.update()
  
pygame.quit()