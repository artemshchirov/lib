# coding: UTF-8
# source: https://www.youtube.com/watch?v=aOLhCLhLAFM


class ChessMan:
    '''
    Вывод фигуры на поле
    '''
    IMG = None  # Хранение изображения фигуры

    def __init__(self, color):
        self.color = color

    def __str__(self):
        '''
        Dunder method __str__ регулирует применение str() или print() к объекту.
        Отвечает за то, как увидят этот объект пользователи.
        '''
        return self.IMG[0 if self.color == Color.WHITE else 1]


class Color:
    '''
    Код цвета фигуры
    '''
    WHITE = 0
    BLACK = 1
    EMPTY = 2


class Empty:
    '''
    Пустая клетка на доске.
    Возвращает свой цвет, чтобы сказать, что путь свободен
    '''
    color = Color.EMPTY

    def get_moves(self, board, x, y):
        '''
        На случай попытки использования "пустой" фигуры
        '''
        raise Exception('Error!')

    def __str__(self):
        return ' . '


class Pawn(ChessMan):
    '''
    Пешка
    '''
    IMG = ('♙ ', '♟ ')

    def get_moves(self, board, x, y):
        '''
        Принимает доску, координаты фигуры от Board().get_moves(x, y) и
        Возвращает возможные для фигуры ходы
        '''
        moves = []
        if self.color == Color.BLACK and y < 7 and board.get_color(x, y+1) == Color.EMPTY:
            moves.append([x, y+1])
        return moves


class King(ChessMan):
    '''
    Король
    '''
    IMG = ('♔ ', '♚ ')


class Board:
    '''
    Доска 8х8
    '''
    count_move = 0

    def __init__(self):

        self.board = [[Empty()] * 8 for y in range(8)]  # 2D list

        self.board[1][2] = King(Color.BLACK)
        self.board[2][3] = Pawn(Color.BLACK)
        self.board[7][2] = King(Color.WHITE)
        self.board[6][4] = Pawn(Color.WHITE)

    def get_color(self, x, y):
        '''
        Возвращает цвет (или пустоту) фигуры по координатам
        '''
        return self.board[y][x].color

    def get_moves(self, x, y):
        '''
        Принимаем координаты фигуры и запрашивает у неё куда она может ходить
        '''
        return self.board[y][x].get_moves(self, x, y)

    def move(self, xy_from, xy_to):
        '''
        Перемещение фигуры
        '''
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __str__(self):
        '''
        Графическое отображение доски
        '''
        Board.count_move += 1
        if (Board.count_move < 10):
            res = f'= = = = = 0{Board.count_move} = = = = = =\n'
        else:
            res = f'= = = = = {Board.count_move} = = = = = =\n'

        for y in range(8):
            res += ''.join(map(str, self.board[y])) + '\n'  # map() для .join для приведения всего к строке
        return res


b = Board()

def set_color(color):
    return f'\033[{color}sm'

colors = [0, 44]
res = ''
i = 0
for y in range(8):
    for x in range(8):
        res += set_color(colors[i]) + '  '
        i = 1 - i
    i = 1 - i
    res += '\n'
print(res)

exit()

b = Board()
print(b)

m = b.get_moves(3, 2)
b.move([3, 2], m[0])
print(m)
print(b)

m = b.get_moves(3, 3)
b.move([3, 3], m[0])
print(m)
print(b)
