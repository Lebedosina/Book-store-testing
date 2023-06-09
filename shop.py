############## Задание 1
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'/Users/elenalebedeva/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/5.6.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("https://practice.automationtesting.in/")
#
# my_account_menu = driver.find_element_by_link_text("My Account")
# my_account_menu.click()
# username = driver.find_element_by_id("username")
# username.send_keys("Nusya91@inbox.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("A1234sdf%")
# login_btn = driver.find_element_by_css_selector(".form-row :nth-child(3)")
# login_btn.click()
# shop_tab = driver.find_element_by_link_text("Shop")
# shop_tab.click()
# open_book = driver.find_element_by_css_selector("ul.products li:nth-child(3) .ajax_add_to_cart")
# open_book.click()
# html_5_forms = driver.find_element_by_css_selector(".entry-title")
# html_5_forms_text = html_5_forms.text
# assert html_5_forms_text == "HTML5 Forms"
# driver.quit()

################### Задание 2
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# path_to_extension = r'/Users/elenalebedeva/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/5.6.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("https://practice.automationtesting.in/")
#
# my_account_menu = driver.find_element_by_link_text("My Account")
# my_account_menu.click()
# username = driver.find_element_by_id("username")
# username.send_keys("Nusya91@inbox.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("A1234sdf%")
# login_btn = driver.find_element_by_css_selector(".form-row :nth-child(3)")
# login_btn.click()
# shop_tab = driver.find_element_by_link_text("Shop")
# shop_tab.click()
# html = driver.find_element_by_css_selector(".cat-item-19 >a")
# html.click()
# wait = WebDriverWait(driver, 3)
# product_elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul .product")))
# assert len(product_elements) == 3
# driver.quit()

############## Задание 3
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.select import Select
#
# path_to_extension = r'/Users/elenalebedeva/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/5.6.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("https://practice.automationtesting.in/")
#
# my_account_menu = driver.find_element_by_link_text("My Account")
# my_account_menu.click()
# username = driver.find_element_by_id("username")
# username.send_keys("Nusya91@inbox.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("A1234sdf%")
# login_btn = driver.find_element_by_css_selector(".form-row :nth-child(3)")
# login_btn.click()
# shop_tab = driver.find_element_by_link_text("Shop")
# shop_tab.click()
# select_element = driver.find_element_by_css_selector(".orderby")
# selected_option = select_element.get_attribute("value")
# assert selected_option == "menu_order"
# price_sort_selector = driver.find_element_by_css_selector(".orderby")
# price_sort_select = Select(price_sort_selector)
# price_sort_select.select_by_value("price-desc")
# main_sort_selector = driver.find_element_by_css_selector(".orderby")
# main_sort_select = Select(main_sort_selector)
# sort_selector = driver.find_element_by_css_selector(".orderby")
# selected_option = sort_selector.get_attribute("value")
# assert selected_option == "price-desc"
# driver.quit()

################### Задание 4
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
#
# path_to_extension = r'/Users/elenalebedeva/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/5.6.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("https://practice.automationtesting.in/")
#
# my_account_menu = driver.find_element_by_link_text("My Account")
# my_account_menu.click()
# username = driver.find_element_by_id("username")
# username.send_keys("Nusya91@inbox.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("A1234sdf%")
# login_btn = driver.find_element_by_css_selector(".form-row :nth-child(3)")
# login_btn.click()
# shop_tab = driver.find_element_by_link_text("Shop")
# shop_tab.click()
# android = driver.find_element_by_css_selector('[title="Android Quick Start Guide"]')
# android.click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver,10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver,10).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
# driver.quit()
