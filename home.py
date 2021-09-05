import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
from selenium.webdriver.common.by import By
driver.implicitly_wait(5)

driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0,600);")
Ruby_book = driver.find_element(By.CSS_SELECTOR, "#text-22-sub_row_1-0-2-0-0  .woocommerce-LoopProduct-link")
Ruby_book.click()
Review = driver.find_element(By.CSS_SELECTOR, "#product-160 li.reviews_tab > a")
Review.click()
Star_5 = driver.find_element(By.CLASS_NAME, "star-5")
Star_5.click()
Review_text = driver.find_element(By.ID,"comment")
Review_text.send_keys("Nice Book!")
Name = driver.find_element(By.ID, "author")
Name.send_keys("Galina")
email = driver.find_element(By.ID, "email")
email.send_keys("email@email.com")
submit = driver.find_element(By.ID, "submit")
submit.click()

driver.quit()