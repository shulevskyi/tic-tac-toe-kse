import random
import time
user_play = 1  # 1 ==> True
comp_play = 0  # 0 ==> False

bet_str = 0
bet_money = 0
balance = 1000


def tic_tac_toe():
    global user_play, comp_play, bet_str, bet_money, balance
    list_of_inputs = []

    for empty_signs in range(0, 9):  # empty strings inside a body
        list_of_inputs.append(' ')

    top_bottom = '---------'
    print(top_bottom)

    def func_in():
        start_index = 0
        end_index = 3
        for signs_inside in range(0, 3):  # inserting signs inside a body
            print('|', ' '.join(list_of_inputs[start_index:end_index]), '|')
            start_index += 3
            end_index += 3
        print(top_bottom)

    func_in()

    tryings = 1
    two_signs = ''

    while True:
        try:
            coordinates = []
            if user_play == 1 and comp_play == 0:
                coordinates = list(map(int, input('Enter the coordinates: ').split()))
            elif comp_play == 1 and user_play == 0:
                for i in range(0, 2):
                    time.sleep(0.2)
                    coordinates.append(random.randint(1, 3))

            actual_index = 0  # index for list_of_inputs
            if (1 <= coordinates[0] <= 3) and 1 <= coordinates[1] <= 3:
                actual_index = 3 * (coordinates[0] - 1) + coordinates[1] - 1  # formula for calculating actual_index from coordinates
                if list_of_inputs[actual_index] == ' ':
                    print(top_bottom)
                    list_of_inputs.pop(actual_index)  # removing element before inserting new one

                    if tryings % 2 != 0:
                        two_signs = 'X'
                    elif tryings % 2 == 0:
                        two_signs = 'O'

                    list_of_inputs.insert(actual_index, two_signs)
                    tryings += 1

                    func_in()

                    x_winnings = 0
                    o_winnings = 0

                    init_dict = [list_of_inputs[0:3], list_of_inputs[3:6], list_of_inputs[6:9]]

                    if init_dict[0].count('X') == 3 or init_dict[1].count('X') == 3 or init_dict[2].count('X') == 3:
                        x_winnings = 1
                    if init_dict[0].count('O') == 3 or init_dict[1].count('O') == 3 or init_dict[2].count('O') == 3:
                        o_winnings = 1

                    # the main logic of the game for columns

                    if 'X' in list_of_inputs[0] and 'X' in list_of_inputs[3] and 'X' in list_of_inputs[6]:
                        x_winnings += 1
                    if 'X' in list_of_inputs[1] and 'X' in list_of_inputs[4] and 'X' in list_of_inputs[7]:
                        x_winnings += 1
                    if 'X' in list_of_inputs[2] and 'X' in list_of_inputs[5] and 'X' in list_of_inputs[8]:
                        x_winnings += 1
                    if 'O' in list_of_inputs[0] and 'O' in list_of_inputs[3] and 'O' in list_of_inputs[6]:
                        o_winnings += 1
                    if 'O' in list_of_inputs[1] and 'O' in list_of_inputs[4] and 'O' in list_of_inputs[7]:
                        o_winnings += 1
                    if 'O' in list_of_inputs[2] and 'O' in list_of_inputs[5] and 'O' in list_of_inputs[8]:
                        o_winnings += 1

                    # the main logic of the game for diagonal

                    if 'X' in list_of_inputs[0] and 'X' in list_of_inputs[4] and 'X' in list_of_inputs[8]:
                        x_winnings += 1
                    if 'X' in list_of_inputs[2] and 'X' in list_of_inputs[4] and 'X' in list_of_inputs[6]:
                        x_winnings += 1
                    if 'O' in list_of_inputs[0] and 'O' in list_of_inputs[4] and 'O' in list_of_inputs[8]:
                        o_winnings += 1
                    if 'O' in list_of_inputs[2] and 'O' in list_of_inputs[4] and 'O' in list_of_inputs[6]:
                        o_winnings += 1

                    def again_play():  # questions to user
                        global user_play, comp_play, bet_money, bet_str
                        play_again = int(input('Do you want to play again (1 - yes, 2 - exit)? or would you like to see how computers play themselves (3)?\n'))
                        if play_again == 1:
                            user_play = 1
                            comp_play = 0
                            tic_tac_toe()
                        elif play_again == 2:
                            exit()
                        elif play_again == 3:
                            bet_game = list(map(int, input(f'Make a bet on X\'s (1), O\'s (0) and Draw (3) and type chosen amount of money. \nType as shown on example: 1 154\nYour current balance is: {balance}\n').split()))
                            bet_str = bet_game[0]
                            bet_money = bet_game[1]
                            comp_play = 1
                            user_play = 0
                            tic_tac_toe()

                    # Draw
                    if x_winnings + o_winnings == 0 and tryings == 10:
                        print('Draw')
                        if comp_play == 1 and bet_str == 3:
                            balance += bet_money * 5.5
                            print(f'You won ${bet_money * 5.5} Your current balance is: {balance}')
                        if comp_play == 1 and bet_str != 3:
                            balance -= bet_money
                            print(f'You lost ${bet_money} Your current balance is: {balance}')
                        again_play()

                    # Winning
                    if x_winnings == 1:
                        print('X wins')
                        if comp_play == 1 and bet_str == 1:
                            balance += bet_money * 2
                            print(f'You won ${bet_money * 2} Your current balance is: {balance}')
                        if comp_play == 1 and bet_str != 1:
                            balance -= bet_money
                            print(f'You lost ${bet_money} Your current balance is: {balance}')
                        again_play()

                    if o_winnings == 1:
                        print('O wins')
                        if comp_play == 1 and bet_str == 0:
                            balance += bet_money * 2
                            print(f'You won ${bet_money * 2} Your current balance is: {balance}')
                        if comp_play == 1 and bet_str != 0:
                            balance -= bet_money
                            print(f'You lost ${bet_money} Your current balance is: {balance}')
                        again_play()

                elif list_of_inputs[actual_index] != ' ':
                    print('This cell is occupied! Choose another one!')
            elif (coordinates[0] < 1 or coordinates[0] > 3) or (coordinates[1] < 1 or coordinates[1] > 3):
                print('Coordinates should be from 1 to 3!')
        except ValueError:
            print('You should enter numbers!')


tic_tac_toe()

