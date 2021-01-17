class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current = self.head
        new_node.next = current
        self.head = new_node
        current.previous = new_node
        return self

    def print_values(self):
        runner = self.head
        while (runner != None):
            print(runner.value)
            runner = runner.next
        return self

    # def add_to_back(self, val):
    #     if self.head == None:
    #         self.add_to_front(val)
    #         return self
    #     new_node = SLNode(val)
    #     runner = self.head
    #     while (runner.next != None):
    #         runner = runner.next
    #     runner.next = new_node
    #     return self

    # def remove_from_front(self):
    #     if self.head == None:
    #         print("There is no head")
    #         return self
    #     removed_value = self.head.value
    #     current = self.head
    #     self.head = current.next
    #     current = None
    #     print(removed_value)
    #     return self

    # def remove_from_back(self):
    #     current = self.head
    #     while (current.next != None):
    #         previous = current
    #         current = current.next
    #     print(current.value)
    #     previous.next = None
    #     return self

    # def remove_val(self, val):
    #     current = self.head
    #     if current.value == val:
    #         current = None
    #         return self
    #     if current.next.value == val:
    #         current.next = current.next.next
    #         return self
    #     while(current.next.value != val):
    #         previous = current
    #         current = current.next
    #     previous.next = current.next
    #     return self

    # def insert_at(self, at, val):
    #     current = self.head
    #     new_node = SLNode(val)
    #     if current.value == at:
    #         temp = current.next
    #         current.next = new_node
    #         new_node.next = temp
    #         return self
    #     if current.next.value == at:
    #         temp = current.next.next
    #         current.next.next = new_node
    #         new_node.next = temp
    #         return self
    #     while(current.next.value is not at):
    #         current = current.next
    #     temp = current.next.next
    #     current.next.next = new_node
    #     new_node.next = temp
    #     return self


class SLNode:
    def __init__(self, val):
        self.value = val
        self.previous = None
        self.next = None


my_list = SList()
my_list.add_to_front(1).add_to_front(2).print_values()
