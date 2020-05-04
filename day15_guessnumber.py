from random import randint

MAX_GUESSES = 5
START,END = 1, 20

def get_random_number():
    return randint(START, END)

class Game:

        def __init__(self):
            self._guesses = set()
            self._answer = get_random_number()
            self._win = False

        def guess(self):
            ''' Takes input form user and validates the input'''
            guess = input(f"Guess a random number between {START} and {END}: ")
            if not guess:
                raise ValueError('Please enter a number')
            try:
                guess = int(guess)
            except ValueError:
                raise ValueError("Enter a number")
            if guess not in range(START, END+1):
                raise ValueError('Number not in range')
            if guess in self._guesses:
                raise ValueError('Number already guessed')
            self._guesses.add(guess)
            return guess

        def validate_guess(self, guess):
            ''' Validate whether the user guessed correctly or not'''
            if guess == self._answer:
                print(f'{guess} is correct')
            elif guess > self._answer:
                print(f'{guess} is too high')
            else:
                print(f'{guess} is too low')

        @property
        def num_guesses(self):
            return len(self._guesses)

        def __call__(self):

            while len(self._guesses) < MAX_GUESSES:
                try:

                    guess = self.guess()
                except ValueError as ve:
                    print(ve)
                    continue
                win = self.validate_guess(guess)
                if win:
                    guess_str = self.num_guesses == 1 and "guess" or "guesses"
                    print(f'It took you {self.num_guesses} {guess_str}')
                    self.win = True
                    break
            else:
                print(f'Guessed {MAX_GUESSES} times, answer was {self._answer}')

if __name__ =='__main__' :
    game = Game()
    game()





