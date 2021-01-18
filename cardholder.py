import stripe
import os

stripe.api_key = os.getenv('api_key')


def cardholderChoice():
    choice = input(
        'Choice one option\n1) Create cardholder?\n2) Retreive cardholders\n3) List all cardholders\n'
    ).lower()
    try:
        if choice == 'create' or choice == 'create cardholder' or choice == '1':
          createCardholder()
        elif choice == 'retreive' or choice == 'retreive cardholders' or choice == '2':
          retreiveCardholder()
        elif choice == 'list' or choice == 'list cardholders' or choice == '3':
          listCardholders()
    except Exception as e:
        print(e)


def createCardholder():
    cardholder = stripe.issuing.Cardholder.create(
        type=input(str('Individual or company: ')).lower(),
        name=input(str('Cardholder name: ')).lower(),
        email=input(str('Email address for: ')).lower(),
        phone_number=input(str('Phone number: ')).lower(),
        billing={
            "address": {
                "line1": input(str('Address Line 1: ')).lower(),
                "city": input(str('City: ')).lower(),
                "state": input(str('State: ')).lower(),
                "country": input(str('Country:')).upper(),
                "postal_code": input(str('Postal Code: ')).lower(),
            },
        },
    )
    print('\n' + cardholder)

def retreiveCardholder():
    cardholder = stripe.issuing.Cardholder.retrieve(
        input(str('Cardholder id: ')))

    print('\n')
    print(cardholder)


def listCardholders():
    cardholders = stripe.issuing.Cardholder.list(
        limit=input(str('How many cardholders to list?'))
    )
    for cardholder in cardholders:
      print(cardholder.id)
