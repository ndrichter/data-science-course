# LISTS
L = ["Michael Jackson", 10.1, 1982]

print('the same element using negative and positive indexing:\n Postive:', L[0],
      '\n Negative:', L[-3])
print('the same element using negative and positive indexing:\n Postive:', L[1],
      '\n Negative:', L[-2])
print('the same element using negative and positive indexing:\n Postive:', L[2],
      '\n Negative:', L[-1])

L = ["Michael Jackson", 10.1, 1982, "MJ", 1]
print(L[3:5])
L.extend(['pop', 10])
print(L)

L.append(["pop", 11])
print(L)

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

print('Before change:', A)
del (A[0])
print('After change:', A)

print('hard rock'.split())
print('A,B,C,D'.split(','))

# TUPLES
tuple1 = ("disco", 10, 1.2)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])

print(tuple1[-1])
print(tuple1[-2])
print(tuple1[-3])

tuple2 = tuple1 + ("hard rock", 10)
print(tuple2)

print(tuple2[0:3])

ratings = (0, 9, 6, 5, 10, 8, 9, 6, 2)
sort_ratings = sorted(ratings)
print(sort_ratings)

nested = (1, 2, ("pop", "rock") ,(3,4),("disco",(1,2)))
print("Element 0 of Tuple: ", nested[0])
print("Element 1 of Tuple: ", nested[1])
print("Element 2 of Tuple: ", nested[2])
print("Element 3 of Tuple: ", nested[3])
print("Element 4 of Tuple: ", nested[4])

print("Element 2, 0 of Tuple: ",   nested[2][0])
print("Element 2, 1 of Tuple: ",   nested[2][1])
print("Element 3, 0 of Tuple: ",   nested[3][0])
print("Element 3, 1 of Tuple: ",   nested[3][1])
print("Element 4, 0 of Tuple: ",   nested[4][0])
print("Element 4, 1 of Tuple: ",   nested[4][1])

