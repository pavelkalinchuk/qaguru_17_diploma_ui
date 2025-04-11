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
    def open_men_page():
        page = browser.element('//span[text()="Men"]')
        return page

    @staticmethod
    def link_for_create_new_account():
        create_account = browser.element(by.link_text("Create an Account"))
        return create_account

