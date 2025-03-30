from selene import be, have, by
from selene.support.shared import browser

from pages.home_page import HomePage


class ManPage(HomePage):

    def open_page(self):
        self.men_page().click()

    def hoodies_and_sweatshirts(self):
        base_url = self.get_base_url()
        section = 'hoodies-and-sweatshirts-men'
        hoodies_and_sweatshirts = browser.element(f'.item a[href="{base_url}/men/tops-men/{section}.html"]')
        return hoodies_and_sweatshirts
