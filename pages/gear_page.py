from selene.support.shared import browser

from pages.home_page import HomePage


class GearPage(HomePage):

    def open_gear_page(self):
        self.gear_page().click()

    @staticmethod
    def bags_list():
        bags_list_locator = browser.element('//a[text()="Bags"]')
        return bags_list_locator
