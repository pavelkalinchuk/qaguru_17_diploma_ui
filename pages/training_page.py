from selene.support.shared import browser

from pages.home_page import HomePage


class TrainingPage(HomePage):

    @staticmethod
    def link_for_recommendations_from_erin_renny():
        link_for_recommendations_locator = browser.element('.block-promo.training-erin')
        return link_for_recommendations_locator
