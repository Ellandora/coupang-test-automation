# 테스트 실행 시 환경 설정이나 동적 경로 추가 등 다양한 상황에서 사용됩니다.
import os # 파일 경로나 환경 변수 관리 등 운영 체제와의 상호작용을 지원
import sys # Python 인터프리터 관련 작업 지원 
# 코드 실행 흐름에서 특정 시간동안 지연을 줄 때 사용
import time #
import pytest

# 특정 요소가 나타날 때 까지 기다리는 데 사용하는 도구 (요소가 DOM에서 로드되거나 특정 조건이 충족되길 기다림)
from slelnium.webdriver.support.ui import WebDriverWait as ws 
# WebDriverWait와 결합하여 요소나 상태를 기다릴 때 자주 사용하며, 다양한 조건을 정의하는 모듈
from selenium.webdriver.support import expected_conditions as EC
# Chrome 브라우저를 조작하기 위한 WebDriver 클래스
from selenium.webdriver.chrome.webdriver import WebDriver # noQA
# DOM에서 특정 요소를 찾을 수 없을 때를 위한 예외처리 및 설정 시간 초과 시 발생하는 예외 처리
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from tests.pages.main_page import MainPage
#HTML 요소를 찾기 위한 다양한 메서드를 제공
from selenium.webdriver.common.by import By
# urllib.parse를 사용하여 URL에서 쿼리 파라미터를 추출하거나 동적으로 URL을 생성할 수 있음
from urllib import parse

# 단위테스트
class TestMainPage:
    @pytest.mark.skip(reason="아직 테스트 케이스 작동 X")
    # self는 Python에서 클래스의 인스턴스(instance)를 참조하는 키워드, 
    # self는 클래스의 메서드가 호출될 때 현재 객체의 상태와 속성에 접근하거나 수정할 수 있도록 도움
    def test_open_main_page(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10) # 최대 10초 까지 기다리기
            wait.until(EC.url_contains("coupang.com")) # URL 검증
            assert "coupang.com" in driver.current_url # 검증

        except NoSuchElementException as e:
            assert False

    # @pytest.mark.skip(reason="아직 테스트 케이스 작동 X")
    def test_click_link_text(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10) 
            wait.until(EC.url_contains("coupang.com")) # URL 검증
            assert "coupang.com" in driver.current_url # 검증

            main_page.click_by_LINK_TEXT("로그인")

            assert "login" in driver.current_url
            driver.save_screenshot("메인페이지-로그인-성공.jpg")

            time.sleep(2)
            driver.back()
            wait.until(EC.url_contains("coupang.com")) # URL 검증
            assert "coupang.com" in driver.current_url # 검증

            # 비로그인 테스트라 마이쿠팡 클릭 시 로그인 페이지로 이동해야 함
            time.sleep(2)
            main_page.click_by_LINK_TEXT("마이쿠팡")
            assert "login" in driver.current_url
            driver.save_screenshot("메인페이지-장바구니-성공.jpg")

        except NoSuchElementException as e:
            driver.save_screenshot("메인페이지-링크텍스트-실패-노서치.jpg")
            assert False

        except TimeoutException as e:
            driver.save_screenshot("메인페이지-링크텍스트-실패-타임에러.jpg")
            assert False

    @pytest.mark.skip(reason="아직 테스트 케이스 작동 X")
    def test_search_items(self, driver: WebDriver):
        try:
            ITEMS_XPATH = "//form//ul/li"
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)
            
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            
            time.sleep(2) # 봇인 것을 들키지 않기 위해 대기
            
            main_page.search_items("갤럭시S25")
            
            ws(driver, 10).until(EC.presence_of_element_located((By.XPATH, ITEMS_XPATH)))
            
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)
            item_name = parse.quot("갤럭시S25")
            
            assert len(items) > 0
            assert item_name in driver.current_url
            
            driver.save_screenshot("메인페이지-검색-성공.jpg")
        except NoSuchElementException as e:
            driver.save_screenshot("메인페이지-검색-실패-노서치.jpg")
        assert False

        except TimeoutException as e:
            driver.save_screenshot("메인페이지-검색-실패-타임에러.jpg")
        assert False