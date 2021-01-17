def select(l):

    for i in range(len(l)):
        min = i
        for j in range(i+1, len(l)):
            if l[min] > l[j]:
                min = j
        l[i], l[min] = l[min], l[i]

    return l


print(select([6, 5, 4, 3, 1]))
