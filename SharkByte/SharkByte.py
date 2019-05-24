'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
SharkByte
Version 1.0

Description:
SharkByte is a 2D based game using pygame, a python module.
The player is given a shark avatar and they must devour the delicious fish before they manage to escape.
The health continuously decreases and the only way to regain it is to eat as many fish as quickly as possible.
There will be some poisonous fish and trash mixed in so you will have to take precautions and avoid them.
Remember: You do not have to eat all of the fish if you are not capable enough.
'''

import pygame
import sys
import random
import time

def newGame():
    #colors
    entity_color = (255, 255, 255)
    hcolor =  (0,0,205)
    YELLOW = (255,255,0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    global lives
    lives = 3
    global score
    score = 0
    global xx
    xx=250

    turtlewing777 = 'underwater.png'
    #speed of the fishes limiter
    spedcount = 0
    spedcount2 = 0
    spedcount3 = 0
    AFKcount = 10

    fish_list = []
    fish_list2 = []
    fish_list3 = []
    fish_list4 = []
    pfish_list = []
    pfish_list2 = []
    pfish_list3 = []
    trash_list = []
    trash_list2 = []
    trash_list3 = []

    global spedIncr
    spedIncr = 5.6 #begenning speed of fish/trash - changes as game goes on

    newLevel = 50  # for when you have to make the fishes faster
    newFish = newLevel

    def draw_text(surf, text, font_size, x, y): #for showing higscores
        font = pygame.font.Font(None, font_size)
        text_surface = font.render(text, True, hcolor)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)

    class Background(pygame.sprite.Sprite):  # game background
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    class Background2(pygame.sprite.Sprite):  # game background
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    class Background3(pygame.sprite.Sprite):  # game background
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    class Background4(pygame.sprite.Sprite):  # game background
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location
    class Background5(pygame.sprite.Sprite):  # game background
        def __init__(self, image_file, location):
            pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
            self.image = pygame.image.load(image_file)
            self.rect = self.image.get_rect()
            self.rect.left, self.rect.top = location

    class Entity(pygame.sprite.Sprite):
        """Inherited by any object in the game."""

        def __init__(self, x, y, width, height):
            pygame.sprite.Sprite.__init__(self)

            self.x = x
            self.y = y
            self.width = width
            self.height = height
            # This makes a rectangle around the entity, used for anything
            # from collision to moving around.
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    class Shark(Entity):
        """
        Player controlled or AI controlled, main interaction with
        the game
        """

        def __init__(self, x, y, width, height):
            super(Shark, self).__init__(x, y, width, height)

            self.image = sharkImg #makes shark accessible to player class
    class Player(Shark):
        """The player controlled Shark"""

        def __init__(self, x, y, width, height):
            super(Player, self).__init__(x, y, width, height)

            # How many pixels the Player Shark should move on a given frame.
            self.y_change = 0
            self.x_change = 0
            # How many pixels the Shark should move each frame a key is pressed.
            self.y_dist = 5
            self.x_dist = 5

        def MoveKeyDown(self, key): #up, down, left, right of shark
            """Responds to a key-down event and moves accordingly"""

            if (key == pygame.K_UP):
                self.y_change += -self.y_dist

            elif (key == pygame.K_DOWN):
                self.y_change += self.y_dist
            elif (key == pygame.K_RIGHT):
                self.x_change += self.x_dist

            elif (key == pygame.K_LEFT):
                self.x_change += -self.x_dist


        def MoveKeyUp(self, key): #up, down, left, right of shark
            """Responds to a key-up event and stops movement accordingly"""

            if (key == pygame.K_UP):
                self.y_change += self.y_dist

            elif (key == pygame.K_DOWN):
                self.y_change += -self.y_dist
            elif (key == pygame.K_RIGHT):
                self.x_change += -self.x_dist

            elif (key == pygame.K_LEFT):
                self.x_change += self.x_dist



        def update(self):
            """
            Moves the Shark while ensuring it stays in bounds
            """
            # Moves it relative to its current location.
            self.rect.move_ip(0, self.y_change)
            self.rect.move_ip(self.x_change, 0)

            # If the Destroyer moves off the screen, put it back on.
            if self.rect.y < 30:
                self.rect.y = 30
            elif self.rect.y > (window_height - self.height)+10: #since there is a invisible box around shark makes sure the actual shark thing can reach bottom
                self.rect.y = (window_height - self.height)+10

            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > (window_width - self.width)-90: #since there is a invisible box around shark makes sure the actual shark thing can reach bottom
                self.rect.x = (window_width - self.width)-90

    class Fish(Entity):
        """
        The Fish!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Fish, self).__init__(x, y, width, height)

            self.image = fishImg1
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Fish2(Entity):
        """
        The Fish!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Fish2, self).__init__(x, y, width, height)

            self.image = fishImg2
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Fish3(Entity):
        """
        The Fish!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Fish3, self).__init__(x, y, width, height)

            self.image = fishImg3
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Fish4(Entity):
        """
        The Fish!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Fish4, self).__init__(x, y, width, height)

            self.image = fishImg4
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Pfish(Entity):
        """
        The Poisonous Fish!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Pfish, self).__init__(x, y, width, height)

            self.image = pfishImg1
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Pfish2(Entity):
        """
        The Poisonous Fish!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Pfish2, self).__init__(x, y, width, height)

            self.image = pfishImg2
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Pfish3(Entity):
        """
        The Poisonous Fish!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Pfish3, self).__init__(x, y, width, height)

            self.image = pfishImg3
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Trash(Entity):
        """
        The Trash!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Trash, self).__init__(x, y, width, height)

            self.image = trashImg1
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Trash2(Entity):
        """
        The Trash!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Trash2, self).__init__(x, y, width, height)

            self.image = trashImg2
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr
    class Trash3(Entity):
        """
        The Trash!  Moves around the screen.
        """

        def __init__(self, x, y, width, height):
            super(Trash3, self).__init__(x, y, width, height)

            self.image = trashImg3
            # Asteroid speed
            self.x_direction = -5

            self.speed = .3

        def update(self):
            # Moves the asteroid left
            self.rect.x -= spedIncr

    def DatHitTho(all): #Checks to see if if shark collided with fish and removes fish
        global score
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and fish collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj2.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    score += 3 #increases score by 3 if shark eats fish
                    xx += 3
    def DatHitTho2(all): #Checks to see if if shark collided with fish and removes fish
        global score
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and fish collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj2.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    score += 5
                    xx += 5
    def DatHitTho3(all): #Checks to see if if shark collided with fish and removes fish
        global score
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and fish collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+150) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj2.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    score += 7
                    xx += 7
    def DatHitTho4(all): #Checks to see if if shark collided with fish and removes fish
        global xx
        global score
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and fish collide by using coordinates
                if a.rect.y < (player.rect.bottom-100)and a.rect.y > (player.rect.y+10) and a.rect.x > (player.rect.x+100) and a.rect.x < (player.rect.x+250): #makes sure fish and shark collide within proper y coordiantes
                    soundObj2.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    score -= 15
                    if xx < 250 and xx > 0:#so player can't go over HP limit and cant get HP back after lost all HP
                        xx += 15
    def pDatHitTho(all): #Checks to see if if shark collided with fish and removes fish
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and fish collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    xx -= 9
    def pDatHitTho2(all): #Checks to see if if shark collided with fish and removes fish
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and fish collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    xx -= 13
    def pDatHitTho3(all): #Checks to see if if shark collided with fish and removes fish
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and fish collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    xx -= 15
    def tDatHitTho(all): #Checks to see if if shark collided with fish and removes fish
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and trash collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    xx -= 11
    def tDatHitTho2(all): #Checks to see if if shark collided with fish and removes fish
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and trash collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    xx -= 15
    def tDatHitTho3(all): #Checks to see if if shark collided with fish and removes fish
        global xx
        for a in all:
            if a.rect.colliderect(player.rect):
                #the if statement below checks to see if the shark and trash collide by using coordinates
                if a.rect.y < (player.rect.bottom-40) and a.rect.y > (player.rect.y+40) and a.rect.x > (player.rect.x+190) and a.rect.x < (player.rect.x+230): #makes sure fish and shark collide within proper y coordiantes
                    soundObj.play()
                    all.remove(a)
                    a.remove(all_sprites_list)
                    xx -= 17

    pygame.init()

    # screen info
    window_width = 1300
    window_height = 732
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("SharkByte")
    clock = pygame.time.Clock()
    screen.fill([255, 255, 255])

    #images
    BackGround = Background(turtlewing777, [0, 0])
    BackGround2 = Background2('oceanfloor.png', [0, 0])
    BackGround3 = Background2('underwater2.png', [0, 0])
    BackGround4 = Background2('underwater3.png', [0, 0])
    BackGround5 = Background2('underwater4.png', [0, 0])
    sharkImg = pygame.image.load('shark.png')  # uploads shark pic
    sharkImg = pygame.transform.scale(sharkImg, (290, 145))
    fishImg1 = pygame.image.load('fish1.png') # uploads good fish pic
    fishImg1 = pygame.transform.scale(fishImg1, (65, 49))

    # sprites,lists
    player = Player(0, 130, 220, 160)
    fishU = Fish(window_width, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
    fish_list.append(fishU)
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(player)
    all_sprites_list.add(fishU)

    #text
    basicfont = pygame.font.SysFont(None, 35)  # 35 is font size, no font type
    basicfont2 = pygame.font.SysFont(None, 35)  # 35 is font size, no font type

    # music
    pygame.mixer.music.load('underwater_sound.mp3')  # imports the music
    pygame.mixer.music.play(-1, 0.0)  # duration of the music, in this case -1 means forever
    pygame.mixer.music.set_volume(0.5)
    soundObj = pygame.mixer.Sound('gagging.wav')  # imports the music on standby
    soundObj.set_volume(0.5)
    soundObj2 = pygame.mixer.Sound('gulp.wav') # imports the music on standby
    soundObj2.set_volume(0.5)
    soundObj4 = pygame.mixer.Sound('Fail.wav')  # imports the music on standby

    #start screen
    end_it = False
    while (end_it == False):
        screen.blit(BackGround2.image, BackGround2.rect)
        myfont = pygame.font.SysFont(None, 40)
        myfont2 = pygame.font.SysFont(None, 20)
        nlabel = myfont.render("Welcome to SharkByte!", 1, (entity_color))
        nLabel2 = myfont.render("Ever wanted to become the main predator?", 1, (entity_color))
        nLabel3 = myfont.render("Now's your chance!", 1, (entity_color))
        nLabel4 = myfont.render("Become a shark and devour the delicious fishies before they manage to escape.", 1, (entity_color))
        nLabel7 = myfont.render("After all, they boost the continuously decreasing health.", 1, (entity_color))
        nLabel5 = myfont.render("But beware of the poisonous fish and trash mixed in...", 1, (entity_color))
        nLabel6 = myfont.render("Left click the mouse to get started!", 1, (entity_color))
        fLabel1 = myfont2.render("Fish carcass (-9 health)", 1, (entity_color))
        fLabel2 = myfont2.render("Poisonous fish (-13 health)", 1, (entity_color))
        fLabel3 = myfont2.render("Poisonous fish (-15 health)", 1, (entity_color))
        tLabel1 = myfont2.render("Trash (-11 health)", 1, (entity_color))
        tLabel2 = myfont2.render("Trash (-15 health)", 1, (entity_color))
        tLabel3 = myfont2.render("Trash (-17 health)", 1, (entity_color))
        SSLabel1 = myfont2.render("Regular Fish (+3 score, +3 health)", 1, (entity_color))
        SSLabel2 = myfont2.render("Regular Fish (+5 score, +5 health)", 1, (entity_color))
        SSLabel3 = myfont2.render("Regular Fish (+7 score, +7 health)", 1, (entity_color))
        SSSLabel = myfont2.render("Special Fish (+15 health, ", 10, (entity_color))
        SSSLabel2 = myfont2.render("-15 score if it goes offscreen)", 10, (entity_color))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #so game doesnt get all glitchy when you try to exit without this code
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: # Left mouse button.
                    end_it = True #stops the while true

        Sfish = pygame.image.load('pfish1.png')  # uploads fish pic
        Sfish = pygame.transform.scale(Sfish, (60, 42))
        screen.blit(Sfish,(0,320))
        Sfish2 = pygame.image.load('pfish2.png')  # uploads fish pic
        Sfish2 = pygame.transform.scale(Sfish2, (100, 44))
        screen.blit(Sfish2,(0,370))
        Sfish3 = pygame.image.load('pfish3.png')  # uploads fish pic
        Sfish3 = pygame.transform.scale(Sfish3, (60, 49))
        screen.blit(Sfish3,(0,440))
        Strash = pygame.image.load('trash1.png')  # uploads trash pic
        Strash = pygame.transform.scale(Strash, (45, 33))
        screen.blit(Strash,(0,520))
        Strash2 = pygame.image.load('trash2.png')  # uploads trash pic
        Strash2 = pygame.transform.scale(Strash2, (45, 33))
        screen.blit(Strash2,(0,580))
        Strash3 = pygame.image.load('trash3.png')  # uploads trash pic
        Strash3 = pygame.transform.scale(Strash3, (45, 33))
        screen.blit(Strash3,(0,640))
        SSfish = pygame.image.load('fish1.png')  # uploads fish pic
        SSfish = pygame.transform.scale(SSfish, (60, 42))
        screen.blit(SSfish,(1000,320))
        SSfish2 = pygame.image.load('fish2.png')  # uploads fish pic
        SSfish2 = pygame.transform.scale(SSfish2, (60, 42))
        screen.blit(SSfish2,(1000,380))
        SSfish3 = pygame.image.load('fish3.png')  # uploads fish pic
        SSfish3 = pygame.transform.scale(SSfish3, (60, 42))
        screen.blit(SSfish3,(1000,440))
        SSSfish = pygame.image.load('fish4.png')  # uploads fish pic
        SSSfish = pygame.transform.scale(SSSfish, (120, 90))
        screen.blit(SSSfish,(970,470))

        #blits make the images appear on the GUI
        screen.blit(nlabel,(500,1))
        screen.blit(nLabel2,(370,50))
        screen.blit(nLabel3,(540,100))
        screen.blit(nLabel4,(170,150))
        screen.blit(nLabel7,(340,200))
        screen.blit(nLabel5,(350,250))
        screen.blit(nLabel6,(420,445))
        screen.blit(fLabel1,(80,335))
        screen.blit(fLabel2,(120,390))
        screen.blit(fLabel3,(80,460))
        screen.blit(tLabel1,(60,530))
        screen.blit(tLabel2,(60,590))
        screen.blit(tLabel3,(60,650))
        screen.blit(SSLabel1,(1068,330))
        screen.blit(SSLabel2,(1070,397))
        screen.blit(SSLabel3,(1070,456))
        screen.blit(SSSLabel,(1070,512))
        screen.blit(SSSLabel2,(1070,540))

        pygame.display.flip()

    while True: #main loop
        DatHitTho(fish_list) #if shark hit fish
        DatHitTho2(fish_list2) #if shark hit fish
        DatHitTho3(fish_list3) #if shark hit fish
        DatHitTho4(fish_list4) #if shark hit fish
        pDatHitTho(pfish_list) #if shark hit poisonous fish
        pDatHitTho2(pfish_list2) #if shark hit poisonous fish
        pDatHitTho3(pfish_list3) #if shark hit poisonous fish
        tDatHitTho(trash_list) #if shark hit trash
        tDatHitTho2(trash_list2) #if shark hit trash
        tDatHitTho3(trash_list3) #if shark hit trash

        ranFish = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #there is a random chance for the fishes to appear, mostly regular blue fish appear
        chosenFish = random.choice(ranFish)
        poison = [1,2,3,4,5,6] #random poisonous fish lottery
        chosenpoison = random.choice(poison)

        if newFish <= 0:  # Creates fish/trash after set amount of time
            #makes so that bunch of fish/trash can't appear at the same time
            if len(fish_list) < 3 and len(fish_list2) < 3 and len(fish_list3) < 3 and len(fish_list4) < 3 and len(trash_list) < 3 and len(trash_list2) < 3 and len(trash_list3) < 3 and len(pfish_list) < 3 and len(pfish_list2) < 3 and len(pfish_list3) < 3:
                if score >= 75:
                    if random.random() < .05: #5 percent chance that a special fish will appear
                        fishImg4 = pygame.image.load('fish4.png')  # uploads good fish pic
                        fishImg4 = pygame.transform.scale(fishImg4, (175, 131))
                        fishImg4 = Fish4(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                        fish_list4.append(fishImg4)
                        all_sprites_list.add(fishImg4)
                        newLevel -= .5  # each time an fish is formed we make it shorter until next is made
                        newFish = newLevel
                if chosenFish == 1 or chosenFish == 2 or chosenFish == 3 or chosenFish == 4 or chosenFish == 5 or chosenFish == 11:
                    x = Fish(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                    fish_list.append(x)
                    all_sprites_list.add(x)
                    newLevel -= .5  # each time an fish is formed we make it shorter until next is made
                    newFish = newLevel

                if score >= 50:
                    if chosenFish == 6 or chosenFish == 7 or chosenFish == 8:
                        fishImg2 = pygame.image.load('fish2.png')  # uploads good fish pic
                        fishImg2 = pygame.transform.scale(fishImg2, (75, 46))
                        fishImg2 = Fish2(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                        fish_list2.append(fishImg2)
                        all_sprites_list.add(fishImg2)
                        newLevel -= .5  # each time an fish is formed we make it shorter until next is made
                        newFish = newLevel
                    elif chosenFish == 9 or chosenFish == 10:
                        fishImg3 = pygame.image.load('fish3.png')  # uploads good fish pic
                        fishImg3 = pygame.transform.scale(fishImg3, (85, 64))
                        fishImg3 = Fish3(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                        fish_list3.append(fishImg3)
                        all_sprites_list.add(fishImg3)
                        newLevel -= .5  # each time an fish is formed we make it shorter until next is made
                        newFish = newLevel

                if score >= 150:
                    if chosenpoison == 1:
                        pfishImg1 = pygame.image.load('pfish1.png')  # uploads poisonous fish pic
                        pfishImg1 = pygame.transform.scale(pfishImg1, (60, 42))
                        pfishImg1 = Pfish(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                        pfish_list.append(pfishImg1)
                        all_sprites_list.add(pfishImg1)
                        newLevel -= .5  # each time an fish is formed we make it shorter until next is made
                        newFish = newLevel
                    elif chosenpoison == 2:
                        pfishImg2 = pygame.image.load('pfish2.png')  # uploads poisonous fish pic
                        pfishImg2 = pygame.transform.scale(pfishImg2, (100, 44))
                        pfishImg2 = Pfish2(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                        pfish_list2.append(pfishImg2)
                        all_sprites_list.add(pfishImg2)
                        newLevel -= .5  # each time an fish is formed we make it shorter until next is made
                        newFish = newLevel
                    elif chosenpoison == 3:
                        pfishImg3 = pygame.image.load('pfish3.png')  # uploads poisonous fish pic
                        pfishImg3 = pygame.transform.scale(pfishImg3, (60, 49))
                        pfishImg3 = Pfish3(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                        pfish_list3.append(pfishImg3)
                        all_sprites_list.add(pfishImg3)
                        newLevel -= .5  # each time an fish is formed we make it shorter until next is made
                        newFish = newLevel

                    if score >= 300:
                        if chosenpoison == 4:
                            trashImg1 = pygame.image.load('trash1.png')  # uploads trash pic
                            trashImg1 = pygame.transform.scale(trashImg1, (45, 33))
                            trashImg1 = Trash(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                            trash_list.append(trashImg1)
                            all_sprites_list.add(trashImg1)
                            newLevel -= .5  # each time an trash is formed we make it shorter until next is made
                            newFish = newLevel
                        elif chosenpoison == 5:
                            trashImg2 = pygame.image.load('trash2.png')  # uploads trash pic
                            trashImg2 = pygame.transform.scale(trashImg2, (45, 33))
                            trashImg2 = Trash2(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                            trash_list2.append(trashImg2)
                            all_sprites_list.add(trashImg2)
                            newLevel -= .5  # each time an trash is formed we make it shorter until next is made
                            newFish = newLevel
                        elif chosenpoison == 6:
                            trashImg3 = pygame.image.load('trash3.png')  # uploads trash pic
                            trashImg3 = pygame.transform.scale(trashImg3, (45, 33))
                            trashU3 = Trash3(window_width - 1, random.randint(80, window_height - 100), 100,73)  # 100 and 73 are the actual dimensions of the image
                            trash_list3.append(trashU3)
                            all_sprites_list.add(trashU3)
                            newLevel -= .5  # each time an trash is formed we make it shorter until next is made
                            newFish = newLevel

        # check for the QUIT event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                player.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                player.MoveKeyUp(event.key)

        for ent in all_sprites_list:
            ent.update()

        #checks to see if images off screen
        for fishy in fish_list:
            if fishy.rect.x <= 0:
                all_sprites_list.remove(fishy)
                fish_list.remove(fishy)
        for fishy2 in fish_list2:
            if fishy2.rect.x <= 0:
                all_sprites_list.remove(fishy2)
                fish_list2.remove(fishy2)
        for fishy3 in fish_list3:
            if fishy3.rect.x <= 0:
                all_sprites_list.remove(fishy3)
                fish_list3.remove(fishy3)
        for fishy4 in fish_list4:
            if fishy4.rect.x <= -40:
                all_sprites_list.remove(fishy4)
                fish_list4.remove(fishy4)
        for pfishy in pfish_list:
            if pfishy.rect.x <= 0:
                all_sprites_list.remove(pfishy)
                pfish_list.remove(pfishy)
        for pfishy2 in pfish_list2:
            if pfishy2.rect.x <= 0:
                all_sprites_list.remove(pfishy2)
                pfish_list2.remove(pfishy2)
        for pfishy3 in pfish_list3:
            if pfishy3.rect.x <= 0:
                all_sprites_list.remove(pfishy3)
                pfish_list3.remove(pfishy3)
        for trashy in trash_list:
            if trashy.rect.x <= 0:
                all_sprites_list.remove(trashy)
                trash_list.remove(trashy)
        for trashy2 in trash_list2:
            if trashy2.rect.x <= 0:
                all_sprites_list.remove(trashy2)
                trash_list2.remove(trashy2)
        for trashy3 in trash_list3:
            if trashy3.rect.x <= 0:
                all_sprites_list.remove(trashy3)
                trash_list3.remove(trashy3)

        #changing backgrounds and increasing speed
        if score >= 50 and score < 150:
            if spedcount == 0: #so fish speed doesn't keep increasing .7 over and over causing fish to go extremely fast
                spedIncr += .7 #fish speed increased by
                spedcount +=1
            screen.blit(BackGround3.image, BackGround3.rect)  # blits to screen. this allows the player to actually see them
        elif score >= 150 and score < 300:
            if spedcount2 == 0: #so fish speed doesn't keep increasing .7 over and over causing fish to go extremely fast
                spedIncr += .7 #fish speed increased by
                spedcount2 +=1
            screen.blit(BackGround4.image, BackGround4.rect)  # blits to screen. this allows the player to actually see them
        elif score >= 300:
            if spedcount3 == 0: #so fish speed doesn't keep increasing .7 over and over causing fish to go extremely fast
                spedIncr += .7 #fish speed increased by
                spedcount3 +=1
            screen.blit(BackGround5.image, BackGround5.rect)  # blits to screen. this allows the player to actually see them
        else:
            screen.blit(BackGround.image, BackGround.rect) #blits to screen. this allows the player to actually see them

        #health bar
        if xx <= 125 and xx > 50:
            GREEN = YELLOW
        elif xx <= 50 and xx > 0:
            GREEN = RED
        if xx > 0:
            pygame.draw.rect(screen, GREEN, (1000, 10, xx, 27), 0)

        #score, health blits
        text = basicfont.render("Score: "+str(score), True, BLUE, (BackGround.image, BackGround.rect))  # first set of parenthesis is the font color, second set is the background of the words
        screen.blit(text, (50, 10))
        text = basicfont2.render("Health: ", True, GREEN, (BackGround.image, BackGround.rect))  # first set of parenthesis is the font color, second set is the background of the words
        screen.blit(text, (900, 13))

        #if player loses all their health
        if xx <= 0:
            try:
                draw_text(screen, "Game Over!", 32, 540, 10)
                draw_text(screen, "Your score: " + str(score), 32, 540, 45)
                draw_text(screen, "Top Ten High Scores:", 25, 540, 80)
                pygame.mixer.music.stop()
                soundObj4.play()

                outfile = open("highscore.txt", "a")
                outfile.write(str(score) + '\n')
                infile = open("highscore.txt", "r")
                l = []
                aline = infile.readline()
                db = []
                while aline:
                    l.append(aline)
                    aline = infile.readline()

                l.append(str(score))
                # original places, restarts everything as if new

                for ab in l:
                    db.append(int(ab))
                db = sorted(db, reverse=True)
                db = db[:10]

                infile.close()

                cn = 105
                hn = 1

                for i in db:
                    draw_text(screen, str(hn) + ". " + str(i).replace('\n', ''), 25, 540, cn)
                    cn += 25
                    hn += 1

                outfile.close()

                end_it = False
                while (end_it == False):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:  # so game doesnt get all glitchy when you try to exit without this code
                            pygame.quit()
                            sys.exit()
                    pygame.display.flip()
                    pygame.time.wait(5000)
                    newGame()

            except FileNotFoundError:  # in case file does not exist
                with open('highscore.txt', 'w') as outfile:
                    for i in range(10):
                        outfile.write("0" + "\n")

        xx -= .1 #health bar automatically decreases as times passes
        all_sprites_list.draw(screen)
        newFish-= .5
        pygame.display.flip()
        clock.tick(60)
newGame()