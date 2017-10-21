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

#########BARCELONA###############################################################

attackDict2 = {"messi": "players/barca/attack/MESSI.png", 
                    "munir":"players/barca/attack/MUNIR.png",
                    "neymar":"players/barca/attack/NEYMAR.png",
                    "suarez":"players/barca/attack/SUAREZ.png"}

defendersDict2 = {"adriano":"players/barca/defenders/ADRIANO.png",
                        "alves":"players/barca/defenders/ALVES.png",
                        "bartra": "players/barca/defenders/BARTRA.png",
                        "alba": "players/barca/defenders/ALBA.png",
                        "mathieu":"players/barca/defenders/MATHIEU.png",
                        "pique":"players/barca/defenders/PIQUE.png",
                        "vermaelen":"players/barca/defenders/VERMAELEN.png",
                        "douglas":"players/barca/defenders/DOUGLAS.png"}

goalieDict2 = {"terstegen":"players/barca/goal/TERSTEGEN.png",
                    "bravo":"players/barca/goal/BRAVO.png" }

midfieldDict2 = {"iniesta":"players/barca/midfield/INIESTA.png",
                        "mascherano":"players/barca/midfield/MASCHERANO.png",
                        "rafinha": "players/barca/midfield/RAFINHA.png",
                        "rakitic": "players/barca/midfield/RAKITIC.png",
                        "roberto":"players/barca/midfield/ROBERTO.png",
                        "turan":"players/barca/midfield/TURAN.png",
                        "busquets":"players/barca/midfield/BUSQUETS.png"}

attackButtonsDict2 = {"messi": "playerButtons/attack/messi.png", 
                    "munir":"playerButtons/attack/munir.png",
                    "neymar":"playerButtons/attack/neymar.png",
                    "suarez":"playerButtons/attack/suarez.png"}

defendersButtonsDict2 = {"adriano":"playerButtons/defenders/adriano.png",
                        "alves":"playerButtons/defenders/alves.png",
                        "bartra": "playerButtons/defenders/bartra.png",
                        "alba": "playerButtons/defenders/alba.png",
                        "mathieu":"playerButtons/defenders/mathieu.png",
                        "pique":"playerButtons/defenders/pique.png",
                        "vermaelen":"playerButtons/defenders/vermaelen.png",
                        "douglas":"playerButtons/defenders/douglas.png"}

goalieButtonsDict2 = {"bravo":"playerButtons/goal/bravo.png",
                    "terstegen":"playerButtons/goal/terstegen.png" }

midfieldButtonsDict2 = {"iniesta":"playerButtons/midfield/iniesta.png",
                        "mascherano":"playerButtons/midfield/mascherano.png",
                        "rafinha": "playerButtons/midfield/rafinha.png",
                        "rakitic": "playerButtons/midfield/rakitic.png",
                        "roberto":"playerButtons/midfield/roberto.png",
                        "turan":"playerButtons/midfield/turan.png",
                        "busquets":"playerButtons/midfield/busquets.png"}

fieldGoalie2 = {"bravo":"fieldplayers/goal/bravo.png",
                    "terstegen":"fieldplayers/goal/terstegen.png" }
fieldMidfielders2 = {"busquets":"fieldplayers/midfield/busquets.png",
                        "iniesta":"fieldplayers/midfield/iniesta.png",
                        "mascherano": "fieldplayers/midfield/mascherano.png",
                        "rafinha": "fieldplayers/midfield/rafinha.png",
                        "rakitic":"fieldplayers/midfield/rakitic.png",
                        "roberto":"fieldplayers/midfield/roberto.png",
                        "turan":"fieldplayers/midfield/turan.png"}
fieldDefense2 = {"adriano":"fieldplayers/defenders/adriano.png",
                        "alba":"fieldplayers/defenders/alba.png",
                        "alves": "fieldplayers/defenders/alves.png",
                        "bartra": "fieldplayers/defenders/bartra.png",
                        "douglas":"fieldplayers/defenders/douglas.png",
                        "mathieu":"fieldplayers/defenders/mathieu.png",
                        "pique":"fieldplayers/defenders/pique.png",
                        "vermaelen":"fieldplayers/defenders/vermaelen.png"}
fieldAttack2 = {"messi": "fieldplayers/attack/messi.png", 
                    "munir":"fieldplayers/attack/munir.png",
                    "neymar":"fieldplayers/attack/neymar.png",
                    "suarez":"fieldplayers/attack/suarez.png"}

startShootingGoalie = {"bravo": "shootingGoalies/straightbravo.png",
                        "terstegen":"shootingGoalies/straightterstegen.png",
                        "casilla":"shootingGoalies/straightcasilla.png",
                        "navas":"shootingGoalies/straightnavas.png"}
flyingShootingGoalie = {"bravo": "shootingGoalies/flyingbravo.png",
                        "terstegen":"shootingGoalies/flyingterstegen.png",
                        "casilla":"shootingGoalies/flyingcasilla.png",
                        "navas":"shootingGoalies/flyingnavas.png"}
downShootingGoalie = {"bravo": "shootingGoalies/downbravo.png",
                        "terstegen":"shootingGoalies/downterstegen.png",
                        "casilla":"shootingGoalies/downcasilla.png",
                        "navas":"shootingGoalies/downnavas.png"}

####VELOCITY#######################################################
attackVelocity = {"bale":9.4, "benzema":8.3, "jese":8.7,"ronaldo":9.2,
                    "messi":9.2, "neymar":9, "suarez":8.2, "munir":8.4}
defenseVelocity = {"arbeloa":7.3, "carvajal":8.1,"danilo":8.1,
                    "marcelo":8.1,"nacho":7.5,"pepe":7.3,
                    "ramos":7.9,"varane":7.9,
                    "adriano":7.6,"alba":9.2,"alves":8.6,"bartra":7.2,
                    "douglas":8.7,"mathieu":7.6,"pique":6.4, "vermaelen":7}
midfieldVelocity = {"casemiro":6.7,"isco":7.5,"kovacic":8.1 ,
                    "kroos":5.6 ,"modric":7.6,"rodriguez":7.8,
                    "vazquez":8.1,
                    "busquets":5.3, "iniesta":7.5, "mascherano":6.8, "rafinha":7.6,
                    "rakitic":6.8, "roberto":7.0, "turan":7.5}
goalVelocity = {"casilla":3.2,"navas":6.1, "bravo":5.8, "terstegen":3.8}

####################################################################
#POWER
#####################################################################

attackPower= {"bale":8.3, "benzema":8.4, "jese":7.4,"ronaldo":9.3,
            "messi":8.8, "neymar":8, "suarez":8.8, "munir":7.3}
defensePower = {"arbeloa":6.1, "carvajal":4,"danilo":7.6 ,
                    "marcelo":6.7,"nacho":3.2,"pepe":5,
                    "ramos":6,"varane":4,
                    "adriano":7.1,"alba":6.9,"alves":7.0,"bartra":4.6,
                    "douglas":6.6,"mathieu":6.4,"pique":5.4, "vermaelen":6.4}
