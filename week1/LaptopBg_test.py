from LaptopBg import *
import unittest


class LaptopBgTests(unittest.TestCase):

    def setUp(self):
        self.product = Product("product", 10, 15)
        self.laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
        self.smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
        self.store = Store('Laptop.bg')

    def test_Product_init(self):
        self.assertEqual("product", self.product.name)
        self.assertEqual(10, self.product.stock_price)
        self.assertEqual(15, self.product.final_price)

    def test_Product_profit(self):
        self.assertEqual(5, self.product.profit())

    def test_Laptop_init(self):
        self.assertEqual(1000, self.laptop.diskspace)
        self.assertEqual(4, self.laptop.RAM)

    def test_Smartphone_init(self):
        self.assertEqual(7, self.smartphone.display_size)
        self.assertEqual(10, self.smartphone.mega_pixels)

    def test_Store_init(self):
        self.assertEqual("Laptop.bg", self.store.name)
        self.assertEqual({}, self.store.products)
        self.assertEqual(0, self.store.total)

    def test_Store_load_new_products(self):
        self.store.load_new_products(self.smartphone, 2)
        self.store.load_new_products(self.laptop, 3)
        self.store.load_new_products(self.product, 4)
        self.assertEqual({self.product: 4, self.laptop: 3, self.smartphone: 2},
                         self.store.products)

    def test_Store_load_new_products_not_instance_of_Product(self):
        self.store.load_new_products('tomato', 2)
        self.assertEqual({}, self.store.products)

    def test_Store_list_products(self):
        # this function prints
        pass

    def test_Store_sell_product(self):
        self.store.load_new_products(self.smartphone, 2)
        self.store.load_new_products(self.laptop, 3)
        self.store.load_new_products(self.product, 4)
        self.assertTrue(self.store.sell_product(self.smartphone))
        self.assertEqual(1, self.store.products[self.smartphone])
        self.assertEqual(320, self.store.total)

    def test_Store_sell_product_not_in_store(self):
        self.assertFalse(self.store.sell_product(self.smartphone))

    def test_total_income(self):
        self.assertEqual(0, self.store.total_income())

    def test_example_code(self):
        self.store.load_new_products(self.smartphone, 2)
        self.store.load_new_products(self.laptop, 10)
        self.store.list_products(Laptop)
        print(self.store.sell_product(self.smartphone))
        print(self.store.sell_product(self.smartphone))
        print(self.store.sell_product(self.smartphone))
        print(self.store.total_income())

if __name__ == '__main__':
    unittest.main()
