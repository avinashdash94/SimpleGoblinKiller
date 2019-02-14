####in This we changed all program to ooops form 

import pygame 
pygame.init()
win =pygame.display.set_mode((500,480))
pygame.display.set_caption("Avinash Game ")
#####Loading image in list form as multiple images are there
walkRight=[pygame.image.load('images/R1.png'),pygame.image.load('images/R2.png'),pygame.image.load('images/R3.png'),pygame.image.load('images/R4.png'),pygame.image.load('images/R5.png'),pygame.image.load('images/R6.png'),pygame.image.load('images/R7.png'),pygame.image.load('images/R8.png'),pygame.image.load('images/R9.png')]
walkLeft=[pygame.image.load('images/L1.png'),pygame.image.load('images/L2.png'),pygame.image.load('images/L3.png'),pygame.image.load('images/L4.png'),pygame.image.load('images/L5.png'),pygame.image.load('images/L6.png'),pygame.image.load('images/L7.png'),pygame.image.load('images/L8.png'),pygame.image.load('images/L9.png')]
####BAckground image
bg=pygame.image.load("images/bg.jpg")
char=pygame.image.load('images/standing.png')#initail standing position of hero 

clock=pygame.time.Clock()# Define the clock 
####**  loading Sounds
bulletSound = pygame.mixer.Sound('sound/bullet.wav')
hitSound=pygame.mixer.Sound("sound/hit.wav")
music=pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.play(-1) #to play the music -1 for music will play for forewer even song finised

score=0

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True
        self.hitbox=(self.x+17,self.y+11,29,52)

    def draw(self,win):
        # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
        ##draw image
        if self.walkCount +1>=27:
            self.walkCount=0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+17,self.y+11,29,52)
        # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        self.isJump=False# these two lines are as if we jump on goblin due to jump we go down as (-)ve direction movment to prevent that
        self.jumpCount=10
        self.x=60
        self.y=410
        self.walkCount=0
        font1=pygame.font.SysFont('comicsans',100)
        text=font1.render('-5',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))# text will display at mid of the screen
        pygame.display.update()
        i=0
        while i<300: # it will give time delay when it colid with goblin as it iterate 300 round
            pygame.time.delay(10) # time Delay for each second to give apuse after colison (both iteration as well as this delay)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()




####Class for bullet fired
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

