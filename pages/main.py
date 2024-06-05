from playwright.sync_api import Page


class MainPage:

    def __init__(self, page: Page):
        self.page = page
        self.products_tab = page.locator('//*[@href="/products"]')

    def navigate_to_search_page(self):
        self.products_tab.click()
        self.page.reload()
        self.products_tab.click()