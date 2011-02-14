import time
class ChessEngine():
    def __init__(self):
        self.vRed = 0
        self.vBlack = 0
        self.PawnValue = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  9,  9,  9, 11, 13, 11,  9,  9,  9,  0,  0,  0,  0,
                          0,  0,  0, 19, 24, 34, 42, 44, 42, 34, 24, 19,  0,  0,  0,  0,
                          0,  0,  0, 19, 24, 32, 37, 37, 37, 32, 24, 19,  0,  0,  0,  0,
                          0,  0,  0, 19, 23, 27, 29, 30, 29, 27, 23, 19,  0,  0,  0,  0,
                          0,  0,  0, 14, 18, 20, 27, 29, 27, 20, 18, 14,  0,  0,  0,  0,
                          0,  0,  0,  7,  0, 13,  0, 16,  0, 13,  0,  7,  0,  0,  0,  0,
                          0,  0,  0,  7,  0,  7,  0, 15,  0,  7,  0,  7,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        self.KingValue = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  2,  2,  2,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0, 11, 15, 11,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        self.AdvisorValue = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0, 20,  0, 20,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0, 23,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0, 20,  0, 20,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        self.BishopValue = [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0, 20,  0,  0,  0, 20,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0, 18,  0,  0,  0, 23,  0,  0,  0, 18,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0, 20,  0,  0,  0, 20,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                             0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        self.KnightValue = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0, 90, 90, 90, 96, 90, 96, 90, 90, 90,  0,  0,  0,  0,
                          0,  0,  0, 90, 96,103, 97, 94, 97,103, 96, 90,  0,  0,  0,  0,
                          0,  0,  0, 92, 98, 99,103, 99,103, 99, 98, 92,  0,  0,  0,  0,
                          0,  0,  0, 93,108,100,107,100,107,100,108, 93,  0,  0,  0,  0,
                          0,  0,  0, 90,100, 99,103,104,103, 99,100, 90,  0,  0,  0,  0,
                          0,  0,  0, 90, 98,101,102,103,102,101, 98, 90,  0,  0,  0,  0,
                          0,  0,  0, 92, 94, 98, 95, 98, 95, 98, 94, 92,  0,  0,  0,  0,
                          0,  0,  0, 93, 92, 94, 95, 92, 95, 94, 92, 93,  0,  0,  0,  0,
                          0,  0,  0, 85, 90, 92, 93, 78, 93, 92, 90, 85,  0,  0,  0,  0,
                          0,  0,  0, 88, 85, 90, 88, 90, 88, 90, 85, 88,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        self.RookValue = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,206,208,207,213,214,213,207,208,206,  0,  0,  0,  0,
                          0,  0,  0,206,212,209,216,233,216,209,212,206,  0,  0,  0,  0,
                          0,  0,  0,206,208,207,214,216,214,207,208,206,  0,  0,  0,  0,
                          0,  0,  0,206,213,213,216,216,216,213,213,206,  0,  0,  0,  0,
                          0,  0,  0,208,211,211,214,215,214,211,211,208,  0,  0,  0,  0,
                          0,  0,  0,208,212,212,214,215,214,212,212,208,  0,  0,  0,  0,
                          0,  0,  0,204,209,204,212,214,212,204,209,204,  0,  0,  0,  0,
                          0,  0,  0,198,208,204,212,212,212,204,208,198,  0,  0,  0,  0,
                          0,  0,  0,200,208,206,212,200,212,206,208,200,  0,  0,  0,  0,
                          0,  0,  0,194,206,204,212,200,212,204,206,194,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                          0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        self.CannonValue = [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                            0,  0,  0,100,100, 96, 91, 90, 91, 96,100,100,  0,  0,  0,  0,
                            0,  0,  0, 98, 98, 96, 92, 89, 92, 96, 98, 98,  0,  0,  0,  0,
                            0,  0,  0, 97, 97, 96, 91, 92, 91, 96, 97, 97,  0,  0,  0,  0,
                            0,  0,  0, 96, 99, 99, 98,100, 98, 99, 99, 96,  0,  0,  0,  0,
                            0,  0,  0, 96, 96, 96, 96,100, 96, 96, 96, 96,  0,  0,  0,  0,
                            0,  0,  0, 95, 96, 99, 96,100, 96, 99, 96, 95,  0,  0,  0,  0,
                            0,  0,  0, 96, 96, 96, 96, 96, 96, 96, 96, 96,  0,  0,  0,  0,
                            0,  0,  0, 97, 96,100, 99,101, 99,100, 96, 97,  0,  0,  0,  0,
                            0,  0,  0, 96, 97, 98, 98, 98, 98, 98, 97, 96,  0,  0,  0,  0,
                            0,  0,  0, 96, 96, 97, 99, 99, 99, 97, 96, 96,  0,  0,  0,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
                            0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
        self.ChessValueTable = {0:self.KingValue,1:self.AdvisorValue,2:self.BishopValue,3:self.KnightValue,
                                4:self.RookValue,5:self.CannonValue,6:self.PawnValue}
        self.HistoryTable=[0]*65536
        self.distance = 0
        self.computerMove = 0
        self.MATE_VALUE = 10000
        self.DEPTH_LIMIT = 32
        self.TIME_LIMIT = 2
        self.WIN_VALUE =  self.MATE_VALUE - 100
        return
    def __MOV(self,src,dest):
        return src+dest*256
    def GenerateMoves(self,boardPhase,board,movs):
        moveCount = 0
        for src in range(256):
            chess_value = boardPhase.board_status[src]
            if(boardPhase.isSelfchess(chess_value)):
                if chess_value == 18 or chess_value == 10: #Bishop
                    for delta in board.BiShopDelta:
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1
                            #print "Bishop %d move: src %d, dest %d" %(chess_value,src,dest)
                elif chess_value == 9 or chess_value == 17: #Advisor
                    for delta in board.AdvisorDelta:
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1
                            #print "Advisor %d move: src %d, dest %d" %(chess_value,src,dest)                    
                elif chess_value == 8 or chess_value == 16: #King
                    for delta in board.KingDelta:
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1  
                            #print "King %d move: src %d, dest %d" %(chess_value,src,dest)                 
                elif chess_value == 19 or chess_value == 11: #Knight
                    for delta in board.KnightDeltaPin.keys():
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1
                            #print "Knight %d move: src %d, dest %d" %(chess_value,src,dest)                               
                elif chess_value == 20 or chess_value == 12: #Rook
                    for delta in board.KingDelta:
                        dest = src+delta
                        while(board.inBoard[dest]==1):
                            if boardPhase.isLegalMove(chess_value,board,src,dest):
                                movs.append(self.__MOV(src,dest))
                                moveCount = moveCount + 1
                                #print "Rook %d move: src %d, dest %d" %(chess_value,src,dest)   
                            dest = dest + delta
                elif chess_value == 21 or chess_value == 13: #Cannon
                    for delta in board.KingDelta:
                        dest = src+delta
                        while(board.inBoard[dest]==1):
                            if boardPhase.isLegalMove(chess_value,board,src,dest):
                                movs.append(self.__MOV(src,dest))
                                moveCount = moveCount + 1
                                #print "Cannon %d move: src %d, dest %d" %(chess_value,src,dest)   
                            dest = dest + delta                    
                elif chess_value == 22 or chess_value == 14: #Pawn
                    for delta in board.KingDelta:
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1 
                            #print "Pawn %d move: src %d, dest %d" %(chess_value,src,dest)                           
        return moveCount
    def __mirrorSquare(self,index):
        return 254 - index
    def __addPiece(self,index,boardPhase,chess_value):
        boardPhase.board_status[index] =  chess_value
        if chess_value < 16:
            self.vRed = self.vRed + self.ChessValueTable[chess_value - 8][index]
        else:
            self.vBlack = self.vBlack + self.ChessValueTable[chess_value - 16][self.__mirrorSquare(index)]
    def __delPiece(self,index,boardPhase,chess_value):
        boardPhase.board_status[index] =  0
        if chess_value < 16:
            self.vRed = self.vRed - self.ChessValueTable[chess_value - 8][index]
        else:
            self.vBlack = self.vBlack - self.ChessValueTable[chess_value - 16][self.__mirrorSquare(index)]   
                 
    def move_piece(self,boardPhase,move):
        src = move%256
        dest = move/256
        dest_chess_value = boardPhase.board_status[dest]
        if dest_chess_value != 0:
            self.__delPiece(dest, boardPhase, boardPhase.board_status[dest])
        self.__addPiece(dest,boardPhase,boardPhase.board_status[src]) #move the piece to new place
        self.__delPiece(src, boardPhase, boardPhase.board_status[src]) # delete the piece in the original place
        return dest_chess_value     #return the dest piece for undo move. even it has no piece in dest, it will still return 0
    
    def undo_move_piece(self,boardPhase,move,dest_chess_value):
        src = move%256
        dest = move/256
        self.__delPiece(dest, boardPhase, boardPhase.board_status[dest])
        self.__addPiece(src,boardPhase,boardPhase.board_status[dest])
        if dest_chess_value != 0:
            self.__addPiece(dest, boardPhase, dest_chess_value)
            
    def makeMove(self,boardPhase,board,move):
        dest_chess_value = self.move_piece(boardPhase, move)
        if boardPhase.isChecked(board):
            self.undo_move_piece(boardPhase, move, dest_chess_value)
            return (False,0)
        boardPhase.changeSide()
        self.distance =  self.distance + 1
        return (True,dest_chess_value)
        
    def undoMakeMove(self,boardPhase,move,dest_chess_value):
        self.undo_move_piece(boardPhase, move,dest_chess_value)
        self.distance =  self.distance - 1
        boardPhase.changeSide()
                           
    def __alpha_beta_search(self,depth,boardPhase,board,alpha,beta):
        best_move = 0
        best_value = alpha
        isMated =  True
        if(depth <= 0):
            return self.__evaluate(boardPhase)
        movs = []
        movecount = self.GenerateMoves(boardPhase,board,movs)
        if movecount != 0:
            movs.sort(cmp=lambda x,y:cmp(self.HistoryTable[x],self.HistoryTable[y]),reverse=True)
            for move in movs:
                result = self.makeMove(boardPhase,board,move)[0]
                if(result[0] == False):
                    self.undo_move_piece(boardPhase,move,result[1])
                else:
                    isMated = False
                    val = -self.__alpha_beta_search(depth - 1,boardPhase,board,-beta,-alpha)
                    self.undo_move_piece(boardPhase, move, result[1])
                    if val > beta:
                        best_value = val
                        best_move = move
                        break
                    if val >alpha:
                        alpha = val
                        best_value = val
                        best_move = move
            if isMated == True:
                return self.distance - self.MATE_VALUE
            if best_move != 0:
                self.HistoryTable[best_move] += depth * depth;
                if self.distance == 0:
                    self.computerMove = best_move
            return best_value
    def __evaluate(self,boardPhase):
        if boardPhase.getSide == 0:           
            return self.vRed - self.vBlack + 3
        else:
            return self.vBlack - self.vRed + 3
    def mainSearch(self,boardPhase,board):
        start_time = time.time()
        for i in range(self.DEPTH_LIMIT):
            value = self.__alpha_beta_search(i+1,boardPhase,board,-self.MATE_VALUE, self.MATE_VALUE)
            if value > self.WIN_VALUE or value < -self.WIN_VALUE:
                break
            if time.time() - start_time > self.TIME_LIMIT :
                break
               
    
    
    
    
    
    
    
    
    
    
    