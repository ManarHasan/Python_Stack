def reverseList(l):
    if len(l) < 2:
        print("This list is too short!")
        return False
    j = 0
    for i in range(len(l)-1, 0, -1):
        l[i], l[j] = l[j], l[i]
        j += 1
    return l


print(reverseList([1, 2, 3]))


def isPalindrome(str):
    for i in range(len(str)):
        if str[i] == str[len(str)-1-i]:
            continue
        elif str[i] != str[len(str)-1-i]:
            return False
    return True


print(isPalindrome("racecar"))
print(isPalindrome("racefar"))


def coins(cost, paid):
    if paid < cost:
        print("Insufficient funds")
        return False
    change = paid - cost
    quarter_c = 0
    dime_c = 0
    nickle_c = 0
    penny_c = 0
    while change != 0:
        if change > 25:
            change -= 25
            quarter_c += 1
        if change > 10 and change <= 25:
            change -= 10
            dime_c += 1
        if change > 5 and change <= 10:
            change -= 5
            nickle_c += 1
        if change > 0 and change <= 5:
            change -= 1
            penny_c += 1
    print(f"{quarter_c} quarters")
    print(f"{dime_c} dimes")
    print(f"{nickle_c} nickles")
    print(f"{penny_c} pennies")


coins(100, 100)
coins(52, 100)
coins(80, 100)
coins(100, 80)
coins(1, 10)


def factorial(num):
    if num == 0:
        return 1
    return factorial(num-1)*num


print(factorial(5))
print(factorial(10))
print(factorial(3))


def fibonacci(num):
    if num <= 1:
        return num
    else:
        return(fibonacci(num-1) + fibonacci(num-2))


print(fibonacci(15))
print(fibonacci(6))
print(fibonacci(1))
