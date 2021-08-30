# Let's make a real program now
from this_is_a_script import *


def function():
    print('Wow, we declared a function, and then called it!')


def ooh_now_with_params(x):
    """
    This is a multi line comment, typically placed inside a function to describe the purpose of a function
    :param x: Something to print
    :return: None
    """
    print('This time, when you made a function, you also passed in:', x)


function()
ooh_now_with_params()  # we need to add something here


def logic_and_loops():
    """
    A basic function to showcase how to use basic logic and loops
    :return: None
    """
    # Let's make a branching path!
    # Some logic:
    if 3 > 2:
        print('wtf')
    if 'Hi there' == 'Hello there':
        print('General Kenobi')
    if -984217594385214 < 4.5:
        print(1)
    # some other branch pieces
    if 'tomatoes' in fruits:
        print("Ha! It's a fruit, told ya so!")  # Note that we want to use ' in It's, so we use " for the string
    elif 'tomatoes' in veggies:
        print('Duh, of course it is')
    else:
        print("I guess we'll never know")
    # Some nesting
    if 'tomatoes' in fruits and 'tomatoes' in veggies:
        print('wait what?')
        if social_constructs['veggies']:
            print('Ohhhhh that makes sense')

    # now that we've branched out a little, let's see what we can do with loops
    cont = True
    while cont:
        txt = input('Tell me something funny > ')
        cont = not txt == 'something funny'
    print('smart', 'ass', sep='-', end='')
    print("wait now I'm next to the other print")

    # How about a set number of loops?
    for i in range(7):
        print(i, i**2, sep=': ')

    # oh look, accessing things in a set
    for fruit in fruits:
        print(f'{fruit} is a fruit')

    # this works for any "iterable", including lists, strings, and dictionaries
    for concept in social_constructs:
        print_str = f'{concept} is a social construct' if social_constructs[concept] else f'{concept} is legit'
        print(print_str)

    for veg in veggies:
        for letter in veg:
            print(letter)
