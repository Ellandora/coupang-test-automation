import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
      # 크롬 옵션 설정
      chrome_options = Options() # 쿠팡에서 자동화툴 사용 못하게 막아서 옵션 수정 필요함

      #proxy : 크롤링 중 ip가 차단되면 vpn을 통해서 ip 우회하는 시도
      # 1) User-Agent 변경 (사용자 접근 환경 강제 입력)
      chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0")

      # 2) SSL 인증서 에러 무시
      chrome_options.add_argument('--ignore-certificate-errors')
      chrome_options.add_argument('--ignore-ssl-errors')

      # 3-1) Selenium이 Automation된 브라우저임을 숨기는 설정 (JS가 인식하지 못하게 함)
      # - (disable-blink-features=AutomationControlled) 제거 : 크롬 88버전 이후로 추가된 설정
      # - excludeSwitches, useAutomationExtension : 크롬 35버전 이후로 추가된 설정
      chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
      chrome_options.add_experimental_option('useAutomationExtension', False)

      # 3-2) 혹은 다음의 방식으로 Blink 특징을 비활성화 할 수도 있음, AutomationControlled 자체가 표기되지 않게 한다
      chrome_options.add_argument('--disable-blink-features=AutomationControlled') 

      # 4) 디버그 로깅 줄이기 (선택)
      # chrome_options.add_argument('--log-level=3')

      # 5) Sandbox나 DevShm 사이즈 문제 우회 (리눅스 환경에서 발생 가능)
      chrome_options.add_argument('--no-sandbox')
      chrome_options.add_argument('--disable-dev-shm-usage')     

      # 드라이버 객체 생성 (header를 쿠팡으로 입력하여 get url로 접근한게 아닌 쿠팡에서 진입한 것으로 강제 입력)
      driver = webdriver.Chrome(service=Service(), options=chrome_options)
      driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://www.couppang.com/"}})

      # 대기 시간 설정
      driver.implicitly_wait(5)
      
      yield driver
      driver.quit()