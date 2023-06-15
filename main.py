import pygame
import sys
import math
from button import Button

pygame.init()
screen = pygame.display.set_mode((640, 640))

black = (0, 0, 0)
purple = (77, 3, 68)
white = (255, 255, 255)
grey = (0, 0, 0)
brown = (210, 125, 45)
TILE_SIZE = 32
oceanBg = pygame.image.load('assets/bgimage.jpg')
diverImg = pygame.image.load('assets/diver.jpg')
shark = pygame.image.load('assets/shark.jpg')
crab = pygame.image.load('assets/crab.jpg')
jellyFish = pygame.image.load('assets/jellyfish.png')
seaMonster = pygame.image.load('assets/seamonster.png')
octopus = pygame.image.load('assets/octo.jpg')
submarine = pygame.image.load('assets/submarine.png')
seashell = pygame.image.load('assets/seashell.jpeg')
pearl = pygame.image.load('assets/pearl.jpg')
pygame.display.set_caption("Menu")
MainBG = pygame.image.load("assets/menubg.jpg")
InstBG = pygame.image.load("assets/instBG.png")
LoseBG = pygame.image.load("assets/loseBG.png")
WinBG = pygame.image.load("assets/winBG.png")

fps = 30
fpsClock = pygame.time.Clock()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font3.otf", size)