#############***Enemy Class 
class enemy(object):
    walkRight=[pygame.image.load('images/R1E.png'),pygame.image.load('images/R2E.png'),pygame.image.load('images/R3E.png'),pygame.image.load('images/R4E.png'),pygame.image.load('images/R5E.png'),pygame.image.load('images/R6E.png'),pygame.image.load('images/R7E.png'),pygame.image.load('images/R8E.png'),pygame.image.load('images/R9E.png'),pygame.image.load('images/R10E.png'),pygame.image.load('images/R11E.png')]
    walkLeft=[pygame.image.load('images/L1E.png'),pygame.image.load('images/L2E.png'),pygame.image.load('images/L3E.png'),pygame.image.load('images/L4E.png'),pygame.image.load('images/L5E.png'),pygame.image.load('images/L6E.png'),pygame.image.load('images/L7E.png'),pygame.image.load('images/L8E.png'),pygame.image.load('images/L9E.png'),pygame.image.load('images/L10E.png'),pygame.image.load('images/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x,self.end]
        self.walkCount=0
        self.vel=3
        self.hitbox=(self.x+17,self.y+2,31,57)
        self.health=10
        self.visible=True
     
    def draw(self,win):
        self.move()
        if self.visible:
            ###Here we see weather to create image to left or to right
            if self.walkCount +1>=33:
                self.walkCount=0
            
            if self.vel>0 : #if velocity is grater then zero move Righr else left 
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            else:
                win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))
            self.hitbox=(self.x+17,self.y+2,31,57)
            # pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        
        
    
    def move(self):
        if self.vel>0:
            if self.x+ self.vel< self.path[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
        else:
            if self.x-self.vel > self.path[0]:
                self.x +=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
    
    ####Method when goblin hit (colision bulet and goblin)
    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible=False



        # print('hit')
        

def redrawGameWindow():
    win.blit(bg,(0,0))
    text=font.render('Score: '+str(score),1,(0,0,0))# render the new Text as increasing score
    win.blit(text,(350,10))
    man.draw(win)
    goblin.draw(win)
    # keys=pygame.key.get_pressed()
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#main loop of game` 
font =pygame.font.SysFont('Comicsans',30,True)# for font of score and True for Bold if i again write True then it is fr italic   
man=player(300,410,64,64)
goblin=enemy(100,410,64,64,450)
shootloop=0
bullets=[]
run=True
while run:
    clock.tick(27) # it will set FPS to 27 per second
    # to make goblin finish not visibel after destroy
    if goblin.visible==True:
        # for bullet in bullets:#### Collision between man and goblin
        if  man.hitbox[1]< goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and man.hitbox[0]< goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                hitSound.play()#*************************************************
                man.hit()
                score-=5
               

    if shootloop>0:
        shootloop+=1
    if shootloop>3:
        shootloop=0

    # pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    for bullet in bullets:####colision between bullet and goblin
        if  bullet.y-bullet.radius < goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                if goblin.visible==True:
                    # hitSound.play()*************************************************
                    goblin.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet)) #to Make bullet disapper when it hit goblin
        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop==0:
        bulletSound.play() #*************************************************************************
       
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
        shootloop=1
    if( keys[pygame.K_LEFT]) and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif(keys[pygame.K_RIGHT] and man.x<500-man.width-man.vel):
        man.x+=man.vel
        man.right=True
        man.left=False
        man.standing=False
    else:
        man.standing=True
        man.walkCount=0
    if not(man.isJump):
        # if(keys[pygame.K_UP] and y>vel):
        #     y-=vel
        # if (keys[pygame.K_DOWN] and y<500-height-vel):
        #     y+=vel
        if keys[pygame.K_UP]:
            man.isJump=True
            man.right=False
            man.left=False
            man.walkCount=0
    else:
        if man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:# if jumpcout Become negativ then
                neg=-1
            man.y-=(man.jumpCount**2)*0.5*neg# sQuaring jump count we subtracting  in  y means going up from down
            man.jumpCount-=1

        else:
            man.isJump=False
            man.jumpCount=10
    redrawGameWindow()
    # win.fill((0,0,0))
    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    # keys=pygame.key.get_pressed()

    # pygame.display.update()

pygame.quit()####in This we changed all program to ooops form 

import pygame 
pygame.init()
win =pygame.display.set_mode((500,480))
pygame.display.set_caption("Avinash Game ")
#####Loading image in list form as multiple images are there
walkRight=[pygame.image.load('images/R1.png'),pygame.image.load('images/R2.png'),pygame.image.load('images/R3.png'),pygame.image.load('images/R4.png'),pygame.image.load('images/R5.png'),pygame.image.load('images/R6.png'),pygame.image.load('images/R7.png'),pygame.image.load('images/R8.png'),pygame.image.load('images/R9.png')]
walkLeft=[pygame.image.load('images/L1.png'),pygame.image.load('images/L2.png'),pygame.image.load('images/L3.png'),pygame.image.load('images/L4.png'),pygame.image.load('images/L5.png'),pygame.image.load('images/L6.png'),pygame.image.load('images/L7.png'),pygame.image.load('images/L8.png'),pygame.image.load('images/L9.png')]
####BAckground image
bg=pygame.image.load("images/bg.jpg")
char=pygame.image.load('images/standing.png')#initail standing position of hero 

clock=pygame.time.Clock()# Define the clock 
####**  loading Sounds
bulletSound = pygame.mixer.Sound('sound/bullet.wav')
hitSound=pygame.mixer.Sound("sound/hit.wav")
music=pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.play(-1) #to play the music -1 for music will play for forewer even song finised

