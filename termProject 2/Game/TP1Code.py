#Sheril Christopher Section:A

import pygame


#CITATIONS
#BASIC FORMAT INCLUDING RUN FUNCTION:
#https://github.com/LBPeraza/Pygame-Asteroids/blob/master/pygamegame.py

###############################################################################
#DICTIONARIES
###############################################################################
DIRECTIONS = {"NE":(1,1), "NW":(1,-1), "SW":(-1,-1), "SE":(-1,1), 
                "N":(1,0), "S":(-1,0), "W":(0,-1), "E":(0,1)}

shootingPositions = {"left": (100,250), "middle":(500,250), "right":(950,250)}

attackDict = {"bale": "players/rm/attack/BALE.png", 
                    "benzema":"players/rm/attack/BENZEMA.png",
                    "jese":"players/rm/attack/JESE.png",
                    "ronaldo":"players/rm/attack/RONALDO.png"}

defendersDict = {"arbeloa":"players/rm/defenders/ARBELOA.png",
                        "carvajal":"players/rm/defenders/CARVAJAL.png",
                        "danilo": "players/rm/defenders/DANILO.png",
                        "marcelo": "players/rm/defenders/MARCELO.png",
                        "nacho":"players/rm/defenders/NACHO.png",
                        "pepe":"players/rm/defenders/PEPE.png",
                        "ramos":"players/rm/defenders/RAMOS.png",
                        "varane":"players/rm/defenders/VARANE.png"}

goalieDict = {"casilla":"players/rm/goal/CASILLA.png",
                    "navas":"players/rm/goal/NAVAS.png" }

midfieldDict = {"casemiro":"players/rm/midfield/CASEMIRO.png",
                        "isco":"players/rm/midfield/ISCO.png",
                        "kovacic": "players/rm/midfield/KOVACIC.png",
                        "kroos": "players/rm/midfield/KROOS.png",
                        "modric":"players/rm/midfield/MODRIC.png",
                        "rodriguez":"players/rm/midfield/RODRIGUEZ.png",
                        "vazquez":"players/rm/midfield/VAZQUEZ.png"}

attackButtonsDict = {"bale": "playerButtons/attack/bale.png", 
                    "benzema":"playerButtons/attack/benzema.png",
                    "jese":"playerButtons/attack/jese.png",
                    "ronaldo":"playerButtons/attack/ronaldo.png"}

defendersButtonsDict = {"arbeloa":"playerButtons/defenders/arbeloa.png",
                        "carvajal":"playerButtons/defenders/carvajal.png",
                        "danilo": "playerButtons/defenders/danilo.png",
                        "marcelo": "playerButtons/defenders/marcelo.png",
                        "nacho":"playerButtons/defenders/nacho.png",
                        "pepe":"playerButtons/defenders/pepe.png",
                        "ramos":"playerButtons/defenders/ramos.png",
                        "varane":"playerButtons/defenders/varane.png"}

goalieButtonsDict = {"casilla":"playerButtons/goal/casilla.png",
                    "navas":"playerButtons/goal/navas.png" }

midfieldButtonsDict = {"casemiro":"playerButtons/midfield/casemiro.png",
                        "isco":"playerButtons/midfield/isco.png",
                        "kovacic": "playerButtons/midfield/kovacic.png",
                        "kroos": "playerButtons/midfield/kroos.png",
                        "modric":"playerButtons/midfield/modric.png",
                        "rodriguez":"playerButtons/midfield/rodriguez.png",
                        "vazquez":"playerButtons/midfield/vazquez.png"}

fieldGoalie = {"casilla":"fieldplayers/goal/casilla.png",
                    "navas":"fieldplayers/goal/navas.png" }
fieldMidfielders = {"casemiro":"fieldplayers/midfield/casemiro.png",
                        "isco":"fieldplayers/midfield/isco.png",
                        "kovacic": "fieldplayers/midfield/kovacic.png",
                        "kroos": "fieldplayers/midfield/kroos.png",
                        "modric":"fieldplayers/midfield/modric.png",
                        "rodriguez":"fieldplayers/midfield/rodriguez.png",
                        "vazquez":"fieldplayers/midfield/vazquez.png"}
