class Product:
    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price


class DiscountedProduct(Product):
    def get_price(self):
        price = super().get_price()
        return price - 0.1 * price


product = DiscountedProduct(100)
print(product.get_price())
