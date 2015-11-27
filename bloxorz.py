import pygame

pygame.init()
screen_width = 500
screen_height = 500
display = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

class Block:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.width = 50
        self.height = 100
        
    def draw(self):
        pygame.draw.line(display,(0,0,0),(self.x,self.y),(self.x,self.y+self.height))

bloxor = Block()

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

while(True):
    clock.tick(30)
    handle_events()
    display.fill((255,255,255)) #fill screen white
    
    bloxor.draw()

    pygame.display.flip() #update screen

