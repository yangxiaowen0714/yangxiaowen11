import  unittest
from selenium import webdriver
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        print("测试开始")
        self.browserengine = BrowserEngine()
        self.driver=self.browserengine.open_browser()
    def tearDown(self):
        self.browserengine.quit_browser()
        print("测试结束")
