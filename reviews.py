from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/maps")

next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
next_button.click()
email = "scraping17@gmail.com"
password = "123qwe!@#QWE"

next_button2 = driver.find_element(By.CLASS_NAME, "whsOnd")
next_button2.send_keys(email)
next_button2.send_keys(Keys.RETURN)
time.sleep(4)

next_button3 = driver.find_element(By.CLASS_NAME, "whsOnd")
next_button3.send_keys(password)
next_button3.send_keys(Keys.RETURN)
time.sleep(4)

search_box = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, "searchboxinput")))
search_box.send_keys("Pizza na wypasie")
search_box.send_keys(Keys.RETURN)
time.sleep(7)

next_button4 = driver.find_elements(By.CLASS_NAME, "hh2c6")
next_button4[1].click()
time.sleep(6)

review_element = driver.find_element(By.CLASS_NAME, "m6QErb")
review_elements = review_element.find_elements(By.CLASS_NAME, "jftiEf")

for review in review_elements:
    review_el = review.find_element(By.CLASS_NAME, 'd4r55')
    review_text = review_el.find_element(By.TAG_NAME, 'span')
    print(review_text.text)

print('s')
search_box.submit()
time.sleep(400)

driver.quit()
