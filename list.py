my_list = list(range(100))
other_list = ["James", "Baby Monkey", 2006, True]


def print_list(words, l):
    print("value of ", words)
    print("size:", len(l))
    print(l)


print_list("My list", my_list)
print_list("Other list", other_list)

for x in other_list:
    print(x)
