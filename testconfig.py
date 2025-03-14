import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
      # 크롬 옵션 설정
      chrome_options = Options() # 쿠팡에서 자동화툴 사용 못하게 막아서 옵션 수정 필요함

      #proxy : 크롤링 중 ip가 차단되면 vpn을 통해서 ip 우회하는 시도
      # 1) User-Agent 변경
      chrome_options.add_argument("user-agent=Mozilla")