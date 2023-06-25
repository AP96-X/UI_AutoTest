import allure

from BasePage.BasePage import BasePage


class HomePage(BasePage):
    # 定位器
    __logout = '//span[text()="退出系统"]'
    __remind = 'a'
    __logout_confirm = 'role=button[name="确 定"]'
    __home_page = '基础平台'

    @allure.step("断言退出可见")
    def ele_to_be_visible(self, locator):
        return self._ele_to_be_visible(locator)

    @allure.step("退出按钮")
    def click_button_logout(self):
        return self._click(self.__logout)

    @allure.step("退出确定按钮")
    def click_button_logout_confirm(self):
        return self._click(self.__logout_confirm)

    @allure.step("关闭提醒")
    def click_password_remind(self):
        return self.page.locator(self.__remind).click()

    @allure.step("主页验证")
    def home_page_confirm(self):
        return self.page.get_by_text(self.__home_page).click()