fieldDefense = {"arbeloa":"fieldplayers/defenders/arbeloa.png",
                        "carvajal":"fieldplayers/defenders/carvajal.png",
                        "danilo": "fieldplayers/defenders/danilo.png",
                        "marcelo": "fieldplayers/defenders/marcelo.png",
                        "nacho":"fieldplayers/defenders/nacho.png",
                        "pepe":"fieldplayers/defenders/pepe.png",
                        "ramos":"fieldplayers/defenders/ramos.png",
                        "varane":"fieldplayers/defenders/varane.png"}
fieldAttack = {"bale": "fieldplayers/attack/bale.png", 
                    "benzema":"fieldplayers/attack/benzema.png",
                    "jese":"fieldplayers/attack/jese.png",
                    "ronaldo":"fieldplayers/attack/ronaldo.png"}

####VELOCITY#######################################################
attackVelocity = {"bale":7, "benzema":5, "jese":5,"ronaldo":7}
defenseVelocity = {"arbeloa":4, "carvajal":4,"danilo":4,
                    "marcelo":4,"nacho":3,"pepe":3,
                    "ramos":4,"varane":5}
midfieldVelocity = {"casemiro":3,"isco":4,"kovacic":4 ,
                    "kroos":2 ,"modric":4,"rodriguez":4,
                    "vazquez":4}
goalVelocity = {"casilla":0,"navas":0 }

####################################################################
#POWER
#####################################################################

attackPower= {"bale":9, "benzema":8, "jese":7,"ronaldo":10}
defensePower = {"arbeloa":6, "carvajal":4,"danilo":8 ,
                    "marcelo":7,"nacho":3,"pepe":5,
                    "ramos":6,"varane":5}
midfieldPower = {"casemiro":7,"isco":8,"kovacic":7,
                    "kroos":8 ,"modric":6,"rodriguez":7,
                    "vazquez":9}
goalPower = {"casilla":7,"navas":10}

#####################################################################

fieldGolPos1 = [(180,260)]
fieldAttPos1 = [(475,260),(590,300),(590,220)]
fieldDefPos1 = [(290,180),(280,250),(250,310),(220,370)]
fieldMidPos1 = [(405,200),(390,270),(370,340)]

fieldGolPos2 = [(1000,260)]
fieldAttPos2 = [(700,210),(690,270),(720,340)]
fieldDefPos2 = [(890,180),(910,250),(930,310),(940,370)]
fieldMidPos2 = [(780,200),(790,270),(810,340)]


goal = {"casilla": (110,415), "navas": (110,436)}
defense = {"arbeloa": (210,415), "carvajal": (210,436), "danilo": (210,457),
            "marcelo": (210,478), "nacho":(320,415), "pepe": (320,436),
            "ramos": (320,457), "varane": (320,478)}
midfield = {"casemiro":(410,415), "isco":(410,436), "kovacic":(410,457),
            "kroos":(410,478),"modric":(520,415),"rodriguez":(520,436),
            "vazquez":(520,457)}
attack = {"bale": (610,415),"benzema":(610,436), "jese":(610,457),
            "ronaldo":(610,478)}

formGoalie = [(321,315)]
formAttack = [(253,60), (321,55), (389,60)]
formMidfield = [(253,145), (321,145), (389,145)]
formDefense = [(219,240), (287,240), (355,240), (423,240)]
###############################################################################
###############################################################################