score=0

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True
        self.hitbox=(self.x+17,self.y+11,29,52)

    def draw(self,win):
        # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
        ##draw image
        if self.walkCount +1>=27:
            self.walkCount=0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+17,self.y+11,29,52)
        # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        self.isJump=False# these two lines are as if we jump on goblin due to jump we go down as (-)ve direction movment to prevent that
        self.jumpCount=10
        self.x=60
        self.y=410
        self.walkCount=0
        font1=pygame.font.SysFont('comicsans',100)
        text=font1.render('-5',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))# text will display at mid of the screen
        pygame.display.update()
        i=0
        while i<300: # it will give time delay when it colid with goblin as it iterate 300 round
            pygame.time.delay(10) # time Delay for each second to give apuse after colison (both iteration as well as this delay)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()




####Class for bullet fired
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

#############***Enemy Class 
class enemy(object):
    walkRight=[pygame.image.load('images/R1E.png'),pygame.image.load('images/R2E.png'),pygame.image.load('images/R3E.png'),pygame.image.load('images/R4E.png'),pygame.image.load('images/R5E.png'),pygame.image.load('images/R6E.png'),pygame.image.load('images/R7E.png'),pygame.image.load('images/R8E.png'),pygame.image.load('images/R9E.png'),pygame.image.load('images/R10E.png'),pygame.image.load('images/R11E.png')]
    walkLeft=[pygame.image.load('images/L1E.png'),pygame.image.load('images/L2E.png'),pygame.image.load('images/L3E.png'),pygame.image.load('images/L4E.png'),pygame.image.load('images/L5E.png'),pygame.image.load('images/L6E.png'),pygame.image.load('images/L7E.png'),pygame.image.load('images/L8E.png'),pygame.image.load('images/L9E.png'),pygame.image.load('images/L10E.png'),pygame.image.load('images/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x,self.end]
        self.walkCount=0
        self.vel=3
        self.hitbox=(self.x+17,self.y+2,31,57)
        self.health=10
        self.visible=True
     
    def draw(self,win):
        self.move()
        if self.visible:
            ###Here we see weather to create image to left or to right
            if self.walkCount +1>=33:
                self.walkCount=0
            
            if self.vel>0 : #if velocity is grater then zero move Righr else left 
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            else:
                win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))
            self.hitbox=(self.x+17,self.y+2,31,57)
            # pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        
        
    
    def move(self):
        if self.vel>0:
            if self.x+ self.vel< self.path[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
        else:
            if self.x-self.vel > self.path[0]:
                self.x +=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
    
    ####Method when goblin hit (colision bulet and goblin)
    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible=False



        # print('hit')
        

def redrawGameWindow():
    win.blit(bg,(0,0))
    text=font.render('Score: '+str(score),1,(0,0,0))# render the new Text as increasing score
    win.blit(text,(350,10))
    man.draw(win)
    goblin.draw(win)
    # keys=pygame.key.get_pressed()
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#main loop of game` 
font =pygame.font.SysFont('Comicsans',30,True)# for font of score and True for Bold if i again write True then it is fr italic   
man=player(300,410,64,64)
goblin=enemy(100,410,64,64,450)
shootloop=0
bullets=[]
run=True
while run:
    clock.tick(27) # it will set FPS to 27 per second
    # to make goblin finish not visibel after destroy
    if goblin.visible==True:
        # for bullet in bullets:#### Collision between man and goblin
        if  man.hitbox[1]< goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and man.hitbox[0]< goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                hitSound.play()#*************************************************
                man.hit()
                score-=5
               

    if shootloop>0:
        shootloop+=1
    if shootloop>3:
        shootloop=0

    # pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    for bullet in bullets:####colision between bullet and goblin
        if  bullet.y-bullet.radius < goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                if goblin.visible==True:
                    # hitSound.play()*************************************************
                    goblin.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet)) #to Make bullet disapper when it hit goblin
        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop==0:
        bulletSound.play() #*************************************************************************
       
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
        shootloop=1
    if( keys[pygame.K_LEFT]) and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif(keys[pygame.K_RIGHT] and man.x<500-man.width-man.vel):
        man.x+=man.vel
        man.right=True
        man.left=False
        man.standing=False
    else:
        man.standing=True
        man.walkCount=0
    if not(man.isJump):
        # if(keys[pygame.K_UP] and y>vel):
        #     y-=vel
        # if (keys[pygame.K_DOWN] and y<500-height-vel):
        #     y+=vel
        if keys[pygame.K_UP]:
            man.isJump=True
            man.right=False
            man.left=False
            man.walkCount=0
    else:
        if man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:# if jumpcout Become negativ then
                neg=-1
            man.y-=(man.jumpCount**2)*0.5*neg# sQuaring jump count we subtracting  in  y means going up from down
            man.jumpCount-=1

        else:
            man.isJump=False
            man.jumpCount=10
    redrawGameWindow()
    # win.fill((0,0,0))
    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    # keys=pygame.key.get_pressed()

    # pygame.display.update()

