import os
import time

import pytest

from Common.AllurePretty import PrettyAllure
from Config.Config import Config
from Pages.HomePage.HomePage import HomePage
from Pages.LoginPage.LoginPage import LoginPage
from Utils.ReadYaml import ReadYaml


class TestLogin:

    @pytest.mark.run(order=2)
    @PrettyAllure.pretty_allure_wrapper
    @pytest.mark.parametrize("case_data",
                             ReadYaml(os.path.join(Config.test_datas_dir, "TestLoginData.yaml")).read()[0:2])
    def test_login_error(self, page, case_data: dict):
        login_operation = LoginPage(page)
        login_operation.goto_login(case_data["url地址"])
        login_operation.fill_none()
        login_operation.fill_username(case_data["账号"])
        login_operation.fill_password(case_data["密码"])
        login_operation.click_button_login()
        HomePage(page).ele_to_be_visible(case_data["断言元素定位"])

    @pytest.mark.run(order=1)
    @PrettyAllure.pretty_allure_wrapper
    @pytest.mark.parametrize("case_data",
                             ReadYaml(os.path.join(Config.test_datas_dir, "TestLoginData.yaml")).read()[2:3])
    def test_login_reset(self, page, case_data: dict):
        login_reset = LoginPage(page)
        login_reset.goto_login(case_data["url地址"])
        login_reset.fill_none()
        login_reset.fill_username(case_data["账号"])
        login_reset.fill_password(case_data["密码"])
        login_reset.click_button_reset()
        assert login_reset.assert_function_reset() is None
