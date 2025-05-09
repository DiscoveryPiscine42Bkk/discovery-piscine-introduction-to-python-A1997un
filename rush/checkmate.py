def distance(i, j):
    return (i, j)

def rook_eats_king(king, rook):
    return king[0] == rook[0] or king[1] == rook[1]

def bishop_eats_king(king, bishop):
    return abs(king[0] - bishop[0]) == abs(king[1] - bishop[1])

def pawn_eats_king(king, pawn):
    return (king[0] - pawn[0] == 1) and abs(king[1] - pawn[1]) == 1

def queen_eats_king(king, queen):
    return rook_eats_king(king, queen) or bishop_eats_king(king, queen)

def checkmate(posKing, queens, rooks, bishops, pawns):
    for q in queens:
        if queen_eats_king(posKing, q):
            return "Queen Eats King: Success"
    for r in rooks:
        if rook_eats_king(posKing, r):
            return "Rook Eats King: Success"
    for b in bishops:
        if bishop_eats_king(posKing, b):
            return "Bishop Eats King: Success"
    for p in pawns:
        if pawn_eats_king(posKing, p):
            return "Pawn Eats King: Success"
    return "King Survived"