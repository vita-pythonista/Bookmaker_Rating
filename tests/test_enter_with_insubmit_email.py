import time

from pages.main_page import Main

class TestEnterWithInsubmitEmail:

    def test_error_about_unregister_email(self, browser):
        browser.get("https://bookmaker-ratings.ru/")
        main = Main(browser)
        main.click_blue_button_enter()
        main.click_auth_with_email()
        main.input_email(email="kahap37224@nifect.com")
        main.input_password(password="7wNb5qSz2iBShH7wNb5qSz2iBShH")
        main.click_submit_enter()
        main.check_error_about_unregister_email()

    def test_register_new_user_with_phone(self, browser):
        browser.get("https://bookmaker-ratings.ru/")
        main = Main(browser)
        main.click_blue_button_enter()
        main.input_phone(phone_number='9912526441')
        main.click_further_btn()
        time.sleep(3)

    def test_enter_with_cookies(self, browser):
        browser.get("https://bookmaker-ratings.ru/")
        main = Main(browser)
        main.authorize_with_cookies()
        browser.get("https://bookmaker-ratings.ru/tips/pszh-mets-prognoz-i-stavka-gosti-obyazany-zabivat//")
        time.sleep(2)