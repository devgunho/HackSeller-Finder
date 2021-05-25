import csv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_exe_path = os.path.dirname(os.path.abspath(__file__)) + \
    "\chromedriver\chromedriver.exe"
print(driver_exe_path)

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=driver_exe_path)
driver.get('https://duckduckgo.com/')
search_box = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.NAME, "q")))
search_box.send_keys("Maple Story Game Hack")
search_box.submit()

# More Results
show_btn = "rld-"
show_btn_counter = 1
while(1):
    now_btn = show_btn+str(show_btn_counter)
    try:
        driver.find_element_by_id(now_btn).click()
        print("Find Btn.", now_btn)
        show_btn_counter += 1
    except:
        break


# Show result text
result_urls = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
    (By.XPATH, "//div[@id='links']/div/div/div[1]/div/a")))
result_documents = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
    (By.XPATH, "//div[@id='links']/div/div/div[2]")))

f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow(["num", "url", "text"])
text_cnt = 0
for result_url, result_text in zip(result_urls, result_documents):
    text_cnt += 1
    print("--------------", text_cnt,
          "--------------")
    print(result_url.get_attribute('href'))
    print(result_text.text)
    wr.writerow([text_cnt, result_url.get_attribute('href'), result_text.text])
f.close

driver.quit()