class Player(object):
    def __init__(self,startPlayer,rect):
        pass
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    
    def move(self):
        if type(self) == Defender:
            self.moveDefender()
        elif type(self) == Midfielder:
            self.moveMidfielder()
        elif type(self) == Attacker:
            self.moveAttacker()
    
    def moveDefender(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        if x <= 450:
            (self.rect.left, self.rect.top) = (self.rect.left+self.velocity/2, self.rect.top)

    def moveMidfielder(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        if x <= 750:
            (self.rect.left, self.rect.top) = (self.rect.left+self.velocity/2, self.rect.top)

    def moveAttacker(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        if x <= 1000:
            (self.rect.left, self.rect.top) = (self.rect.left+self.velocity/2, self.rect.top)

    def moveLeft(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        bound1Y = ((7/4) * x) - 102.5
        bound2Y = ((-28/17)*x) + (31980/17)
        if ((500-y) <= bound1Y ) and ((500-y) <= bound2Y) and (y >= 200):
            (self.rect.left, self.rect.top) = (self.rect.left, self.rect.top-self.velocity)

    def moveRight(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        bound1Y = ((7/4) * x) - 102.5
        bound2Y = ((-28/17)*x) + (31980/17)
        if ( (500-y) <= bound1Y ) and ((500-y) <= bound2Y) and (y <= 480):
            (self.rect.left, self.rect.top) = (self.rect.left, self.rect.top+self.velocity)

    def moveForward(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        boundY = ((-28/17)*x) + (31980/17)
        if (500-y) <= boundY:
            (self.rect.left, self.rect.top) = (self.rect.left+self.velocity, self.rect.top)
    
    def moveBackward(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        boundY = ((7/4) * x) - 102.5
        if  (500-y) <= boundY :
            (self.rect.left, self.rect.top) = (self.rect.left-self.velocity, self.rect.top)


class Goalie(Player):
    def __init__(self,team,name, pos,image):
        self.name = name
        self.team = team
        if team == 1:
            self.position = fieldGolPos1[pos]
        else: self.position = fieldGolPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity = goalVelocity[name]
        self.power = goalPower[name]

class Defender(Player):
    def __init__(self,team,name,pos,image):
        self.name = name
        self.team = team
        if team == 1:
            self.position = fieldDefPos1[pos]
        else: self.position = fieldDefPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity =defenseVelocity[name]
        self.power = defensePower[name]

class Midfielder(Player):
    def __init__(self,team,name,pos,image):
        self.name = name
        self.team = team
        if team == 1:
            self.position = fieldMidPos1[pos]
        else: self.position = fieldMidPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity =midfieldVelocity[name]
        self.power = midfieldPower[name]

class Attacker(Player):
    def __init__(self,team,name,pos,image):
        self.name = name
        self.team = team
        if team == 1:
            self.position = fieldAttPos1[pos]
        else: self.position = fieldAttPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity = attackVelocity[name]
        self.power = attackPower[name]

class Ball(object):
    def __init__(self,currentPlayer,image):
        self.currentPlayer = currentPlayer #object
        self.image = image
        self.rect = self.image.get_rect()
        (topx,topy) = (currentPlayer.rect.left, currentPlayer.rect.top)
        position = (topx + currentPlayer.rect.width/2, topy + currentPlayer.rect.height-10)
        self.rect.left, self.rect.top = position

    def passBall(self,player, direction):
        (xPos, yPos) = (self.rect.left+self.rect.width, self.rect.top+self.rect.height)
        bound1Y = ((7/4) * xPos) - 102.5
        bound2Y = ((-28/17)*xPos) + (31980/17)
        if (((500-yPos) < bound1Y ) and ((500-yPos) < bound2Y) and (yPos < 475)
            and (yPos > 205)):
            velocity = player.power/4
            (x,y) = DIRECTIONS[direction]
            moveX, moveY = ((x*velocity), (y*velocity))
            (self.rect.left, self.rect.top) = (self.rect.left+moveX, self.rect.top+moveY)

    def move(self, passingBall, currentPlayer):
        player = currentPlayer
        if passingBall == False:
            (topx,topy) = (player.rect.left, player.rect.top)
            position = (topx + player.rect.width/2, topy + player.rect.height-10)
            self.rect.left, self.rect.top = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class ShootingModeGoalie(object):
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (570,60)
        self.horizVelocity = 5
        self.vertVelocity = 4

    def changeImage(self,image,direction):
        self.image = image
        self.rect = self.image.get_rect()
        if direction == "left":
            self.rect.left, self.rect.top = (455,80)
        elif direction == "right":
            self.rect.left, self.rect.top = (550,90)


    def draw(self,screen):
        screen.blit(self.image, self.rect)
    
    def moveLeft(self):
        if (350 < self.rect.left < 850) and (0 <self.rect.top <200):
            (self.rect.left, self.rect.top) = (self.rect.left- self.horizVelocity, self.rect.top-self.vertVelocity)
    
    def moveRight(self):
        if (350 < self.rect.left < 850) and (0 <self.rect.top <200):
            (self.rect.left, self.rect.top) = (self.rect.left+ self.horizVelocity, self.rect.top-self.vertVelocity)

class ShootBall(object):

    def __init__(self,image,playerPosition):
        self.image = image
        self.rect = self.image.get_rect()
        x,y = shootingPositions[playerPosition]
        (self.rect.left, self.rect.top) = (x+50, y+230)

    def draw(self,screen):
        screen.blit(self.image, self.rect)


class PygameGame(object):
    def init(self):
        self.setDict()
        self.intro = True
        self.startButtonRect = None
        self.helpButtonRect = None
        self.help = False
        self.continueRect = None
        self.formation = False
        self.startGameButtonRect = None
        self.fullTeam = 11
        pygame.init()

    def getFormation(self,x,y):
        for goalie in self.goalCards:
            if self.goalCards[goalie].collidepoint(x,y):
                if len(self.formationGoalies)==0:
                    self.formationGoalies.append(goalie)
        for attacker in self.attackCards:
            if self.attackCards[attacker].collidepoint(x,y):
                if len(self.formationAttack) < 3 and attacker not in self.formationAttack:
                    self.formationAttack.append(attacker)
        for defender in self.defenderCards:
            if self.defenderCards[defender].collidepoint(x,y):
                if len(self.formationDefender) < 4 and defender not in self.formationDefender:
                    self.formationDefender.append(defender)
        for midfielder in self.midfieldCards:
            if self.midfieldCards[midfielder].collidepoint(x,y):
                if len(self.formationMidfield) <3 and midfielder not in self.formationMidfield:
                    self.formationMidfield.append(midfielder)
    
    def removeCards(self, x, y):
        for goalie in self.goalRects:
            if goalie[1].collidepoint(x,y):
                self.formationGoalies.remove(goalie[0])
                self.goalRects.remove(goalie)
        for attacker in self.attackRects:
            if attacker[1].collidepoint(x,y):
                self.formationAttack.remove(attacker[0])
                self.attackRects.remove(attacker)
        for midfielder in self.midRects:
            if midfielder[1].collidepoint(x,y):
                self.formationMidfield.remove(midfielder[0])
                self.midRects.remove(midfielder)
        for defender in self.defenseRects:
            if defender[1].collidepoint(x,y):
                self.formationDefender.remove(defender[0])
                self.defenseRects.remove(defender)
    
    def setPlayerInstances(self):
        for i in range(len(self.formationGoalies)):
            goalie = self.formationGoalies[i]
            image = self.fieldGoalImages[goalie]
            self.players.append(Goalie(1,goalie,i,image))
        for i in range(len(self.formationDefender)):
            defender = self.formationDefender[i]
            image = self.fieldDefImages[defender]
            self.players.append(Defender(1,defender,i,image))
        for i in range(len(self.formationMidfield)):
            midfielder = self.formationMidfield[i]
            image = self.fieldMidImages[midfielder]
            self.players.append(Midfielder(1,midfielder,i,image))
        for i in range(len(self.formationAttack)):
            attacker = self.formationAttack[i]
            image = self.fieldAttImages[attacker]
            self.players.append(Attacker(1,attacker,i,image))
        

    def mousePressed(self, x, y):
        if self.intro == True:
            if self.startButtonRect.collidepoint(x,y):
                self.intro = False
                self.formation = True
            if self.helpButtonRect.collidepoint(x,y):
                self.intro = False
                self.help = True
        elif self.help == True:
            if self.continueRect.collidepoint(x,y):
                self.help = False
                self.intro = True
        elif self.formation == True:
            self.getFormation(x,y)
            self.removeCards(x,y)
            if self.startGameButtonRect.collidepoint(x,y):
                if (len(self.formationGoalies) + len(self.formationAttack)+
                    len(self.formationDefender) + 
                    len(self.formationMidfield)) == self.fullTeam:
                        self.setPlayerInstances()
                        self.curPlayer = self.players[-1]
                        self.ball = Ball(self.curPlayer,self.ballImage)
                        self.start = True
                        self.formation = False
                        self.width = 1200
                        self.height = 500
                        

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass
    
    def isShootingMode(self):
        if self.passingBall == False:
            (x,y) = (self.ball.rect.left + self.ball.rect.width, self.ball.rect.top+self.ball.rect.height)
            if 250 <= y <= 400 and x >= 875:
                self.shootingMode = True
                self.start = False
                self.shootingModeGoalie = ShootingModeGoalie(self.startGoalkeeper)
                if 250 <= y < 280:
                    self.shootingPosition = "left"
                elif 280 <= y < 350:
                    self.shootingPosition = "middle"
                elif 350 <= y < 400:
                    self.shootingPosition = "right"
                self.shootBall = ShootBall(self.shootingBall, self.shootingPosition)

    def getDirection(self,keys):
        if self.passingBall == False:
            if keys[pygame.K_UP] and keys[pygame.K_LEFT]:
                self.direction = "NW"
            elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
                self.direction =  "NE"
            elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
                self.direction =  "SW"
            elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
                self.direction =  "SE"
            elif keys[pygame.K_DOWN]:
                self.direction =  "S"
            elif keys[pygame.K_UP]:
                self.direction =  "N"
            elif keys[pygame.K_RIGHT]:
                self.direction =  "E"
            elif keys[pygame.K_LEFT]:
                self.direction =  "W"


    def keyPressed(self, keyCode, modifier, keys):
        if self.start == True:
            if keys[pygame.K_SPACE]:
                self.getDirection(keys)
                if self.direction != None:
                    self.passingPlayer = self.curPlayer
                    self.passingBall = True
                    self.justPassed = True
                # self.ball.passBall(self.passingPlayer, self.direction)
            elif keyCode == pygame.K_LEFT:
                self.curPlayer.moveLeft()
                self.ball.move(self.passingBall,self.curPlayer)
            elif keyCode == pygame.K_RIGHT:
                self.curPlayer.moveRight()
                self.ball.move(self.passingBall,self.curPlayer)
            elif keyCode == pygame.K_DOWN:
                self.curPlayer.moveBackward()
                self.ball.move(self.passingBall,self.curPlayer)
            elif keyCode == pygame.K_UP:
                self.curPlayer.moveForward()
                self.ball.move(self.passingBall,self.curPlayer)            
        elif self.shootingMode == True:
            if keyCode == pygame.K_LEFT:
                self.shootingModeGoalie.changeImage(self.goalkeeperLeft,"left")
                self.moveLeft = True
            elif keyCode == pygame.K_RIGHT:
                self.shootingModeGoalie.changeImage(self.goalkeeperRight,"right")
                self.moveRight = True

    def keyReleased(self, keyCode, modifier):
        pass
    
    
    # def wasKeyPressed(self, key):
    #     ''' return whether a specific key was pressed'''
    #     return self._keys.get(key,False)

    def changeCurrentPlayer(self):
        minPlayer = self.curPlayer
        width, height = self.curPlayer.rect.width, self.curPlayer.rect.height
        (x,y) = (self.curPlayer.rect.left+width/2, self.curPlayer.rect.top+height-10)
        x2,y2 = self.ball.rect.left, self.ball.rect.top
        minDistance = (((x2-x)**2+(y2-y)**2)**0.5)
        for player in self.players:
            if type(player) != Goalie:
                width,height = player.rect.width,player.rect.height
                (x,y) = (player.rect.left+width/2, player.rect.top+height-10)
                distance = (((x2-x)**2+(y2-y)**2)**0.5)
                if distance < minDistance:
                    minDistance = distance
                    minPlayer = player
        self.curPlayer = minPlayer
        self.interceptBall(self.curPlayer)

        
    
    def interceptBall(self,player):
        width, height = self.curPlayer.rect.width, self.curPlayer.rect.height
        (x,y) = (self.curPlayer.rect.left+width/2, self.curPlayer.rect.top+height-10)
        x2,y2 = self.ball.rect.left, self.ball.rect.top
        distance = (((x2-x)**2+(y2-y)**2)**0.5)
        if distance < 5 and player != self.passingPlayer:
            self.passingBall = False
            self.passingPlayer = None

    def timerFired(self, dt):
        self.step +=1
        if self.shootingMode == True:
            if self.moveLeft == True:
                self.shootingModeGoalie.moveLeft()
            elif self.moveRight == True:
                self.shootingModeGoalie.moveRight()
        if self.start == True and self.passingBall == True:
            self.ball.passBall(self.passingPlayer, self.direction)
        if self.step % 5 == 0 and self.start == True:
            for player in self.players:
                if player != self.curPlayer:
                    player.move()
        if self.start == True:
            self.isShootingMode()
        if self.passingBall == True:
            self.changeCurrentPlayer()
        if self.step % 10 == 0:
            self.justPassed = False
        

    def introScreen(self,screen):
        screen.blit(self.background,(0,0))
        self.startButtonRect = self.startButton.get_rect()
        (self.startButtonRect.left, self.startButtonRect.top) = (500,0)
        screen.blit(self.startButton,self.startButtonRect)
        self.helpButtonRect = self.helpButton.get_rect()
        (self.helpButtonRect.left,self.helpButtonRect.top) = (500,50)
        screen.blit(self.helpButton,self.helpButtonRect)
    
    def helpScreen(self,screen):
        screen.blit(self.helpPage,(0,0))
        self.continueRect = self.continueGame.get_rect()
        self.continueRect.left, self.continueRect.top = (50,50)
        screen.blit(self.continueGame,self.continueRect)

    def loadNames(self):
        for goalie in goalieButtonsDict:
            image1 = pygame.image.load(goalieButtonsDict[goalie]).convert_alpha()
            self.goalButtons[goalie] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(goalieDict[goalie])
            goalieCard = pygame.transform.smoothscale(image, (58,80))
            self.loadGoalCard[goalie] = goalieCard
        for attacker in attackButtonsDict:
            image1 = pygame.image.load(attackButtonsDict[attacker]).convert_alpha()
            self.attackButtons[attacker] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(attackDict[attacker])
            attack = pygame.transform.smoothscale(image, (58,80))
            self.loadAttCard[attacker] = attack
        for defender in defendersButtonsDict:
            image1 = pygame.image.load(defendersButtonsDict[defender]).convert_alpha()
            self.defendersButtons[defender] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(defendersDict[defender])
            defend = pygame.transform.smoothscale(image, (58,80))
            self.loadDefCard[defender] = defend
        for midfielder in midfieldButtonsDict:
            image1 = pygame.image.load(midfieldButtonsDict[midfielder]).convert_alpha()
            self.midfieldButtons[midfielder] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(midfieldDict[midfielder])
            midfield = pygame.transform.smoothscale(image, (58,80))
            self.loadMidCard[midfielder] = midfield

    def displayNames(self,screen):
        for goalie in self.goalButtons:
            goalieRect = self.goalButtons[goalie].get_rect()
            goalieRect.left, goalieRect.top = goal[goalie]
            self.goalCards[goalie] = goalieRect
            screen.blit(self.goalButtons[goalie],goalieRect)
        for mid in self.midfieldButtons:
            midRect = self.midfieldButtons[mid].get_rect()
            midRect.left, midRect.top = midfield[mid]
            self.midfieldCards[mid] = midRect
            screen.blit(self.midfieldButtons[mid],midRect)
        for defender in self.defendersButtons:
            defRect = self.defendersButtons[defender].get_rect()
            defRect.left, defRect.top = defense[defender]
            self.defenderCards[defender] = defRect
            screen.blit(self.defendersButtons[defender],defRect)
        for attacker in self.attackButtons:
            attackRect = self.attackButtons[attacker].get_rect()
            attackRect.left, attackRect.top = attack[attacker]
            self.attackCards[attacker] = attackRect
            screen.blit(self.attackButtons[attacker],attackRect)

    def selectPlayers(self,screen):
        image = pygame.transform.smoothscale(self.playersChooseBack, (700,500))
        screen.blit(image,(0,0))
        image = pygame.transform.smoothscale(self.bottomPlayers, (700,100)).convert_alpha()
        screen.blit(image,(0,400))
        self.loadNames()
        self.displayNames(screen)

    def drawFormation(self,screen):
        for goalie in self.formationGoalies:
            goalieRect = self.loadGoalCard[goalie].get_rect()
            goalieRect.left, goalieRect.top = formGoalie[0]
            screen.blit(self.loadGoalCard[goalie],goalieRect)
            if (goalie,goalieRect) not in self.goalRects:
                self.goalRects.append((goalie,goalieRect))
        for i in range(len(self.formationDefender)):
            defender = self.formationDefender[i]
            defenseRect = self.loadDefCard[defender].get_rect()
            defenseRect.left, defenseRect.top = formDefense[i]
            screen.blit(self.loadDefCard[defender],defenseRect)
            if (defender,defenseRect) not in self.defenseRects:
                self.defenseRects.append((defender,defenseRect))
        for i in range(len(self.formationAttack)):
            attacker = self.formationAttack[i]
            attackRect = self.loadAttCard[attacker].get_rect()
            attackRect.left, attackRect.top = formAttack[i]
            screen.blit(self.loadAttCard[attacker], attackRect)
            if (attacker,attackRect) not in self.attackRects:
                self.attackRects.append((attacker,attackRect))
        for i in range(len(self.formationMidfield)):
            midfielder = self.formationMidfield[i]
            midRect = self.loadMidCard[midfielder].get_rect()
            midRect.left, midRect.top = formMidfield[i]
            screen.blit(self.loadMidCard[midfielder], midRect)
            if (midfielder,midRect) not in self.midRects:
                self.midRects.append((midfielder,midRect))


    def drawStartButton(self, screen):
        self.startGameButtonRect = self.startGame.get_rect()
        (self.startGameButtonRect.left, self.startGameButtonRect.top) = (550, 25)
        screen.blit(self.startGame, self.startGameButtonRect)

    def drawField(self,screen):
        # image = pygame.transform.smoothscale(self.field, (700,500))
        screen.blit(self.field,(0,0))

    def drawPlayers(self,screen):
        for player in self.players:
            player.draw(screen)

    def drawShootingField(self, screen):
        screen.blit(self.shootingField, (0,0))
        self.goalRect = self.goal.get_rect()
        self.goalRect.left, self.goalRect.top = (350,0)
        screen.blit(self.goal, self.goalRect)

    def drawShooter(self,screen):
        shooter = self.curPlayer
        for midfielder in fieldMidfielders:
            if shooter.name == midfielder:
                image = pygame.image.load(fieldMidfielders[midfielder])
                transformImage = pygame.transform.smoothscale(image, (70,256))
        for defender in fieldDefense:
            if shooter.name == defender:
                image = pygame.image.load(fieldDefense[defender])
                transformImage = pygame.transform.smoothscale(image, (70,256))
        for attacker in fieldAttack:
            if shooter.name == attacker:
                image = pygame.image.load(fieldAttack[attacker])
                transformImage = pygame.transform.smoothscale(image, (70,256))
        position = shootingPositions[self.shootingPosition]
        screen.blit(transformImage, position)

    def drawGoalie(self, screen):
        self.shootingModeGoalie.draw(screen)

    def drawBall(self, screen):
        self.shootBall.draw(screen)

    def redrawAll(self, screen):
        if self.intro == True:
            self.introScreen(screen)
        elif self.help == True:
            self.helpScreen(screen)
        elif self.formation == True:
            self.selectPlayers(screen)
            self.drawFormation(screen)
            self.drawStartButton(screen)
        elif self.start == True:
            self.drawField(screen)
            self.drawPlayers(screen)
            self.ball.draw(screen)
        elif self.shootingMode == True:
            self.drawShootingField(screen)
            self.drawShooter(screen)
            self.drawGoalie(screen)
            self.drawBall(screen)
 

    def loadImages(self):
        self.background = pygame.image.load("stadium.jpg")
        self.startButton = pygame.image.load("playbutton2.png")
        self.helpButton = pygame.image.load("helpbutton.png")
        self.helpPage = pygame.image.load("help.png")
        self.continueGame = pygame.image.load("continue.png")
        self.playersChooseBack = pygame.image.load("stadium3.jpg")
        self.bottomPlayers = pygame.image.load("playerschoose.png")
        self.startGame = pygame.image.load("startgame.png")
        self.field = pygame.image.load("longfield.png")
        self.shootingField = pygame.image.load("shootingField.png")
        self.goal = pygame.image.load("goal.png")
        self.startGoalkeeper = pygame.image.load("startgoalkeeper.png")
        self.goalkeeperLeft = pygame.image.load("goalkeeperLeft.png")
        self.goalkeeperRight = pygame.image.load("goalkeeperRight.png")
        self.shootingBall = pygame.image.load("shootingBall.png")

    def loadFieldPlayers(self):
        self.fieldGoalImages = dict()
        self.fieldAttImages= dict()
        self.fieldMidImages= dict()
        self.fieldDefImages = dict()
        image = pygame.transform.smoothscale(self.playersChooseBack, (700,500))
        for goalie in fieldGoalie:
            image = pygame.image.load(fieldGoalie[goalie])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldGoalImages[goalie] = transformImage
        for midfielder in fieldMidfielders:
            image = pygame.image.load(fieldMidfielders[midfielder])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldMidImages[midfielder] = transformImage
        for defender in fieldDefense:
            image = pygame.image.load(fieldDefense[defender])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldDefImages[defender] = transformImage
        for attacker in fieldAttack:
            image = pygame.image.load(fieldAttack[attacker])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldAttImages[attacker] = transformImage

    def setDict(self):
        self.goalButtons = dict()
        self.attackButtons = dict()
        self.midfieldButtons = dict()
        self.defendersButtons = dict()
        self.goalCards = dict()
        self.attackCards = dict()
        self.midfieldCards = dict()
        self.defenderCards = dict()
        self.formationGoalies = []
        self.formationAttack = []
        self.formationMidfield = []
        self.formationDefender = []
        self.loadGoalCard = dict()
        self.loadDefCard = dict()
        self.loadMidCard = dict()
        self.loadAttCard = dict()
        self.goalRects = []
        self.attackRects = []
        self.midRects = []
        self.defenseRects = []

    def loadBall(self):
        image =  pygame.image.load("ball.png")
        self.ballImage = pygame.transform.smoothscale(image, (15,15))

    def __init__(self, width=700, height=500, fps=30, title="World Class Football"):
        self.loadImages()
        self.loadFieldPlayers()
        self.loadBall()
        self.start = False
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.players = []
        self.step = 0
        self.ball = None
        self.curPlayer = None
        self.passingBall = False
        self.passingPlayer = None  
        self.direction = None
        self.justPassed = False
        self.shootingMode = None
        self.shootingPosition = None
        self.goalRect = None
        self.shootingModeGoalie = None
        self.shootBall = None
        self.moveLeft = False
        self.moveRight = False

    def run(self):
        clock = pygame.time.Clock()
        if self.start == True:
            screen = pygame.display.set_mode((1000,500))
        else:
            screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)
            
        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            if self.start == True:
                screen = pygame.display.set_mode((1200,500))
            else:
                screen = pygame.display.set_mode((self.width, self.height))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                    event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                    event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keys = pygame.key.get_pressed()
                    self.keyPressed(event.key, event.mod, self.keys)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()