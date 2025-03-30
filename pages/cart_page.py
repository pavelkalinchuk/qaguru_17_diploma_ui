from selene import browser, have


class Cart:
    @staticmethod
    def open_cart():
        cart = browser.element('.action.showcart')
        return cart

    @staticmethod
    def product_name(name):
        browser.element('.product-item-details .product-item-name').should(have.text(name))

    @staticmethod
    def product_details(size, color):
        browser.element('.toggle').click()
        details = browser.all('.values span[data-bind="text: option.value"]')
        details.should(have.texts(size, color))
