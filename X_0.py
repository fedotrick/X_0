# Функция create_board создает игровое поле размером 3х3.
# Используется генератор списков, чтобы заполнить поле пустыми клетками.
# Внешний список содержит три внутренних списка, представляющих три строки игрового поля.
# Внутренний список содержит три пустых символа, обозначающих свободные клетки в строке.

def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

''' Функция display_board выводит текущее состояние игрового поля на экран.
Принмает в качестве аргумента двумерный список board, представляющий игровое поле.
В цикле проходится по каждой строке игрового поля.
Для каждой строки вызывается метод join, который объединяет элементы строки символом '|',
чтобы разделить клетки игрового поля.
После каждой строки выводится горизонтальная черта '-' для разделения строк.'''

def display_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)
        
'''
Функция make_move позволяет сделать ход в игре.
Принимает в качестве аргументов:
- board: игровое поле (двумерный массив),
- col: номер столбца, куда нужно поставить символ, 
- symbol: символ, который нужно поставить ('X' или '0').
Проверяет, что указанная клетка пуста (содержит символ ' ').
и функция возвращает True, обозгачая успешный ход.
Если клетка занята, то функция возвращает False.
'''

def make_move(board, row, col, symbol):
    if board[row][col] == ' ':
        board[row][col] = symbol
        return True
    else:
        return False
                
'''
Функция check_winner проверяет, есть ли победитель в текущей позиции на игровом поле.
Принимает в качестве аргументов:
- board: игровое поле (двумерный массив),
- symbol: символ, за который играет игрок ('X' или '0').
Проверяет выигрышные комбинации:
1. Победа по горизонтали: если в одной из строк все элементы равны символу.
2. Победа по вертикали: если в одной из столбцов все элементы равны символу.
3. Победа по диагонали: если все элементы на главной или побочной диагоналях равны символу.
Если одна из выигрышных комбинаций найдена, функция возращает True, иначе - False.
'''

def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 -i] == symbol for i in range(3)):
        return True
    return False


'''
Основной игровой цикл
'''

def main():
    # Создание пустого игрового поля
    board = create_board()
    # Начальный игрок
    current_player = 'X'
    # Основной игровой цикл
    while True:
        # Вывод игрового поля на экран
        display_board(board)
        # Получение строки и столбца от текущего игрока
        row = int(input(f'Player {current_player}, enter row (0-2): '))
        col = int(input(f'Player {current_player}, enter column (0-2): '))
        # Попытка сделать ход на игровом поле
        if make_move(board, row, col, current_player):
            # Проверка на победу текущего игрока
            if check_winner(board, current_player):
                display_board(board)
                print(f'Player {current_player} wins!')
                break
            # Проверка на ничью
            if ' ' not in [cell for row in board for cell in row]:
                display_board(board)
                print('It\'s a draw!')
                break
            # Смена игрока после успешного хода 
            current_player = '0' if current_player == 'X' else 'X'
        else: 
            # Если выбранная клетка уже занята
            print('This cell is already occupied. Try again.')
            
if __name__ == '__main__':
    main()
                                                

                
                