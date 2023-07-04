# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import logging

def log():
    time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return ("LOG" + time)


URL_LOGIN = 'https://www.saucedemo.com/'
URL_INVENTORY = 'https://www.saucedemo.com/inventory.html'
URL_CART = 'https://www.saucedemo.com/cart.html'

# Start the browser and login with standard_user
def login (driver, user, password):
    print (f'{log()} Starting the browser...')
    print (f'{log()} Browser started successfully. Navigating to the demo page to login.')
    driver.get(URL_LOGIN)
    print ('Login with user: {},  password: {}'.format(user, password))
    driver.find_element(By.NAME, 'user-name').send_keys(user)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'login-button').click()
    assert URL_INVENTORY in driver.current_url
    print (f'{log()} Test Login Success')

def add_items(driver):
    print (f'{log()} Add all items to the cart')
    shopping_cart = []
    list_items = driver.find_elements(By.CLASS_NAME,"inventory_item")
    for i in list_items:
        item_name = i.find_element(By.CLASS_NAME,'inventory_item_name').text
        shopping_cart.append(item_name)
        i.find_element(By.CLASS_NAME,'btn_inventory').click()
        print(f'{log()} Add {} to cart'.format(item_name))
    cart_item = driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
    assert int(cart_item.text) == len(list_items)

    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert URL_CART in driver.current_url

    for i in driver.find_elements(By.CLASS_NAME,'inventory_item_name'):
        assert i.text in shopping_cart
    print(f'{log()} Finished testing adding items to the cart')


def remove_items(driver):
    print (f'{log()} Remove items from the cart')
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert URL_CART in driver.current_url
    print(f'{log()} Items in Cart: {}'.format(len(driver.find_elements(By.CLASS_NAME,'cart_item'))))
    for i in driver.find_elements(By.CLASS_NAME,'cart_item'):
        item_name = i.find_element(By.CLASS_NAME,'inventory_item_name').text
        i.find_element(By.CLASS_NAME,'cart_button').click()
        print(f'{log()} Removed {} from cart'.format(item_name))
    cart_items = len(driver.find_elements(By.CLASS_NAME,'cart_item'))
    assert cart_items == 0
    print(f'{log()} Finshed testing removing items from the cart')

def tests():
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    login(driver, "standard_user", "secret_sauce")
    add_items(driver)
    remove_items(driver)
    print(f'{log()} Tests Completed')

if __name__ == "__main__":
    tests()