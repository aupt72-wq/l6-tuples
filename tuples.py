stuDetails = ("Jacob", 94)
print(stuDetails)

address = ("123", "Turn Street", "London", "Westminster", "125741")
for x in address:
    print(x, end=" ")

houseno, apartName, city, state, pin = address
print("HNO", houseno)
print("APT NO", apartName)
print(city)
print(state)
print(pin)

my_tuple = 1, 2, 3, 4, 5, 6, 7
print(my_tuple)

n_tuple = ("dog", [8, 1, 2], (1, 6, 4))

print(n_tuple[0][2])
print(n_tuple[1][1])

my_tuple = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print("values from 1 to 3",my_tuple[1:4])
print("values from 1 to the end",my_tuple[1:])
print("values from 7 to the end",my_tuple[7:])
print("values to 1",my_tuple[:1])

my_tuple = ("1", "2", "3", ["cat", "dog"])
my_tuple[3][0] = 9
print(my_tuple)

my_tuple = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print(my_tuple)