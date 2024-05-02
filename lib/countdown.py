# your code goes here!
import time

def countdown(integer):
    while integer:
        print(f"{integer} SECOND(S)!")
        integer -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    while number:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')