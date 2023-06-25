#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：playwright-demo
@File    ：test_Standard.py
@IDE     ：PyCharm
@Author  ：Pan Junmeng
@Date    ：2023/6/14 09:17
"""
import os

import pytest

from Common.AllurePretty import PrettyAllure
from Config.Config import Config
from Pages.StandardPage.StandardPage import StandardPage
from Utils.ReadYaml import ReadYaml


class TestStandard:

    @PrettyAllure.pretty_allure_wrapper
    @pytest.mark.parametrize("case_data",
                             ReadYaml(os.path.join(Config.test_datas_dir, "TestStandardData.yaml")).read()[0:1])
    def test_create_standard(self, page, case_data: dict):
        create_standard = StandardPage(page)
        create_standard.goto_page(case_data["url地址"])
        create_standard.click_new_standard()
        create_standard.type_standard_code(case_data["标准编码"])
        create_standard.type_standard_name(case_data["标准名称"])
        create_standard.type_standard_descript(case_data["说明"])
        create_standard.click_button_confirm()
        create_standard.assert_success(case_data["断言元素定位"])

    @PrettyAllure.pretty_allure_wrapper
    @pytest.mark.parametrize("case_data",
                             ReadYaml(os.path.join(Config.test_datas_dir, "TestStandardData.yaml")).read()[1:2])
    def test_delete_standard(self, page, case_data: dict):
        delete_standard = StandardPage(page)
        delete_standard.goto_page(case_data["url地址"])
        delete_standard.table_operation(case_data["删除按钮"])
        delete_standard.click_button_confirm()
        delete_standard.assert_success(case_data["断言元素定位"])

    @PrettyAllure.pretty_allure_wrapper
    @pytest.mark.parametrize("case_data",
                             ReadYaml(os.path.join(Config.test_datas_dir, "TestStandardData.yaml")).read()[2:3])
    def test_standard_upload_file(self, page, case_data: dict):
        upload_standard_value = StandardPage(page)
        upload_standard_value.goto_page(case_data["url地址"])
        upload_standard_value.table_operation(case_data["详情按钮"])
        upload_standard_value.click_button_import()
        upload_standard_value.select_import_mode(case_data["下拉框值"])
        upload_standard_value.upload_file(case_data["files"])
        upload_standard_value.click_button_confirm()
