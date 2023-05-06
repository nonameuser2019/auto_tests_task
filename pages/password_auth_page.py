from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PasswordAuthPage(BasePage):

    def phone_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-phone")

    def email_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-email")

    def login_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-login")

    def ls_tab(self):
        return self.browser.find_element(By.CSS_SELECTOR, "div#t-btn-tab-ls")

    def user_name_input(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input#username")

    def password_input(self):
        return self.browser.find_element(By.CSS_SELECTOR, "input#password")

    def forgot_password_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, "a#forgot_password")

    def enter_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "button#kc-login")

    def enter_by_code_btn(self):
        return self.browser.find_element(By.CSS_SELECTOR, "button#back_to_otp_btn")

    def register_link(self):
        return self.browser.find_element(By.CSS_SELECTOR, "a#kc-register")

    def click_register_link(self):
        from pages.register_page import RegisterPage
        self.register_link().click()
        return RegisterPage(self.browser)


