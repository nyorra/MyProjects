def main():
    introduction = intro()
    board = create_grid()
    pretty = printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)


def intro():
    print("Привет! Добро пожаловать в игру Крестики-нолики!")
    print("\n")
    print("Правила: Игрок 1 и игрок 2, представленные символами X и O, по очереди ставят свои marks на поле 3*3.\n" 
          "Выигрывает тот, кто первым выстроит три своих символа в ряд по горизонтали, вертикали или диагонали.\n")
    print("\n")
    input("Нажмите Enter для продолжения.")
    print("\n")


def create_grid():
    print("Вот игровое поле: ")
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    return board


def sym():
    symbol_1 = input("Игрок 1, выберите X или O: ")
    if symbol_1 == "X":
        symbol_2 = "O"
        print("Игрок 2, вы играете O. ")
    else:
        symbol_2 = "X"
        print("Игрок 2, вы играете X. ")
    input("Нажмите Enter для продолжения.")
    print("\n")
    return (symbol_1, symbol_2)


def startGamming(board, symbol_1, symbol_2, count):
    if count % 2 == 0:
        player = symbol_1
    elif count % 2 == 1:
        player = symbol_2
    print("Игрок " + player + ", ваш ход. ")
    row = int(input("Выберите строку:"
                    "[верхняя строка: введите 0, средняя: 1, нижняя: 2]: "))
    column = int(input("Выберите колонку:"
                       "[левая колонка: 0, средняя: 1, правая: 2]: "))

    while (row > 2 or row < 0) or (column > 2 or column < 0):
        outOfBoard(row, column)
        row = int(input("Выберите строку:"
                        "[0, 1, 2]: "))
        column = int(input("Выберите колонку:"
                           "[0, 1, 2]: "))

    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        filled = illegal(board, symbol_1, symbol_2, row, column)
        row = int(input("Выберите строку:"
                        "[0, 1, 2]: "))
        column = int(input("Выберите колонку:"
                           "[0, 1, 2]: "))

    if player == symbol_1:
        board[row][column] = symbol_1
    else:
        board[row][column] = symbol_2

    return (board)


def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True
    while count < 10 and winner == True:
        gaming = startGamming(board, symbol_1, symbol_2, count)
        pretty = printPretty(board)

        if count == 9:
            print("Игровое поле заполнено. Игра окончена.")
            if winner == True:
                print("Ничья.")

        winner = isWinner(board, symbol_1, symbol_2, count)
        count += 1
    if winner == False:
        print("Игра окончена.")
    report(count, winner, symbol_1, symbol_2)


def outOfBoard(row, column):
    print("Вы выбрали ячейку за пределами поля. Выберите другую.")


def printPretty(board):
    rows = len(board)
    cols = len(board)
    print("---+---+---")
    for r in range(rows):
        print(board[r][0], " |", board[r][1], "|", board[r][2])
        print("---+---+---")
    return board


def isWinner(board, symbol_1, symbol_2, count):
    winner = True
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Игрок " + symbol_1 + " победил!")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Игрок " + symbol_2 + " победил!")

    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Игрок " + symbol_1 + " победил!")
        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Игрок " + symbol_2 + " победил!")

    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False
        print("Игрок " + symbol_1 + " победил!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Игрок " + symbol_2 + " победил!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Игрок " + symbol_1 + " победил!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Игрок " + symbol_2 + " победил!")

    return winner


def illegal(board, symbol_1, symbol_2, row, column):
    print("Эта ячейка уже занята. Выберите другую.")


def report(count, winner, symbol_1, symbol_2):
    print("\n")
    input("Нажмите Enter чтобы увидеть итог игры. ")
    if (winner == False) and (count % 2 == 1):
        print("Победитель: Игрок " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0):
        print("Победитель: Игрок " + symbol_2 + ".")
    else:
        print("Ничья.")


main()