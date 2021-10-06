def add(a):
    b = a + 1
    print(a, "if you add one", b)
    return b


add(5)


def mult(a, b):
    c = a * b
    return c
    # print('This is not printed')


result = mult(12, 2)
print(result)


def mj():
    # returns None
    print('Michael Jackson')


mj()

# built ins
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]
print(album_ratings)
print(len(album_ratings))
print(sum(album_ratings))


def print_all(*args):  # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args))
    for argument in args:
        print(argument)


# printAll with 3 arguments
print_all('Horsefeather', 'Adonis', 'Bone')
# printAll with 4 arguments
print_all('Sidecar', 'Long Island', 'Mudslide', 'Carriage')


def print_dictionary(**args):  # pack into dictionary
    for key in args:
        print(key + " : " + args[key])


print_dictionary(Country='Canada', Province='Ontario', City='Toronto')
