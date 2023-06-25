#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
@Project ：Platform2.0_UI_Auto_Test
@File    ：get_auth.py
@IDE     ：PyCharm
@Author  ：Pan Junmeng
@Date    ：2023/6/20 15:37
"""
import os

from Config.Config import Config
from Utils.ReadYaml import ReadYaml
from playwright.sync_api import sync_playwright

auth_path = Config.auth_dir + os.path.sep + "auth.json"
case_data = ReadYaml(os.path.join(Config.test_datas_dir, "TestLoginData.yaml")).read()[2]
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(
        headless=True,
        channel=Config.browser,
        args=['--start-maximized']
    )
    context = browser.new_context()
    page = context.new_page()

    # 登陆系统
    page.goto(case_data["url地址"])
    page.fill('id=username', case_data["账号"])
    page.fill('id=password', case_data["密码"])
    page.click('role=button[name="登 录"]')

    # 判断是否登陆成功
    assert '基础平台' in page.get_by_text("基础平台").text_content()

    # 保存状态文件
    context.storage_state(path=auth_path)
