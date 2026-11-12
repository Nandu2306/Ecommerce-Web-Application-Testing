from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
def test_sort_products_low_to_high():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        dropdown = driver.find_element(
            By.CLASS_NAME, "product_sort_container"
        )

        Select(dropdown).select_by_value("lohi")

        prices = driver.find_elements(
            By.CLASS_NAME, "inventory_item_price"
        )

        price_values = [
            float(price.text.replace("$", "")) for price in prices
        ]

        assert price_values == sorted(price_values)

    finally:
        driver.quit()
