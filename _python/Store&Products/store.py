from product import Product


class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.list = products

    def add_product(self, name, price, category, id):
        """
        This will add a product in the form of an object to the list of products
        """
        if price <= 0:
            print("invalid price value")
            return False
        new_product = Product(name, price, category, id)
        self.list.append(new_product)

    def sell_product(self, id):
        """
        This method will remove a product in the form of an object from the list of products
        """
        for i in range(len(self.list)):
            if self.list[i].id is id:
                self.list.remove(self.list[i])
                break
            if self.list[i].id is not id:
                print("You have the wrong id! This product doesn't exist")
                return False

    def inflation(self, percent_increase):
        """
        This will increase the price of all the products
        """
        for i in range(len(self.list)):
            self.list[i].price += self.list[i].price * percent_increase

    def set_clearance(self, category, percent_discount):
        """
        This will decrease the price of all the products in the same category
        """
        if percent_discount == 1:
            print("This will make this category free")
            return False
        for i in range(len(self.list)):
            if self.list[i].category is category:
                self.list[i].price -= self.list[i].price * percent_discount

    def print_info(self):
        """
        This will print the info of the store
        """
        print(
            f"Name: {self.name}, Products{[self.list.name for self.list in self.list]}")
