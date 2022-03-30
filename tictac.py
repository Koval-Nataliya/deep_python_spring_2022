board = list(range(1, 10))


def draw_board(board):
    for j in range(3):
        print("|", board[0 + j * 3], "|",
              board[1 + j * 3], "|", board[2 + j * 3], "|")


def start(fir):
    if fir == 'X' or fir == 'x' or fir == 'х' or fir == 'Х':
        return 'X'
    elif fir == 'O' or fir == 'o' or fir == 'о' or fir == 'О' or fir == '0':
        return 'O'
    else:
        return False


def take_input(player_token):
    valid = True
    while valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Введите число от 1 до 9.")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = False
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


if __name__ == '__main__':
    counter = 0
    win = False
    print("Кто начнет игру? Введите X или O.")
    i = input()
    first = start(i)
    while not first:
        print('Некорректный ввод. Введите Х или О')
        i = input()
        first = start(i)

    if first == 'X':
        second = 'O'
    else:
        second = 'X'

    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input(first)
        else:
            take_input(second)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
