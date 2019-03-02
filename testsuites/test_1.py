import  unittest
from framework.logger import Logger
from  testsuites.BaseTestCase import BaseTestCase
from  pageobject.discuz_homepage import HomePage
class DiscuzSearch(BaseTestCase):
    def test_discuz_search(self):
        home_page = HomePage(self.driver)
        home_page.login("admin","tt147258")
        home_page.login_button()
        name=home_page.setname()
        self.assertEquals(name,"admin",msg="登陆失败")
        home_page.click_moren()
        home_page.sendemail("杨大大","杨二二")
        home_page.back_email("杨三三")
        home_page.quit_search()
if __name__ == "__main__":
    unittest.main(verbosity=2)