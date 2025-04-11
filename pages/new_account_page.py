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
        last_name = browser.element('#lastname')
        return last_name

    @staticmethod
    def email_field():
        email = browser.element('#email_address')
        return email

    @staticmethod
    def password_field():
        password = browser.element('#password')
        return password

    @staticmethod
    def confirm_password_field():
        confirm_password = browser.element('#password-confirmation')
        return confirm_password

    @staticmethod
    def button_for_create_account():
        create_account_button = browser.element('button.action.submit.primary')
        return create_account_button
