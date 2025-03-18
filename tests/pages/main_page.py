from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class MainPage:
    URL = "https://www.coupang.com"
    SEARCH_INPUT_ID = "headerSearchKeyword" # 검색 입력 필드의 HTML ID 값

#__init__은 클래스 인스턴스가 생성될 때 필요한 데이터를 초기화 하거나 준비 작업을 수행함
    def __init__(self, driver: WebDriver): # WebDriver 객체를 받아 클래스 인스턴스의 driver로 저장
        self.driver = driver

    def open(self):
        self.driver.get(self.URL) # self.url에 지정된 페이지 열기

    def search_items(self, item_name: str): 
        search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER)

    def click_by_LINK_TEXT(self, link_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, link_text)
        login_button.click()

# https://login.coupang.com/login/memberJoinFrm.pang