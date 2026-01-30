from frontend.pages.home_page import HomePage


def test_user_can_open_store(driver):
    home = HomePage(driver)
    home.open()

    assert "STORE" in driver.title
