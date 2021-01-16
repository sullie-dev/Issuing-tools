import stripe
import time
import os

stripe.api_key = os.getenv('api_key')

# ic_1I59JDJHB9Lj4R4fA0SW1aDh
# ic_1Hx9vCJHB9Lj4R4fXzZo7MfU
# ic_1Hori9JHB9Lj4R4fZjlWmXmB
# ic_1HX1ziJHB9Lj4R4f74uoggxH
# ic_1HUtdsJHB9Lj4R4fJV5fQ5lS


def auth_choice():
  print('Authorisation type outcome: manual you will get a link once the pi is made, automatic authoirsiations will be approved/declined in 60 seconds\n')
  choice = str(input('Manual or automatic auth confirmation? ')).lower()

  if choice == 'manual' or choice =='manual authorisation':
    manual_auth()
  elif choice == 'automatic' or choice =='automatic authorisation':
    automatic_auth()
  else:
    print('invalid input\n')
    auth_choice()

def manual_auth():
  try:
    card_id = str(input('Enter card id - '))
    c = stripe.issuing.Card.retrieve(
      card_id,
      expand=['number', 'cvc'],
    )

    pm = stripe.PaymentMethod.create(
      type="card",
      card={
        "number": c.number,
        "exp_month": c.exp_month,
        "exp_year": c.exp_year,
        "cvc": "123",
        },
      )

    pi = stripe.PaymentIntent.create(
      amount=20000,
      currency="usd",
      payment_method_types=["card"],
      payment_method = pm.id,
      capture_method  = "manual",
      confirmation_method = "automatic",
      confirm = "true",
    ) 

    print('https://dashboard.stripe.com/test/payments/'+ pi.id)

  except Exception as e:
    print(e)

def automatic_auth():
  try:
    card_id = str(input('Enter card id - '))
    c = stripe.issuing.Card.retrieve(
      card_id,
      expand=['number', 'cvc'],
    )

    pm = stripe.PaymentMethod.create(
      type="card",
      card={
        "number": c.number,
        "exp_month": c.exp_month,
        "exp_year": c.exp_year,
        "cvc": "123",
        },
      )

    pi = stripe.PaymentIntent.create(
      amount=200,
      currency="usd",
      payment_method_types=["card"],
      payment_method = pm.id,
      capture_method  = "manual",
      confirmation_method = "automatic",
      confirm = "true",
    ) 
    time.sleep(60)
    stripe.PaymentIntent.capture(
      pi.id,
    )
    print('https://dashboard.stripe.com/test/payments/'+ pi.id)


  except Exception as e:
    print(e)