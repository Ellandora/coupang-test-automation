# test 폴더의 pages 폴더의 loginpage.py 파일을 import 한다.
# loginpage.py 파일의 LoginPage 클래스를 사용한다.
from tests.pages.loginpage import LoginPage 

class TestLoginPage:
      def test_login_url(self, driver):
          loginpage = LoginPage(driver)
          loginpage.open()
          current_url = driver.current_url
          assert "coupang.com" in current_url