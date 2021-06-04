from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Locators
import pandas as pd

class PL_DATA:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get(Locators.URL)
    
    def close_ads(self, locator):
        try:
            adverts = WebDriverWait(self.driver, Locators.wait_5).until(EC.visibility_of_element_located(locator))
        except exceptions.TimeoutException as e:
            pass
        else:
            adverts.click()
    
    def click(self, locator):
        WebDriverWait(self.driver, Locators.wait_5).until(EC.visibility_of_element_located(locator)).click()
    
    def click_script(self, locator):
        el = WebDriverWait(self.driver, Locators.wait_5).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", el)
        
    def is_visible(self, locator):
        try:
            el = WebDriverWait(self.driver, Locators.wait_10).until(EC.visibility_of_element_located(locator))
            return el
        except exceptions.TimeoutException as e:
            print(e, 'Table content not visible')
            return None
    
    def is_present_with_text(self, locator, text):
        try:
            el = WebDriverWait(self.driver, Locators.wait_10).until(EC.text_to_be_present_in_element(locator, text))
            return el
        except exceptions.TimeoutException as e:
            print(e, 'Text presence not detected')
            return None
    
    def fetch_pl_table_data(self, table_xpath, gw):
        list_ = self.driver.find_elements_by_xpath(table_xpath)
        temp_list = [x.text for x in list_]
        if temp_list == []:
            print(f'list_: {list_}, temp_list: {temp_list}')
        else:
            if temp_list[0] == '':
                teams = [temp_list[i] for i in range(len(temp_list)) if i%2!=0]
            else:
                teams = [temp_list[i] for i in range(len(temp_list)) if i%2==0]
            
        temp = pd.DataFrame([team.split('\n')[:2][-1::-1]+team.split('\n')[2].split(' ')[4:6]+[team.split('\n')[2].split(' ')[-1]] for team in teams], 
                            columns=['Teams', f'Position-{gw}', f'Goals_For-{gw}', f'Goal_Against-{gw}', f'Points-{gw}'])
        return temp
    
    def close(self):
        self.driver.quit()