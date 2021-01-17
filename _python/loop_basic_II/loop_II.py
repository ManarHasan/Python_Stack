def biggie(l):
    for i in range(len(l)):
        if l[i] >= 0:
            l[i] = "big"
    return l


def count_positives(l):
    count = 0
    for i in range(len(l)):
        if l[i] > 0:
            count = count + 1
    l[-1] = count
    return l


def sum_total(l):
    sum = 0
    for i in range(len(l)):
        sum += i
    return sum


def average(l):
    sum = 0
    for i in range(len(l)):
        sum += i
    avg = sum/len(l)
    return avg


def length(l):
    return len(l)


def min(l):
    min = l[0]
    if len(l) == 0:
        return False
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    return min


def max(l):
    max = l[0]
    if len(l) == 0:
        return False
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    return max


def ultimate_analysis(l):
    sum = 0
    min = l[0]
    max = l[0]
    length = len(l)
    for i in l:
        sum += i
        if i < min:
            min = i
        if i > max:
            max = i
    return {"sumTotal": sum, "average": sum/len(l), "minimum": min, "maximum": max, "length": length}


# def reverse_list(a):
#     print(a[::-1])
def reverse_list(l):
    end = len(l)-1
    for i in range(int((len(l)-1)/2)):
        l[i], l[end] = l[end], l[i]
        end = end-1
    return l


print(biggie([1, 2, -1, -2]))
print(count_positives([1, 2, -1, -2]))
print(sum_total([1, 2, 3, 4, 5]))
print(average([1, 2, 3, 4, 5]))
print(length([1, 2, 3, 4, 5]))
print(min([37, 2, 1, -9]))
print(max([2, 37, 1, -9]))
print(ultimate_analysis([37, 2, 1, -9]))
print(reverse_list([1, 2, 3, 4, 5]))
