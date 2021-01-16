from card import cardChoice
from test_authorisations import auth_choice

def choices():
  choice = input("What tool would you like to use\n1) Cards\n2) Cardholders\n3) Test Authorisations\n\n0) Help\n").lower()
  if choice == 'card' or choice == "cards":
	  cardChoice()
  elif choice == 'cardholder' or choice == "cardholders":
    print('Cardholder path')
  elif choice == 'help' or choice == '0':
    print('helper path')
  elif choice == 'test' or choice == "auth" or choice == "test authorisation":
    auth_choice()
  else:
    auth_choice()

def inv():
  print("Incorrect choice, please select one of the below choices\n")
  choices()

choices()