for i in range(151):
    print(i)
for i in range(5, 1001):
    if i % 5 == 0:
        print(i)
for i in range(101):
    if i % 5 == 0:
        print("Coding")
    if i % 10 == 0:
        print("Coding Dojo")
sum = 0
for i in range(500001):
    sum += i
print(sum)
for i in range(2018, 0, -1):
    if i % 2 == 0:
        print(i)


def loop(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        if i % mult == 0:
            print(i)


loop(2, 9, 3)
