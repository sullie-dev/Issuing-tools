import stripe
import os

stripe.api_key = os.getenv('api_key')


def cardChoice():
    choice = input(
        'Choice one option\n1) Create card?\n2) List all cards\n3) List card\n'
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
    print('Leave crdholder blank to have a new cardholer created')
    ch_id = str(input('Enter cardholder id - '))
    cur = input(str('Enter currency (USD only) - '))
    card_type = input(str('Physical or virtual card - '))
    st = input(str('Is the card active or inactive? - '))
    try:
        new_card = stripe.issuing.Card.create(
            cardholder=ch_id,
            currency=cur,
            type=card_type,
            status=st,
        )
        print(new_card.id)
    except Exception as e:
        print(e)


def lstAll():
    lstAmount = int(input('How many card ids would you liske to list - '))
    try:
        lst = stripe.issuing.Card.list(limit=lstAmount)
        for card in lst:
            print(card.id)
    except Exception as e:
        print(e)


def retreiveCard():
    card_id = str(input('Enter card id - '))
    try:
        card = stripe.issuing.Card.retrieve(card_id, )
        print(card)
    except Exception as e:
        print(e)
