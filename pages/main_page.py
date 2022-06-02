from locators.main_page import MainPage, WindowsEnterOrRegistration as W_Enter
from helper.base_actions import BaseAction


class Main(BaseAction):

    def click_blue_button_enter(self):
        self.mouse_click(*MainPage.btn_enter)

    def input_phone(self, phone_number):
        self.input(*W_Enter.phone_input, phone_number)

    def click_further_btn(self):
        self.wait_elem(*W_Enter.btn_further_phone_registration)
        self.click(*W_Enter.btn_further_phone_registration)

    def click_auth_with_email(self):
        self.click(*W_Enter.enter_with_email)

    def input_email(self, email):
        self.input(*W_Enter.email_input, email)

    def input_password(self, password):
        self.input(*W_Enter.password_input, password)

    def click_submit_enter(self):
        self.click(*W_Enter.btn_submit)

    def check_error_about_unregister_email(self):
        error_text_element = self.find_element(*W_Enter.text_about_unregister_email)
        assert error_text_element.text == "Данный email не зарегистрирован"

    def authorize_with_cookies(self):
        self.driver.add_cookie(dict(name="accessToken", value="1567e02d62f8f624640181628f81b4e2ebaac133"))
        self.driver.add_cookie({"name": "auth", "value": "%7B%22access_token%22%3A"
                                                     "%221567e02d62f8f624640181628f81b4e2ebaac133%22%2C%22id%22"
                                                     "%3A631114%2C%22refresh_token%22%3A"
                                                     "%2252c983a1d4d005fe0ace535beead683fd1937b3d%22%2C%22initials%22"
                                                     "%3A%22%D0%92%D0%90%22%2C%22avatar%22%3Anull%2C%22subscriptions"
                                                     "%22%3A%5B%5D%2C%22roles%22%3A%5B%22subscriber%22%5D%7D"})