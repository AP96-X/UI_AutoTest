import allure
import functools
import os.path
import pytest

from Config.Config import Config


class PrettyAllure(object):

    @classmethod
    def pretty_allure_case(cls, page, case_data):
        allure.dynamic.feature(case_data.get("模块"))
        allure.dynamic.story(case_data.get("功能"))
        allure.dynamic.severity(case_data.get("优先级"))
        allure.dynamic.title(f'{case_data.get("用例编号")}_{case_data.get("用例标题")}')
        if case_data.get("是否执行") != "Y":
            allure.dynamic.description("用例指定跳过")
            pytest.skip("用例指定跳过")

    @classmethod
    def pretty_allure_screen_shot(cls, page, case_data):
        filename = os.path.join(Config.test_screenshot_dir, f"{case_data.get('用例标题')}.png")
        page.screenshot(path=filename)
        allure.attach.file(source=filename, name=case_data.get('用例标题'), attachment_type=allure.attachment_type.PNG)

    @classmethod
    def pretty_allure_wrapper(cls, func):
        """装饰器函数"""

        @functools.wraps(func)
        def inner(*args, **kwargs):
            # 添加用例信息
            cls.pretty_allure_case(page=kwargs.get("page"), case_data=kwargs.get("case_data"))  # 如何获取case_data?
            r = func(*args, **kwargs)  # 运行用例
            # 添加截图
            cls.pretty_allure_screen_shot(page=kwargs.get("page"), case_data=kwargs.get("case_data"))
            return r

        return inner


if __name__ == '__main__':
    pass
