def countdown(num):
    l = []
    for i in range(num, 0, -1):
        l.append(i)
    print(l)


def print_and_return(l):
    if len(l) != 2:
        return False
    print(l[0])
    return(l[1])


def first_plus_length(l):
    sum = l[0] + len(l)
    return sum


def values_greater_than_second(l):
    l2 = []
    if len(l) < 2:
        return False
    for i in range(len(l)):
        if l[i] > l[1]:
            l2.append(l[i])
    return l2


def length_and_value(size, value):
    l = []
    for i in range(size):
        l.append(value)
    print(l)


countdown(5)
print_and_return([1, 2])
print(first_plus_length([1, 2, 3, 4, 5]))
print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
length_and_value(4, 7)
