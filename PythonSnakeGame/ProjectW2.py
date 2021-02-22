#Pyhton game
import pygame, sys, random, math, time, os
#importing Vector2 will shorten pygame.math.Vector2
from pygame.math import Vector2 


class FRUIT:
	def __init__(self):
		self.randomize()
    #creating size and color.
	def draw_fruit(self):
		fruit_rect = pygame.Rect(int(self.pos.x * cellsize),int(self.pos.y * cellsize),cellsize,cellsize)
		#screen.blit(apple,fruit_rect)
		pygame.draw.rect(screen,(227, 177, 0),fruit_rect)
    #Randomily placing fruit anywhere on screen
	def randomize(self):
		self.x = random.randint(0,cellnum - 1)
		self.y = random.randint(0,cellnum - 1)
		self.pos = Vector2(self.x,self.y)

class SNAKE:
    #creating snake and blocks for the snake
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False
    #drawing it onto the screen, creating color
    def draw_snake(self):
        for block in self.body:
            x_pos = int(block.x * cellsize)
            y_pos = int(block.y * cellsize)
            block_rect = pygame.Rect(x_pos,y_pos, cellsize, cellsize)
            pygame.draw.rect(screen,(0,0,0),block_rect)
    #function to move the snake. 
    def move_snake(self):
        #creating one more block if the snake has eaten a fruit
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        #creates a new block for head. deletes off tail to create same length
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    #runs if snake has eaten fruit
    def add_block(self):
        self.new_block = True
    
    #run if the snake dies
    def reset(self):
        #placing snake into the center of screen
        self.body = [Vector2(5,10), Vector2(4,10),Vector2(3,10)]
        #snake moving
        self.direction = Vector2(1,0)
        global score_text
        #creating font
        endfont = pygame.font.Font(r'Font\font.ttf', 40)
        #rendering fonts to place onto end screen
        endtext = endfont.render("YOU   DIED!",True,(56, 56, 56))
        endtext2 = endfont.render("PRESS   'ENTER'   TO  RESTART!",True,(56, 56, 56))
        #showing the score the player achived
        endscore = endfont.render("FINAL SCORE:  " + score_text,True,(56, 56, 56))
        #pacing on screen using piexels 
        screen.blit(endtext,(300,200))
        screen.blit(endtext2,(170,280))
        screen.blit(endscore,(290,360))
        var = True
        #running to display end screen
        while var:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        main_running = False
                        start_running = True
                        var = False
            #refreashing the page      
            pygame.display.update()
        
                

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.collision()
        self.death()
    #Drawing the elements into the main loop
    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.scoreboard()
    #if snake collides with fruit
    def collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
    #if fruit spawns in body, respawn the page
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
    #if snake hits a wall. gameover!!
    def death(self):
        if not 0 <= self.snake.body[0].x < cellnum or not 0 <= self.snake.body[0].y < cellnum:
            self.gameover()
    #Snake dies if it hits itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.gameover()


    #go to endscreen
    def gameover(self):
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        self.snake.reset()
    #creating score board
    def scoreboard(self):
        global score_text
        #creates score number. body starts with 3 blocks. -3 to start with 0
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 56, 56))
        #placing into bottom right of screen
        score_x = int(cellsize * cellnum - 60)
        score_y = int(cellsize * cellnum - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface, score_rect)

def start_screen():
    #background black
    screen.fill((0,0,0)) 
    #image for start screen
    image = pygame.image.load(r'Photo\start.png')
    screen.blit(image,(100,100))



pygame.init()
#creating size of game screen.
cellsize = 40
cellnum = 20
screen = pygame.display.set_mode((cellnum * cellsize,cellnum * cellsize))
pygame.display.set_caption("First Game")
#calling the clock to start the game
clock = pygame.time.Clock()
#creating game font for score on bottom right
game_font = pygame.font.Font(r'Font\font.ttf', 40)
#game_font = pygame.font.Font(None, 25)

#Creating game speed
SCREEN_UPDATE = pygame.USEREVENT
game_speed = 150
pygame.time.set_timer(SCREEN_UPDATE, game_speed)

main_game = MAIN()
main_running = False
start_running = True
end_running = False


#start loop
while start_running: #start loop
    start_screen()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #starts game when 'enter' is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                main_running = True
                start_running = False
                


    pygame.display.update()


#Creating game loop and movement of snake 
while main_running:

    for event in pygame.event.get(): 
        #allow user to close out of tab
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        #all movement
        #snake cant turn in on itself
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
    #background color of game
    screen.fill(pygame.Color('gold'))
    main_game.draw_elements()
    pygame.display.update()
    #fps of game.
    clock.tick(150)