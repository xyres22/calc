import logging
logging.basicConfig(level=logging.DEBUG,format='%(message)s')

def add(num1,num2):
    logging.info(f'Dodaję {num1} i {num2}')
    print(f'Wynik to {num1 + num2}')

def subtract(num1,num2):
    logging.info(f'Odejmuję {num1} i {num2}')
    print(f'Wynik to {num1 - num2}')

def multiply(num1,num2):
    logging.info(f'Mnożę {num1} i {num2}')
    print(f'Wynik to {num1 * num2}')

def divide(num1,num2):
    logging.info(f'Dzielę {num1} i {num2}')
    print(f'Wynik to {num1 / num2}')
    
question = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: '))
if question in (1,2,3,4):
    num1 = float(input('Podaj składnik 1. '))
    num2 = float(input('Podaj składnik 2. '))

    operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide,
    }

    result  = operations[question](num1, num2)
    
else:
    print('Podałes zła liczbę')