class Product:
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if quantity < 0:
            raise ValueError('Кол-во товара не может быть меньше 0!')
        else:
            return self.quantity >= quantity

    def buy(self, quantity):
        if self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError('Недостаточно продукта!')

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    products: dict[Product, int]

    def __init__(self):
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count

    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None or remove_count >= self.products[product]:
            del self.products[product]
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        total_price = 0
        for product, quantity in self.products.items():
            total_price += product.price * quantity
        return total_price

    def buy(self):
        copy_prod = self.products.copy()
        for product, quantity in copy_prod.items():
            if product.check_quantity(quantity):
                product.buy(self.products[product])
                self.remove_product(product)
            else:
                raise ValueError('Недостаточно продукта!')
