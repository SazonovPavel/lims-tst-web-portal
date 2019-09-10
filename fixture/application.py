from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.first_application import FirstApplicationHelper
from fixture.second_application import SecondApplicationHelper
from fixture.third_application import ThirdApplicationHelper

class Application:

    def __init__(self):
        # self.wd = WebDriver(executable_path='tools//chromedriver.exe')
        self.wd = WebDriver()
        self.wd.maximize_window()
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.first_application = FirstApplicationHelper(self)
        self.second_application = SecondApplicationHelper(self)
        self.third_application = ThirdApplicationHelper(self)

    def open_home_page(self):
        wd = self.wd


# Prod
#        wd.get('http://lims-web-portal.bitsoft.group/')

# Stage portal
#        wd.get('http://stage-diklz-portal.bitsoft.com.ua')

# Test portal
        wd.get('http://test-diklz-portal.bitsoft.com.ua/')

# Dev portal
#        wd.get('http://dev-diklz-portal.bitsoft.com.ua')

    def destroy(self):
        self.wd.quit()
