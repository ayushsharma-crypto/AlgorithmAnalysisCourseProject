import pygame
import random
import math

# Add draw condition
pygame.init()
screenX = 500
screenY = 600
screenXOneThird = screenX//3
screenYOneThird = screenX//3
screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption("| Tic Tac Toe |")
White = (255, 255, 255)
Black = (0, 0, 0)
Grey = (128, 128, 128)
fontUsed = 'Arial'


# defining buttons
class buttons:
    def __init__(self, colour, x, y, height, width, text):
        self.colour = colour
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.width, self.height), 0)
        font = pygame.font.SysFont(fontUsed, 45)
        text = font.render(self.text, True, White)
        screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isover(self, pos):
        if self.x < pos[0] < self.x + self.width:
            if self.y < pos[1] < self.y + self.height:
                return True
        return False


# drawing X
def drawX(x, y):
    pygame.draw.line(screen, White, (x + 20, y + 20), (x + 150, y + 150), 10)
    pygame.draw.line(screen, White, (x + 150, y + 20), (x + 20, y + 150), 10)
    pygame.display.update()


# drawing O
def drawO(x, y):
    pygame.draw.ellipse(screen, White, (x + 20, y + 20, 130, 130), 10)
    pygame.display.update()


# displaying tictactoe squares
def showTictactoeBoard(player1, player2, player1Score, player2Score, chance, whoWon, playersChoiceList):
    playerMessageFont = pygame.font.SysFont(fontUsed, 35)
    player1Message = playerMessageFont.render(player1 + ": " + player1Score, True, White)
    player2Message = playerMessageFont.render(player2 + ": " + player2Score, True, White)
    if whoWon == 0:
        if chance == 1:
            presentPlayerMessage = playerMessageFont.render(player1, True, White)
        if chance == 2:
            presentPlayerMessage = playerMessageFont.render(player2, True, White)
    else:
        if whoWon == 1:
            presentPlayerMessage = playerMessageFont.render(player1 + " Won", True, White)
        if whoWon == 2:
            presentPlayerMessage = playerMessageFont.render(player2 + " Won", True, White)
        if whoWon == 3:
            presentPlayerMessage = playerMessageFont.render("Draw", True, White)
    pygame.draw.rect(screen, Black, (0, 550, screenX, 50), 0)
    pygame.draw.rect(screen, Black, (0, 0, screenX, 50), 0)
    screen.blit(player1Message, (10, 10))
    screen.blit(player2Message, (320, 10))
    screen.blit(presentPlayerMessage, (180, 560))
    pygame.draw.rect(screen, White, (166, 50, 2, screenX), 0)
    pygame.draw.rect(screen, White, (332, 50, 2, screenX), 0)
    pygame.draw.rect(screen, White, (0, 216, screenX, 2), 0)
    pygame.draw.rect(screen, White, (0, 382, screenX, 2), 0)
    pygame.draw.rect(screen, White, (0, 50, screenX, 2), 0)
    pygame.draw.rect(screen, White, (0, 548, screenX, 2), 0)
    pygame.draw.rect(screen, White, (0, 50, 2, screenX), 0)
    pygame.draw.rect(screen, White, (498, 50, 2, screenX), 0)
    for i in range(9):
        x = (i % 3) * 166
        y = (i // 3) * 166 + 50
        if playersChoiceList[i] == 1:
            drawX(x, y)
        if playersChoiceList[i] == 2:
            drawO(x, y)
    pygame.display.update()


# function checking end of game
def checkEndGame(playersChoiceList):
    for i in range(3):
        if playersChoiceList[i] == playersChoiceList[i + 3] and playersChoiceList[i] == playersChoiceList[i + 6]:
            if playersChoiceList[i] != 0:
                x = (166 * i) + 85
                pygame.draw.line(screen, White, (x, 60), (x, 540), 10)
                return playersChoiceList[i]
        if playersChoiceList[3 * i] == playersChoiceList[3 * i + 1] and playersChoiceList[3 * i + 1] == \
                playersChoiceList[3 * i + 2]:
            if playersChoiceList[3 * i] != 0:
                y = i * 166 + 50 + 85
                pygame.draw.line(screen, White, (10, y), (490, y), 10)
                return playersChoiceList[3 * i]
    if playersChoiceList[0] == playersChoiceList[4] and playersChoiceList[4] == playersChoiceList[8]:
        if playersChoiceList[0] != 0:
            pygame.draw.line(screen, White, (10, 60), (490, 540), 10)
            return playersChoiceList[0]
    if playersChoiceList[2] == playersChoiceList[4] and playersChoiceList[4] == playersChoiceList[6]:
        if playersChoiceList[2] != 0:
            pygame.draw.line(screen, White, (490, 60), (10, 540), 10)
            return playersChoiceList[2]
    for i in range(9):
        if playersChoiceList[i] == 0:
            return 0
    return 3


# function which checks only end of game but does not draw any lines
def checkEndGameDontDraw(playersChoiceList):
    for i in range(3):
        if playersChoiceList[i] == playersChoiceList[i + 3] and playersChoiceList[i] == playersChoiceList[i + 6]:
            return playersChoiceList[i]
        if playersChoiceList[3 * i] == playersChoiceList[3 * i + 1] and playersChoiceList[3 * i + 1] == \
                playersChoiceList[3 * i + 2]:
            return playersChoiceList[3 * i]
    if playersChoiceList[0] == playersChoiceList[4] and playersChoiceList[4] == playersChoiceList[8]:
        return playersChoiceList[0]
    if playersChoiceList[2] == playersChoiceList[4] and playersChoiceList[4] == playersChoiceList[6]:
        return playersChoiceList[2]
    for i in range(9):
        if playersChoiceList[i] == 0:
            return 0
    return 3


# function checking for optimal move for computer
def getBestMove(playersChoiceList):
    bestScore = -math.inf
    move = 0
    for i in range(9):
        if playersChoiceList[i] == 0:
            playersChoiceList[i] = 2
            score = minimax(playersChoiceList, 0, False)
            playersChoiceList[i] = 0
            if score > bestScore:
                bestScore = score
                move = i
    #print( str(i) + " " + str(bestScore))
    return move


# Minimax function
def minimax(playersChoiceList, depth, isMaximizing):
    result = checkEndGameDontDraw(playersChoiceList)
    if result != 0:
        if result == 1:
            return -10
        if result == 2:
            return 10
        if result == 3:
            return 0
    if isMaximizing:
        bestScore = -math.inf
        for i in range(9):
            if playersChoiceList[i] == 0:
                playersChoiceList[i] = 2
                score = minimax(playersChoiceList, depth + 1, False)
                playersChoiceList[i] = 0
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = math.inf
        for i in range(9):
            if playersChoiceList[i] == 0:
                playersChoiceList[i] = 1
                score = minimax(playersChoiceList, depth + 1, True)
                playersChoiceList[i] = 0
                bestScore = min(score, bestScore)
        return bestScore
    return 0


# initializing buttons
initButton = buttons(Black, 185, 100, 50, 130, "Start")
singlePlayerButton = buttons(Black, 100, 140, 50, 300, "Single Player")
doublePlayerButton = buttons(Black, 100, 340, 50, 300, "Double Player")
pointsButton3 = buttons(Black, 150, 200, 50, 200, "3 points")
pointsButton4 = buttons(Black, 150, 300, 50, 200, "4 points")
pointsButton5 = buttons(Black, 150, 400, 50, 200, "5 points")
yesButton = buttons(Black, 100, 400, 50, 100, "YES")
noButton = buttons(Black, 300, 400, 50, 100, "NO")
# to check count of game
gameCount = 0
running = True


def game():
    # initializing all variables

    global running
    global gameCount
    #print(gameCount)
    Init_message = True
    multiplayerMssg = True
    pointsMssg = True
    singlePlayerGame = False
    doublePlayerGame = False
    playAgainMssg = True
    playersChoiceList = [0] * 9
    player1Score = 0
    player2Score = 0
    points = 0

    while running:
        ticTacToeMssgFont = pygame.font.SysFont("Arial", 50)
        if gameCount == 0:
            # welcome message
            while Init_message:
                ticTacToeMssg = ticTacToeMssgFont.render("Tic Tac Toe", True, White)
                ticTacToeImage = pygame.image.load('ticTacToe.jpg')
                screen.blit(ticTacToeMssg, (110, 25))
                screen.blit(ticTacToeImage, (0, 150))
                initButton.draw()
                for events in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    if events.type == pygame.QUIT:
                        Init_message = False
                        pygame.quit()
                        quit()
                    if events.type == pygame.KEYUP:
                        Init_message = False
                    if events.type == pygame.MOUSEMOTION:
                        if initButton.isover(pos):
                            initButton.colour = Grey
                        else:
                            initButton.colour = Black
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        if initButton.isover(pos):
                            Init_message = False
                            initButton.colour = Black
                pygame.display.update()
        screen.fill(Black)

        # Uncomment this lines if you want to play double player game.
        # choose between single player or double player
        # while multiplayerMssg:
        #     singlePlayerButton.draw()
        #     doublePlayerButton.draw()
        #     for events in pygame.event.get():
        #         pos = pygame.mouse.get_pos()
        #         if events.type == pygame.QUIT:
        #             running = False
        #             multiplayerMssg = False
        #             pygame.quit()
        #             quit()
        #         if events.type == pygame.MOUSEMOTION:
        #             if singlePlayerButton.isover(pos):
        #                 singlePlayerButton.colour = Grey
        #             else:
        #                 singlePlayerButton.colour = Black
        #             if doublePlayerButton.isover(pos):
        #                 doublePlayerButton.colour = Grey
        #             else:
        #                 doublePlayerButton.colour = Black
        #         if events.type == pygame.MOUSEBUTTONDOWN:
        #             if singlePlayerButton.isover(pos):
        #                 singlePlayerGame = True
        #                 multiplayerMssg = False
        #                 singlePlayerButton.colour = Black
        #             if doublePlayerButton.isover(pos):
        #                 doublePlayerGame = True
        #                 multiplayerMssg = False
        #                 doublePlayerButton.colour = Black
        #     pygame.display.update()
        # screen.fill(Black)
        while pointsMssg:
            ticTacToePointsFont = pygame.font.SysFont(fontUsed, 40)
            Mssg = ticTacToePointsFont.render("How many points game", True, White)
            MssgContinue = ticTacToePointsFont.render("you want to play?", True, White)
            screen.blit(Mssg, (50, 10))
            screen.blit(MssgContinue, (80, 65))
            pointsButton3.draw()
            pointsButton4.draw()
            pointsButton5.draw()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pointsMssg = False
                    running = False
                    pygame.quit()
                    quit()
                if events.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if pointsButton3.isover(pos):
                        pointsButton3.colour = Grey
                    else:
                        pointsButton3.colour = Black
                    if pointsButton4.isover(pos):
                        pointsButton4.colour = Grey
                    else:
                        pointsButton4.colour = Black
                    if pointsButton5.isover(pos):
                        pointsButton5.colour = Grey
                    else:
                        pointsButton5.colour = Black
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if pointsButton3.isover(pos):
                        points = 3
                        pointsMssg = False
                        pointsButton3.colour = Black
                    if pointsButton4.isover(pos):
                        points = 4
                        pointsMssg = False
                        pointsButton4.colour = Black
                    if pointsButton5.isover(pos):
                        points = 5
                        pointsMssg = False
                        pointsButton5.colour = Black
            pygame.display.update()
        while player1Score != points and player2Score != points:
            singlePlayerGame = True # Comment this line if you want to play double player game.
            for i in range(9):
                playersChoiceList[i] = 0
            screen.fill(Black)
            pygame.display.update()
            chance = random.randint(1, 2)
            # single player logic
            whoWon = 0
            countFlag = True
            while singlePlayerGame:
                if whoWon == 0:
                    whoWon = checkEndGame(playersChoiceList)
                if whoWon == 1 and countFlag:
                    player1Score += 1
                    countFlag = False
                if whoWon == 2 and countFlag:
                    player2Score += 1
                    countFlag = False
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        running = False
                        singlePlayerGame = False
                        pygame.quit()
                        quit()
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        x = (pos[0] // 166)
                        y = (pos[1] - 50) // 166
                        i = y * 3 + x
                        if playersChoiceList[i] == 0:
                            if chance == 1:
                                playersChoiceList[i] = 1
                                chance = 2
                                whoWon = checkEndGame(playersChoiceList)
                                if whoWon == 1:
                                    player1Score += 1
                                if whoWon == 2:
                                    player2Score += 1
                showTictactoeBoard("You", "Comp", str(player1Score), str(player2Score), chance, whoWon,
                                   playersChoiceList)
                pygame.display.update()
                if chance == 2 and whoWon == 0:
                    chance = 1
                    i = getBestMove(playersChoiceList)
                    if playersChoiceList[i] == 0:
                        playersChoiceList[i] = 2
                if whoWon != 0:
                    pygame.time.wait(1000)
                    break

            # double player logic
            # Uncomment the below lines if you want to play for double player.
            # countFlag = True
            # whoWon = 0
            # while doublePlayerGame:
            #     if whoWon == 0:
            #         whoWon = checkEndGame(playersChoiceList)
            #     if whoWon == 1 and countFlag:
            #         player1Score += 1
            #         countFlag = False
            #     if whoWon == 2 and countFlag:
            #         player2Score += 1
            #         countFlag = False
            #     for events in pygame.event.get():
            #         if events.type == pygame.QUIT:
            #             running = False
            #             doublePlayerGame = False
            #             pygame.quit()
            #             quit()
            #         if events.type == pygame.MOUSEBUTTONDOWN:
            #             pos = pygame.mouse.get_pos()
            #             x = (pos[0] // 166)
            #             y = (pos[1] - 50) // 166
            #             i = y * 3 + x
            #             if playersChoiceList[i] == 0:
            #                 if chance == 1:
            #                     playersChoiceList[i] = 1
            #                     chance = 2
            #                 elif chance == 2:
            #                     playersChoiceList[i] = 2
            #                     chance = 1
            #                 #print(playersChoiceList,whoWon)
            #             # print(x, y, playersChoiceList, whoWon)
            #     showTictactoeBoard("Player 1", "Player 2", str(player1Score), str(player2Score), chance, whoWon,
            #                        playersChoiceList)
            #     pygame.display.update()
            #     if whoWon != 0:
            #         pygame.time.wait(1000)
            #         break
        screen.fill(Black)
        while playAgainMssg:
            if player1Score == points and doublePlayerGame:
                whoWonMssg = ticTacToeMssgFont.render("Player 1 Won", True, White)
            if player2Score == points and doublePlayerGame:
                whoWonMssg = ticTacToeMssgFont.render("Player 2 Won", True, White)
            if player1Score == points and singlePlayerGame:
                whoWonMssg = ticTacToeMssgFont.render("You Won", True, White)
            if player2Score == points and singlePlayerGame:
                whoWonMssg = ticTacToeMssgFont.render("Computer Won", True, White)
            playAgain = ticTacToeMssgFont.render("Play Again?", True, White)
            screen.blit(whoWonMssg, (100, 100))
            screen.blit(playAgain, (100, 300))
            yesButton.draw()
            noButton.draw()
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if events.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if yesButton.isover(pos):
                        yesButton.colour = Grey
                    else:
                        yesButton.colour = Black
                    if noButton.isover(pos):
                        noButton.colour = Grey
                    else:
                        noButton.colour = Black
                if events.type == pygame.MOUSEBUTTONDOWN:
                    gameCount += 1
                    pos = pygame.mouse.get_pos()
                    if yesButton.isover(pos):
                        yesButton.colour = Black
                        game()
                    if noButton.isover(pos):
                        screen.fill(Black)
                        thankyou = ticTacToeMssgFont.render("Thank You", True, White)
                        screen.blit(thankyou, (100, 250))
                        pygame.display.update()
                        pygame.time.wait(3000)
                        pygame.quit()
                        quit()
            pygame.display.update()


if running:
    game()
