import random


def guess_random_number(tries, start, stop):
    randnum = random.randint(start, stop)
    guesses = []
    while tries != 0:
        print(f'Number of tries left: {tries}')
        try:
            user_input = int(
                input(f'Guess a number between {start} and {stop}: '))
        except ValueError:
            print('Input integer')
            continue
        if user_input not in guesses:
            guesses.append(user_input)
            if user_input not in range(start, stop + 1):
                print(' Guessed number not in range')
                continue
            if user_input == randnum:
                print('You guessed the correct number!')
                return
            elif user_input > randnum:
                print('Guess lower!')
            elif user_input < randnum:
                print('Guess higher!')
            tries -= 1
        else:
            print('Number already guessed!')

    print(f'You have failed to guess the number: {randnum}')


def guess_random_num_linear(tries, start, stop):
    randnum = random.randint(start, stop)
    for num in range(start, stop + 1):
        print(f'tries: {tries}')
        tries -= 1
        print(f'random number: {randnum}, computer guess: {num}')
        if num == randnum:
            print(f'Success! The program guessed the number')
            return 0
        if tries == 0:
            return print('Failed to guess number')


def guess_random_num_binary(tries, start, stop):
    randnum = random.randint(start, stop)
    lower_bound = start
    upper_bound = stop
    while tries != 0:
        print(f'tries: {tries}')
        pivot = (lower_bound + upper_bound) // 2
        tries -= 1
        print(f'random number: {randnum}, computer guess: {pivot}')
        if randnum == pivot:
            return print(f'Found it! {randnum}')
        elif pivot > randnum:
            print('Number is lower')
            upper_bound = pivot - 1
        else:
            print('Number is higher')
            lower_bound = pivot + 1
    return print('Your program failed to find the number.')


def select_guess():
    user_tries = int(input('Input number of tries: '))
    user_start = int(input('Input start value: '))
    user_stop = int(input('Input stop value: '))
    print("\nSelect random number from user input, linear search or binary search ")
    user_pick = input(
        '1: user input        2: linear search        3: binary search ')
    if user_pick == '1':
        guess_random_number(user_tries, user_start, user_stop)
    elif user_pick == '2':
        guess_random_num_linear(user_tries, user_start, user_stop)
    elif user_pick == '3':
        guess_random_num_binary(user_tries, user_start, user_stop)


def gambling_game():
    player_money = 45
    while player_money > 0:
        user_input = input(
            "Will the computer guess the correct number? \n Y or N ")
        bet = int(input('Place a bet from 1 - 10 '))
        if bet > player_money or bet > 10 or bet <= 0:
            print("invalid bet")
            continue
        else:
            comp_guess = guess_random_num_linear(5, 0, 10)
        # player guesses right , 0 = program found number
        if comp_guess == 0 and user_input == 'Y':
            player_money = player_money + (bet*2)
            print(f'player money: {player_money}')
        elif comp_guess != 0 and user_input == 'N':
            player_money = player_money + (bet*2)
            print(f'player money: {player_money}')
        else:
            player_money = player_money - bet
            print(f'player money: {player_money}')

        if player_money > 50:
            print("You Won!")
            break
    if player_money == 0:
        print('You ran out of money')


#guess_random_num_binary(5, 0, 10)
#guess_random_number(5, 0, 15)
# guess_random_num_linear(5,0,10)
# select_guess()
gambling_game()
