from selene.support.shared import browser

from pages.home_page import HomePage


class WomenPage(HomePage):

    def open_women_page(self):
        self.women_page().click()

    @staticmethod
    def hoodies_and_sweatshirts_for_women():
        hoodies_and_sweatshirts_locator = browser.element('//a[text()="Hoodies & Sweatshirts"]')
        return hoodies_and_sweatshirts_locator
