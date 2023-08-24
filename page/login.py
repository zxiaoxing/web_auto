from selenium import webdriver
from common.base import Base
from time import sleep

# 登录的定位
loc_username = ("xpath", "//*[@placeholder = '请输入用户名']")
loc_password = ("xpath", "//*[@placeholder='请输入密码' and @type='password']")
loc_click_login = ("xpath", "//span[text()='登录']")

# 断言的定位
loc_login_success = ("xpath", "//*[@class='<lg:hidden text-14px pl-[5px] text-[var(--top-header-text-color)]']")

def login_success(driver):

    # 输入正确的用户名
    ysir = Base(driver)
    sleep(3)

    ysir.sendKeys(loc_username, "15927391992")
    


    # 输入正确的密码
    sleep(3)
    ysir.sendKeys(loc_password, "qn123456")

    sleep(3)
    ysir.click(loc_click_login)

    sleep(3)

    # 获取登录成功的字样，如“首页”
    result = ysir.get_text(loc_login_success)

    return result