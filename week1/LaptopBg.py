class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM


class Smartphone(Product):

    def __init__(self, name, stock_price, final_price,
                 display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.total = 0

    def load_new_products(self, product, count):
        if isinstance(product, Product):
            self.products[product] = count

    def list_products(self, product_class):
        for key in self.products:
            if isinstance(key, product_class):
                print("%s - %s" % (key.name, self.products[key]))

    def sell_product(self, product):
        if (product in self.products and
           self.products[product] > 0):
            self.products[product] -= 1
            self.total += product.profit()
            return True
        return False

    def total_income(self):
        return self.total


def main():
    store = Store('Laptop.bg')
    smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    #laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
    store.load_new_products(smartphone, 2)
    #store.load_new_products(laptop, 10)
    #store.list_products(Laptop)
    print(store.sell_product(smartphone))
    print(store.sell_product(smartphone))
    #print(store.sell_product(smartphone))
    print(store.total_income())

if __name__ == '__main__':
    main()
