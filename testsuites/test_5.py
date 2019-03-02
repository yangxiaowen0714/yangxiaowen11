import  unittest
import  time
from selenium.webdriver.common.keys import Keys
from  testsuites.BaseTestCase import BaseTestCase
from  pageobject.discuz_homepage import HomePage
class DiscuzSearch3(BaseTestCase):
    def test_discuz_search(self):
        home_page = HomePage(self.driver)
        home_page.login("杨晓文", "tt147258")
        home_page.login_button()
        home_page.click_moren()
        home_page.click_fatie()
        home_page.click_toupiao()
        home_page.hand_title("杨晓文帅不帅")
        home_page.title_shuru("帅","很帅","非常帅")
        home_page.tp_names()
        name = home_page.toupiao()
        self.assertEquals(name, "提交", msg="投票失败")
        home_page.quit_search()
if __name__ == "__main__":
    unittest.main(verbosity=2)