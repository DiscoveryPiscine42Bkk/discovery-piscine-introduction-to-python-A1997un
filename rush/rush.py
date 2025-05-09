#!/usr/bin/python3

import checkmate

def main():

    
    boardMap = [
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]
    ]

   
    boardMap[6][6] = "K"
    # boardMap[6][4] = "Q"
    # boardMap[3][0] = "R"  
    # boardMap[0][7] = "B"  
    boardMap[4][3] = "P"  

    posKing = None
    queens = []
    rooks = []
    bishops = []
    pawns = []

   
    for i in range(8):
        for j in range(8):
            piece = boardMap[i][j]
            if piece == "K":
                posKing = (i, j)           
            elif piece == "Q":
                queens.append((i, j))      
            elif piece == "R":
                rooks.append((i, j))        
            elif piece == "B":
                bishops.append((i, j))
            elif piece == "P":
                pawns.append((i, j))

  
    print()                                 
    print("  a b c d e f g h")             
    for i in range(7, -1, -1):              
        print(i + 1, end=" ")               
        for j in range(8):                 
            print(boardMap[i][j], end=" ")  
        print()                             
    print("  a b c d e f g h\n")            

    if not posKing:
        print("No King Found")              
    else:  
        result = checkmate.checkmate(posKing, queens, rooks, bishops, pawns) 
                                           
        print(result)                      
        print()

if __name__ == "__main__":               

    main()                               