from selene.support.shared import browser


class AuthorizationPage:

    @staticmethod
    def email_input_field():
        email_field_locator = browser.element('#email')
        return email_field_locator

    @staticmethod
    def password_input_field():
        password_field_locator = browser.element('#pass')
        return password_field_locator

    @staticmethod
    def button_for_authorization():
        button_for_authorization_locator = browser.element('#send2')
        return button_for_authorization_locator
