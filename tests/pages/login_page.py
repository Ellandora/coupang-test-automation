class LoginPage:
      def __init__(self, driver):
          self.driver = driver

      def open (self):
          self.driver.get('http://www.coupang.com')

      def input_password_and_email(self):
           pass #input password and email

      def click_login_button(self):
           pass #click login button
