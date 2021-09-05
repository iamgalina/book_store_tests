import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

#блокировка рекламы
path_to_extension = r'C:\Users\Asus\AppData\Local\Google\Chrome\User Data\Profile 2\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.35.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension='+path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(10)
first_tab = driver.window_handles[0]
driver.switch_to.window(first_tab)

# #отображение страницы товара
# driver.get("http://practice.automationtesting.in/")
# #LOGIN
# my_acc = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_acc.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("gasha@mail.com")
# pswd = driver.find_element(By.ID, "password")
# pswd.send_keys("Pr-Ac-Ti-Ce")
# wait = WebDriverWait(driver, 20)
# log_btn = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button"))
# )
# log_btn.click()
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
#
# html5_book = wait.until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/ul/li[3]/a[1]'))
# )
# html5_book.click()
# book_name = driver.find_element(By.CSS_SELECTOR,'#product-181  h1')
# assert book_name.text == 'HTML5 Forms'
# driver.quit()

# #количество товаров в категории
# driver.get("http://practice.automationtesting.in/")
# #LOGIN
# my_acc = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_acc.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("gasha@mail.com")
# pswd = driver.find_element(By.ID, "password")
# pswd.send_keys("Pr-Ac-Ti-Ce")
# wait = WebDriverWait(driver, 20)
# log_btn = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button"))
# )
# log_btn.click()
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# html_btn = driver.find_element(By.CSS_SELECTOR, '#woocommerce_product_categories-2 .cat-item-19 > a')
# html_btn.click()
# assert len(driver.find_elements_by_class_name("product")) == 3
# driver.quit()

# #сортировка товаров
# driver.get("http://practice.automationtesting.in/")
# #LOGIN
# my_acc = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_acc.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("gasha@mail.com")
# pswd = driver.find_element(By.ID, "password")
# pswd.send_keys("Pr-Ac-Ti-Ce")
# wait = WebDriverWait(driver, 20)
# log_btn = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button"))
# )
# log_btn.click()
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
#
# sort_actual = driver.find_element(By.CSS_SELECTOR, '[selected="selected"]')
# assert sort_actual.get_attribute('value') == 'menu_order'
# sort = driver.find_element(By.CSS_SELECTOR, '#content  select')
# select = Select(sort)
# select.select_by_value('price-desc')
#
# sort_actual = driver.find_element(By.CSS_SELECTOR, '[selected="selected"]')
# assert sort_actual.get_attribute('value') == 'price-desc'
# driver.quit()

# #отображение, скидка товара
# driver.get("http://practice.automationtesting.in/")
# #LOGIN
# driver.get("http://practice.automationtesting.in/")
# my_acc = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_acc.click()
# login = driver.find_element(By.ID, "username")
# login.send_keys("gasha@mail.com")
# pswd = driver.find_element(By.ID, "password")
# pswd.send_keys("Pr-Ac-Ti-Ce")
# wait = WebDriverWait(driver, 20)
# log_btn = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > input.woocommerce-Button.button"))
# )
# log_btn.click()
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# andoid_book = driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[1]/a[1]')
# andoid_book.click()
# old_price = driver.find_element(By.CSS_SELECTOR,"#product-169 > .summary > div:nth-child(2) > p > del > span")
# assert old_price.text == "₹600.00"
# actual_price = driver.find_element(By.CSS_SELECTOR,"#product-169 > .summary > div:nth-child(2) > p > ins > span")
# assert actual_price.text == "₹450.00"
# android_picture = driver.find_element(By.CSS_SELECTOR, "#product-169 > div.images > a > img")
# android_picture.click()
# close_btn = wait.until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
#
# )
# close_btn.click()
#
# driver.quit()

##проверка цены в корзине
# driver.get('http://practice.automationtesting.in/')
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# HTML5_WAD_add_btn = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
# HTML5_WAD_add_btn.click()
# cart_items_not_null = WebDriverWait(driver,10).until_not(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'cartcontents'), '0 Items')
# )
# cart_items = driver.find_element(By.CLASS_NAME, 'cartcontents')
# assert cart_items.text == '1 Item'
# sum_amount = driver.find_element(By.CSS_SELECTOR, '#wpmenucartli span.amount')
# price_in_cart = sum_amount.text
# assert price_in_cart == '₹180.00'
# cart = driver.find_element(By.CSS_SELECTOR, '#wpmenucartli > a')
# cart.click()
# wait = WebDriverWait(driver, 5)
# wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'cart-subtotal'), price_in_cart)
# )
# #этот тест не прходит для России, т.к. есть комиссия
# # wait.until(
# #     EC.text_to_be_present_in_element((By.CLASS_NAME, 'order-total'), price_in_cart)
# # )
#
# driver.quit()

