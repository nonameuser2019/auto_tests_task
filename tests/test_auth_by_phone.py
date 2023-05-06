from pages.code_auth_page import CodeAuthPage


class TestAuthByPhone:
    phone = '+79611653166'
    password = 'Pro33160900'

    @staticmethod
    def auth_page(browser):
        code_auth_page = CodeAuthPage(browser).open()
        pass_auth_page = code_auth_page.click_on_enter_with_password_btn()
        return pass_auth_page

    def test_auth_by_phone(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.user_name_input().send_keys(self.phone)
        auth_page.password_input().send_keys(self.password)
        auth_page.enter_btn().click()
        auth_page.url_should_have('redirect_uri')

    def test_auth_with_not_existing_phone_number(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.user_name_input().send_keys('+7 961 999 99 00')
        auth_page.password_input().send_keys(self.password)
        auth_page.enter_btn().click()
        auth_page.enter_btn().click()
        auth_page.check_wrong_login_error_message('Неверный логин или пароль')

    def test_with_blank_login_and_password(self, browser):
        auth_page = self.auth_page(browser)
        auth_page.enter_btn().click()
        auth_page.check_error_message('Введите номер телефона')

    def test_go_back_to_auth_by_code_page(self, browser):
        auth_page = self.auth_page(browser)
        auth_by_code_page = auth_page.click_on_enter_by_code_btn()
        auth_by_code_page.enter_with_password_btn().is_displayed()

    def test_go_to_forgot_password_page(self, browser):
        auth_page = self.auth_page(browser)
        forgot_password_page = auth_page.click_on_forgot_password_link()
        forgot_password_page.should_be_restore_page()