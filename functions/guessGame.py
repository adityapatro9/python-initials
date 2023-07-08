from random import shuffle

buckets_list = [' ', 'O', ' ']


def validate_user_guess(guessed_index: int):
    if guessed_index == '':
        print('Please enter a bucket number \n')
        return False
    if int(guessed_index) not in [1, 2, 3]:
        print('Please enter the bucket numbers between 1-3 \n')
        return False
    else:
        return True


def shuffle_game(guessed_index: int):
    if validate_user_guess(guessed_index):
        index = 0
        shuffle(buckets_list)
        print(buckets_list)
        for i in buckets_list:
            if buckets_list[index] == 'O' and index == guessed_index-1:
                return 'HIT'
            else:
                return 'MISS'
        index += 1
    else:
        return


while True:
    guess_position = input('Enter the bucket number 1,2,3 where you think the ball is \n')
    print(shuffle_game(int(guess_position)))
