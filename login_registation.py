import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://practice.automationtesting.in/")
my_acc = driver.find_element_by_css_selector("#menu-item-50 > a")
my_acc.click()
reg_email = driver.find_element(By.ID, "reg_email")
reg_email.send_keys("gasha@mail.com")
reg_pswd = driver.find_element(By.ID, "reg_password")
reg_pswd.send_keys("Pr-Ac-Ti-Ce")
wait = WebDriverWait(driver, 20)
register = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#customer_login  p.woocomerce-FormRow.form-row > input.woocommerce-Button.button"))
    )
register.click()
driver.quit()

driver.get("http://practice.automationtesting.in/")
my_acc = driver.find_element_by_css_selector("#menu-item-50 > a")
my_acc.click()
login = driver.find_element(By.ID, "username")
login.send_keys("gasha@mail.com")
pswd = driver.find_element(By.ID, "password")
pswd.send_keys("Pr-Ac-Ti-Ce")
wait = WebDriverWait(driver, 20)
log_btn = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button"))
)
log_btn.click()
#Проверка, что на странице есть Logout
logout = driver.find_element(By.LINK_TEXT, "Logout")
assert logout.text == 'Logout'
driver.quit()