from selenium import webdriver
from selenium.webdriver.common.by import By


def test_valid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert "inventory.html" in driver.current_url

    finally:
        driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("wrong123")
        driver.find_element(By.ID, "login-button").click()

        error = driver.find_element(
            By.CSS_SELECTOR, "[data-test='error']"
        )

        assert error.is_displayed()

    finally:
        driver.quit()