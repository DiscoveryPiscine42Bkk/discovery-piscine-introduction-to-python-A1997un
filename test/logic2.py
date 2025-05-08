#!/usr/bin/python3

# ROOK 

# Bishop("H8")=     H     8
#               B  [0]  [1]

# King("F6")=       F     6
#               K  [0]   [1]

#             B[0]-K[0]   B[1]-K[1]

#                   3  ==  3           it means Bishop EATS King


# H=8

# [0,1,2,3,4,5,6,7]


# ROOK + BISHOP = QUEEN

# def bishop_check(bishop_x,bishop_y,king_x,king_y):
#         calc_x=abs(bishop_x-king_x)
#         calc_y=abs(bishop_y-king_y)
#         if calc_x == calc_y:
#             print("Success")
#         else:
#             print("Fail")
# def checkmate(board,piece_play):
    
#     for y in range(len(board)):
#         for x in range(len(board[y])):
#             if board[y][x] == 'K':
#                 king_x = x
#                 king_y = y
#                  return

                
#     print("Fail")

def p_check(x, y, king_x, king_y):
    # โจมตีเฉียงซ้ายหรือขวาขึ้นด้านบน (ตามบอร์ดจากล่างขึ้นบน)
    return (x - 1 == king_x and y - 1 == king_y) or (x + 1 == king_x and y - 1 == king_y)

def check_direction(board, x, y, dx, dy, king_x, king_y):
    while True:
        x += dx
        y += dy
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[y]):
            return False
        if board[y][x] == 'K':
            return True
        if board[y][x] != '.':
            return False

def checkmate(board):
    # หา King
    king_x = king_y = -1
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'K':
                king_x = x
                king_y = y
                break

    # วนหาทุกหมาก
    for y in range(len(board)):
        for x in range(len(board[y])):
            piece = board[y][x]

            if piece == 'P':
                if p_check(x, y, king_x, king_y):
                    print("Success")
                    return

            elif piece == 'B':
                for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    if check_direction(board, x, y, dx, dy, king_x, king_y):
                        print("Success")
                        return

            elif piece == 'R':
                for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if check_direction(board, x, y, dx, dy, king_x, king_y):
                        print("Success")
                        return

            elif piece == 'Q':
                for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1),
                               (0, -1), (0, 1), (-1, 0), (1, 0)]:
                    if check_direction(board, x, y, dx, dy, king_x, king_y):
                        print("Success")
                        return

    print("Fail")