pygame.quit()####in This we changed all program to ooops form 

import pygame 
pygame.init()
win =pygame.display.set_mode((500,480))
pygame.display.set_caption("Avinash Game ")
#####Loading image in list form as multiple images are there
walkRight=[pygame.image.load('images/R1.png'),pygame.image.load('images/R2.png'),pygame.image.load('images/R3.png'),pygame.image.load('images/R4.png'),pygame.image.load('images/R5.png'),pygame.image.load('images/R6.png'),pygame.image.load('images/R7.png'),pygame.image.load('images/R8.png'),pygame.image.load('images/R9.png')]
walkLeft=[pygame.image.load('images/L1.png'),pygame.image.load('images/L2.png'),pygame.image.load('images/L3.png'),pygame.image.load('images/L4.png'),pygame.image.load('images/L5.png'),pygame.image.load('images/L6.png'),pygame.image.load('images/L7.png'),pygame.image.load('images/L8.png'),pygame.image.load('images/L9.png')]
####BAckground image
bg=pygame.image.load("images/bg.jpg")
char=pygame.image.load('images/standing.png')#initail standing position of hero 

clock=pygame.time.Clock()# Define the clock 
####**  loading Sounds
bulletSound = pygame.mixer.Sound('sound/bullet.wav')
hitSound=pygame.mixer.Sound("sound/hit.wav")
music=pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.play(-1) #to play the music -1 for music will play for forewer even song finised

score=0

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True
        self.hitbox=(self.x+17,self.y+11,29,52)

    def draw(self,win):
        # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
        ##draw image
        if self.walkCount +1>=27:
            self.walkCount=0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+17,self.y+11,29,52)
        # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        self.isJump=False# these two lines are as if we jump on goblin due to jump we go down as (-)ve direction movment to prevent that
        self.jumpCount=10
        self.x=60
        self.y=410
        self.walkCount=0
        font1=pygame.font.SysFont('comicsans',100)
        text=font1.render('-5',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))# text will display at mid of the screen
        pygame.display.update()
        i=0
        while i<300: # it will give time delay when it colid with goblin as it iterate 300 round
            pygame.time.delay(10) # time Delay for each second to give apuse after colison (both iteration as well as this delay)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()




####Class for bullet fired
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

