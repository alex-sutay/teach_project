# this is a script! Read top to bottom, executing in that order

print('this one first')

print('next this one')

print('finally this one')

# when reading code, the computer ignores lines with # in front
# use them to leave helpful comments about how your code works!


# Let's talk remembering things

x = 3  # there's a thing called x, and it represents 3
print(x)

y = x + 1  # now we have something called y, and it's a little bigger than x
print(y)

x = x + 1  # mathematicians, calm down  (simpler way would x += 1)
print(x)

# x was an int
# We also have floats
x += 0.5
print(x)

first_str = "Hello"  # store some literal text
second_str = 'World'
print(first_str + " " + second_str)

# Those are all way too complicated, I really just need to remember yes or no
yes = True
no = False

# Now let's remember a bunch of things
veggies = ['tomatoes', 'smaller tomatoes', 'chocolate']
print(veggies)
veggies.append('Vegetables are a social construct')
print(veggies)

# oooh curly, what does this one do?
fruits = {'tomatoes', 'mangoes', 'peaches'}
print(fruits)
fruits.add('mangoes')
fruits.add('apples')
print(fruits)

# Curly 2: Electric boogaloo; this time with more colons
social_constructs = {'fruits': False, 'veggies': True, False: 'Probably not?', 42: 'Wait what was this dict for again?'}
print(social_constructs)

# let's try accessing things now!
print(veggies[2])
print(veggies[-1])
print(veggies[:2])
print(veggies[:-1])
print(veggies[::-1])
print(second_str[1] + first_str[0])  # oh look it works on strings too!

# you can't get a specific item from a set, but you can check if your item is in there
print('apples' in fruits)
print('tomatoes' in fruits)

# Dictionaries are used to look things up
print(social_constructs['fruits'])
print(social_constructs['veggies'])

resp = input('You can also ask users for things > ')
print(resp.lower()[:2])
