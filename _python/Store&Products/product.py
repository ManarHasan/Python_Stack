class Product:
    def __init__(self, name, price, category, id):
        self.name = name
        self.price = price
        self.id = id
        self.category = category

    def update_price(self, percent_change, is_increased):
        """
        This will update the price of a product (increase or decrease)
        """
        if is_increased is False and percent_change == 1:
            ("This will make this product free")
            return False
        if is_increased is True:
            self.price += self.price * percent_change
        else:
            self.price -= self.price * percent_change

    def print_info(self):
        """
        This will print the info about a certain product
        """
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: {self.price}")
