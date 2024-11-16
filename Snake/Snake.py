import pygame, sys, random, time
from pygame.math import Vector2


class SNAKE: # creates a class called SNAKE
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)] # creates 3 vectors of the snake's body
        self.direction = Vector2(0,0) # creates a vector of the snake's direction
        self.new_block = False # attribute snake has not collided with apple

        self.head_up = pygame.image.load("Graphics/head_up.png").convert_alpha()
        self.head_down = pygame.image.load("Graphics/head_down.png").convert_alpha()
        self.head_right = pygame.image.load("Graphics/head_right.png").convert_alpha()
        self.head_left = pygame.image.load("Graphics/head_left.png").convert_alpha()

        self.tail_up = pygame.image.load("Graphics/tail_up.png").convert_alpha()
        self.tail_down = pygame.image.load("Graphics/tail_down.png").convert_alpha()
        self.tail_right = pygame.image.load("Graphics/tail_right.png").convert_alpha()
        self.tail_left = pygame.image.load("Graphics/tail_left.png").convert_alpha()

        self.body_horizontal = pygame.image.load("Graphics/body_horizontal.png").convert_alpha()
        self.body_vertical = pygame.image.load("Graphics/body_vertical.png").convert_alpha()

        self.body_tr = pygame.image.load("Graphics/body_tr.png").convert_alpha()
        self.body_tl = pygame.image.load("Graphics/body_tl.png").convert_alpha()
        self.body_br = pygame.image.load("Graphics/body_br.png").convert_alpha()
        self.body_bl = pygame.image.load("Graphics/body_bl.png").convert_alpha()

        self.crunch_sound = pygame.mixer.Sound("Sound/crunch.wav")

    def draw_snake(self):
            
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cellSize) # x position of each vector of each block
            y_pos = int(block.y * cellSize) # y position of each vector of each block
            blockRect = pygame.Rect((x_pos, y_pos, cellSize, cellSize))
            
            if index == 0:
                screen.blit(self.head, blockRect)

            elif index == (len(self.body) - 1): # length of the snake - 1 as index starts at 0
                screen.blit(self.tail, blockRect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, blockRect)
                
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, blockRect)

                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, blockRect)

                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, blockRect)
                    
                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, blockRect)

                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, blockRect)
                    
                     
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): # if snake is moving left: snake head vector is (x,y), snake body vector is (x+1, y), thus head_relation is (x+1,y) - (x,y) = (1,0)
            self.head = self.head_left
        
        elif head_relation == Vector2(-1,0): # if snake is moving right: snake head vector is (x,y), snake body vector is (x-1,y), thus head_relation is (x-1,y) - (x,y) = (-1,0)
            self.head = self.head_right
        
        elif head_relation == Vector2(0,1): # if snake is moving up: snake head vector is (x,y), snake body vector is (x,y+1) because increasing y in python, moves vectors down, thus head_relation is (x,y+1) - (x,y) = (0,1)
            self.head = self.head_up

        elif head_relation == Vector2(0,-1): # if snake is moving down: snake head vector is (x,y), snake body vector is (x,y-1) because decreasing y in python moves vectors up, thus head_relation is (x,y-1) - (x,y) = (0,-1)
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): # if snake is moving left: snake head vector is (x,y), snake body vector is (x+1, y), thus head_relation is (x+1,y) - (x,y) = (1,0)
            self.tail = self.tail_left
        
        elif tail_relation == Vector2(-1,0): # if snake is moving right: snake head vector is (x,y), snake body vector is (x-1,y), thus head_relation is (x-1,y) - (x,y) = (-1,0)
            self.tail = self.tail_right
        
        elif tail_relation == Vector2(0,1): # if snake is moving up: snake head vector is (x,y), snake body vector is (x,y+1) because increasing y in python, moves vectors down, thus head_relation is (x,y+1) - (x,y) = (0,1)
            self.tail = self.tail_up

        elif tail_relation == Vector2(0,-1): # if snake is moving down: snake head vector is (x,y), snake body vector is (x,y-1) because decreasing y in python moves vectors up, thus head_relation is (x,y-1) - (x,y) = (0,-1)
            self.tail = self.tail_down
        

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:] # makes a copy of the snake's body vectors
            body_copy.insert(0, body_copy[0] + self.direction) # requires (index, vectors + direction), inserts a new vector at index 0
                                                            # which is the snake head's new vector position. 
            self.body = body_copy[:]
            self.new_block = False

        else:
            body_copy = self.body[:-1] # makes a copy of the snake's body vectors - only the first and second vector
            body_copy.insert(0, body_copy[0] + self.direction) # requires (index, vectors + direction), inserts a new vector at index 0
                                                            # which is the snake head's new vector position. 
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True # if snake has collided with apple

    def play_crunch_sound(self):
        self.crunch_sound.play()
    
    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        

