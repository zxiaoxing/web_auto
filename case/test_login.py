# coding:utf-8
import pytest
import time
from page.login import login_success


class Test_Login():

    # @pytest.fixture(scope="function",  autouse=True)
    # def startPaget(self, driver, host):
    #     print("---让每个用例都从登录首页开始:---start!---")
    #     driver.get("host")
    #     driver.delete_all_cookies()
    #     driver.refresh()

    @pytest.fixture(scope="function", autouse=True)
    def start(self, driver, host):
        driver.get(host)
        driver.delete_all_cookies()
        driver.refresh()

    def test_login_pass(self, driver):
        '''登录成功案例'''
        result = login_success(driver)
        assert result == "秦能1"
