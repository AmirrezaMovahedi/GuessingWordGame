import random

words_list = ['rainbow', 'computer', 'science', 'programming',
              'python', 'mathematics', 'player', 'condition',
              'reverse', 'water', 'board', 'geeks']
word = random.choice(words_list)
chance = len(word) + 3
counter = 0
guess = ['_'] * (len(word))


while counter != chance:
    user_guess = input('please enter your guess [char] ')
    if user_guess.isdigit():
        print(f'please enter char not {user_guess}')
        continue
    for i, char in enumerate(word):
        if user_guess == char:
            guess[i] = user_guess
    print(guess)
    if guess == list(word):
        print(f'You won!! counter: {counter}')
        break
    else:
        counter += 1
        continue
else:
    print(f'your chance to guess was end!! word: {word}')