## работа в корзине
# driver.get('http://practice.automationtesting.in/')
# shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
# shop.click()
# driver.execute_script('window.scrollBy(0,300);')
# HTML5_WAD_add_btn = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
# HTML5_WAD_add_btn.click()
# time.sleep(3)
# JS_DSaA_add_btn = driver.find_element(By.CSS_SELECTOR, '[data-product_id="180"]')
# JS_DSaA_add_btn.click()
# time.sleep(3)
# cart = driver.find_element(By.CSS_SELECTOR, '#wpmenucartli > a')
# cart.click()
# time.sleep(5)
# delete_first_item = driver.find_element(By.CSS_SELECTOR, '#page-34 tbody>.cart_item:nth-child(1)>.product-remove>a')
# delete_first_item.click()
# undo_btn = driver.find_element(By.CSS_SELECTOR, '#page-34 .woocommerce-message > a')
# undo_btn.click()
# quantity_JS_book = driver.find_element(By.CSS_SELECTOR, '#page-34 tbody > tr:nth-child(1) >.product-quantity  input')
# quantity_JS_book.clear()
# quantity_JS_book.send_keys('3')
# update_btn = driver.find_element(By.NAME, 'update_cart')
# update_btn.click()
# assert quantity_JS_book.get_attribute('value') == '3'
# time.sleep(3)
# apply_coupon_btn = driver.find_element(By.NAME, 'apply_coupon')
# apply_coupon_btn.click()
# wait =WebDriverWait(driver,10)
# warning_msg = wait.until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, 'woocommerce'), 'Please enter a coupon code.')
# )
# if  warning_msg is not True:
#     print('No warning message')
#
# driver.quit()

#покупка товара
driver.get('http://practice.automationtesting.in/')
shop = driver.find_element(By.CSS_SELECTOR, "#menu-item-40 > a")
shop.click()
driver.execute_script('window.scrollBy(0,300);')
HTML5_WAD_add_btn = driver.find_element(By.CSS_SELECTOR, '[data-product_id="182"]')
HTML5_WAD_add_btn.click()
time.sleep(3)
cart = driver.find_element(By.CSS_SELECTOR, '#wpmenucartli > a')
cart.click()
wait = WebDriverWait(driver,5)
Checkout_btn = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button'))
)
Checkout_btn.click()
wait.until(
    EC.url_to_be('http://practice.automationtesting.in/checkout/')
)
first_name = driver.find_element(By.ID, 'billing_first_name')
first_name.send_keys('Galina')
last_name = driver.find_element(By.ID, 'billing_last_name')
last_name.send_keys('Fedorova')
email = driver.find_element(By.ID, 'billing_email')
email.send_keys('email@mail.com')
phone = driver.find_element(By.ID, 'billing_phone')
phone.send_keys('89991234567')
country_selector = driver.find_element(By.ID, 's2id_billing_country')
country_selector.click()
time.sleep(1)
country_enter = driver.find_element(By.ID, 's2id_autogen1_search')
country_enter.send_keys('Russia')
country_srch_result = driver.find_element(By.ID, 'select2-results-1')
country_srch_result.click()
adress = driver.find_element(By.ID, 'billing_address_1')
adress.send_keys('Nevskiy prospect')
city = driver.find_element(By.ID, 'billing_city')
city.send_keys('Saint-Petersburg')
state = driver.find_element(By.ID, 'billing_state')
state.send_keys('Saint-Petersburg')
postcode = driver.find_element(By.ID, 'billing_postcode')
postcode.send_keys('177888')
driver.execute_script('window.scrollBy(0,600);')
time.sleep(3)
check_payments = driver.find_element(By.ID,'payment_method_cheque')
check_payments.click()
place_order_btn = driver.find_element(By.ID, 'place_order')
place_order_btn.click()
thanks_text_check = wait.until(
    EC.text_to_be_present_in_element((By.ID, 'body'),'Thank you. Your order has been received.')
)
payment_method_check = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#page-35  tfoot > tr:nth-child(3) > td'), 'Check Payments')
)

driver.quit()
