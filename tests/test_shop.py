import pytest
from models.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture()
def cart():
    return Cart()


class TestProducts:

    def test_product_check_quantity(self, product):
        test_q = [0, 1, 500, 999, 1000]
        for i in test_q:
            assert product.check_quantity(i)

        assert product.check_quantity(1001) == False

        with pytest.raises(ValueError):
            product.check_quantity(-1)

    def test_product_buy(self, product):
        product.buy(501)
        assert product.quantity == 499

    def test_product_buy_more_than_available(self, product):
        with pytest.raises(ValueError):
            product.buy(1001)

        product.buy(500)
        with pytest.raises(ValueError):
            product.buy(501)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, 100)
        assert cart.products[product] == 100

        cart.add_product(product, 1000)
        assert cart.products[product] == 1100

        cart.add_product(product, 0)
        assert cart.products[product] == 1100

    def test_remove_product(self, product, cart):
        cart.add_product(product, 100)
        cart.remove_product(product, 50)
        assert cart.products[product] == 50

        cart.remove_product(product, 0)
        assert cart.products[product] == 50

        cart.remove_product(product, 50)
        assert product not in cart.products

    def test_remove_all_product(self, product, cart):
        cart.add_product(product, 50)
        cart.remove_product(product, 51)
        assert product not in cart.products

        cart.add_product(product, 100)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self, product, cart):
        cart.add_product(product, 1000)
        cart.clear()
        assert product not in cart.products

    def test_total_price(self, product, cart):
        cart.add_product(product, 1000)
        assert cart.get_total_price() == 100000

    def test_buy(self, product, cart):
        cart.add_product(product, 300)
        cart.buy()
        assert product.quantity == 700

        cart.add_product(product, 700)
        cart.buy()
        assert product.quantity == 0

        cart.add_product(product, 1)
        with pytest.raises(ValueError):
            cart.buy()
