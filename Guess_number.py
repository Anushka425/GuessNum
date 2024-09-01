import random

def guess(x):
  comp=random.randint(1,x)
  guess=0
  while guess!=comp:
    guess=int(input(f'Guess a number between 1 and {x} :'))
    if guess<comp:
      print('too low')
    elif guess>comp:
      print('too high')

 print(f'Yay, Congrats. You have guessed the number {comp} correctly !!')

x=int(input('Enter range for the game:'))
guess(x)
