class ChessEngine():
    def __init__(self):
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
                elif chess_value == 9 or chess_value == 17: #Advisor
                    for delta in board.AdvisorDelta:
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1                    
                elif chess_value == 8 or chess_value == 16: #King
                    for delta in board.KingDelta:
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1                     
                elif chess_value == 19 or chess_value == 11: #Knight
                    for delta in board.KnightDeltaPin.keys():
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1                            
                elif chess_value == 20 or chess_value == 12: #Rook
                    for delta in board.KingDelta:
                        dest = src+delta
                        while(board.inBoard[dest]==1):
                            if boardPhase.isLegalMove(chess_value,board,src,dest):
                                movs.append(self.__MOV(src,dest))
                                moveCount = moveCount + 1
                            dest = dest + delta
                elif chess_value == 21 or chess_value == 13: #Cannon
                        dest = src+delta
                        while(board.inBoard[dest]==1):
                            if boardPhase.isLegalMove(chess_value,board,src,dest):
                                movs.append(self.__MOV(src,dest))
                                moveCount = moveCount + 1
                            dest = dest + delta                    
                elif chess_value == 22 or chess_value == 14: #Pawn
                    for delta in board.KingDelta:
                        dest = src+delta
                        if boardPhase.isLegalMove(chess_value,board,src,dest):
                            movs.append(self.__MOV(src,dest))
                            moveCount = moveCount + 1                              
        return moveCount
    
    
    
    
    
    
    
    
    
    
    