midfieldPower = {"casemiro":6.8,"isco":7.5,"kovacic":6.6,
                    "kroos":8.1 ,"modric":7.4,"rodriguez":8.6,
                    "vazquez":6.5,
                    "busquets":5.9, "iniesta":7.2, "mascherano":5.9, "rafinha":7.3,
                    "rakitic":8.2, "roberto":6.6, "turan":7.4}
goalPower = {"casilla":8.3,"navas":8.2, "bravo":8.3, "terstegen":8.3}

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

goal2 = {"bravo": (110,415), "terstegen": (110,436)}
defense2 = {"adriano": (210,415), "alba": (210,436), "alves": (210,457),
            "bartra": (210,478), "douglas":(320,415), "mathieu": (320,436),
            "pique": (320,457), "vermaelen": (320,478)}
midfield2 = {"busquets":(410,415), "iniesta":(410,436), "mascherano":(410,457),
            "rafinha":(410,478),"rakitic":(520,415),"roberto":(520,436),
            "turan":(520,457)}
attack2 = {"messi": (610,415),"neymar":(610,436), "suarez":(610,457),
            "munir":(610,478)}

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
    
    def move(self, curPlayer,otherPlayer,ball,players):
        if not self.rect.colliderect(curPlayer.rect) and not self.rect.colliderect(otherPlayer.rect):
            if type(self) == Defender:
                self.moveDefender(ball,players)
            elif type(self) == Midfielder:
                self.moveMidfielder(ball,players)
            elif type(self) == Attacker:
                self.moveAttacker(ball,players)
    
    def moveToPlayer(self, minPlayer):
        top1 = self.rect.top
        top2 = minPlayer.rect.top
        left1 = self.rect.left
        left2 = minPlayer.rect.left
        xDiff = left2-left1
        yDiff = top2-top1
        if abs(xDiff) >= self.rect.width + 10:
            vel = (self.velocity*(abs(yDiff)))/(abs(xDiff))
            if xDiff > 0:
                xVelocity = self.velocity
            if xDiff <= 0:
                xVelocity = -self.velocity
            if yDiff > 0:
                yVelocity = vel
            if yDiff <= 0:
                yVelocity = -vel 
            (self.rect.left, self.rect.top) = (self.rect.left+xVelocity/2, self.rect.top+yVelocity/2)


    def moveToDefend(self, players):
        minDistance = None
        minPlayer = None
        for player in players:
            if player.team != self.team and player.name!=self.name:
                x,y = player.rect.left, player.rect.top
                x2,y2 = self.rect.left, self.rect.top
                distance = ((x2-x)**2 + (y2-y)**2)**0.5
                if minDistance == None or distance < minDistance:
                    minDistance = distance
                    minPlayer = player
        if minPlayer != None:
            self.moveToPlayer(minPlayer)

    def moveDefender(self,ball,players):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        if self.team == 1:
            if ball.rect.left <= 450:
                self.moveToDefend(players)
            elif x <= 450:
                (self.rect.left, self.rect.top) = (self.rect.left+self.velocity/2, self.rect.top)
        elif self.team == 2:
            if ball.rect.left >= 725:
                self.moveToDefend(players)
            elif x <= 725:
                (self.rect.left, self.rect.top) = (self.rect.left+self.velocity/2, self.rect.top)

    def moveMidfielder(self,ball,players):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        if self.team == 1 and x <= 750 and ball.rect.left >= 450:
            (self.rect.left, self.rect.top) = (self.rect.left+self.velocity/2, self.rect.top)
        elif self.team == 2 and x > 450 and ball.rect.left <= 750:
            (self.rect.left, self.rect.top) = (self.rect.left-self.velocity/2, self.rect.top)
    
    def moveAttacker(self,ball,players):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        if self.team == 1 and x <= 1000 and ball.rect.left >= 450:
            (self.rect.left, self.rect.top) = (self.rect.left+self.velocity/2, self.rect.top)
        elif self.team == 2 and x > 200 and ball.rect.left <= 750:
            (self.rect.left, self.rect.top) = (self.rect.left-self.velocity/2, self.rect.top)

    def moveLeft(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        bound1Y = ((7/4) * x) - 102.5
        bound2Y = ((-28/17)*x) + (31980/17)
        if ((500-y) <= bound1Y ) and ((500-y) <= bound2Y) and (205 <= y <= 475):
            if self.team == 1:
                (self.rect.left, self.rect.top) = (self.rect.left, self.rect.top-self.velocity)
            elif self.team == 2:
                (self.rect.left, self.rect.top) = (self.rect.left, self.rect.top+self.velocity)

    def moveRight(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        bound1Y = ((7/4) * x) - 102.5
        bound2Y = ((-28/17)*x) + (31980/17)
        if ((500-y) <= bound1Y ) and ((500-y) <= bound2Y) and (205 <= y <= 475):
            if self.team == 1:
                (self.rect.left, self.rect.top) = (self.rect.left, self.rect.top+self.velocity)
            elif self.team == 2:
                (self.rect.left, self.rect.top) = (self.rect.left, self.rect.top-self.velocity)

    def moveForward(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        boundY = ((-28/17)*x) + (31980/17)
        boundY2 = ((7/4) * x) - 112.5
        if (self.team ==1 and (500-y) <= boundY) or (self.team ==2 and (500-y) <= boundY2):
            if self.team == 1:
                (self.rect.left, self.rect.top) = (self.rect.left+self.velocity, self.rect.top)
            elif self.team == 2:
                (self.rect.left, self.rect.top) = (self.rect.left-self.velocity, self.rect.top)

    def moveBackward(self):
        x = self.rect.left + self.rect.width
        y = self.rect.top + self.rect.height
        boundY = ((7/4) * x) - 112.5
        boundY2 = ((-28/17)*x) + (31980/17)
        if  (self.team ==1 and (500-y) <= boundY) or (self.team ==2 and (500-y) <= boundY2):
            if self.team == 1:
                (self.rect.left, self.rect.top) = (self.rect.left-self.velocity, self.rect.top)
            elif self.team == 2:
                (self.rect.left, self.rect.top) = (self.rect.left+self.velocity, self.rect.top)


class Goalie(Player):
    def __init__(self,team,name, pos,image):
        self.name = name
        self.team = team
        self.pos = pos
        if team == 1:
            self.position = fieldGolPos1[pos]
        else: self.position = fieldGolPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity = goalVelocity[name]
        self.power = goalPower[name]
    
    def initPosition(self):
        pos = self.pos
        if self.team == 1:
            self.position = fieldGolPos1[pos]
        else: self.position = fieldGolPos2[pos]
        self.rect.left, self.rect.top = self.position

class Defender(Player):
    def __init__(self,team,name,pos,image):
        self.name = name
        self.team = team
        self.pos = pos
        if team == 1:
            self.position = fieldDefPos1[pos]
        else: self.position = fieldDefPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity =defenseVelocity[name]
        self.power = defensePower[name]
    
    def initPosition(self):
        pos = self.pos
        if self.team == 1:
            self.position = fieldDefPos1[pos]
        else: self.position = fieldDefPos2[pos]
        self.rect.left, self.rect.top = self.position

class Midfielder(Player):
    def __init__(self,team,name,pos,image):
        self.name = name
        self.team = team
        self.pos = pos
        if team == 1:
            self.position = fieldMidPos1[pos]
        else: self.position = fieldMidPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity = midfieldVelocity[name]
        self.power = midfieldPower[name]

    def initPosition(self):
        pos = self.pos
        if self.team == 1:
            self.position = fieldMidPos1[pos]
        else: self.position = fieldMidPos2[pos]
        self.rect.left, self.rect.top = self.position

class Attacker(Player):
    def __init__(self,team,name,pos,image):
        self.name = name
        self.team = team
        self.pos = pos
        if team == 1:
            self.position = fieldAttPos1[pos]
        else: self.position = fieldAttPos2[pos]
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.velocity = attackVelocity[name]
        self.power = attackPower[name]

    def initPosition(self):
        pos = self.pos
        if self.team == 1:
            self.position = fieldAttPos1[pos]
        else: self.position = fieldAttPos2[pos]
        self.rect.left, self.rect.top = self.position

class Ball(object):
    def __init__(self,currentPlayer,image):
        self.currentPlayer = currentPlayer 
        self.image = image
        
        self.rect = self.image.get_rect()
        self.initPosition()


    def initPosition(self):
        currentPlayer = self.currentPlayer
        if currentPlayer.team == 1:
           offset = 0
        elif currentPlayer.team == 2:
            offset = 10
        (topx,topy) = (currentPlayer.rect.left, currentPlayer.rect.top)
        position = (topx + currentPlayer.rect.width/2-offset, topy + currentPlayer.rect.height-10)
        self.rect.left, self.rect.top = position

    def passBall(self,player, direction):
        (xPos, yPos) = (self.rect.left, self.rect.top)
        bound1Y = ((7/4) * xPos) - 102.5
        bound2Y = ((-28/17)*xPos) + (31980/17)
        if (((500-yPos) <= bound1Y ) and ((500-yPos) <= bound2Y) and (yPos <= 475)
            and (yPos >= 205) and (self.rect.top+self.rect.height <=475)):
            velocity = player.power/2 
            (x,y) = DIRECTIONS[direction]  
            moveX, moveY = ((x*velocity), (y*velocity))
            (self.rect.left, self.rect.top) = (self.rect.left+moveX, self.rect.top+moveY)

    def move(self, passingBall, currentPlayer):
        player = currentPlayer
        if player.team == 1:
           offset = 0
        elif player.team == 2:
            offset = 10
        if passingBall == False:
            (topx,topy) = (player.rect.left, player.rect.top)
            position = (topx + player.rect.width/2-offset, topy + player.rect.height-10)
            self.rect.left, self.rect.top = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class ShootingModeGoalie(object):
    def __init__(self, goalie, startImage,flyingImage,downImage):
        self.goalie = goalie
        self.image = startImage
        self.flyingImage = flyingImage
        self.downImage = downImage
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (570,60)
        self.horizVelocity = goalVelocity[goalie.name] 
        self.vertVelocity = goalVelocity[goalie.name]
        self.down = False
        self.left = False
        self.right = False
        self.endImage = None
        self.end = False

    def changeImage(self,direction):
        self.image = self.flyingImage
        self.rect = self.flyingImage.get_rect()
        if direction == "left":
            self.rect.left, self.rect.top = (455,80)
            self.left = True
        elif direction == "right":
            self.image = pygame.transform.flip(self.flyingImage,1,0)
            self.rect = self.image.get_rect()
            self.right = True
            self.rect.left, self.rect.top = (550,90)

    def draw(self,screen):
        if self.down == True:
            if self.left == True:
                self.endImage = self.downImage
            elif self.right == True:
                self.endImage = pygame.transform.flip(self.downImage,1,0)
        elif self.end == True: 
            self.image = self.endImage
            self.rect.top = 200
        screen.blit(self.image, self.rect)
    
    def moveLeft(self):
        if self.down == False and (350 < self.rect.left < 850) and (0 <self.rect.top <200):
            (self.rect.left, self.rect.top) = (self.rect.left- self.horizVelocity, self.rect.top-self.vertVelocity)
        else: 
            self.down = True
            
    def moveRight(self):
        if self.down == False and (350 < self.rect.left < 850) and (0 <self.rect.top <200):
            (self.rect.left, self.rect.top) = (self.rect.left+ self.horizVelocity, self.rect.top-self.vertVelocity)
        else:
            self.down = True


    def moveDown(self):
        if self.down == True and (self.rect.top <= 100):
            (self.rect.left, self.rect.top) = (self.rect.left, self.rect.top + self.vertVelocity)
        else: 
            self.down = False
            self.end = True

class ShootBall(object):

    def __init__(self,image,playerPosition):
        self.image = image
        self.rect = self.image.get_rect()
        x,y = shootingPositions[playerPosition]
        (self.rect.left, self.rect.top) = (x+50, y+210)
        self.moving = False

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def move(self,x,y):
        (self.rect.left, self.rect.top) = (x,y)

class PygameGame(object):
    def init(self):
        self.setDict1()
        self.setDict2()
        self.intro = True
        self.startButtonRect = None
        self.helpButtonRect = None
        self.help = False
        self.continueRect = None
        self.teamTwoButtonRect = None
        self.startGameButtonRect = None
        self.fullTeam = 11
        self.loadImages()
        self.loadFieldPlayers()
        self.loadFieldPlayers2()
        self.loadBall()
        self.loadShootingGoalieImages()
        self.initStats()
        self.start = False
        self.team1 = False
        self.team2 = False
        self.players = []
        self.step = 0
        self.ball = None
        self.curPlayer = None
        self.curPlayer2 = None 
        self.initPassingMode()
        self.initShootingMode()
        self.teamOneGoalie = None
        self.teamTwoGoalie = None
        self.pressedStart = False
        self.halfTime = False
        self.fullTime = False
        self.secondHalf = False
        self.timer = 0
        pygame.init()

    def getFormation(self,x,y):
        for goalie in self.goalCards:
            if self.goalCards[goalie].collidepoint(x,y):
                if len(self.formationGoalies)== 0:
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
                if len(self.formationMidfield) < 3 and midfielder not in self.formationMidfield:
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
   
    def getFormation2(self,x,y):
        for goalie in self.goalCards2:
            if self.goalCards2[goalie].collidepoint(x,y):
                if len(self.formationGoalies2)== 0:
                    self.formationGoalies2.append(goalie)
        for attacker in self.attackCards2:
            if self.attackCards2[attacker].collidepoint(x,y):
                if len(self.formationAttack2) < 3 and attacker not in self.formationAttack2:
                    self.formationAttack2.append(attacker)
        for defender in self.defenderCards2:
            if self.defenderCards2[defender].collidepoint(x,y):
                if len(self.formationDefender2) < 4 and defender not in self.formationDefender2:
                    self.formationDefender2.append(defender)
        for midfielder in self.midfieldCards2:
            if self.midfieldCards2[midfielder].collidepoint(x,y):
                if len(self.formationMidfield2) < 3 and midfielder not in self.formationMidfield2:
                    self.formationMidfield2.append(midfielder)
    
    def removeCards2(self, x, y):
        for goalie in self.goalRects2:
            if goalie[1].collidepoint(x,y):
                self.formationGoalies2.remove(goalie[0])
                self.goalRects2.remove(goalie)
        for attacker in self.attackRects2:
            if attacker[1].collidepoint(x,y):
                self.formationAttack2.remove(attacker[0])
                self.attackRects2.remove(attacker)
        for midfielder in self.midRects2:
            if midfielder[1].collidepoint(x,y):
                self.formationMidfield2.remove(midfielder[0])
                self.midRects2.remove(midfielder)
        for defender in self.defenseRects2:
            if defender[1].collidepoint(x,y):
                self.formationDefender2.remove(defender[0])
                self.defenseRects2.remove(defender)

    def setPlayerInstances(self):
        for i in range(len(self.formationGoalies)):
            goalie = self.formationGoalies[i]
            image = self.fieldGoalImages[goalie]
            goalieInstance = Goalie(1,goalie,i,image)
            self.players.append(goalieInstance)
            self.teamOneGoalie = goalieInstance
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

    def setPlayerInstances2(self):
        for i in range(len(self.formationGoalies2)):
            goalie = self.formationGoalies2[i]
            image = self.fieldGoalImages2[goalie]
            fieldImage = pygame.transform.flip(image,1,0)
            goalieInstance = Goalie(2,goalie,i,fieldImage)
            self.players.append(goalieInstance)
            self.teamTwoGoalie = goalieInstance
        for i in range(len(self.formationDefender2)):
            defender = self.formationDefender2[i]
            image = self.fieldDefImages2[defender]
            fieldImage = pygame.transform.flip(image,1,0)
            self.players.append(Defender(2,defender,i,fieldImage))
        for i in range(len(self.formationMidfield2)):
            midfielder = self.formationMidfield2[i]
            image = self.fieldMidImages2[midfielder]
            fieldImage = pygame.transform.flip(image,1,0)
            self.players.append(Midfielder(2,midfielder,i,fieldImage))
        for i in range(len(self.formationAttack2)):
            attacker = self.formationAttack2[i]
            image = self.fieldAttImages2[attacker]
            fieldImage = pygame.transform.flip(image,1,0)
            self.players.append(Attacker(2,attacker,i,fieldImage))
        

    def mousePressed(self, x, y):
        if self.intro == True:
            if self.startButtonRect.collidepoint(x,y):
                self.intro = False
                self.team1 = True
            if self.helpButtonRect.collidepoint(x,y):
                self.intro = False
                self.help = True
        elif self.help == True:
            if self.continueRect.collidepoint(x,y):
                self.help = False
                self.intro = True
        elif self.team1 == True:
            self.getFormation(x,y)
            self.removeCards(x,y)
            if self.teamTwoButtonRect.collidepoint(x,y):
                if (len(self.formationGoalies) + len(self.formationAttack)+
                    len(self.formationDefender) + 
                    len(self.formationMidfield)) == self.fullTeam:
                    self.team2 = True
                    self.team1 = False
        elif self.team2 == True:
            self.getFormation2(x,y)
            self.removeCards2(x,y)
            if self.startGameButtonRect.collidepoint(x,y):
                if (len(self.formationGoalies2) + len(self.formationAttack2)+
                    len(self.formationDefender2) + 
                    len(self.formationMidfield2)) == self.fullTeam:
                        self.setPlayerInstances()
                        self.setPlayerInstances2()
                        self.curPlayer = self.players[self.fullTeam-1]
                        self.curPlayer2= self.players[-1]
                        self.ball = Ball(self.curPlayer,self.ballImage)
                        self.start = True
                        self.team2 = False
                        self.width = 1200
                        self.height = 500   
        elif self.shootingMode == True:
            if self.shootBall.rect.collidepoint(x,y):
                self.clicked = True
            if self.continueRect != None and self.continueRect.collidepoint(x,y):
                if self.curPlayer.team ==1:
                    self.teamOneShots += 1
                    if self.outcome == "SCORED" or self.outcome == "SAVED":
                        self.teamOneShotsOnTar += 1 
                    if self.outcome == "SAVED":
                        self.teamTwoGoalsSaved += 1
                elif self.curPlayer.team == 2:
                    self.teamTwoShots += 1
                    if self.outcome == "SCORED" or self.outcome == "SAVED":
                        self.teamTwoShotsOnTar += 1
                    if self.outcome == "SAVED":
                        self.teamOneGoalsSaved += 1
                self.restart()
            elif self.clicked == True and len(self.path) > 2:
                self.shootBall.moving = True
                self.clicked = False
                self.kicked = True
                self.path = []

    def restart(self):
         for player in self.players:
            player.initPosition()
            self.curPlayer = self.players[self.fullTeam-1]
            self.curPlayer2 = self.players[-1]
            self.shootingMode = False
            self.start = True
            self.ball.move(False, self.curPlayer)
            self.initPassingMode()
            self.initShootingMode()
            self.pressedStart = False

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        if self.shootingMode == True and self.clicked == True and self.kicked == False:
            self.ballMovements.append((x,y))
            self.path.append((x,y))

    def mouseDrag(self, x, y):
        pass

    def setShootingGoalie(self,goalie):
        sI = self.startGoalie[goalie.name]
        fI = self.flyingGoalie[goalie.name]
        dI = self.downGoalie[goalie.name]
        self.shootingModeGoalie = ShootingModeGoalie(goalie, sI, fI, dI)

    def isShootingMode(self):
        if self.passingBall == False:
            (x,y) = (self.ball.rect.left + self.ball.rect.width, self.ball.rect.top+self.ball.rect.height)
            if ((self.curPlayer.team == 1 and 250 <= y <= 400 and x >= 875)
                or (self.curPlayer.team == 2 and 250 <= y <= 400 and x <=350)):
                self.shootingMode = True
                self.start = False
                if self.curPlayer.team == 1:
                    self.setShootingGoalie(self.teamTwoGoalie)
                elif self.curPlayer.team == 2:
                    self.setShootingGoalie(self.teamOneGoalie)
                if 250 <= y < 280:
                    if self.curPlayer.team == 1:
                        self.shootingPosition = "left"
                    else: self.shootingPosition = "right"
                elif 280 <= y < 350:
                    self.shootingPosition = "middle"
                elif 350 <= y < 400:
                    if self.curPlayer.team == 1:
                        self.shootingPosition = "right"
                    else: self.shootingPosition = "left"
                self.shootBall = ShootBall(self.shootingBall, self.shootingPosition)

    def getDirection(self):
        if self.curPlayer.team == 1:
            up = pygame.K_UP
            down = pygame.K_DOWN
            left = pygame.K_LEFT
            right = pygame.K_RIGHT
        if self.curPlayer.team == 2:
            down = pygame.K_w
            up = pygame.K_s
            right = pygame.K_a
            left = pygame.K_d
        if self.passingBall == False:
            if self.isKeyPressed(up) and self.isKeyPressed(left):
                self.direction = "NW"
            elif self.isKeyPressed(up) and self.isKeyPressed(right):
                self.direction =  "NE"
            elif self.isKeyPressed(down) and self.isKeyPressed(left):
                self.direction =  "SW"
            elif self.isKeyPressed(down) and self.isKeyPressed(right):
                self.direction =  "SE"
            elif self.isKeyPressed(down):
                self.direction =  "S"
            elif self.isKeyPressed(up):
                self.direction =  "N"
            elif self.isKeyPressed(right):
                self.direction =  "E"
            elif self.isKeyPressed(left):
                self.direction =  "W"

    def keyPressed(self, keyCode, modifier):
        if self.start == True:
            if self.pressedStart == True:
                if self.isKeyPressed(pygame.K_SPACE):
                    self.getDirection()
                    if self.direction != None:
                        self.passingPlayer = self.curPlayer
                        self.passingBall = True
                        self.justPassed = True
                if self.curPlayer.team == 1:
                    if keyCode == pygame.K_LEFT:
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
                if self.curPlayer2.team == 1:
                    if keyCode == pygame.K_LEFT:
                        self.curPlayer2.moveLeft()
                    elif keyCode == pygame.K_RIGHT:
                        self.curPlayer2.moveRight()
                    elif keyCode == pygame.K_DOWN:
                        self.curPlayer2.moveBackward()
                    elif keyCode == pygame.K_UP:
                        self.curPlayer2.moveForward()
                if self.curPlayer.team == 2:
                    if keyCode == pygame.K_a:
                        self.curPlayer.moveLeft()
                        self.ball.move(self.passingBall,self.curPlayer)
                    elif keyCode == pygame.K_d:
                        self.curPlayer.moveRight()
                        self.ball.move(self.passingBall,self.curPlayer)
                    elif keyCode == pygame.K_s:
                        self.curPlayer.moveBackward()
                        self.ball.move(self.passingBall,self.curPlayer)
                    elif keyCode == pygame.K_w:
                        self.curPlayer.moveForward()
                        self.ball.move(self.passingBall,self.curPlayer)
                if self.curPlayer2.team == 2:
                    if keyCode == pygame.K_a:
                        self.curPlayer2.moveLeft()
                    elif keyCode == pygame.K_d:
                        self.curPlayer2.moveRight()
                    elif keyCode == pygame.K_s:
                        self.curPlayer2.moveBackward()
                    elif keyCode == pygame.K_w:
                        self.curPlayer2.moveForward()
            if (self.halfTime == False and self.fullTime == False and keyCode == pygame.K_p):
                self.pressedStart = False
            if self.pressedStart == False and keyCode == pygame.K_ESCAPE:
                self.restart()
                self.intro = True
                self.width = 700
                self.height = 500
                self.init()
                self.start = False
            elif self.fullTime == True and keyCode == pygame.K_r:
                self.restart()
                self.intro = True
                self.width = 700
                self.height = 500
                self.init()
                self.start = False
            elif self.halfTime == True and keyCode == pygame.K_r:
                self.halfTime = False
                self.secondHalf = True
                self.restart()
            elif (self.halfTime == False and self.fullTime == False
                    and keyCode == pygame.K_RETURN):
                self.pressedStart = True
            
        elif self.shootingMode == True:
            if keyCode == pygame.K_LEFT and self.movedGoalie == False:
                self.shootingModeGoalie.changeImage("left")
                self.moveLeft = True
                self.movedGoalie = True
            elif keyCode == pygame.K_RIGHT and self.movedGoalie == False:
                self.shootingModeGoalie.changeImage("right")
                self.moveRight = True
                self.movedGoalie = True
            elif keyCode == pygame.K_p:
                self.shootBall.moving = True
                self.clicked = False
                self.kicked = True
                self.path = []

    def keyReleased(self, keyCode, modifier):
        pass
    
    
    def isKeyPressed(self, key):
        ''' return whether a specific key was pressed'''
        return self._keys.get(key,False)
        

    def findDistance(self):
        width, height = self.curPlayer2.rect.width, self.curPlayer2.rect.height
        (x,y) = (self.curPlayer2.rect.left+width/2-10, self.curPlayer2.rect.top+height-10)
        x2,y2 = self.ball.rect.left, self.ball.rect.top
        minDistance = (((x2-x)**2+(y2-y)**2)**0.5)
        return minDistance

    def changeCurrentPlayer(self):
        minPlayer = self.curPlayer
        width, height = self.curPlayer.rect.width, self.curPlayer.rect.height
        (x,y) = (self.curPlayer.rect.left+width/2, self.curPlayer.rect.top+height-10)
        x2,y2 = self.ball.rect.left, self.ball.rect.top
        minDistance = (((x2-x)**2+(y2-y)**2)**0.5)
        for player in self.players:
            width,height = player.rect.width,player.rect.height
            (x,y) = (player.rect.left+width/2, player.rect.top+height-10)
            distance = (((x2-x)**2+(y2-y)**2)**0.5)
            if distance < minDistance:
                minDistance = distance
                minPlayer = player
        self.curPlayer = minPlayer
        self.interceptBall(self.curPlayer)
        

    def interceptBall(self,player):
        if player.team == 1: offset = 0
        elif player.team == 2: offset = 10
        width, height = player.rect.width, player.rect.height
        (x,y) = (player.rect.left+width/2-offset, player.rect.top+height-10)
        x2,y2 = self.ball.rect.left, self.ball.rect.top
        distance = (((x2-x)**2+(y2-y)**2)**0.5)
        if distance < 10 and self.justPassed == False:
            if self.passingPlayer != None and self.passingPlayer.team == player.team:
                if player.team == 1:
                    self.teamOnePassing +=1
                elif player.team == 2:
                    self.teamTwoPassing += 1
            self.passingBall = False
            self.passingPlayer = None

    def updateGame(self):
        if self.outcome == "SAVED!" or self.outcome == "SCORED!" or self.outcome == "MISSED!":
            self.showOutcome = True
            if self.outcome == "SCORED!":
                if self.curPlayer.team == 1:
                    self.teamOneScore += 1
                elif self.curPlayer.team == 2:
                    self.teamTwoScore += 1
    
    def goalieCollision(self):
        goalie = self.shootingModeGoalie
        (x,y) = self.shootBall.rect.left, self.shootBall.rect.top
        (x2, y2) = (x + self.shootBall.rect.width, y + self.shootBall.rect.height)
        if self.shootingModeGoalie.left == True:
            if (((55 <= x <= 165) and (0 <= y <= 60) and 
                (55 <= x2 <= 165) and (0 <= y2 <= 60)) or 
                ((0<=x<=25) and (40<=y<=165) and 
                 (0<=x2<=25) and (40<=y2<=165))):
                 return False
            elif goalie.rect.colliderect(self.shootBall.rect):
                return True
            else:
                return False
        elif self.shootingModeGoalie.right == True:
            if (((0 <= x <= 110) and (0 <= y <= 60) and 
                (0 <= x2 <= 110) and (0 <= y2 <= 60)) or 
                ((140 <= x <= 165) and (40 <= y <=165) and 
                 (140 <= x2 <= 165) and (40 <= y2 <=165))):
                 return False
            elif goalie.rect.colliderect(self.shootBall.rect):
                return True 
            else:
                return False

    def checkCollision(self):
        goalie = self.shootingModeGoalie
        if self.goalieCollision():
            self.outcome = "SAVED!"
        elif (len(self.ballMovements) == 0 and 
            self.goalRect.colliderect(self.shootBall.rect)):
            self.outcome = "SCORED!"
        elif len(self.ballMovements) == 0 and self.kicked == True:
            self.outcome = "MISSED!"
        self.updateGame()

    def moveGoalie(self):
        if self.moveLeft == True:
            self.shootingModeGoalie.moveLeft()
        elif self.moveRight == True:
            self.shootingModeGoalie.moveRight()
        elif self.moveDown == True:
            self.shootingModeGoalie.moveDown()

    def getOtherCurPlayer(self):
        otherMinPlayer = self.curPlayer2
        otherMinDistance = self.findDistance()
        x2,y2 = self.ball.rect.left, self.ball.rect.top
        teamType = self.curPlayer.team
        if teamType == 1: offset = 0
        elif teamType == 2: offset = 10
        for player in self.players:
            if player.team != teamType:
                width,height = player.rect.width,player.rect.height
                (x,y) = (player.rect.left+width/2-offset, player.rect.top+height-10)
                distance = (((x2-x)**2+(y2-y)**2)**0.5)
                if distance < otherMinDistance:
                    otherMinDistance = distance
                    otherMinPlayer = player
        self.curPlayer2 = otherMinPlayer
        self.interceptBall(self.curPlayer2)
    
    def isGoal(self):
        x = self.ball.rect.left
        y = self.ball.rect.top
        boundY = ((7/4) * x) - 112.5
        boundY2 = ((-28/17)*x) + (31980/17)
        if (285 <= y <= 340) and (500-y) >= (boundY-5):
            self.teamTwoScore += 1
            self.restart()
        elif (285 <= y+self.ball.rect.height <= 340) and (500-(y+self.ball.rect.height)) >= (boundY2-5):
            self.teamOneScore += 1
            self.restart()


    def timerFired(self, dt):
        if self.pressedStart == True:
            self.step +=1
            if self.step % 30 == 0:
                self.timer +=1
                if self.curPlayer.team ==1:
                    self.teamOnePos += 1
                elif self.curPlayer.team == 2:
                    self.teamTwoPos += 1
        if self.timer == self.half:
            if self.secondHalf == True:
                self.fullTime = True
            else:
                self.halfTime = True
            self.pressedStart = False
            self.timer = 0
        if self.shootingMode == True: 
            if self.outcome == None:
                if self.shootBall.moving == True and len(self.ballMovements) > 0:
                    if self.step % round(10-self.curPlayer.power) == 0: 
                        (x,y) = self.ballMovements[0]
                        self.ballMovements.pop(0)
                        self.shootBall.move(x,y)
                if (self.shootingModeGoalie.down == True):
                        self.moveLeft = False
                        self.moveRight = False
                        self.moveDown = True
                self.moveGoalie() 
                self.checkCollision() 
        elif self.start == True and self.pressedStart == True:
            self.isShootingMode()
            if self.passingBall == True:
                self.ball.passBall(self.passingPlayer, self.direction)
            if self.step % 5 == 0:
                for player in self.players:
                    if player.name != self.curPlayer.name and player.name != self.curPlayer2.name:
                        player.move(self.curPlayer, self.curPlayer2,self.ball,self.players) 
            self.getOtherCurPlayer()
            self.isGoal()
        if self.passingBall == True:
            self.changeCurrentPlayer()
            self.getOtherCurPlayer()
            self.isGoal()
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


    def loadNames2(self):
        for goalie in goalieButtonsDict2:
            image1 = pygame.image.load(goalieButtonsDict2[goalie]).convert_alpha()
            self.goalButtons2[goalie] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(goalieDict2[goalie])
            goalieCard = pygame.transform.smoothscale(image, (58,80))
            self.loadGoalCard2[goalie] = goalieCard
        for attacker in attackButtonsDict2:
            image1 = pygame.image.load(attackButtonsDict2[attacker]).convert_alpha()
            self.attackButtons2[attacker] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(attackDict2[attacker])
            attack = pygame.transform.smoothscale(image, (58,80))
            self.loadAttCard2[attacker] = attack
        for defender in defendersButtonsDict2:
            image1 = pygame.image.load(defendersButtonsDict2[defender]).convert_alpha()
            self.defendersButtons2[defender] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(defendersDict2[defender])
            defend = pygame.transform.smoothscale(image, (58,80))
            self.loadDefCard2[defender] = defend
        for midfielder in midfieldButtonsDict2:
            image1 = pygame.image.load(midfieldButtonsDict2[midfielder]).convert_alpha()
            self.midfieldButtons2[midfielder] = pygame.transform.smoothscale(image1,(80,12))
            image = pygame.image.load(midfieldDict2[midfielder])
            midfield = pygame.transform.smoothscale(image, (58,80))
            self.loadMidCard2[midfielder] = midfield

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

    def displayNames2(self,screen):
        for goalie in self.goalButtons2:
            goalieRect = self.goalButtons2[goalie].get_rect()
            goalieRect.left, goalieRect.top = goal2[goalie]
            self.goalCards2[goalie] = goalieRect
            screen.blit(self.goalButtons2[goalie],goalieRect)
        for mid in self.midfieldButtons2:
            midRect = self.midfieldButtons2[mid].get_rect()
            midRect.left, midRect.top = midfield2[mid]
            self.midfieldCards2[mid] = midRect
            screen.blit(self.midfieldButtons2[mid],midRect)
        for defender in self.defendersButtons2:
            defRect = self.defendersButtons2[defender].get_rect()
            defRect.left, defRect.top = defense2[defender]
            self.defenderCards2[defender] = defRect
            screen.blit(self.defendersButtons2[defender],defRect)
        for attacker in self.attackButtons2:
            attackRect = self.attackButtons2[attacker].get_rect()
            attackRect.left, attackRect.top = attack2[attacker]
            self.attackCards2[attacker] = attackRect
            screen.blit(self.attackButtons2[attacker],attackRect)

    def selectPlayers(self,screen):
        image = pygame.transform.smoothscale(self.playersChooseBack, (700,500))
        screen.blit(image,(0,0))
        image = pygame.transform.smoothscale(self.bottomPlayers, (700,100)).convert_alpha()
        screen.blit(image,(0,400))
        self.loadNames()
        self.displayNames(screen)
        
    def selectPlayers2(self,screen):
        image = pygame.transform.smoothscale(self.playersChooseBack, (700,500))
        screen.blit(image,(0,0))
        image = pygame.transform.smoothscale(self.barcabanner, (700,100)).convert_alpha()
        screen.blit(image,(0,400)) 
        self.loadNames2()
        self.displayNames2(screen)

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

    def drawFormation2(self,screen):
        for goalie in self.formationGoalies2:
            goalieRect = self.loadGoalCard2[goalie].get_rect()
            goalieRect.left, goalieRect.top = formGoalie[0]
            screen.blit(self.loadGoalCard2[goalie],goalieRect)
            if (goalie,goalieRect) not in self.goalRects2:
                self.goalRects2.append((goalie,goalieRect))
        for i in range(len(self.formationDefender2)):
            defender = self.formationDefender2[i]
            defenseRect = self.loadDefCard2[defender].get_rect()
            defenseRect.left, defenseRect.top = formDefense[i]
            screen.blit(self.loadDefCard2[defender],defenseRect)
            if (defender,defenseRect) not in self.defenseRects2:
                self.defenseRects2.append((defender,defenseRect))
        for i in range(len(self.formationAttack2)):
            attacker = self.formationAttack2[i]
            attackRect = self.loadAttCard2[attacker].get_rect()
            attackRect.left, attackRect.top = formAttack[i]
            screen.blit(self.loadAttCard2[attacker], attackRect)
            if (attacker,attackRect) not in self.attackRects2:
                self.attackRects2.append((attacker,attackRect))
        for i in range(len(self.formationMidfield2)):
            midfielder = self.formationMidfield2[i]
            midRect = self.loadMidCard2[midfielder].get_rect()
            midRect.left, midRect.top = formMidfield[i]
            screen.blit(self.loadMidCard2[midfielder], midRect)
            if (midfielder,midRect) not in self.midRects2:
                self.midRects2.append((midfielder,midRect))

    def drawStartButton(self, screen):
        self.startGameButtonRect = self.startGame.get_rect()
        (self.startGameButtonRect.left, self.startGameButtonRect.top) = (550, 25)
        screen.blit(self.startGame, self.startGameButtonRect)

    def drawTeamTwoButton(self,screen):
        self.teamTwoButtonRect = self.teamTwoButton.get_rect()
        (self.teamTwoButtonRect.left, self.teamTwoButtonRect.top) = (550, 25)
        screen.blit(self.teamTwoButton, self.teamTwoButtonRect)


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
        transformImage = None
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
        for midfielder2 in fieldMidfielders2:
            if shooter.name == midfielder2:
                image = pygame.image.load(fieldMidfielders2[midfielder2])
                transformImage = pygame.transform.smoothscale(image, (70,256))
        for defender2 in fieldDefense2:
            if shooter.name == defender2:
                image = pygame.image.load(fieldDefense2[defender2])
                transformImage = pygame.transform.smoothscale(image, (70,256))
        for attacker2 in fieldAttack2:
            if shooter.name == attacker2:
                image = pygame.image.load(fieldAttack2[attacker2])
                transformImage = pygame.transform.smoothscale(image, (70,256))
        if transformImage != None:
            position = shootingPositions[self.shootingPosition]
            screen.blit(transformImage, position)

    def drawGoalie(self, screen):
        self.shootingModeGoalie.draw(screen)

    def drawBall(self, screen):
        self.shootBall.draw(screen)

    def drawPath(self, screen):
        if len(self.path) > 2:
            for i in range (1,len(self.path)):
                pygame.draw.line(screen, (0,0,0), self.path[i-1], self.path[i])
    
    def drawOutcome(self, screen):
        font = pygame.font.Font(None, 100)
        text = font.render(self.outcome, 1, (236, 15, 30))
        rect = text.get_rect()
        rect.left, rect.top = 500, self.height/2
        screen.blit(text, rect)
        self.continueRect = self.continueGame.get_rect()
        self.continueRect.left, self.continueRect.top = (50,50)
        screen.blit(self.continueGame,self.continueRect)

    def drawShootingScore(self,screen):
        rect = (950,50,200,20)
        pygame.draw.rect(screen, (255,255,255),rect)
        font = pygame.font.Font(None, 30)
        score = ("Real Madrid: %d Barcelona: %d" % (self.teamOneScore, self.teamTwoScore))
        text = font.render(score, 1, (10, 10, 10))
        rect = text.get_rect()
        (rect.left, rect.top) = (900, 50)
        screen.blit(text, rect)

    def drawGameScore(self,screen):
        font = pygame.font.Font(None, 30)
        score = ("Real Madrid: %d  Barcelona: %d" %(self.teamOneScore, self.teamTwoScore))
        text = font.render(score, 1, (250, 250, 250))
        rect = text.get_rect()
        (rect.left, rect.top) = (500, 30)
        screen.blit(text, rect)
    
    def drawPressStart(self,screen):
        if self.pressedStart == False:
            font = pygame.font.Font(None, 30)
            msg = "Press ENTER to start"
            text = font.render(msg, 1, (250, 250, 250))
            rect = text.get_rect()
            (rect.left, rect.top) = (550, 300)
            screen.blit(text, rect)

    def drawCurrentPlayers(self,screen):
        x,y = self.curPlayer.rect.left,self.curPlayer.rect.top
        xpos = x+(self.curPlayer.rect.width//2)
        ypos = y - 10
        pygame.draw.circle(screen, (15,15,15), (xpos,ypos), 5)
        x,y = self.curPlayer2.rect.left,self.curPlayer2.rect.top
        xpos = x+(self.curPlayer2.rect.width//2)
        ypos = y - 10
        pygame.draw.circle(screen, (150,150,150), (xpos,ypos), 5)


    def displayTime(self,screen):
        font = pygame.font.Font(None, 30)
        sec = self.timer % 60
        minute = self.timer//60
        text = font.render("Time %d:%d " %(minute,sec), 1, (10, 10, 10))
        rect = text.get_rect()
        (rect.left, rect.top) = (600, 10)
        screen.blit(text, rect)
    
    def displayStats(self, screen, time):
        if time == "half":
            total = self.half
        elif time == "full":
            total = 2*self.half
        pygame.draw.rect(screen, (255,255,255), (500,200,250,150))
        font = pygame.font.Font(None, 20)
        stats = "                 Real Madrid    Barcelona"
        score = "Score                       %d            %d" %((self.teamOneScore), (self.teamTwoScore))
        shots = "Shots                       %d            %d" %((self.teamOneShots),(self.teamTwoShots))          
        shotsTar= "Shots On Target       %d            %d" %((self.teamOneShotsOnTar), (self.teamTwoShotsOnTar))          
        goals = "Goals Saved             %d            %d" %((self.teamOneGoalsSaved), (self.teamTwoGoalsSaved))
        passing="Passing Completion  %d            %d" %((self.teamOnePassing),(self.teamTwoPassing))
        possession = "Possession               %d            %d" % (((self.teamOnePos)/total)*100, ((self.teamTwoPos)/total)*100)
        resume = "Press r to continue"
        items = [stats,score,shots,shotsTar,goals,passing,possession]
        for i in range(len(items)):
            text = font.render(items[i], 1, (10, 10, 10))
            rect = text.get_rect()
            (rect.left, rect.top) = (500, 200+(20*i))
            screen.blit(text, rect)
        text = font.render(resume, 1, (10, 10, 10))
        rect = text.get_rect()
        (rect.left, rect.top) = (550, 360)
        screen.blit(text, rect)
    
    def displayWinner(self,screen):
        font = pygame.font.Font(None, 50)
        if self.teamOneScore > self.teamTwoScore:
            message = "Real Madrid Wins!"
        elif self.teamTwoScore > self.teamOneScore:
            message = "Barcelona Wins!"
        else:
            message = "Tie Game!"
        text = font.render(message, 1, (10, 10, 10))
        rect = text.get_rect()
        (rect.left, rect.top) = (500, 400)
        screen.blit(text, rect)

    def drawDirections(self, screen):
        font = pygame.font.Font(None, 20)
        message = """Press p to pause and Escape to go back to home screen"""
        text = font.render(message, 1, (255,255,255))
        rect = text.get_rect()
        (rect.left, rect.top) = (10, 10)
        screen.blit(text, rect)

    def redrawAll(self, screen):
        if self.intro == True:
            self.introScreen(screen)
        elif self.help == True:
            self.helpScreen(screen)
        elif self.team1 == True:
            self.selectPlayers(screen)
            self.drawFormation(screen)
            self.drawTeamTwoButton(screen)
        elif self.team2 == True:
            self.selectPlayers2(screen)
            self.drawFormation2(screen)
            self.drawStartButton(screen)
        elif self.start == True:
            self.drawField(screen)
            self.drawCurrentPlayers(screen)
            self.drawPlayers(screen)
            self.ball.draw(screen)
            self.drawGameScore(screen)
            self.drawDirections(screen)
            self.drawPressStart(screen)
            self.displayTime(screen)
            if self.halfTime == True:
                self.displayStats(screen,"half")
            if self.fullTime == True:
                self.displayStats(screen,"full")
                self.displayWinner(screen)
        elif self.shootingMode == True:
            self.drawShootingField(screen)
            self.drawShooter(screen)
            self.drawGoalie(screen)
            self.drawBall(screen)
            self.drawPath(screen)
            self.drawShootingScore(screen)
            if self.showOutcome == True:
                self.drawOutcome(screen)
 

    def loadImages(self):
        self.background = pygame.image.load("stadium.jpg")
        self.startButton = pygame.image.load("playbutton.png")
        self.helpButton = pygame.image.load("helpbutton.png")
        self.helpPage = pygame.image.load("help.png")
        self.continueGame = pygame.image.load("continue.png")
        self.playersChooseBack = pygame.image.load("stadium3copy.jpg")
        self.bottomPlayers = pygame.image.load("playerschoose.png")
        self.startGame = pygame.image.load("startgame.png")
        self.field = pygame.image.load("longfield.png")
        self.shootingField = pygame.image.load("shootingField.png")
        self.goal = pygame.image.load("goal.png")
        self.startGoalkeeper = pygame.image.load("startgoalkeeper.png")
        self.goalkeeperLeft = pygame.image.load("goalkeeperLeft.png")
        self.goalkeeperRight = pygame.image.load("goalkeeperRight.png")
        image = pygame.image.load("ball.png")
        self.shootingBall = pygame.transform.smoothscale(image, (33,33))
        self.teamTwoButton = pygame.image.load("team2.png")
        self.barcabanner = pygame.image.load("barcabanner.png")
        self.player1 = pygame.image.load("player1.png")
        self.player2 = pygame.image.load("player2.png")

    def loadShootingGoalieImages(self):
        self.startGoalie = dict()
        self.flyingGoalie = dict()
        self.downGoalie = dict()
        for goalie in startShootingGoalie:
            image = pygame.image.load(startShootingGoalie[goalie])
            self.startGoalie[goalie] = image
        for goalie in flyingShootingGoalie:
            image = pygame.image.load(flyingShootingGoalie[goalie])
            self.flyingGoalie[goalie] = image
        for goalie in downShootingGoalie:
            image = pygame.image.load(downShootingGoalie[goalie])
            self.downGoalie[goalie] = image

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

    def loadFieldPlayers2(self):
        self.fieldGoalImages2 = dict()
        self.fieldAttImages2= dict()
        self.fieldMidImages2= dict()
        self.fieldDefImages2 = dict()
        image = pygame.transform.smoothscale(self.playersChooseBack, (700,500))
        for goalie in fieldGoalie2:
            image = pygame.image.load(fieldGoalie2[goalie])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldGoalImages2[goalie] = transformImage
        for midfielder in fieldMidfielders2:
            image = pygame.image.load(fieldMidfielders2[midfielder])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldMidImages2[midfielder] = transformImage
        for defender in fieldDefense2:
            image = pygame.image.load(fieldDefense2[defender])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldDefImages2[defender] = transformImage
        for attacker in fieldAttack2:
            image = pygame.image.load(fieldAttack2[attacker])
            transformImage = pygame.transform.smoothscale(image, (18,63))
            self.fieldAttImages2[attacker] = transformImage

    def setDict1(self):
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

    def setDict2(self):
        self.goalButtons2 = dict()
        self.attackButtons2 = dict()
        self.midfieldButtons2 = dict()
        self.defendersButtons2 = dict()
        self.goalCards2 = dict()
        self.attackCards2 = dict()
        self.midfieldCards2 = dict()
        self.defenderCards2 = dict()
        self.formationGoalies2 = []
        self.formationAttack2 = []
        self.formationMidfield2 = []
        self.formationDefender2 = []
        self.loadGoalCard2 = dict()
        self.loadDefCard2 = dict()
        self.loadMidCard2 = dict()
        self.loadAttCard2 = dict()
        self.goalRects2 = []
        self.attackRects2 = []
        self.midRects2 = []
        self.defenseRects2 = []

    def loadBall(self):
        image =  pygame.image.load("ball.png")
        self.ballImage = pygame.transform.smoothscale(image, (15,15))

    def initShootingMode(self):
        self.shootingMode = False
        self.shootingPosition = None
        self.goalRect = None
        self.shootingModeGoalie = None
        self.shootBall = None
        self.moveLeft = False
        self.moveRight = False
        self.moveDown = False
        self.clicked = False
        self.ballMovements = []
        self.kicked = False
        self.outcome = None
        self.path = []
        self.showOutcome = False
        self.movedGoalie = False
        
    def initPassingMode(self):
        self.passingBall = False
        self.passingPlayer = None  
        self.direction = None
        self.justPassed = False
    
    def initStats(self):
        self.teamOneShots = 0
        self.teamTwoShots = 0
        self.teamOneScore = 0
        self.teamTwoScore = 0
        self.teamOneShotsOnTar = 0
        self.teamTwoShotsOnTar = 0
        self.teamOneGoalsSaved = 0
        self.teamTwoGoalsSaved = 0
        self.teamOnePassing = 0
        self.teamTwoPassing = 0
        self.teamOnePos = 0
        self.teamTwoPos = 0
        self.half = 100


    def __init__(self, width=700, height=500, fps=30, title="World Class Football"):
        # self.loadImages()
        # self.loadFieldPlayers()
        # self.loadFieldPlayers2()
        # self.loadBall()
        # self.loadShootingGoalieImages()
        # self.initStats()
        # self.start = False
        # self.team1 = False
        # self.team2 = False
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        self.start = False
        # self.players = []
        # self.step = 0
        # self.ball = None
        # self.curPlayer = None
        # self.curPlayer2 = None 
        # self.initPassingMode()
        # self.initShootingMode()
        # self.teamOneGoalie = None
        # self.teamTwoGoalie = None
        # self.pressedStart = False
        # self.halfTime = False
        # self.fullTime = False
        # self.secondHalf = False
        # self.timer = 0


    def run(self):
        clock = pygame.time.Clock()
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
                elif (event.type == pygame.MOUSEMOTION): 
                    # and event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #     event.buttons[0] == 1):
                #     self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    # self.keys = pygame.key.get_pressed()
                    self.keyPressed(event.key, event.mod)
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


#instructions
#possibilty 2 computers
#direction players are faced
#bug w/ goalie
#time limit
#indicate current player 
#esc to go back to home page  
#change backgrounds
#load/save 
#players move/aim at opposite players 