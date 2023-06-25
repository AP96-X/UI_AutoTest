import os
import time
import allure
import pytest
from playwright.sync_api import sync_playwright
from Config.Config import Config

pageobject = None
auth_path = Config.auth_dir + os.path.sep + "auth.json"


@pytest.fixture(scope="class")
def page():
    global pageobject
    global auth_path
    with sync_playwright() as play:
        browser = play.chromium.launch(
            headless=Config.headless,
            channel=Config.browser,
            args=['--start-maximized'],
        )
        if os.path.exists(auth_path):
            context = browser.new_context(no_viewport=True, storage_state=auth_path)
        else:
            context = browser.new_context(no_viewport=True)
        # 录制日志
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        if pageobject is None:
            pageobject = context.new_page()
        yield pageobject
        pageobject = None
        context.tracing.stop(path="trace.zip")
        if os.path.exists(path=auth_path):
            pass
        else:
            context.storage_state(path=f"{Config.auth_dir + os.path.sep}auth.json")
        context.close()
        browser.close()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: object, call: object) -> object:
    """
    获取每个用例状态的钩子函数
    :param item: 测试用例
    :param call: 测试步骤
    :return:
    """
    # 获取钩子方法的调用结果
    out_come = yield
    rep = out_come.get_result()  # 从钩子方法的调用结果中获取测试报告
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == 'call' and rep.failed:
        failures_log = os.path.join(Config.logs, "failures.log")
        mode = "a" if os.path.exists(failures_log) else "w"
        with open(failures_log, mode) as f:
            # let's also access a fixture for the fun of it
            if "case_data" in item.fixturenames:
                extra = " (%s)" % item.funcargs["case_data"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(pageobject, "screenshot"):
            with allure.step('添加失败截图...'):
                path = Config.test_screenshot_dir + os.path.sep + item.funcargs["case_data"].get(
                    "用例编号") + "失败截图.png"
                file = pageobject.screenshot(path=path)
                allure.attach(file, "失败截图",
                              allure.attachment_type.PNG)


@pytest.fixture(scope="session", autouse=True)
def auth():
    global auth_path
    auth_path = Config.auth_dir + os.path.sep + "auth.json"
    '''
    调试需要登录状态的用例时，先将下面两个if语句注释掉，运行一次登录成功的用例。
    提交代码时不要提交这个文件。
    其余时候则保持原样。
    '''
    if os.path.exists(auth_path):
        os.remove(auth_path)
    yield
    if os.path.exists(auth_path):
        os.remove(auth_path)
