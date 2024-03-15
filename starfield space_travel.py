import pygame, sys, random , time

width=800
height=800

clock = pygame.time.Clock()
pygame.init() # initiates pygame
pygame.display.set_caption('Caption')
WINDOW_SIZE = (width,height)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window



class Starfield():
    def __init__(self):
        self.x=random.randint(-width//2,width//2)
        self.y=random.randint(-height//2,height//2)
        self.z=random.randint(width//2,width)
        self.sx=(self.x//self.z)*width
        self.sy=(self.y//self.z)*height
        self.radius=((width-self.z)/width)*8
        self.color=(255,255,255)
        self.speedz=3
        self.speedy=10
        self.speedx=10
        #self.accelertiony=1

    def update(self):
        if (self.z-self.speedz<=20)or ((width/2+self.sx+self.radius<=0) or (width/2+self.sx-self.radius>=height)) or ((height/2+self.sy+self.radius<=0) or (height/2+self.sy-self.radius>=height)):
            self.z=random.randint(width//2,width)
            self.x=random.randint(-width//2,width//2)
            self.y=random.randint(-height//2,height//2)
        self.z-=self.speedz
        if self.speedy<-10:
            self.speedy=10
        self.sx=(self.x/self.z)*(width/2)
        self.sy=(self.y/self.z)*(height/2)
        self.radius=((width-self.z)/width)*8
         
    def show(self):
        pygame.draw.circle(screen, self.color, [width/2+self.sx,height/2+ self.sy], self.radius)

l=[Starfield() for i in range(int(100))]
    
while True: # game loop
    screen.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()
    spd=pygame.mouse.get_pos()[0]/16

    for i in range(len(l)):
        l[i].update()
        l[i].show()
        l[i].speedz=spd

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    #moving charecter
    print(keys[pygame.K_a])
    if keys[pygame.K_a]:
        time.sleep(1)
    pygame.display.update()
    clock.tick(60)
