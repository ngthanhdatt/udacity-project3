# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

URL_LOGIN = 'https://www.saucedemo.com/'
URL_INVENTORY = 'https://www.saucedemo.com/inventory.html'
URL_CART = 'https://www.saucedemo.com/cart.html'

# Start the browser and login with standard_user
def login (driver, user, password):
    print ('Starting the browser...')
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get(URL_LOGIN)
    driver.find_element(By.NAME, 'user-name').send_keys(user)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.NAME, 'login-button').click()
    assert URL_INVENTORY in driver.current_url
    print ('Test Login Success')

def add_items(driver):
    print ('Add all items to the cart')
    shopping_cart = []
    list_items = driver.find_elements(By.CLASS_NAME,"inventory_item")
    for i in list_items:
        item_name = i.find_element(By.CLASS_NAME,'inventory_item_name').text
        shopping_cart.append(item_name)
        i.find_element(By.CLASS_NAME,'btn_inventory').click()
    cart_item = driver.find_element(By.CLASS_NAME,'shopping_cart_badge')
    assert int(cart_item.text) == len(list_items)

    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert URL_CART in driver.current_url

    for i in driver.find_elements(By.CLASS_NAME,'inventory_item_name'):
        assert i.text in shopping_cart
    print('Finished testing adding items to the cart')


def remove_items(driver):
    print ('Remove items from the cart')
    driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
    assert URL_CART in driver.current_url

    for i in driver.find_elements(By.CLASS_NAME,'cart_item'):
        item_name = i.find_element(By.CLASS_NAME,'inventory_item_name').text
        i.find_element(By.CLASS_NAME,'cart_button').click()
    cart_items = len(driver.find_elements(By.CLASS_NAME,'cart_item'))
    assert cart_items == 0
    print('Finshed testing removing items from the cart')

def tests():
    # options = ChromeOptions()
    # options.add_argument("--headless")
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome()
    login(driver, "standard_user", "secret_sauce")
    add_items(driver)
    remove_items(driver)
    print("Tests Completed")

if __name__ == "__main__":
    tests()