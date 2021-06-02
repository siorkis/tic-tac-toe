import os
import random

board = [['   ', '|', '   ', '|', '   '],
         ['--', '--', '--', '--', '---'],
         ['   ', '|', '   ', '|', '   '],
         ['--', '--', '--', '--', '---'],
         ['   ', '|', '   ', '|', '   ']]

board_clear = [['   ', '|', '   ', '|', '   '],
               ['--', '--', '--', '--', '---'],
               ['   ', '|', '   ', '|', '   '],
               ['--', '--', '--', '--', '---'],
               ['   ', '|', '   ', '|', '   ']]


def print_board(array):
    for i in range(5):
        for j in range(5):
            print(array[i][j], end='')
        print()


def computer_turn(array):
    while True:
        x = random.randint(0, 4)
        y = random.randint(0, 4)

        while x % 2 != 0:
            x = random.randint(0, 4)

        while y % 2 != 0:
            y = random.randint(0, 4)

        if array[x][y] == '   ':
            array[x][y] = ' O '
            break

    print_board(board)


def player_turn_touch_pad(position):
    response = False

    if position == '7':
        if board[0][0] == '   ':
            board[0][0] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '8':
        if board[0][2] == '   ':
            board[0][2] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '9':
        if board[0][4] == '   ':
            board[0][4] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '4':
        if board[2][0] == '   ':
            board[2][0] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '5':
        if board[2][2] == '   ':
            board[2][2] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '6':
        if board[2][4] == '   ':
            board[2][4] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '1':
        if board[4][0] == '   ':
            board[4][0] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '2':
        if board[4][2] == '   ':
            board[4][2] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response

    elif position == '3':
        if board[4][4] == '   ':
            board[4][4] = ' X '
            print_board(board)
            response = True
        else:
            print('Ooops seems like this place is already taken')
            print("Try again:")
        return response
    else:
        print('Ooops that not a touchpad! Try again:')
        return response


def player_turn_index(row, column):
    row = int(row)
    column = int(column)
    if row == 1:
        row -= 1
    elif row == 3:
        row += 1

    if column == 1:
        column -= 1
    elif column == 3:
        column += 1

    if board[column][row] == '   ':
        board[column][row] = ' X '
        print_board(board)
        return True
    else:
        print('Ooops seems like this place is already taken')
        print("Try again:")


def winner(array, counter):
    y = 0

    for x in range(0, 5, 2):
        if array[x][y] == array[x][y + 2] == array[x][y + 4] == ' X ':
            print("X is winner !")
            return True
        elif array[x][y] == array[x][y + 2] == array[x][y + 4] == ' O ':
            print("O is winner !")
            return True

    x = 0

    for y in range(0, 5, 2):
        if array[x][y] == array[x + 2][y] == array[x + 4][y] == ' X ':
            print("X is winner !")
            return True
        elif array[x][y] == array[x + 2][y] == array[x + 4][y] == ' O ':
            print("O is winner !")
            return True

    x = 0
    y = 0

    if array[x][y] == array[x + 2][y + 2] == array[x + 4][y + 4] == ' X ':
        print("X is winner !")
        return True
    elif array[x][y] == array[x + 2][y + 2] == array[x + 4][y + 4] == ' O ':
        print("O is winner !")
        return True

    x = 0
    y = 0

    if array[x][y + 4] == array[x + 2][y + 2] == array[x + 4][y] == ' X ':
        print("X is winner !")
        return True
    elif array[x][y + 4] == array[x + 2][y + 2] == array[x + 4][y] == ' O ':
        print("O is winner !")
        return True

    if counter == 9:
        os.system("cls")
        print("Draw !")
        return True


def control(choice):
    if choice == '1':
        while True:
            turns = 0
            if winner(board, turns):
                print()
                print_board(board)
                break
            else:
                computer_turn(board)
                turns += 1

                if winner(board, turns):
                    os.system("cls")
                    winner(board, turns)
                    print()
                    print_board(board)
                    break
                else:
                    print('Your turn: column (1-3) row (1-3)')
                    while True:
                        myx, myy = input().split()

                        if player_turn_index(myx, myy):
                            break
                turns += 1
                os.system("cls")
        return True
    elif choice == '2':

        turns = 0

        while True:

            if winner(board, turns):
                print()
                print_board(board)
                break
            else:
                computer_turn(board)
                turns += 1

            if winner(board, turns):
                os.system('cls')
                winner(board, turns)
                print()
                print_board(board)
                break
            else:
                print()
                print("Your turn:", end='')
                while True:
                    my_position = input()
                    if player_turn_touch_pad(my_position):
                        break
                turns += 1
                os.system("cls")
        return True
    else:
        print("Ooops that not an option, try again:")


def end_game(letter):

    if letter == 'E' or letter == 'e':
        os.system('cls')
        return False
    elif letter == 'Q' or letter == 'q':
        os.system('cls')
        exit()


def error(letter):

    if letter != 'E' and letter != 'e' and letter != 'Q' and letter != 'q':
        print("Ooops that not an option, try again:")
        print("Press - E to restart")
        print("Press - Q to exit")
        return False
    else:
        return True


def control_check(choice):
	if choice != '1' and choice != '2':
		print('Ooops, that not an option, try again:')
	else:
		return True


while True:

    print_board(board)
    print()
    print("Choose controls: coordinates - 1 or touch_pad - 2 ")
    print()
    print("\t    7 8 9")
    print("touch_pad = 4 5 6")
    print("\t    1 2 3")


    while True:

        controls = input()
        os.system('cls')
        print_board(board)
        print()
        print("Choose controls: coordinates - 1 or touch_pad - 2 ")
        print()
        print("\t    7 8 9")
        print("touch_pad = 4 5 6")
        print("\t    1 2 3")

        if control_check(controls):
            os.system('cls')
            if control(controls):
                board = board_clear
                print("Press - E to restart")
                print("Press - Q to exit")
            break

    while True:

        end = input()

        if error(end):
            break

    if end_game(end):
        break
