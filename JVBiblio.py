from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker

fake = Faker()

first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postcode()

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

password_field = driver.find_element(By.ID, "password") 
password_field.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
add_to_cart_button.click()


cart_button = driver.find_element(By.ID, "shopping_cart_container")
cart_button.click()

checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

first_name_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")
first_name_field.click
first_name_field.send_keys(first_name)

last_name_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")
last_name_field.click
last_name_field.send_keys(last_name)

postal_code_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input")
postal_code_field.click
postal_code_field.send_keys(postal_code)

continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

finish_button = driver.find_element(By.ID, "finish")
finish_button.click()

successful_message = driver.find_element(By.ID, "checkout_complete_container")
if "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in successful_message.text:
        print("successful text appears!")
else:
        print("successful text does not appear.")