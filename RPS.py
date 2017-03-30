"""A rock-paper scissors program."""

from random import randint
from time import sleep

options = ["R", "P", "S"]

LOSS_MESSAGE = "You lost"
WON_MESSAGE = "You won"
TIE_MESSAGE = "It's a tie"

def decide_winner(user_choice, computer_choice):
  print "You selected: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print "Computer selected: %s" % computer_choice
  print "Computer selecting..."
  sleep(1)
  
  USER_CHOICE_INDEX = options.index(user_choice)
  COMPUTER_CHOICE_INDEX = options.index(computer_choice)
  
  if USER_CHOICE_INDEX == COMPUTER_CHOICE_INDEX:
    print TIE_MESSAGE
  elif USER_CHOICE_INDEX == 0 and COMPUTER_CHOICE_INDEX == 2:
    print WON_MESSAGE 
  elif USER_CHOICE_INDEX == 1 and COMPUTER_CHOICE_INDEX == 0:
    print WON_MESSAGE
  elif USER_CHOICE_INDEX == 2 and COMPUTER_CHOICE_INDEX == 1:
    print WON_MESSAGE
  elif USER_CHOICE_INDEX > 2:
    print "Invalid option."
    return 
  else:
    print LOSS_MESSAGE

def play_RPS():
  print "Rock, Paper, or Scissors?"
  user_choice = raw_input("Select R for Rock, P for Paper, or S for Scissors:")
  sleep(1)
  user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)
play_RPS()
    


  