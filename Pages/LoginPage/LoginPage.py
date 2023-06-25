import allure
from BasePage.BasePage import BasePage


class LoginPage(BasePage):
    # 元素定位器
    __username = "id=username"
    __password = "id=password"
    __button_login = 'role=button[name="登 录"]'
    __button_reset = 'role=button[name="重 置"]'
    __ele_login_error = 'text[value="用户名或密码错误"]'

    def del_auth(self):
        self._delete_auth()

    @allure.step("打开登录页面")
    def goto_login(self, url):
        self._goto_url(url)

    @allure.step("清空输入框操作")
    def fill_none(self):
        self._fill(self.__username, '')
        self._fill(self.__password, '')

    @allure.step("输入账号")
    def fill_username(self, value):
        self._type(self.__username, value)

    @allure.step("输入密码")
    def fill_password(self, value):
        self._type(self.__password, value)

    @allure.step("点击登录按钮")
    def click_button_login(self):
        self._click(self.__button_login)

    @allure.step("点击重置按钮")
    def click_button_reset(self):
        self._click(self.__button_reset)

    @allure.step("断言登录失败")
    def login_ele_to_be_visible(self):
        self._ele_to_be_visible(self.__ele_login_error)

    @allure.step("断言重置功能")
    def assert_function_reset(self):
        self.page.text_content(self.__username)

    def browser_operation(self, reload=True, forward=False, back=False):
        self._browser_operation(reload=reload, forward=forward, back=back)
