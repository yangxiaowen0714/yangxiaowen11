import  unittest
import  time
from selenium.webdriver.common.keys import Keys
from  testsuites.BaseTestCase import BaseTestCase
from  pageobject.discuz_homepage import HomePage
class DiscuzSearch1(BaseTestCase):
    def test_discuz_search(self):
        home_page = HomePage(self.driver)
        home_page.login("admin", "tt147258")
        home_page.login_button()
        name = home_page.setname()
        self.assertEquals(name, "admin", msg="登陆失败")
        home_page.click_moren()
        home_page.delete_email()
        home_page.glmk()
        self.driver.switch_to.window(self.driver.window_handles[1])
        home_page.luntan()
        self.driver.switch_to.frame(0)
        home_page.xinbankuai("wen1")
        self.driver.switch_to.window(self.driver.window_handles[1])
        home_page.admin_quit()
        home_page.quit_search()
        home_page.login("杨晓文", "tt147258" )
        home_page.login_button()
        home_page.newbankuai_email()
        home_page.sendemail("杨大大", "杨二二杨三三杨四四")
        home_page.back_email("杨三三杨五五杨六六")
        home_page.quit_search()
        name=home_page.tuich()
        self.assertEquals(name,"登录",msg="退出失败")
        # home_page.glmk()
        # home_page.wait_time()
        # self.driver.switch_to.window(self.driver.window_handles[1])
if __name__ == "__main__":
    unittest.main(verbosity=2)