#############***Enemy Class 
class enemy(object):
    walkRight=[pygame.image.load('images/R1E.png'),pygame.image.load('images/R2E.png'),pygame.image.load('images/R3E.png'),pygame.image.load('images/R4E.png'),pygame.image.load('images/R5E.png'),pygame.image.load('images/R6E.png'),pygame.image.load('images/R7E.png'),pygame.image.load('images/R8E.png'),pygame.image.load('images/R9E.png'),pygame.image.load('images/R10E.png'),pygame.image.load('images/R11E.png')]
    walkLeft=[pygame.image.load('images/L1E.png'),pygame.image.load('images/L2E.png'),pygame.image.load('images/L3E.png'),pygame.image.load('images/L4E.png'),pygame.image.load('images/L5E.png'),pygame.image.load('images/L6E.png'),pygame.image.load('images/L7E.png'),pygame.image.load('images/L8E.png'),pygame.image.load('images/L9E.png'),pygame.image.load('images/L10E.png'),pygame.image.load('images/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x,self.end]
        self.walkCount=0
        self.vel=3
        self.hitbox=(self.x+17,self.y+2,31,57)
        self.health=10
        self.visible=True
     
    def draw(self,win):
        self.move()
        if self.visible:
            ###Here we see weather to create image to left or to right
            if self.walkCount +1>=33:
                self.walkCount=0
            
            if self.vel>0 : #if velocity is grater then zero move Righr else left 
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            else:
                win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))
            self.hitbox=(self.x+17,self.y+2,31,57)
            # pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        
        
    
    def move(self):
        if self.vel>0:
            if self.x+ self.vel< self.path[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
        else:
            if self.x-self.vel > self.path[0]:
                self.x +=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
    
    ####Method when goblin hit (colision bulet and goblin)
    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible=False



        # print('hit')
        

def redrawGameWindow():
    win.blit(bg,(0,0))
    text=font.render('Score: '+str(score),1,(0,0,0))# render the new Text as increasing score
    win.blit(text,(350,10))
    man.draw(win)
    goblin.draw(win)
    # keys=pygame.key.get_pressed()
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#main loop of game` 
font =pygame.font.SysFont('Comicsans',30,True)# for font of score and True for Bold if i again write True then it is fr italic   
man=player(300,410,64,64)
goblin=enemy(100,410,64,64,450)
shootloop=0
bullets=[]
run=True
while run:
    clock.tick(27) # it will set FPS to 27 per second
    # to make goblin finish not visibel after destroy
    if goblin.visible==True:
        # for bullet in bullets:#### Collision between man and goblin
        if  man.hitbox[1]< goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and man.hitbox[0]< goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                hitSound.play()#*************************************************
                man.hit()
                score-=5
               

    if shootloop>0:
        shootloop+=1
    if shootloop>3:
        shootloop=0

    # pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    for bullet in bullets:####colision between bullet and goblin
        if  bullet.y-bullet.radius < goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                if goblin.visible==True:
                    # hitSound.play()*************************************************
                    goblin.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet)) #to Make bullet disapper when it hit goblin
        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop==0:
        bulletSound.play() #*************************************************************************
       
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
        shootloop=1
    if( keys[pygame.K_LEFT]) and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif(keys[pygame.K_RIGHT] and man.x<500-man.width-man.vel):
        man.x+=man.vel
        man.right=True
        man.left=False
        man.standing=False
    else:
        man.standing=True
        man.walkCount=0
    if not(man.isJump):
        # if(keys[pygame.K_UP] and y>vel):
        #     y-=vel
        # if (keys[pygame.K_DOWN] and y<500-height-vel):
        #     y+=vel
        if keys[pygame.K_UP]:
            man.isJump=True
            man.right=False
            man.left=False
            man.walkCount=0
    else:
        if man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:# if jumpcout Become negativ then
                neg=-1
            man.y-=(man.jumpCount**2)*0.5*neg# sQuaring jump count we subtracting  in  y means going up from down
            man.jumpCount-=1

        else:
            man.isJump=False
            man.jumpCount=10
    redrawGameWindow()
    # win.fill((0,0,0))
    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    # keys=pygame.key.get_pressed()

    # pygame.display.update()

pygame.quit()####in This we changed all program to ooops form 

import pygame 
pygame.init()
win =pygame.display.set_mode((500,480))
pygame.display.set_caption("Avinash Game ")
#####Loading image in list form as multiple images are there
walkRight=[pygame.image.load('images/R1.png'),pygame.image.load('images/R2.png'),pygame.image.load('images/R3.png'),pygame.image.load('images/R4.png'),pygame.image.load('images/R5.png'),pygame.image.load('images/R6.png'),pygame.image.load('images/R7.png'),pygame.image.load('images/R8.png'),pygame.image.load('images/R9.png')]
walkLeft=[pygame.image.load('images/L1.png'),pygame.image.load('images/L2.png'),pygame.image.load('images/L3.png'),pygame.image.load('images/L4.png'),pygame.image.load('images/L5.png'),pygame.image.load('images/L6.png'),pygame.image.load('images/L7.png'),pygame.image.load('images/L8.png'),pygame.image.load('images/L9.png')]
####BAckground image
bg=pygame.image.load("images/bg.jpg")
char=pygame.image.load('images/standing.png')#initail standing position of hero 

