from selenium.webdriver.common.by import By


class MainPage:

    btn_enter = (By.CSS_SELECTOR, ".menu-wrapper .login-wrapper")


class WindowsEnterOrRegistration:

    phone_input = (By.CSS_SELECTOR, '.js-auth-phone')
    btn_further_phone_registration = (By.CSS_SELECTOR, "#auth-form-container > "
                                                       "div.popup-content.auth-form.align-right.align-left.js-auth"
                                                       "-form > div > form > button")
    enter_with_email = (By.CSS_SELECTOR, ".auth-link[data-form='email']")
    email_input = (By.CSS_SELECTOR, "input.input[name='email']")
    password_input = (By.CSS_SELECTOR, "input.input[name='password']")
    btn_submit = (By.CSS_SELECTOR, "button.auth-button[name='submit']")
    text_about_unregister_email = (By.CSS_SELECTOR, ".error-message .error-text")
