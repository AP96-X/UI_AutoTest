import os

from playwright.sync_api import expect, Page
from BuildInLibrary.BuildInLibrary import BuildInLibrary
from Config.Config import Config


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def _goto_url(self, url):
        """打开网页"""
        self.page.goto(url)

    def _click(self, locator, frame_locator=None):
        """
        点击元素
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般点击
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).click()
            else:
                self.page.click(locator)
        except Exception as e:
            print(e)

    def _hover(self, locator, frame_locator=None):
        """
        点击元素
        :param locator: 传入元素定位器
        :param frame_locator: 传入frame框架的的定位器，如果没有传入，则一般点击
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).hover()
            else:
                self.page.hover(locator)
        except Exception as e:
            print(e)

    def _fill(self, locator, value, frame_locator=None):
        """
        定位元素，输入内容
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        value = BuildInLibrary().replace_parameter(value)
        try:
            if frame_locator is not None:
                self.page.frame_locator(selector=frame_locator).locator(selector_or_locator=locator).fill(value)
            else:
                self.page.fill(selector=locator, value=value)
        except Exception as e:
            print(e)

    def _type(self, locator, value, frame_locator=None):
        """
        模拟人工输入，一个键一个键的输入
        :param locator:传入元素定位器
        :param value:传入输入的值
        :param frame_locator: 传入frame框架
        :return:
        """
        value = BuildInLibrary().replace_parameter(value)
        try:
            if frame_locator is not None:
                self.page.frame_locator(selector=frame_locator).locator(selector_or_locator=locator).type(text=value,
                                                                                                          delay=100)
            else:
                self.page.type(selector=locator, text=value, delay=100)
        except Exception as e:
            print(e)

    def _file(self, locator, files, frame_locator=None):
        """
        上传文件的方法
        :param locator: 定位器
        :param files: 单个文件名，或者列表存放多个文件
        :param frame_locator: iframe框架定位器，如果没有就不传
        :return:
        """
        try:
            if frame_locator is not None:
                self.page.frame_locator(frame_locator).locator(locator).set_input_files(files=files)
            else:
                self.page.locator(locator).set_input_files(files=files)
        except Exception as e:
            print(e)

    def _ele_to_be_visible(self, locator):
        """断言元素可见"""
        return expect(self.page.locator(locator)).to_be_visible()

    def _ele_to_be_visible_force(self, locator, frame_locator=None, timout: int = 5):
        """强制等待某个元素可见"""
        if frame_locator is not None:
            ele = self.page.frame_locator(frame_locator).locator(locator)
        else:
            ele = self.page.locator(locator)
        for t in range(0, timout):
            self.page.wait_for_timeout(500)
            if ele.is_visible():
                break
        else:
            raise Exception("元素未找到!")

    def _ele_is_checked(self, selector):
        """判断元素是否被选选中"""
        return self.page.is_checked(selector)

    def _text_content(self, selector):
        return self.page.text_content(selector)

    def _browser_operation(self, reload=False, forward=False, back=False):
        """浏览器操作，reload 刷新，forward 前进，back 后退"""
        if reload:
            self.page.reload()
        if back:
            self.page.go_back()
        if forward:
            self.page.go_forward()

    def screenshot(self, path, full_page=True, locator=None):
        """截图功能，默认截取全屏，如果传入定位器表示截取元素"""
        if locator is not None:
            self.page.locator(locator).screenshot(path=path)
            return path
        self.page.screenshot(path=path, full_page=full_page)
        return path

    @staticmethod
    def _delete_auth():
        auth_path = Config.auth_dir + os.path.sep + "auth.json"
        if os.path.exists(auth_path):
            os.remove(auth_path)
