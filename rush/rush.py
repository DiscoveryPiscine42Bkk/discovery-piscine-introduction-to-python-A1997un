from logic import checkmate

def main():
    #`""" = input multiple lines \ end
    board = """\
    R...
    .K..
    ..P.
    ....\
    """
    checkmate(board)
if __name__ == "__main__":
    main()