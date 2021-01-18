import stripe
import os
from cardholder import createCardholder

stripe.api_key = os.getenv('api_key')


def cardChoice():
    choice = input(
        'Choice one option\n1) Create card?\n2) List all cards\n3) List card\n\nChoice: '
    ).lower()
    try:
        if choice == 'create' or choice == 'create card' or choice == '1':
            createCard()
        elif choice == 'list all' or choice == 'list all cards' or choice == '2':
            lstAll()
        elif choice == 'list' or choice == 'list card' or choice == '3':
            retreiveCard()
    except Exception as e:
        print(e)


def createCard():
    try:
        new_card = stripe.issuing.Card.create(
            cardholder=input(str('Enter cardholder id - ')),
            currency=input(str('Enter currency (USD only) - ')),
            type=input(str('Physical or virtual card - ')),
            status=input(str('Is the card active or inactive? - ')),
        )
        print(new_card.id)
    except Exception as e:
        print(e)


def lstAll():
    try:
        lst = stripe.issuing.Card.list(limit=int(input('How many card ids would you liske to list - ')))

        for card in lst:
            print(card.id)
    except Exception as e:
        print(e)


def retreiveCard():
    try:
        card = stripe.issuing.Card.retrieve(
          input(str('Enter card id - ')), 
          )
        print(card)
    except Exception as e:
        print(e)
