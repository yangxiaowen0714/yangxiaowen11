import  unittest
import  time
from selenium.webdriver.common.keys import Keys
from  testsuites.BaseTestCase import BaseTestCase
from  pageobject.discuz_homepage import HomePage
class DiscuzSearch2(BaseTestCase):
    def test_discuz_search(self):
        home_page = HomePage(self.driver)
        home_page.login("杨晓文", "tt147258")
        home_page.login_button()
        time.sleep(5)
        home_page.find_email("haotest")
        time.sleep(3)
        home_page.click_suosou()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        home_page.click_suosou_first()
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(5)
        name=home_page.suosou_bijiao()
        self.assertEqual( name,"haotest",msg="输出内容不匹配")
        home_page.quit_search()
if __name__ == "__main__":
    unittest.main(verbosity=2)