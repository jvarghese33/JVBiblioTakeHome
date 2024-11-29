# Jonathan Varghese 
# Bibliocommons take home assignment

# Import modules from Selenium for browser automation and import Faker for generating test data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from faker import Faker

# Create an instance of Faker to generate random user data for form inputs
fake = Faker()

# Using Faker, generate random first name, last name, and postal code
first_name = fake.first_name()
last_name = fake.last_name()
postal_code = fake.postcode()

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open browser, then maximize the website
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Find the username field via ID, then input the user name into the field
username_field = driver.find_element(By.ID, "user-name")
username_field.send_keys("standard_user")

# Find the password field via ID, then input the password into the field
password_field = driver.find_element(By.ID, "password") 
password_field.send_keys("secret_sauce")

# Find the login button via the ID, then select said button to log in
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Find "add to card" button for the 3rd item by the CSS selector, which in this case is the sauce lab bolt t shirt, then select add to cart
add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]')
add_to_cart_button.click()

# Find the shopping cart button, then select the cart button
cart_button = driver.find_element(By.ID, "shopping_cart_container")
cart_button.click()

# Find the "checkout" button by ID, then select the button
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()

# Find the first name field by the XPath, then select the field to initialize it, then using the faker info above input the "first_name"
first_name_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[1]/input")
first_name_field.click
first_name_field.send_keys(first_name)

# Find the last name field by the XPath, then select the field to initialize it, then using the faker info above input the "last_name"
last_name_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[2]/input")
last_name_field.click
last_name_field.send_keys(last_name)

# Find the postal code field by the XPath, then select the field to initialize it, then using the faker info above input the "postal_code"
postal_code_field = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[3]/input")
postal_code_field.click
postal_code_field.send_keys(postal_code)

# Find the "continue" button by the ID, then select it
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Find the "finish" button by the ID to complete the purchase, then select the button
finish_button = driver.find_element(By.ID, "finish")
finish_button.click()

# Find the checkout container found by the ID, check for the success text below and assert that the text you should see appears. Add a line to send an error message if not found
successful_message = driver.find_element(By.ID, "checkout_complete_container")
assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in successful_message.text, "Success message not found!"