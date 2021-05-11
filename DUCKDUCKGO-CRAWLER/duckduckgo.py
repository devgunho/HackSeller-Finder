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
search_box.send_keys("Game Hack")
search_box.submit()
elements = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located(
    (By.XPATH, "//div[@id='links']/div/div/div[2]")))
for ele in elements:
    print(ele.text)
    print("--------------")
# driver.quit()
