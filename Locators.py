from selenium.webdriver.common.by import By

URL = 'https://www.premierleague.com/tables?co=1&se=363&ha=-1'

# Locators:
AD_CLOSE_BTN = (By.XPATH, '//*[@id="advertClose"]')
POP_CLOSE = (By.XPATH, '/html/body/section/div/div')
DRPDN_EL = (By.XPATH, '//*[@class="tabbedContent"]//*[@data-dropdown-block="gameweekNumbers"]')
TABLE_CONTENT = (By.XPATH, '//*[@class="tabbedContent"]//*[@data-ui-tab="First Team"]//tbody//tr')

# Wait seconds:
wait_5 = 5
wait_10 = 10