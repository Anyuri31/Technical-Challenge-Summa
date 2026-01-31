from frontend.pages.home_page import HomePage


def test_user_can_open_store(driver):
    home = HomePage(driver)
    home.open()

    assert "STORE" in driver.title


def test_user_can_navigate_to_monitors_category(driver):
    home = HomePage(driver)
    home.open()
    home.select_monitors_category()
    assert home.are_products_visible()


def test_user_can_see_most_expensive_monitor_price(driver):
    home = HomePage(driver)
    home.open()
    home.select_monitors_category()
    highest_price = home.get_most_expensive_product_price()
    assert highest_price > 0
