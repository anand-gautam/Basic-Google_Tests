from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options_chrome = Options()
options_chrome.add_argument("--start-maximized")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options_chrome)

google_url = "https://www.google.com"
search_items = "//*[@role='presentation']//*[@role='option']"


def google_test_for_partial_keyword_goo():
    driver.get(google_url)
    time.sleep(3)
    driver.find_element(By.NAME, 'q').send_keys('goo')
    time.sleep(2)
    items = driver.find_elements(By.XPATH, search_items)
    ls=[]
    for i in range(len(items)):
        search_item = driver.find_element(By.XPATH, '(' + search_items + ')' + '[' + str(i+1) + ']')
        ls.append(search_item.text)
    print(f"Search_list is : {ls}")

    for i in ls[:-1]:  #omitting last item as it is ''
        if 'google' not in i.lower():
            print(f"the search item {i} may not belong to google and is at list index position of {ls.index(i)}")

    driver.quit()


google_test_for_partial_keyword_goo()

