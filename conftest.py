from selenium import webdriver
import pytest

_driver = None

def pytest_addoption(parser):
    '''添加命令行参数--browser、--host'''
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser option: firefox or chrome"
             )
    
    '''添加host参数，设置默认测试环境地址'''
    parser.addoption(
        "--host", action="store", default="https://cloud.yoseenir.com/login", help="case host->https://cloud.yoseenir.com/login"
    )

@pytest.fixture(scope='session')
def host(request):
    '''全局host参数'''
    return request.config.getoption("--host")

@pytest.fixture(scope='session')
def driver(request):
    '''定义全局driver参数'''
    global _driver

    if _driver is None:
        name = request.config.getoption("--browser")
        if name == "firefox":
            _driver = webdriver.Firefox()
        elif name == "chrome":
            _driver = webdriver.Chrome()
        else:
            _driver = webdriver.Chrome()
            _driver.get("https://cloud.yoseenir.com/login")
        print("正在启动浏览器名称：%s" % name)

    def fn():
        print("当全部用例执行完之后：teardown quit driver！")
        _driver.quit()
    request.addfinalizer(fn)
    return _driver