maze = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 0],
    [0, 1, 4, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 4, 0, 0, 0, 5, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 4, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 3, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 4, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 4, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


class Maze:

    def drawMaze(self):
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                x = column * TILE_SIZE
                y = row * TILE_SIZE

                if maze[row][column] == 1:
                    # Create a rect with the size of the image.
                    pygame.draw.rect(screen, black, (x, y, 32, 32))
                elif maze[row][column] == 2:
                    # door
                    pygame.draw.rect(screen, brown, (x, y, 32, 32))
                elif maze[row][column] == 3:
                    # key
                    screen.blit(submarine, (x, y))
                elif maze[row][column] == 4:
                    # candy
                    screen.blit(seashell, (x, y))
                elif maze[row][column] == 5:
                    # gift
                    screen.blit(pearl, (x, y))

    def wall_left(self, row, col):
        if maze[row][col] == 1:
            return True

    def wall_right(self, row, col):
        if maze[row][col + 1] == 1:
            return True

    def wall_up(self, row, col):
        if maze[row][col] == 1:
            return True

    def wall_down(self, row, col):
        if maze[row + 1][col] == 1:
            return True

    def door(self, row, col):
        if maze[row][col] == 2:
            return True

    def issubmarine(self, row, col):
        if maze[row][col] == 3:
            return True

    def isseashell(self, row, col):
        if maze[row][col] == 4:
            return True

    def ispearl(self, row, col):
        if maze[row][col] == 5:
            return True


class diver:
    x = 90
    y = 590
    step = 4
    havesubmarine = False
    havepearl = False
    seashellCount = 0

    def newgame(self):
        self.x = 90
        self.y = 590
        self.step = 7
        self.havesubmarine = False
        self.seashellCount = 0
        self.havepearl = False
        
        maze[10][10] = 3  # for key
        maze[2][2] = 4  # for candy
        maze[2][10] = 4
        maze[5][14] = 5
        maze[3][16] = 4
        maze[8][8] = 4
        maze[17][17] = 4
        maze[14][14] = 4
        maze[5][10] = 4
        maze[10][2] = 4
        maze[5][14] = 5 # for gift

    def draw(self):
        screen.blit(diverImg, (self.x, self.y))

    def move(self, keys):
        pos = self.x, self.y
        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.step
        if keys[pygame.K_RIGHT]:
            if self.x < 590:
                self.x += self.step
        if keys[pygame.K_UP]:
            if self.y > 0:
                self.y -= self.step
        if keys[pygame.K_DOWN]:
            if self.y < 590:
                self.y += self.step

        row = self.y // 32
        column = self.x // 32

        if grid.wall_left(row, column):
            self.x, self.y = pos

        if grid.wall_down(row, column):
            self.x, self.y = pos

        if grid.wall_up(row, column):
            self.x, self.y = pos

        if grid.wall_right(row, column):
            self.x, self.y = pos

        if grid.issubmarine(row, column):
            self.havesubmarine = True
            drawblank(row, column)

        if grid.isseashell(row, column):
            self.seashellCount += 1
            drawblank(row, column)

        if grid.ispearl(row, column):
            enemy.octopus()
            Diver.havepearl = True
            drawblank(row, column)

        if grid.isseashell(row + 1, column):
            self.seashellCount += 1
            drawblank(row + 1, column)

        if grid.isseashell(row, column + 1):
            self.seashellCount += 1
            drawblank(row, column + 1)

        if grid.door(row, column):
            if self.havesubmarine:
                youwin()
            else:
                if grid.door(row, column):
                    self.x, self.y = pos


class Enemy:
    sharkX = 180
    sharkY = 500

    crabX = 80
    crabY = 200

    jellyFishX = 300
    jellyFishY = 320

    seaMonsterX = 480
    seaMonsterY = 100

    octopusX = 90
    octopusY = 590

    sharkStep = 6
    crabStep = 3
    jellyFishStep = 4
    seaMonsterStep = 6
    octopusStep = 2

    def shark(self):
        screen.blit(shark, (self.sharkX, self.sharkY))
        # movement
        self.sharkY += self.sharkStep
        if self.sharkY <= 50:
            self.sharkStep = 6
        elif self.sharkY >= 550:
            self.sharkStep = -6

    def crab(self):  # near the keys
        screen.blit(crab, (self.crabX, self.crabY))
        # movement
        self.crabX += self.crabStep
        if self.crabX <= 250:
            self.crabStep = 3
        elif self.crabX >= 450:
            self.crabStep = -3

    def jellyFish(self):  # near the exit
        screen.blit(jellyFish, (self.jellyFishX, self.jellyFishY))
        # movement
        self.jellyFishX += self.jellyFishStep
        if self.jellyFishX <= 450:
            self.jellyFishStep = 3
        elif self.jellyFishX >= 600:
            self.jellyFishStep = -3

    def seaMonster(self):
        screen.blit(seaMonster, (self.seaMonsterX, self.seaMonsterY))
        # movement
        self.seaMonsterY += self.seaMonsterStep
        if self.seaMonsterY <= 50:
            self.seaMonsterStep = 3
        elif self.seaMonsterY >= 500:
            self.seaMonsterStep = -3

    def octopus(self):  # chase after the diver
        screen.blit(octopus, (self.octopusX, self.octopusY))
        # movement
        if self.octopusX < Diver.x:
            self.octopusX += self.octopusStep
        if self.octopusX > Diver.x:
            self.octopusX -= self.octopusStep
        if self.octopusY < Diver.y:
            self.octopusY += self.octopusStep
        if self.octopusY > Diver.y:
            self.octopusY -= self.octopusStep


def drawblank(row, col):
    maze[row][col] = 0
    pygame.display.update()


def isCollision(enemyX, enemyY, diverx, divery):
    distance = math.sqrt(math.pow(enemyX - diverx, 2) + (math.pow(enemyY - divery, 2)))
    if distance < 25:
        return True
    return False


Diver = diver()
grid = Maze()
enemy = Enemy()


def play():
    # game loop
    while True:

        screen.fill(grey)
        screen.blit(oceanBg, (0, 0))
        pygame.display.set_caption("Game Mode")
        grid.drawMaze()
        Diver.draw()
        enemy.shark()
        enemy.crab()
        enemy.seaMonster()
        enemy.jellyFish()

        if Diver.havepearl:
            enemy.octopus()
            pygame.display.update()
            if isCollision(enemy.octopusX, enemy.octopusY, Diver.x, Diver.y):
                youlose()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        Diver.move(keys)

        if isCollision(enemy.sharkX, enemy.sharkY, Diver.x, Diver.y):
            youlose()

        if isCollision(enemy.seaMonsterX, enemy.seaMonsterY, Diver.x, Diver.y):
            youlose()

        if isCollision(enemy.crabX, enemy.crabY, Diver.x, Diver.y):
            youlose()

        if isCollision(enemy.jellyFishX, enemy.jellyFishY, Diver.x, Diver.y):
            youlose()

        pygame.display.update()
        fpsClock.tick(fps)


def instructions():
    while True:
        inst_mousepos = pygame.mouse.get_pos()

        screen.fill("white")
        screen.blit(InstBG, (0, 0))

        inst_back = Button(image=None, pos=(100, 600),
                           text_input="Back", font=get_font(40), base_color="White", hovering_color="Green")

        inst_back.changeColor(inst_mousepos)
        inst_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if inst_back.checkForInput(inst_mousepos):
                    main_menu()

        pygame.display.update()


def youlose():
    while True:
        lose_mousepos = pygame.mouse.get_pos()

        screen.fill("white")
        screen.blit(LoseBG, (0, 0))

        Lose_PlayAgain = Button(image=None, pos=(500, 500),
                                text_input="Play Again", font=get_font(40), base_color="Yellow", hovering_color="Green")

        Lose_Quit = Button(image=None, pos=(500, 600),
                           text_input="Quit", font=get_font(40), base_color="Yellow", hovering_color="Green")

        Lose_PlayAgain.changeColor(lose_mousepos)
        Lose_PlayAgain.update(screen)
        Lose_Quit.changeColor(lose_mousepos)
        Lose_Quit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Lose_PlayAgain.checkForInput(lose_mousepos):
                    Diver.newgame()
                    play()
                if Lose_Quit.checkForInput(lose_mousepos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def youwin():
    while True:
        win_mousepos = pygame.mouse.get_pos()

        screen.fill("white")
        screen.blit(WinBG, (0, 0))

        scoretext = "Seashells Collected: " + str(Diver.seashellCount)

        win_seashellScore = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(300, 400),
                                text_input=scoretext, font=get_font(40), base_color="Yellow", hovering_color="White")

        win_PlayAgain = Button(image=None, pos=(150, 500),
                               text_input="Play Again", font=get_font(40), base_color="White", hovering_color="Green")

        win_Quit = Button(image=None, pos=(150, 600),
                          text_input="Quit", font=get_font(40), base_color="White", hovering_color="Green")

        win_seashellScore.changeColor(win_mousepos)
        win_seashellScore.update(screen)
        win_PlayAgain.changeColor(win_mousepos)
        win_PlayAgain.update(screen)
        win_Quit.changeColor(win_mousepos)
        win_Quit.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if win_PlayAgain.checkForInput(win_mousepos):
                    Diver.newgame()
                    play()
                if win_Quit.checkForInput(win_mousepos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def main_menu():
    while True:
        screen.blit(MainBG, (0, 0))

        menu_mousepos = pygame.mouse.get_pos()

        playButton = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(320, 230),
                            text_input="Play", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        instButton = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(320, 380),
                            text_input="Instructions", font=get_font(45), base_color="#d7fcd4", hovering_color="White")
        quitButton = Button(image=pygame.image.load("assets/GreyRect.png"), pos=(320, 530),
                            text_input="Quit", font=get_font(45), base_color="#d7fcd4", hovering_color="White")

        for button in [playButton, instButton, quitButton]:
            button.changeColor(menu_mousepos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playButton.checkForInput(menu_mousepos):
                    play()
                if instButton.checkForInput(menu_mousepos):
                    instructions()
                if quitButton.checkForInput(menu_mousepos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()
