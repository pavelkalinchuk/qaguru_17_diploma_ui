from selene import browser, be, have

from pages.home_page import HomePage


class ProductPage(HomePage):
    def product(self, product_url):
        base_url = self.get_base_url()
        product = browser.element(f'.product-item-link[href="{base_url}/{product_url}.html"]')
        return product

    @staticmethod
    def select_size(size):
        size_mapping = {
            'XS': '#option-label-size-143-item-166',
            'S': '#option-label-size-143-item-167',
            'M': '#option-label-size-143-item-168',
            'L': '#option-label-size-143-item-169',
            'XL': '#option-label-size-143-item-170'
        }

        if size in size_mapping:
            size_element = browser.element(size_mapping[size])
            size_element.should(be.visible)
        else:
            raise ValueError(f"Invalid size: {size}")
        return size_element

    @staticmethod
    def select_color(color):
        color_mapping = {
            'Blue': '#option-label-color-93-item-50',
            'Green': '#option-label-color-93-item-53',
            'Lavender': '#option-label-color-93-item-54'
        }
        if color in color_mapping:
            color_element = browser.element(color_mapping[color])
            color_element.should(be.visible)
        else:
            raise ValueError(f"Invalid size: {color}")
        return color_element

    @staticmethod
    def add_to_cart():
        product_addtocart_button = browser.element('#product-addtocart-button')
        return product_addtocart_button

    @staticmethod
    def should_be_message_added_cart_product(product_name):
        message = browser.element('div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
        message.should(be.visible)
        message.should(have.text(f'You added {product_name} to your shopping cart.'))
        return message
