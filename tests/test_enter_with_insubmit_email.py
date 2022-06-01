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
        browser.add_cookie({"name": "accessToken", "value": "1567e02d62f8f624640181628f81b4e2ebaac133", "path": "/"})
        browser.add_cookie({"name": "auth", "value": "%7B%22access_token%22%3A"
                                                     "%221567e02d62f8f624640181628f81b4e2ebaac133%22%2C%22id%22"
                                                     "%3A631114%2C%22refresh_token%22%3A"
                                                     "%2252c983a1d4d005fe0ace535beead683fd1937b3d%22%2C%22initials%22"
                                                     "%3A%22%D0%92%D0%90%22%2C%22avatar%22%3Anull%2C%22subscriptions"
                                                     "%22%3A%5B%5D%2C%22roles%22%3A%5B%22subscriber%22%5D%7D"})
        browser.get("https://bookmaker-ratings.ru/tips/pszh-mets-prognoz-i-stavka-gosti-obyazany-zabivat//")
        time.sleep(2)