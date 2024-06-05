from playwright.sync_api import Page


class SearchPage:

    def __init__(self, page: Page):
        self.page = page
        self.search_field = page.locator('input#search_product')
        self.search_button = page.locator('button#submit_search')
        self.product_title = page.locator(".single-products")

    def search_product(self, product_name):
        self.search_field.fill(product_name)
        self.search_button.click()

    def get_number_of_visible_products(self):
        return self.product_title.count()

