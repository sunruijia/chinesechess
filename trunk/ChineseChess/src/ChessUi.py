import sys, os, pygame
from pygame.locals import * 
from pygame.sprite import Sprite



class Board():
    def __init__(self):
        self.TOP = 3
        self.BUTTOM = 12
        self.LEFT = 3
        self.RIGHT = 11
        self.chessList = [];
        self.board_status = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0, 20, 19, 18, 17, 16, 17, 18, 19, 20,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0, 21,  0,  0,  0,  0,  0, 21,  0,  0,  0,  0,  0,
                             0,  0,  0, 22,  0, 22,  0, 22,  0, 22,  0, 22,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0, 14,  0, 14,  0, 14,  0, 14,  0, 14,  0,  0,  0,  0,
                             0,  0,  0,  0, 13,  0,  0,  0,  0,  0, 13,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0, 12, 11, 10,  9,  8,  9, 10, 11, 12,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0] 
        self.__creatChessObjs()   
    def __creatChessObjs(self):       
        for i in range(8):
            self.chessList.append(0)   
        for i in range(8,15):
            chessObj = Chess(i)
            self.chessList.append(chessObj) 
        self.chessList.append(0)         
        for i in range(16,23):
            chessObj = Chess(i)
            self.chessList.append(chessObj) 
    def getChessItem(self,chessValue):
        if(chessValue > 0)and (chessValue < 23) and (chessValue != 15):
            return self.chessList[chessValue]
        else:
            return None 
    def boardClick(self,position,boardWindow):
        xx = position[0]
        yy = position[1]
        x = (xx-boardWindow.EDGE)/boardWindow.SQUARE +3
        y = (yy-boardWindow.EDGE)/boardWindow.SQUARE +3
        chess_value = board.board_status[x+y*16]
        if chess_value != 0:
            print"click chess ",chess_value
            chessObj = self.getChessItem(chess_value)
            chessObj.setSelect() 
            
        
class BoardWindow():
    def __init__(self):
        self.EDGE = 8
        self.SQUARE = 56
        self.WITH = 520
        self.HEIGHT = 576
        self.window = pygame.display.set_mode((self.WITH, self.HEIGHT))
        pygame.display.set_caption('Chinese Chess') 
        self.boardImage = pygame.image.load(os.path.join("RES", "BOARD.BMP")).convert()
        self.screen = pygame.display.get_surface()   
    def __drawBoardBackgound(self):
        self.screen.blit(self.boardImage, (0, 0))   
    def __drawChess(self,chess):
        self.screen.blit(chess.Image, (0,0)) 
    def __getWindowX(self,x):
        return (x-3)*self.SQUARE +self.EDGE
    def __getWindowY(self,y):
        return (y-3)*self.SQUARE +self.EDGE   
    def drawBoard(self,board):
        self.__drawBoardBackgound()
        for x in range(board.LEFT, board.RIGHT+1):
            for y in range(board.TOP,board.BUTTOM+1):
                chess_value = board.board_status[x+y*16]
                if(chess_value != 0):
                    chess = board.getChessItem(chess_value)
                    self.screen.blit(chess.Image,(self.__getWindowX(x),self.__getWindowY(y)))          
                    if(chess.getSelect()):
                        return 
        pygame.display.flip()
                    

        
              
class Chess(Sprite):
    chessImage = {8:os.path.join("RES", "RK.BMP"),9:os.path.join("RES", "RA.BMP"),
                  10:os.path.join("RES", "RB.BMP"),11:os.path.join("RES", "RN.BMP"),
                  12:os.path.join("RES", "RR.BMP"),13:os.path.join("RES", "RC.BMP"),
                  14:os.path.join("RES", "RP.BMP"),16:os.path.join("RES", "BK.BMP"),
                  17:os.path.join("RES", "BA.BMP"),18:os.path.join("RES", "BB.BMP"),
                  19:os.path.join("RES", "BN.BMP"),20:os.path.join("RES", "BR.BMP"),
                  21:os.path.join("RES", "BC.BMP"),22:os.path.join("RES", "BP.BMP"),}
    def __init__(self,chess_value):
        Sprite.__init__(self)
        self.chess_value = chess_value
        self.Image = self.__createChessImage()
        self.COLOR_KEY = (0,255,0)
        self.Image.set_colorkey(self.COLOR_KEY)
        self.isSelect = False
    def __createChessImage(self):
        return pygame.image.load(self.chessImage[self.chess_value]).convert()
    def setSelect(self):
        self.isSelect = True
    def getSelect(self):
        return self.isSelect
                  
def input(events,board,boardWindow): 
    for event in events: 
        if event.type == QUIT: 
            sys.exit(0) 
        elif event.type == MOUSEBUTTONDOWN:
            board.boardClick(pygame.mouse.get_pos(),boardWindow)
            return
        else: 
            pass
         

pygame.init() 
boardWindow = BoardWindow()
board = Board()
boardWindow.drawBoard(board)

while True: 
    input(pygame.event.get(),board,boardWindow)
    pygame.display.flip()
   
   
