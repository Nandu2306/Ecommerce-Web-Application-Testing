
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_cart():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        wait = WebDriverWait(driver, 15)

        wait.until(EC.url_contains("inventory.html"))

        print("Current URL:", driver.current_url)

        buttons = driver.find_elements(
            By.CSS_SELECTOR, "button.btn_inventory"
        )

        print("Number of product buttons:", len(buttons))

        assert len(buttons) > 0, "Products did not load"

        buttons[0].click()

        cart_badge = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "shopping_cart_badge")
            )
        )

        assert cart_badge.text == "1"

    finally:
        driver.quit()
