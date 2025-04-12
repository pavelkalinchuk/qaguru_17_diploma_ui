from selene.support.shared import browser
from selene import be, by


class HomePage:
    @staticmethod
    def get_base_url():
        return 'https://magento.softwaretestingboard.com'

    @staticmethod
    def accept_permission_to_process_data():
        agree = browser.element('//span[text()="AGREE"]').should(be.visible)
        return agree

    @staticmethod
    def men_page():
        man_page_locator = browser.element('//span[text()="Men"]')
        return man_page_locator

    @staticmethod
    def women_page():
        woman_page_locator = browser.element('//span[text()="Women"]')
        return woman_page_locator

    @staticmethod
    def link_for_create_new_account():
        create_account_link = browser.element(by.link_text("Create an Account"))
        return create_account_link

    @staticmethod
    def link_for_authorization():
        sing_in_link = browser.element(by.link_text("Sign In"))
        return sing_in_link

    @staticmethod
    def user_is_authorized():
        user_is_authorized = browser.element('.logged-in')
        return user_is_authorized

    @staticmethod
    def open_user_actions_list():
        open_list_button_locator = browser.element('button.action.switch')
        return open_list_button_locator

    @staticmethod
    def log_out_of_account_link():
        log_out_link_locator = browser.element('//li[@class="authorization-link" and @data-label="or"]/a[contains(., "Sign Out")]')
        return log_out_link_locator
