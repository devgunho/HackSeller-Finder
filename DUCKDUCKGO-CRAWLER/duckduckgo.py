import csv
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

# Load Keywords
df_games = pd.read_csv('input-games.csv')
# print(df_games)
df_keywords = pd.read_csv('input-keywords.csv')
# print(df_keywords)

for index, row in df_games.iterrows():
    for key_index, key_row in df_keywords.iterrows():
        query = row['GAMES']+' '+key_row['KEY']
        print(query)

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
        search_box.send_keys(query)
        search_box.submit()

        # More Results
        show_btn = "rld-"
        show_btn_counter = 1
        while(1):
            now_btn = show_btn+str(show_btn_counter)
            try:
                driver.implicitly_wait(5)
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

        output_filename = query+'.csv'
        f = open(output_filename, 'w', encoding='utf-8', newline='')
        wr = csv.writer(f)
        wr.writerow(["num", "url", "text"])
        text_cnt = 0
        for result_url, result_text in zip(result_urls, result_documents):
            text_cnt += 1
            print("--------------", text_cnt,
                  "--------------")
            print(result_url.get_attribute('href'))
            print(result_text.text)
            wr.writerow(
                [text_cnt, result_url.get_attribute('href'), result_text.text])
        # f.close

        # driver.quit()
