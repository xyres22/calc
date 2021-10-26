import logging
logging.basicConfig(level=logging.DEBUG)

def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

question = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
if question in (1,2,3,4):
    num1 = float(input('Podaj składnik 1. '))
    num2 = float(input('Podaj składnik 2. '))

    if question == 1:
        logging.info(f'Dodaję {num1} i {num2}')
        print(f'Wynik to {add(num1,num2)}')

    elif question == 2:
        logging.info(f'Odejmuję {num1} i {num2}')
        print(f'Wynik to {subtract(num1,num2)}')

    elif question == 3:
        logging.info(f'Mnożę {num1} i {num2}')
        print(f'Wynik to {multiply(num1,num2)}')

    elif question == 4:
        logging.info(f'Dzielę {num1} i {num2}')
        print(f'Wynik to {divide(num1,num2)}')
else:
    print('Podałes zła liczbę')



    
