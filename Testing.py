import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser_setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_checkout_process(browser_setup):
    driver = browser_setup
    url = "https://www.justwatches.com"
    driver.get(url)
    print("Opened website")

    # Search for a product
    search_input = driver.find_element(By.ID, "boost-sd__search-widget-init-input-1")
    search_input.send_keys("watch")
    search_input.submit()
    print("Searched for product")

    # Click on the product 
    product_link = driver.find_element(By.CSS_SELECTOR, ".boost-sd__product-image-img.boost-sd__product-image-img--second")
    product_link.click()
    print("Clicked on product")

    # Add the product to the cart
    buy_now_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-simpl-event-id='simpl-checkout-product-addToCart-v2']"))
        )
    buy_now_button.click()
    print("Added product to cart")

    # Proceed to checkout
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "cart__checkout"))
    )
    checkout_button.click()
    print("Clicked on checkout")

    # Find and click the login link
    email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "email"))
    )
    email.send_keys("xolorider433@gmail.com")
    first_name=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"TextField1"))
    )
    first_name.send_keys("xolo")
    last_name=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"TextField2"))
    )
    last_name.send_keys("rider")
    address = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID, "shipping-address1"))
    )
    address.send_keys("Malleshwaram")

    area=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"TextField4"))
    )
    area.send_keys("#42c, mahalakshmi layout, temple road")

    city=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"TextField4"))
    )
    city.send_keys("Bengaluru")

    pincode =WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"TextField5"))
    )
    pincode.send_keys("560069")

    phone_number = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.ID,"TextField6"))
    )
    phone_number.send_keys("8217746678")
    '''complete_order_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "QT4by"))
    )
    complete_order_button.click()
    print("Clicked Complete order button")



    # Verify successful checkout (add more assertions as necessary)
    assert "Checkout" in driver.title
    print("Verified successful checkout")'''

    # Close the browser
    driver.quit()
    print("Browser closed")
