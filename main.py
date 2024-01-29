from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://www.jumia.com.ng/oraimo-20000mah-power-bank-opb-p208dn-127135392.html")
#
# price = driver.find_element(By.CLASS_NAME, value="-prxs")
#
# comment = driver.find_elements(By.CSS_SELECTOR, value='._bet h3')
# comment_para = driver.find_elements(By.CSS_SELECTOR, value="._bet p")
#
# print(price.text)
# for c in comment:
#     print(c.text)
#
#
# for p in comment_para:
#     print(p.text)
#
#
# driver.quit()

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# #article_count.click()
#
# login_link = driver.find_element(By.LINK_TEXT, value="Log in")
# #login_link.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# driver.get("https://secure-retreat-92358.herokuapp.com/")
#
# fname = driver.find_element(By.NAME, "fName")
# fname.send_keys("Michael")
#
# lname = driver.find_element(By.NAME, "lName")
# lname.send_keys("Charles")
#
# email = driver.find_element(By.NAME, "email")
# email.send_keys("myemail@example.com")
# email.send_keys(Keys.ENTER)

# button = drive/r.find_element(By.CLASS_NAME, "btn-block")
# button.click()

driver.get("https://www.youtube.com/")

search_bar = driver.find_element(By.NAME, "search_query")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.RETURN)

# button = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]')
# button.click()

#driver.quit()