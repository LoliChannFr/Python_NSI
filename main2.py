import pygame
from tile import *
from settings import *
from player import Player, Bullet
import time
import sys
import run
import select
import button
import json

class Level:
    def __init__(self, level_data, surface, spawn):
        self.display_surface = surface
        self.spawn = spawn
        self.setup(level_data, surface)
        self.world_shift = 0
        
        
    def setup(self, layout_index, screen):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        messages = levelsign[layout_index]
        sign_index = 0
        self.layout_index = layout_index
        layout = levelmap[layout_index]
        self.bullet = pygame.sprite.GroupSingle()
        
        
        
        for row_index,row in enumerate(layout):
            for col_index, cell in enumerate(row): 
                if cell == 'T':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'G':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_ground((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'E':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_earth((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'W':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_wall((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'L':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_sign((x,y),tile_size)
                    tile.sign[1] = messages[sign_index]
                    self.tiles.add(tile)
                    print(sign_index)
                    sign_index = sign_index + 1
                if cell == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    player_sprite = Player((x,y))
                        
                    self.player.add(player_sprite)
                    print(self.spawn)
                if cell == 'S':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_spike((x,y+48),tile_size)
                    self.tiles.add(tile)
                if cell == 'Y':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_s((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'F':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_end((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'B':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Bullet((x,y))
                    self.bullet.add(player_sprite)
                if cell == 'D':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_door((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 'K':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile_key((x,y), tile_size)
                    self.tiles.add(tile)
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx 
        direction_x = player.direction.x
        width, h = pygame.display.get_surface().get_size()
        
        if player_x < width / 3 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        
        elif player_x > width - (width / 2) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        
        else:
            self.world_shift = 0
            player.speed = 5
        
    def horizontal_mouvement_collision(self,screen, level_map):
        player = self.player.sprite
        
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                try: #end
                    if sprite.end:
                        with open("data.json", "r") as f:	#config size screen
                            data = json.load(f)
                            WIDTH = data["WIDTH"]
                            HEIGHT = data["HEIGHT"]
                        text_font = pygame.font.Font(None, 60)  #Text Font
                        white = (255,255,255)
                        text = text_font.render("Level finished !", True, white)
                        textRect = text.get_rect()
                        textRect.center = (WIDTH/2, HEIGHT/2)
                        screen.blit(text, textRect)
                        player.speed = 0
                        player.status = "idle"
                        self.world_shift = 0
                        if player.death == 4:
                            level_map = level_map + 1
                            data["unlock"][0][f"map{level_map}"] = "True"
                            with open (f"data.json", "w") as f:
                                json.dump(data,f)
                            select.main()
                        
                except AttributeError: 
                    
                
                    try:
                        if sprite.key:
                            player.key = player.key + 1
                            sprite.rect.y = sprite.rect.y + 2000
                            
                    except AttributeError:
                        pass
                    
                    try:
                        if sprite.door:
                            if player.key > 0:
                                player.key -= 1
                                sprite.door = False
                                sprite.image = sprite.open_image
                                
                    
                    except AttributeError:
                        pass
                    
                    if sprite.sign[0]:
                        
                        text_font = pygame.font.Font(None, 40)  #Text Font
                        white = (255,255,255)
                        text = text_font.render(sprite.sign[1], True, white)
                        textRect = text.get_rect()
                        textRect.center = (sprite.rect.x, sprite.rect.y - 48)
                        screen.blit(text, textRect)
                        
                    else:    
                        
                        if sprite.damage == True:
                            
                            #Death animation
                            player.status = 'death'
                            if player.death == 20:
                                
                                main(self.layout_index)  
                        
                        else:    

                            try:
                                if sprite.open:
                                    pass
                            except AttributeError: 

                                if player.direction.x < 0:
                                    player.rect.left = sprite.rect.right
                                    if sprite.climb:
                                        player.direction.y = 1
                                        player.double_jump = 1
                                elif player.direction.x > 0:
                                    player.rect.right = sprite.rect.left
                                    if sprite.climb:
                                        player.direction.y = 1
                                        player.double_jump = 1
            else: player.gravity = 0.8
                    
                    
        
    def vertical_mouvement_collision(self,screen, level_map):
        player = self.player.sprite
        player.apply_gravity()
        
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                try:
                    if sprite.end:
                        with open("data.json", "r") as f:	#config size screen
                            data = json.load(f)
                            WIDTH = data["WIDTH"]
                            HEIGHT = data["HEIGHT"]
                        text_font = pygame.font.Font(None, 60)  #Text Font
                        white = (255,255,255)
                        text = text_font.render("Level finished !", True, white)
                        textRect = text.get_rect()
                        textRect.center = (WIDTH/2, HEIGHT/2)
                        screen.blit(text, textRect)
                        player.speed = 0
                        player.status = "win"
                        self.world_shift = 0
                        if player.death == 4:
                            run.main()
                        
                except AttributeError:
                    
                    try:
                        if sprite.key:
                            player.key = player.key + 1
                            sprite.rect.y = sprite.rect.y + 2000
                            
                    except AttributeError:
                        pass
                    
                    try:
                        if sprite.door:
                            if player.key > 0:
                                player.key -= 1
                                sprite.door = False
                                sprite.image = sprite.open_image
                                
                    
                    except AttributeError:
                        pass
                     
                    if sprite.sign[0]:
                        
                        text_font = pygame.font.Font(None, 40)  #Text Font
                        white = (255,255,255)
                        dark = (0,0,0)
                        text = text_font.render(sprite.sign[1], True, white, dark)
                        textRect = text.get_rect()
                        
                        textRect.center = (sprite.rect.x, sprite.rect.y - 48)
                        screen.blit(text, textRect)
                    else:    
                        
                        if sprite.damage == True:
                        #Death animation
                            player.status = 'death'
                        if player.death == 20:
                            main(self.layout_index)  
                            
                        else:
                            try:
                                if sprite.open:
                                    pass
                            except AttributeError:
                                if player.direction.y > 0:
                                    player.rect.bottom = sprite.rect.top
                                    player.direction.y = 0
                                    player.double_jump = 1
                                    player.time = time.time()
                                elif player.direction.y < 0:
                                    player.rect.top = sprite.rect.bottom
                                    player.direction.y = 0
                    
    def bullet_update(self):
        player = self.player.sprite
        bullet = self.bullet.sprite 
        if player.bullet and bullet.Ask_bullet:
            bullet.bullet(player)   
    
    def run(self,screen, level_map):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.bullet_update()
        self.bullet.update()
        self.bullet.draw(self.display_surface)
        self.scroll_x()
        
        self.player.update()
        self.horizontal_mouvement_collision(screen, level_map)
        self.vertical_mouvement_collision(screen, level_map)
        self.player.draw(self.display_surface)
        
        with open("data.json", "r") as f:	#config size screen
            data = json.load(f)
            WIDTH = data["WIDTH"]
            HEIGHT = data["HEIGHT"]
        
        
        # Text
        text_font = pygame.font.Font(None, 40)	#Text Font
        white = (255,255,255)
        text = text_font.render(f'Level {level_map}', True, white)
        # create a rectangular object for the text
        textRect = text.get_rect()
        textRect.center = (WIDTH - (WIDTH-80) , HEIGHT - (HEIGHT-20))
        screen.blit(text, textRect)
        
        # Text
        text_font = pygame.font.Font(None, 40)	#Text Font
        white = (255,255,255)
        text = text_font.render(f'Keys : {self.player.sprite.key}', True, white)
        # create a rectangular object for the text
        textRect = text.get_rect()
        textRect.center = (WIDTH - (WIDTH-300) , HEIGHT - (HEIGHT-20))
        screen.blit(text, textRect)


def main(level_map):
    def buttons_draw(screen):
        for b in buttons:
            b.draw(screen)

    pygame.init()
    pygame.display.set_caption('NekoDarkLand')	#window title

    buttons = []
    
    with open("data.json", "r") as f:	#config size screen
        data = json.load(f)
        WIDTH = data["WIDTH"]
        HEIGHT = data["HEIGHT"]
        FULL = data["FULL"]

    if FULL == "None":	
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
    else:
        screen = pygame.display.set_mode()
        WIDTH, HEIGHT = screen.get_size()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    spawn = "null"
    level = Level(level_map, screen, spawn)

    bg = pygame.image.load("./alien/background.jpg")
    pause = pygame.image.load("./game-image/pause.png")

	#button position
    w1= WIDTH/2					#column button
    h1 = HEIGHT/2-100			#First lign (resume)

    #buttons
    button1 = button.Button('Resume', 200, 40, (w1, h1), 5)      #resume
    button2 = button.Button('Menu', 200, 40, (w1, h1+50), 5)	    #menu redirection
    button3 = button.Button('Exit', 200, 40, (w1, h1+100), 5)	#exit game
    buttons.append(button1)
    buttons.append(button2)
    buttons.append(button3)
    
    RUNNING, PAUSE = 0, 1
    state = RUNNING

    pause_text = pygame.font.SysFont('Consolas', 32).render('Pause', True, pygame.color.Color('White'))

    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if state == RUNNING:
                    if event.key == pygame.K_ESCAPE:
                        state = PAUSE
                else:
                    if event.key == pygame.K_ESCAPE:
                        state = RUNNING
        else:
            screen.fill((0, 0, 0))

            if state == RUNNING:
                screen.fill('black')
                screen.blit(bg,(0,0))
                level.run(screen, level_map)
                screen.blit(pause,(WIDTH-70, HEIGHT-(HEIGHT-20)))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:	#Check click button and react
                        if WIDTH-70 <= mouse[0] <= WIDTH-70+53 and HEIGHT-(HEIGHT-20) <= mouse[1] <= HEIGHT-(HEIGHT-20)+55: #pause buton
                            state = PAUSE
                            time.sleep(0.3)

            elif state == PAUSE:
                screen.blit(pause_text, (WIDTH/2-48, 100))     #text "pause"
                screen.blit(pause,(WIDTH-70, HEIGHT-(HEIGHT-20)))   #pause button
                # buttons_draw(screen)	#show button

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:	#Check click button and react
                        if WIDTH-70 <= mouse[0] <= WIDTH-70+53 and HEIGHT-(HEIGHT-20) <= mouse[1] <= HEIGHT-(HEIGHT-20)+55: #pause buton
                            state = RUNNING
                            time.sleep(0.3)

            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    spawn = "null"
    main(spawn)
