from selene.support.shared import browser

from pages.home_page import HomePage


class ErinRecommendsPage(HomePage):

    @staticmethod
    def title_page():
        title_page_locator = browser.element('[data-ui-id="page-title-wrapper"]')
        return title_page_locator

    @staticmethod
    def list_products():
        product_names = browser.all('.product-item-link')
        return product_names
