import pygame

pygame.init()
screen_width = 1000
screen_height = 500
display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Bloxorz")
clock = pygame.time.Clock()

class Block:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.width = 40
        self.height = 30
        
    def draw(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        ang = 15
        b_w = 80
        #pygame.draw.polygon(display,(199,208,207),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)])
        #pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)],1)
        pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y-b_w))
        pygame.draw.line(display,(45,56,65),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w))
        pygame.draw.line(display,(45,56,65),(x+ang,y+h),(x+ang,y+h-b_w))
        #pygame.draw.line(display,(45,56,65),(x-10+w,y-10),(x-10+w,y-10-b_w))

        #pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
        #pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x-10,y+10))
        pygame.draw.polygon(display,(76,48,34),[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)])
        pygame.draw.polygon(display,(0,0,0),[(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang+w,y-10+h-b_w),(x-10+w,y-10-b_w)],1)

        pygame.draw.polygon(display,(76,48,34),[(x-10+w,y-10),(x-10,y),(x-10,y-b_w),(x-10+w,y-10-b_w)])
        pygame.draw.polygon(display,(0,0,0),[(x-10+w,y-10),(x-10,y),(x-10,y-b_w),(x-10+w,y-10-b_w)],1)

        pygame.draw.polygon(display,(76,48,34),[(x-10,y),(x+ang,y+h),(x+ang,y+h-b_w),(x-10,y-b_w)])
        pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h-b_w),(x-10,y-b_w)],1)

        pygame.draw.polygon(display,(76,48,34),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h-b_w),(x+ang+w,y-10+h-b_w)])
        pygame.draw.polygon(display,(0,0,0),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h-b_w),(x+ang+w,y-10+h-b_w)],1)

    def rotate_around(self,degrees,point):
        pX,pY = point
        xRot = pX + (math.cos(degrees)*(x-pX))-(math.sin(degrees)*(y-pY))
        yRot = pY + (math.sin(degrees)*(x-pX))-(math.cos(degrees)*(y-pY))

        

class Tile:
    def __init__(self,x=100,y=100):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 30

    def draw(self):
        x,y,w,h = self.x,self.y,self.width,self.height
        ang = 15
        pygame.draw.polygon(display,(199,208,207),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)])
        pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x-10+w,y-10),(x+ang+w,y-10+h),(x+ang,y+h)],1)
        pygame.draw.line(display,(45,56,65),(x-10,y),(x-10,y+10))
        pygame.draw.line(display,(45,56,65),(x+ang+w,y-10+h),(x+ang+w,y+h))
        pygame.draw.line(display,(45,56,65),(x+ang,y+h),(x+ang,y+h+10))

        #pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x+ang+w,y+h))
        #pygame.draw.line(display,(45,56,65),(x+ang,y+h+10),(x-10,y+10))

        pygame.draw.polygon(display,(45,56,65),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)])
        pygame.draw.polygon(display,(0,0,0),[(x-10,y),(x+ang,y+h),(x+ang,y+h+10),(x-10,y+10)],1)
        pygame.draw.polygon(display,(45,56,65),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)])
        pygame.draw.polygon(display,(0,0,0),[(x+ang+w,y-10+h),(x+ang,y+h),(x+ang,y+h+10),(x+ang+w,y+h)],1)

bloxor = Block()
block2 = Block()
block2.y -= block2.height
bloxor.x = 165
bloxor.y = 220

new_tile = Tile(100,100)
new_tile_2 = Tile(140,100-10)

'''level_array = [
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,0,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]'''
level_array = [
    [1,1,1,0,0,0,0,0,0,0],
    [1,1,1,1,1,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,0],
    [0,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,1,1,0,1,1],
    [0,0,0,0,0,0,1,1,1,0]
]

def draw_level(level_data,startX=100,startY=200):
    '''startX+=len(level_data[0]*40)
    x,y = startX,startY
    i = 0
    for j in range(len(level_data)-1,0,-1):
        #print(k)
        row = level_data[j]
        for k in range(len(row)-1,0,-1):
            tile_data = row[k]
            if(tile_data == 1):
                Tile(x,y).draw()
            x-=40
            y+=10
        x=startX-(i*25)
        y=startY-(i*30)
        i+=1'''
    x,y=startX,startY
    i=1
    for row in level_data:
        for tile_data in row:
            if(tile_data == 1):
                Tile(x,y).draw()
            x+=40
            y-=10
        x=startX+(i*25)
        y=startY+(i*30)
        i+=1

def handle_events():
    for e in pygame.event.get():
        if(e.type == pygame.KEYDOWN):
            if(e.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()
            if(e.key == pygame.K_LEFT):
                print("LEFT")
            if(e.key == pygame.K_RIGHT):
                print("RIGHT")
            if(e.key == pygame.K_UP):
                print("UP")
            if(e.key == pygame.K_DOWN):
                print("DOWN")
        if(e.type == pygame.QUIT):
            pygame.quit()
            quit()

while(True):
    clock.tick(30)
    handle_events()
    display.fill((193,39,1)) #fill screen white
    
    
    #block2.draw()
    #new_tile_2.draw()
    #new_tile.draw()
    draw_level(level_array)
    bloxor.draw()

    pygame.display.flip() #update screen

