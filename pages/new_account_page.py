from selene import by
from selene.support.shared import browser

from pages.home_page import HomePage


class NewAccountPage(HomePage):
    def open_create_new_account_page(self):
        self.link_for_create_new_account().click()

    @staticmethod
    def first_name_field():
        first_name = browser.element('#firstname')
        return first_name

    @staticmethod
    def last_name_field():
        last_name_locator = browser.element('#lastname')
        return last_name_locator

    @staticmethod
    def email_field():
        email_locator = browser.element('#email_address')
        return email_locator

    @staticmethod
    def password_field():
        password_locator = browser.element('#password')
        return password_locator

    @staticmethod
    def confirm_password_field():
        confirm_password_locator = browser.element('#password-confirmation')
        return confirm_password_locator

    @staticmethod
    def button_for_create_account():
        create_account_button_locator = browser.element('button.action.submit.primary')
        return create_account_button_locator
