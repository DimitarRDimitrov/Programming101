class Product():
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        profit = 0
        profit = self.final_price - self.stock_price
        return profit


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.mega_pixels = mega_pixels
        self.display_size = display_size


class Store():
    def __init__(self, name):
        self.name = name
        self.stuff = {}
        self.income = 0

    def load_new_products(self, product, count):
        if isinstance(product, Product):
            if product in self.stuff:
                self.stuff[product] += count
            else:
                self.stuff[product] = count

    def list_products(self, product_class):
        for product in self.stuff:
            if isinstance(product, Product):
                return "{} - {}".format(product.name, self.stuff[product])

    def sell_product(self, product):
        if product in self.stuff and self.stuff[product] > 0:
            self.stuff[product] -= 1
            self.income += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.income

store = Store('Laptop.bg')
print(store.name)
smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
store.load_new_products(smartphone, 2)
print(store.list_products(Smartphone))
print(store.sell_product(smartphone))
print(store.sell_product(smartphone))
print(store.sell_product(smartphone))

print(store.total_income())
