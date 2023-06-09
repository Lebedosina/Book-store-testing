######### Задание 1
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
# driver.execute_script("window.scrollBy(0, 600);")
# read_more = driver.find_element_by_css_selector("ul.products li:nth-child(1) .ajax_add_to_cart")
# read_more.click()
# reviews = driver.find_element_by_css_selector(".reviews_tab>a")
# reviews.click()
# stars = driver.find_element_by_class_name("star-5")
# stars.click()
# review_field = driver.find_element_by_id("comment")
# review_field.send_keys("Nice book!")
# name = driver.find_element_by_id("author")
# name.send_keys("Elena")
# email = driver.find_element_by_id("email")
# email.send_keys("Nusya91@inbox.ru")
# submit_btn = driver.find_element_by_id("submit")
# submit_btn.click()
# driver.quit()