clock=pygame.time.Clock()# Define the clock 
####**  loading Sounds
bulletSound = pygame.mixer.Sound('sound/bullet.wav')
hitSound=pygame.mixer.Sound("sound/hit.wav")
music=pygame.mixer.music.load('sound/music.mp3')
pygame.mixer.music.play(-1) #to play the music -1 for music will play for forewer even song finised

score=0

class player(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.vel=5
        self.isJump=False
        self.jumpCount=10
        self.left=False
        self.right=False
        self.walkCount=0
        self.standing=True
        self.hitbox=(self.x+17,self.y+11,29,52)

    def draw(self,win):
        # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
        ##draw image
        if self.walkCount +1>=27:
            self.walkCount=0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            elif self.right:
                win.blit(walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
        else:
            if self.right:
                win.blit(walkRight[0],(self.x,self.y))
            else:
                win.blit(walkLeft[0],(self.x,self.y))
        self.hitbox=(self.x+17,self.y+11,29,52)
        # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def hit(self):
        self.isJump=False# these two lines are as if we jump on goblin due to jump we go down as (-)ve direction movment to prevent that
        self.jumpCount=10
        self.x=60
        self.y=410
        self.walkCount=0
        font1=pygame.font.SysFont('comicsans',100)
        text=font1.render('-5',1,(255,0,0))
        win.blit(text,(250-(text.get_width()/2),200))# text will display at mid of the screen
        pygame.display.update()
        i=0
        while i<300: # it will give time delay when it colid with goblin as it iterate 300 round
            pygame.time.delay(10) # time Delay for each second to give apuse after colison (both iteration as well as this delay)
            i+=1
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    i=301
                    pygame.quit()




####Class for bullet fired
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.facing=facing
        self.vel=8*facing
    
    def draw(self,win):
        pygame.draw.circle(win,self.color,(self.x,self.y),self.radius)

#############***Enemy Class 
class enemy(object):
    walkRight=[pygame.image.load('images/R1E.png'),pygame.image.load('images/R2E.png'),pygame.image.load('images/R3E.png'),pygame.image.load('images/R4E.png'),pygame.image.load('images/R5E.png'),pygame.image.load('images/R6E.png'),pygame.image.load('images/R7E.png'),pygame.image.load('images/R8E.png'),pygame.image.load('images/R9E.png'),pygame.image.load('images/R10E.png'),pygame.image.load('images/R11E.png')]
    walkLeft=[pygame.image.load('images/L1E.png'),pygame.image.load('images/L2E.png'),pygame.image.load('images/L3E.png'),pygame.image.load('images/L4E.png'),pygame.image.load('images/L5E.png'),pygame.image.load('images/L6E.png'),pygame.image.load('images/L7E.png'),pygame.image.load('images/L8E.png'),pygame.image.load('images/L9E.png'),pygame.image.load('images/L10E.png'),pygame.image.load('images/L11E.png')]

    def __init__(self,x,y,width,height,end):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.end=end
        self.path=[self.x,self.end]
        self.walkCount=0
        self.vel=3
        self.hitbox=(self.x+17,self.y+2,31,57)
        self.health=10
        self.visible=True
     
    def draw(self,win):
        self.move()
        if self.visible:
            ###Here we see weather to create image to left or to right
            if self.walkCount +1>=33:
                self.walkCount=0
            
            if self.vel>0 : #if velocity is grater then zero move Righr else left 
                win.blit(self.walkRight[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            else:
                win.blit(self.walkLeft[self.walkCount//3],(self.x,self.y))
                self.walkCount+=1
            
            pygame.draw.rect(win,(255,0,0),(self.hitbox[0],self.hitbox[1]-20,50,10))
            pygame.draw.rect(win,(0,128,0),(self.hitbox[0],self.hitbox[1]-20,50-(5*(10-self.health)),10))
            self.hitbox=(self.x+17,self.y+2,31,57)
            # pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        
        
    
    def move(self):
        if self.vel>0:
            if self.x+ self.vel< self.path[1]:
                self.x+=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
        else:
            if self.x-self.vel > self.path[0]:
                self.x +=self.vel
            else:
                self.vel=self.vel* -1
                self.walkCount=0
    
    ####Method when goblin hit (colision bulet and goblin)
    def hit(self):
        if self.health>0:
            self.health-=1
        else:
            self.visible=False



        # print('hit')
        

def redrawGameWindow():
    win.blit(bg,(0,0))
    text=font.render('Score: '+str(score),1,(0,0,0))# render the new Text as increasing score
    win.blit(text,(350,10))
    man.draw(win)
    goblin.draw(win)
    # keys=pygame.key.get_pressed()
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


#main loop of game` 
font =pygame.font.SysFont('Comicsans',30,True)# for font of score and True for Bold if i again write True then it is fr italic   
man=player(300,410,64,64)
goblin=enemy(100,410,64,64,450)
shootloop=0
bullets=[]
run=True
while run:
    clock.tick(27) # it will set FPS to 27 per second
    # to make goblin finish not visibel after destroy
    if goblin.visible==True:
        # for bullet in bullets:#### Collision between man and goblin
        if  man.hitbox[1]< goblin.hitbox[1]+goblin.hitbox[3] and man.hitbox[1]+man.hitbox[3]>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if man.hitbox[0]+man.hitbox[2]>goblin.hitbox[0] and man.hitbox[0]< goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                hitSound.play()#*************************************************
                man.hit()
                score-=5
               

    if shootloop>0:
        shootloop+=1
    if shootloop>3:
        shootloop=0

    # pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
    for bullet in bullets:####colision between bullet and goblin
        if  bullet.y-bullet.radius < goblin.hitbox[1]+goblin.hitbox[3] and bullet.y+bullet.radius>goblin.hitbox[1]:#if bullets is inside the y cordinate of goblin
            if bullet.x+bullet.radius>goblin.hitbox[0] and bullet.x-bullet.radius < goblin.hitbox[0]+goblin.hitbox[2]:#if bullets is inside the x cordinate of goblin
                if goblin.visible==True:
                    # hitSound.play()*************************************************
                    goblin.hit()
                    score+=1
                    bullets.pop(bullets.index(bullet)) #to Make bullet disapper when it hit goblin
        if bullet.x<500 and bullet.x>0:
            bullet.x+=bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    keys=pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootloop==0:
        bulletSound.play() #*************************************************************************
       
        if man.left:
            facing=-1
        else:
            facing=1
        if len(bullets)<5:
            bullets.append(projectile(round(man.x+man.width//2),round(man.y+man.height//2),6,(0,0,0),facing))
        shootloop=1
    if( keys[pygame.K_LEFT]) and man.x>man.vel:
        man.x-=man.vel
        man.left=True
        man.right=False
        man.standing=False
    elif(keys[pygame.K_RIGHT] and man.x<500-man.width-man.vel):
        man.x+=man.vel
        man.right=True
        man.left=False
        man.standing=False
    else:
        man.standing=True
        man.walkCount=0
    if not(man.isJump):
        # if(keys[pygame.K_UP] and y>vel):
        #     y-=vel
        # if (keys[pygame.K_DOWN] and y<500-height-vel):
        #     y+=vel
        if keys[pygame.K_UP]:
            man.isJump=True
            man.right=False
            man.left=False
            man.walkCount=0
    else:
        if man.jumpCount>=-10:
            neg=1
            if man.jumpCount<0:# if jumpcout Become negativ then
                neg=-1
            man.y-=(man.jumpCount**2)*0.5*neg# sQuaring jump count we subtracting  in  y means going up from down
            man.jumpCount-=1

        else:
            man.isJump=False
            man.jumpCount=10
    redrawGameWindow()
    # win.fill((0,0,0))
    # pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    # keys=pygame.key.get_pressed()

    # pygame.display.update()

pygame.quit()