########## Задание 1
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
# reg_email = driver.find_element_by_id("reg_email")
# reg_email.send_keys("Nusya91@inbox.ru")
# reg_password = driver.find_element_by_id("reg_password")
# reg_password.send_keys("A1234sdf%")
# register_btn = driver.find_element_by_class_name("register")
# register_btn.click()
#driver.quit()

############# Задание 2

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
# logout_elements = driver.find_element_by_link_text("Logout")
# if logout_elements:
#     print("Элемент 'Logout' найден на странице")
# else:
#     print("Элемент 'Logout' не найден на странице")
# driver.quit()

