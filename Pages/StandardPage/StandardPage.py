import allure

from BasePage.BasePage import BasePage


class StandardPage(BasePage):
    # 定位器
    __standard_page = '//div[text()="基础平台"]'
    __standard_icon = '//div[text()="数据标准管理"]'
    __new_standard = '//span[text()="新增标准"]'
    __standard_code = 'role=dialog[name="新增"]'
    __standard_name = 'get_by_role("dialog", name="新增)'
    __standard_descript = '//form[@id="standardDescription"]'
    __standard_default = ""
    __button_confirm = 'role=button[name="确 定"]'
    __button_cancel = 'role=button[name="取 消"]'
    __op_success = '//span[text()="操作成功"]'
    __button_import = 'role=button[name="导 入"]'
    __upload_button = 'id=file'

    @allure.step("打开页面")
    def goto_page(self, url):
        self._goto_url(url)

    @allure.step("进入基础平台页面")
    def click_base_page(self):
        return self._click(self.__standard_page)

    @allure.step("进入标准管理界面")
    def click_standard_icon(self):
        return self._click(self.__standard_icon)

    @allure.step("点击新增标准")
    def click_new_standard(self):
        return self._click(self.__new_standard)

    @allure.step("输入标准编码")
    def type_standard_code(self, value):
        return self.page.get_by_role("dialog", name="新增").locator("#standardCode").type(value, delay=100)

    @allure.step("输入标准名称")
    def type_standard_name(self, value):
        return self.page.get_by_role("dialog", name="新增").locator("#standardName").type(value, delay=100)

    @allure.step("输入标准说明")
    def type_standard_descript(self, value):
        return self.page.get_by_role("dialog", name="新增").locator("#standardDescription").type(value, delay=100)

    @allure.step("点击确定按钮")
    def click_button_confirm(self):
        return self._click(self.__button_confirm)

    @allure.step("点击取消按钮")
    def click_button_cancel(self):
        return self._click(self.__button_cancel)

    @allure.step("断言是否成功")
    def assert_success(self, locator):
        return self._ele_to_be_visible(locator)

    @allure.step("表格操作")
    def table_operation(self, locator):
        self._click(locator)

    @allure.step("点击导入按钮")
    def click_button_import(self):
        self._click(self.__button_import)

    @allure.step("选择导入模式")
    def select_import_mode(self, value):
        self.page.get_by_label("导入方式").click()
        self.page.get_by_text(value).click()

    @allure.step("点击上传按钮")
    def upload_file(self, files):
        self._file(self.__upload_button, files)
