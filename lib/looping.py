#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    pass

def square_integers(int_list):
    # i is whatever the list of number containing in int_list is.
    square_list = [i ** 2 for i in int_list]
    return (square_list)
    pass

def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
    pass
