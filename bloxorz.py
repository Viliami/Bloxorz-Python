import pygame

pygame.init()
screen_width = 500
screen_height = 500
display = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Bloxorz")
clock = pygame.time.Clock()

class Block:
    def __init__(self):
        self.x = 250
        self.y = 250
        self.width = 50
        self.height = 50
        
    def draw(self):
	angle_length = 21.65
	print(0.433*self.width)
        '''pygame.draw.line(display,(0,0,0),(self.x,self.y),(self.x,self.y+self.height)) #left edge
        pygame.draw.line(display,(0,0,0),(self.x+self.width,self.y-angle_length),(self.x+self.width,self.y+self.height-angle_length)) #right edge
        pygame.draw.line(display,(0,0,0),(self.x,self.y),(self.x+self.width,self.y-angle_length)) #top edge
        pygame.draw.line(display,(0,0,0),(self.x,self.y+self.height),(self.x+self.width,self.y+self.height-angle_length)) #bottom edge
	'''
	pygame.draw.line(display,(0,0,0),(self.x,self.y),(self.x,self.y+self.height))
	#pygame.draw.line(display,(255,0,0),(self.x,self.y-self.height),(self.x,self.y))

	pygame.draw.line(display,(0,0,0),(self.x+self.width,self.y-angle_length),(self.x+self.width,self.y+self.height-angle_length))
	pygame.draw.line(display,(0,0,0),(self.x-self.width,self.y-angle_length),(self.x-self.width,self.y+self.height-angle_length))
	
	pygame.draw.line(display,(0,0,255),(self.x,self.y),(self.x-self.width,self.y-angle_length))
	pygame.draw.line(display,(0,0,255),(self.x,self.y+self.height),(self.x-self.width,self.y+self.height-angle_length))

	pygame.draw.line(display,(0,0,255),(self.x,self.y),(self.x+self.width,self.y-angle_length))
	pygame.draw.line(display,(0,0,255),(self.x,self.y+self.height),(self.x+self.width,self.y+self.height-angle_length))

	pygame.draw.line(display,(0,0,0),(self.x,self.y-self.height),(self.x+self.width,self.y-angle_length))
	pygame.draw.line(display,(0,0,0),(self.x,self.y-self.height),(self.x-self.width,self.y-angle_length))


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