class FRUIT: # creates a class called FRUIT
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruitRect= pygame.Rect((int(self.pos.x * cellSize)), int((self.pos.y * cellSize)), cellSize, cellSize) # requires (x, y, width, height)
        screen.blit(apple, fruitRect)
        #pygame.draw.rect(screen, (126, 166, 114), fruitRect) # requires (surface, colour, specified rectangle)

    def randomize(self):
        self.x = random.randint(0, cellNumber - 1) # random x position of fruit
        self.y = random.randint(0, cellNumber - 1) # random y position of fruit
        self.pos = Vector2(self.x, self.y) # creates an attribute of the position of the fruit as a vector

class MAIN: # creates a class called MAIN
    def __init__(self):
        self.snake = SNAKE() # self.snake inheritS attributes of the clasW SNAKE()
        self.fruit = FRUIT() # self.fruit inherits attributes of the class FRUIT()
    
    def update(self): 
        self.snake.move_snake() # calls the move_snake function in the class SNAKE()
        self.check_collision() # calls the check_collision function created in this class
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]: # if the fruit's position is equal to the snake head's position
            self.fruit.randomize() # calls the randomize function in the class FRUIT() - reposiion the snake
            self.snake.add_block() # calls the add_block function in the class SNAKE()
            self.snake.play_crunch_sound() # calls the play_crunch_sound function in the class SNAKE() 

        for block in self.snake.body[1:]: # for each block in the snake's body except the head
            if block == self.fruit.pos: # if the block's position is equal to the fruit's position
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cellNumber or not 0 <= self.snake.body[0].y < cellNumber: # if snake head's x or y position is not within the grid
            self.game_over()
            self.fruit.randomize()

        for block in self.snake.body[1:]: # for each block in the snake's body except the head
            if block == self.snake.body[0]: # if the block's position is equal to the snake head's position
                self.game_over() 

            else:
                pass                

    def game_over(self):
        self.snake.reset()
    
    def draw_grass(self): 
        grass_color = (167,209,61) 

        for row in range(cellNumber): # for each row in the grid
            if row % 2 == 0: # if row is even
                for col in range(cellNumber): # for each column in the row
                    if col % 2 == 0: # if column is even
                        grass_rect = pygame.Rect(col * cellSize, row * cellSize, cellSize, cellSize) # requires (x, y, width, height) 
                        pygame.draw.rect(screen, grass_color, grass_rect) # requires (surface, colour, specified rectangle)

            else:
                for col in range(cellNumber):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cellSize, row * cellSize, cellSize, cellSize)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3 ) # score is the length of the snake's body - 3
        score_surface = game_font.render(score_text, True, (56,74,12)) # requires (text, anti-aliasing, colour)
        score_x = int(cellSize * cellNumber - 60) # x position of the score 
        score_y = int(cellSize * cellNumber - 40) # y position of the score
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left - 10, score_rect.centery)) # requires (position), we place the midright of the apple image at the left of the score_rect and the centery of the score_rect
        bg_rect = pygame.Rect(apple_rect.left - 5, apple_rect.top, apple_rect.width + score_rect.width + 20, apple_rect.height) # requires (x, y, width, height) - creates a rectangle behind the score and apple image

        pygame.draw.rect(screen, (167,209,61), bg_rect) # requires (surface, colour, specified rectangle)
        screen.blit(score_surface, score_rect) # requires (surface, position)
        screen.blit(apple, apple_rect) # requires (surface, position)
        pygame.draw.rect(screen, (56,74,12), bg_rect, 2) # requires (surface, colour, specified rectangle, thickness)

pygame.mixer.pre_init(44100, -16, 2, 512) # requires (frequency, size, channels, buffersize) - pre-initialises the mixer module for pygame.mixer.init()
pygame.init()

cellSize = 40 # number of pixels a cell takes up
cellNumber = 20 # number of cells/blocks in total 

screen = pygame.display.set_mode((((cellNumber * cellSize), (cellNumber * cellSize)))) # display surface which created elements are generated on
clock = pygame.time.Clock() # clock object which controls the fps the game runs at
apple = pygame.image.load("Graphics/apple.png").convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25) # requires (font, size) - creates a font object

SCREEN_UPDATE = pygame.USEREVENT # creates custom user event called SCREEN_UPDATE
pygame.time.set_timer(SCREEN_UPDATE, 150) # requires(event, time in ms), allowing for the event to be on a timer. 

main_game = MAIN() # main_game inherits the attributes of the class MAIN()

while True:
    for event in pygame.event.get(): # checks for all events/actions done by user
        if event.type == pygame.QUIT: # if user closes the window
            pygame.quit()
            sys.exit()
        
        if event.type == SCREEN_UPDATE:
            main_game.update() # calls the update function in the class MAIN() everytime the event SCREEN_UPDATE occurs.
        
        if event.type == pygame.KEYDOWN: # if user presses arrow keys
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1) # moves snake up 1 block

            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0) # moves snake right 1 block
            
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1) # moves snake down 1 block
            
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0) # moves snake left 1 block

        


    screen.fill((175, 215, 70)) # requires (colour) - fills the screen with the colour specified
    main_game.draw_elements() 
    pygame.display.update() # updates the display surface
    clock.tick(60) # sets the fps of the game to 60

