from framework.base import BasePage
from  selenium.webdriver.common.by import By
import time
from  selenium import  webdriver
class HomePage(BasePage):
    #定位器,通过元素属性定位元素对象
    home_page_input_search_loc = (By.NAME, "username")#用户名
    home_page_password_search_loc=(By.NAME,"password")#密码
    home_page_name_search_loc=(By.XPATH,'//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em')
    home_page_mokuai_search_loc=(By.CSS_SELECTOR,".fl_icn>a")#默认板块
    home_page_subject_search_loc=(By.NAME,"subject")#发送人
    home_page_subject1_search_loc=(By.ID,"fastpostmessage")#发送内容
    home_page_send_search_loc=(By.NAME,"topicsubmit")#发送按钮
    home_page_back_search_loc=(By.NAME,"message")#回复框
    home_page_huifu_search_loc=(By.NAME,"replysubmit")#回复按钮
    home_page_quit_search_loc=(By.LINK_TEXT,"退出")
    home_name =(By.CSS_SELECTOR,".vwmy a")
    home_page_glmk_search_loc = (By.LINK_TEXT,"管理中心")#点击管理模块
    home_page_admin_password_search_loc=(By.NAME,"admin_password") #登陆管理中心密码
    home_page_tijiao_search_loc=(By.NAME,"submit") #提交按钮
    home_page_email_fiest_search_loc=(By.NAME,"moderate[]")#邮件第一个
    home_page_delete_search_loc=  (By.LINK_TEXT,"删除")   #邮件删除按钮
    home_page_delete_name_search_loc=(By.NAME,"modsubmit")#删除的确认功能
    home_page_luntan_search_loc=(By.ID,"header_forum")  #管理中心下论坛
    home_page_dianjixin_search_loc = (By.LINK_TEXT, "添加新版块")  # 点击添加新板块
    # home_page_dianjixin1_search_loc=(By.CLASS_NAME,"addtr")
    home_page_xbkmc_search_loc=(By.NAME,"name[37]")#新板块名称
    home_page_tijiaobuttun_search_loc=(By.ID,"submit_editsubmit")#提交按钮
    home_page_admin_quit_search_loc=(By.LINK_TEXT,"退出")#管理员退出
    home_page_email_new_search_loc=(By.LINK_TEXT,"yang")#点击新板块
    home_page_find_email_search_loc=(By.ID,"scbar_txt")   #搜索框
    home_page_sousuo_search_loc=(By.NAME,"searchsubmit")#点击搜索
    home_page_suosou_first_search_loc=(By.CSS_SELECTOR,".xs3 strong font")#默认搜索第一个
    get_sousuo_id=(By.CSS_SELECTOR,"#thread_subject")
    home_page_clike_send_email_search_loc =(By.ID,"newspecial")#点击发贴
    home_page_clike_send_toupian_search_loc=(By.XPATH,'// *[ @ id = "ct"] / div / ul / li[2] / a')#点击发起投票
    titles=(By.NAME,"subject")
    titles1=(By.CSS_SELECTOR,"#pollm_c_1 :first-of-type input")
    titles2=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(2) > input")
    titles3=(By.CSS_SELECTOR,"#pollm_c_1 > p:nth-child(3) > input")
    button_toupiao=(By.ID,"postsubmit")#  投票按钮
    def login_button(self):
        self.click(*self.home_page_name_search_loc)
    def wait_time(self):
        time.sleep(3)
    def login(self,username,password):
        #登陆管理员
        self.sendkeys(username,*self.home_page_input_search_loc)
        self.sendkeys(password,*self.home_page_password_search_loc)
    def setname(self):
        w=self.find_element(*self.home_name).text
        return w
    def click_moren(self):
        self.click(*self.home_page_mokuai_search_loc)
    def sendemail(self,admins,texts):
        #点击默认板块,发送邮件
        self.sendkeys(admins,*self.home_page_subject_search_loc)
        self.sendkeys(texts, *self.home_page_subject1_search_loc)
        self.click(*self.home_page_send_search_loc)
    def back_email(self,huifu):
        # 点击回复,输入内容
        self.sendkeys(huifu, *self.home_page_back_search_loc)
        self.click(*self.home_page_huifu_search_loc)
    def quit_search(self):
        #点击退出
        self.click(*self.home_page_quit_search_loc)
    def delete_email(self):
        self.click(*self.home_page_email_fiest_search_loc)#点击第一个的小沟
        self.click(*self.home_page_delete_search_loc)#点击删除按钮
        self.click(*self.home_page_delete_name_search_loc)#点击确认删除
    def glmk(self):
        #管理中心的点击
        self.click(*self.home_page_glmk_search_loc)
    def luntan(self):
        #点击论坛
        self.click(*self.home_page_luntan_search_loc)
    def xinbankuai(self,names):
        #新增板块
        self.click(*self.home_page_dianjixin_search_loc)#点击新板块
        self.clear(self.home_page_xbkmc_search_loc)
        self.sendkeys(names,*self.home_page_xbkmc_search_loc)
        self.click(*self.home_page_tijiaobuttun_search_loc)#点击提交按钮
    def admin_quit(self):
        self.click(*self.home_page_admin_quit_search_loc)
    def newbankuai_email(self):
        self.click(*self.home_page_email_new_search_loc)
    def find_email(self,email_name):
        self.sendkeys(email_name,*self.home_page_find_email_search_loc)
    def click_suosou(self):
        self.click(*self.home_page_sousuo_search_loc)
    def click_suosou_first(self):
        self.click(*self.home_page_suosou_first_search_loc)
    def suosou_bijiao(self):
        return  self.gettext(*self.get_sousuo_id)
    def click_fatie(self):
        #点击发送邮件
        self.click(*self.home_page_clike_send_email_search_loc)
    def click_toupiao(self):
        #点击发起投票
        self.click(*self.home_page_clike_send_toupian_search_loc)
    def hand_title(self,titli):
        #输入投票名称
        self.sendkeys(titli,*self.titles)
    def title_shuru(self,title1,title2,title3):
        #输入投票内容
        self.sendkeys(title1,*self.titles1)
        self.sendkeys(title2, *self.titles2)
        self.sendkeys(title3, *self.titles3)
        self.click(*self.button_toupiao)
    '''
        投票统计
           '''
    tp_name = (By.ID, "thread_subject")  # 投票名称
    tp_xuanxiang = (By.CSS_SELECTOR,".pvt label")#选项
    tp_xuanxiang1 = (By.CSS_SELECTOR,"#poll>div.pcht>table>tbody>tr:nth-child(3)>td>label")  # 选项
    tp_xuanxiang2 = (By.CSS_SELECTOR,"#poll>div.pcht>table>tbody>tr:nth-child(5)>td>label")  # 选项
    tp_shuju=(By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[2]/td[2]')
    tp_shuju1 = (By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[4]/td[2]')
    tp_shuju2 = (By.XPATH,'//*[@id="poll"]/div[2]/table/tbody/tr[6]/td[2]')
    def tp_names(self):
        tp_name=self.gettext(*self.tp_name)#标题
        tp_xuanxiang=self.gettext(*self.tp_xuanxiang)#选项1
        tp_xuanxiang1=self.gettext(*self.tp_xuanxiang1)
        tp_xuanxiang2=self.gettext(*self.tp_xuanxiang2)
        tp_shuju=self.gettext(*self.tp_shuju)
        tp_shuju1=self.gettext(*self.tp_shuju1)
        tp_shuju2=self.gettext(*self.tp_shuju2)
        print("投票的主题:",tp_name,"\n",
              "投票选项:","\n",tp_xuanxiang,tp_shuju,)
        print(tp_xuanxiang1, tp_shuju1)
        print(tp_xuanxiang2, tp_shuju2)
    ####断言的设置
    tuichu=(By.XPATH,'//*[@id="lsform"]/div/div/table/tbody/tr[2]/td[3]/button/em')
    toupiaos=(By.NAME,"pollsubmit")
    def tuich(self):
        w=self.find_element(*self.tuichu).text
        return w
    def toupiao(self):
        w=self.find_element(*self.toupiaos).text
        return  w
