"""This program rolls a pair of dice and asks the user to guess a number. 
Based on the user's guess, the program should determine a winner. 
If the user's guess is greater than the total value of the dice roll, they win. Otherwise, the computer wins."""

from random import randint
from time import sleep

def get_user_guess():
  user_guess = int(raw_input("Enter your guess of number: "))
  return user_guess
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum value is: " + str(max_val)
  sleep(1)
  user_guess = get_user_guess()
  if user_guess > max_val:
    print "You guessed higher than the maximum value! Try again"
    return
  else:
    print "Rolling..."
    sleep(2)
    print "The first value is: %d" % first_roll
    sleep(1)
    print "The second value is: %d" % second_roll
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if user_guess > total_roll:
      print "You won!"
      return
    else:
      print "You lost"
      return
roll_dice(4)