# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import datetime

login_url = 'https://www.saucedemo.com/'
inventory_url = 'https://www.saucedemo.com/inventory.html'
cart_url = 'https://www.saucedemo.com/cart.html'

def log():
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return ("LOG " + time)

def startup():
    print(f'{log()} Starting the browser...')
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    print (f'{log()} Browser started successfully. Navigating to the demo page to login.')
    return driver

# Start the browser and login with standard_user
def login (driver, user, password):
    driver.get(login_url)
    driver.find_element(By.ID, 'user-name').send_keys(user)
    driver.find_element(By.ID, 'password').send_keys(password)
    driver.find_element(By.ID,'login-button').click()
    assert inventory_url in driver.current_url, "Error, login failed!"
    print(f'{log()} User {user} logged in successfully')

def add_products(driver):
    print(f'{log()} Starting to add products to the cart')
    
    cart_items = []
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')

    for product in products:
        product_item = product.find_element(By.CLASS_NAME, 'inventory_item_name').text
        cart_items.append(product_item)
        product.find_element(By.CLASS_NAME, 'btn_inventory').click()
        print(f'{log()} {product_item} added to the cart')

    cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    assert int(cart.text) == len(products), 'ERROR: The cart count does not match the number of products added'

    for item in driver.find_elements(By.CLASS_NAME, 'inventory_item_name'):
        assert item.text in cart_items, 'ERROR: All products are not added to the cart'

    print(f'{log()} All products added to the cart successfully')

def delete_products(driver):
    print(f'{log()} Navigating to cart page')
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert cart_url in driver.current_url

    cart_items = driver.find_elements(By.CLASS_NAME,'cart_item')
    cart_items_count = len(cart_items)
    print(f'{log()} Number of items in the cart {cart_items_count}')

    for product in cart_items:
        product_item = product.find_element(By.CLASS_NAME,'inventory_item_name').text
        product.find_element(By.CLASS_NAME,'cart_button').click()
        print(f'{log()} {product_item} removed from the cart')

    cart_items_count = len(driver.find_elements(By.CLASS_NAME,'cart_item'))
    assert cart_items_count == 0,'ERROR: Not all products were removed from the cart'

    print(f'{log()} All products removed from the cart successfully')

if __name__ == "__main__":
    driver_active = startup()
    login(driver_active, 'standard_user', 'secret_sauce')
    add_products(driver_active)
    delete_products(driver_active)