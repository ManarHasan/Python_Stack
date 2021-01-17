def firstnlast(l):
    if len(l) < 2:
        return False
    return l[0],l[-1]
print(firstnlast([1,2,3,4]))

def sum(l):
    sum=0
    for i in l:
        sum+=i
    return sum
print(sum([1,2,3,4]))

def reverse(l):
    return l[::-1]
print(reverse([1,2,3,4]))

def mmas(l):
    #d=dict()
    sum=0
    min=l[0]
    max=l[0]
    for i in l:
        sum+=i
        if i < min:
            min = i
        if i > max:
            max = i
    return {"sum":sum,"avg":sum/len(l), "min":min, "max":max}
    """
    d["sum"]=sum
    d["avg"]=sum/len(l)
    d["min"]=min
    d["max"]=max
    return d
    """
    
print(mmas([1,2,3,4]))

# def bubble(l, end):
#     if end == 0:
#         return l
#     max=0
#     for i in range(end+1):
#         if l[i]>l[max]:
#             max=i
#     l[max], l[end]=l[end], l[max]
#     return bubble(l,end-1)
# lop=[1,5,3,7,2]
# print(bubble(lop,len(lop)-1))


def bubble(l, end):
    if end == 0:
        return l
    for i in range(1, end+1):
        if l[i]<l[i-1]:
            l[i], l[i-1] = l[i-1],l[i]

    return bubble(l,end-1)
lop=[1,5,3,7,2]
print(bubble(lop,len(lop)-1))