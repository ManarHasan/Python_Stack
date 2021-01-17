class Underscore:
    def map(self, l, callback):
        l2 = []
        for i in range(len(l)):
            x = l[i]
            l2.append(callback(x))
        return l2

    def find(self, l, callback):
        for i in range(len(l)):
            x = l[i]
            if callback(x) is True:
                break
        return x

    def filter(self, l, callback):
        l2 = []
        for i in range(len(l)):
            x = l[i]
            if callback(x) is True:
                l2.append(x)
        return l2

    def reject(self, l, callback):
        l2 = []
        for i in range(len(l)):
            x = l[i]
            if callback(x) is False:
                l2.append(x)
        return l2


_ = Underscore()
print(_.map([1, 2, 3, 4, 5, 6], lambda x: x*2))
print(_.find([1, 2, 3, 4, 5, 6], lambda x: x > 4))
print(_.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
print(_.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0))
