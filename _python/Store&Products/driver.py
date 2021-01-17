from store import Store
from product import Product

store = Store("Abu Yousef")
store.add_product(["lipton"], 5, "tea", 1)
store.add_product(["xl"], 4, "drink", 2)
store.add_product(["nescafe"], 0.1, "neccessity", 3)
store.add_product(["test"], 10, "test", 4)
store.set_clearance("drink", 0.02)
store.inflation(0.05)
store.sell_product(2)
for i in range(len(store.list)):
    print(f"Name: {store.list[i].name}, Price: {store.list[i].price}")
store.print_info()
