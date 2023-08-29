#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square()
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 'j'
my_square.my_print()

print("--")
