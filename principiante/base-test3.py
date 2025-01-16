class ChessBoard():
    SIZE = 8
    def __init__(self):
        self.matrix = [[(x, y) for y in range(ChessBoard.SIZE)] for x in range(ChessBoard.SIZE)]

    def print(self, queen, destination):
        # chessboard = [[(x, y) for y in range(ChessBoard.SIZE)] for x in range(ChessBoard.SIZE)]
        possible_moves = queen.get_possible_moves()
        for x in range(ChessBoard.SIZE):
            for y in range(ChessBoard.SIZE):
                if (x, y) == (queen.x, queen.y):
                    self.matrix[x][y] = '👑'
                elif (x, y) == destination:
                    self.matrix[x][y] = '🟦'
                elif (x, y) in possible_moves:
                    self.matrix[x][y] = '⬜️'
                else:
                    self.matrix[x][y] = '  '
        if destination not in possible_moves:
            x, y = destination
            self.matrix[x][y] = '🟥'
        
        columns_label = "  ".join([str(count+1) for count in range(ChessBoard.SIZE)])
        columns_label = '  {} '.format(columns_label)
        print()
        print(columns_label)
        for i, row in enumerate(self.matrix):
            rows_label = "{} {} {}".format(i+1, '|'.join(row), i+1)
            print(rows_label)
        print(columns_label)
        print()

    @classmethod
    def areCoordinatesOk(cls, coordinates):
        x, y = coordinates
        if x < 1 or x > cls.SIZE:
            return False
        if y < 1 or y > cls.SIZE:
            return False
        return True


class Queen():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_possible_moves(self):
        moves = set()
        horizontal = [(x, self.y) for x in range(ChessBoard.SIZE)]
        vertical = [(self.x, y) for y in range(ChessBoard.SIZE)]
        diagonal= [(x, y) for x in range(ChessBoard.SIZE) for y in range(ChessBoard.SIZE) if ChessBoard.areCoordinatesOk((x+1, y+1)) and y-x==self.y-self.x]
        diagonals = {(x, y) for x in range(ChessBoard.SIZE) for y in range(ChessBoard.SIZE) if ChessBoard.areCoordinatesOk((x+1, y+1)) and x+y==self.x+self.y}
        diagonals.update(diagonal)
        moves.update(horizontal)
        moves.update(vertical)
        moves.update(diagonals)
        return moves

    def can_move(self, to_coordinates):
        if to_coordinates == (self.x, self.y):
            print("\n[!] You are here already!")
        elif to_coordinates in self.get_possible_moves():
            print("\nYES")
        else:
            print("\nNO")


def try_int(num):
    try:
        return int(num)
    except:
        print('Enter a valid digit!')
        exit()


chessboard = ChessBoard()

initial_x = try_int(input("[*] Queen's X coordinate (1-8)? "))
initial_y = try_int(input("[*] Queen's Y coordinate (1-8)? "))
if not chessboard.areCoordinatesOk((initial_x, initial_y)):
    print("X or Y coordinates out of bound! Type a value between 1-{}".format(ChessBoard.SIZE))
    exit()

queen = Queen(initial_x-1, initial_y-1)

final_x = try_int(input("[*] Queen's X destination coordinate (1-8)? "))
final_y = try_int(input("[*] Queen's Y destination coordinate (1-8)? "))

if not chessboard.areCoordinatesOk((final_x, final_y)):
    print("X or Y coordinates out of bound! Type a value between 1-{}".format(ChessBoard.SIZE))
    exit()

destination = (final_x-1, final_y-1)
chessboard.print(queen, destination)
queen.can_move(destination)