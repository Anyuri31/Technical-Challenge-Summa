from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_page import ProductPage


def test_user_can_open_store(driver):
    home = HomePage(driver)
    home.open()

    assert "STORE" in driver.title


def test_user_can_navigate_to_monitors_category(driver):
    home = HomePage(driver)
    home.open()
    home.select_monitors_category()
    assert home.are_products_visible()


def test_user_can_select_the_most_expensive_monitor(driver):
    home = HomePage(driver)
    home.open()
    home.select_monitors_category()
    highest_price = home.get_most_expensive_product_price()
    assert highest_price > 0

def test_user_can_add_most_expensive_monitor_to_cart(driver):
    home = HomePage(driver)
    home.open()
    home.select_monitors_category()

    highest_price = home.get_most_expensive_product_price()
    assert highest_price > 0

    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open_cart()

    assert cart.has_products(), "El carrito debería contener al menos un producto"

def test_user_can_buy_most_expensive_monitor(driver):
    home = HomePage(driver)
    home.open()
    home.select_monitors_category()

    highest_price = home.get_most_expensive_product_price()
    assert highest_price > 0, "No se encontró un monitor con precio válido"

    product = ProductPage(driver)
    product.add_to_cart()

    cart = CartPage(driver)
    cart.open_cart()
    assert cart.has_products(), "El carrito debería contener productos"

    assert cart.open_place_order_modal(), "El modal de compra no se abrió"

    cart.fill_purchase_form()
    assert cart.confirm_purchase(), "La compra no se completó exitosamente"