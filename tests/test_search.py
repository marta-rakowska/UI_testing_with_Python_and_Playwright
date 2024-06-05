from playwright.sync_api import Page

def test_search_results_pop(main_page, search_page, measure_time):
    main_page.navigate_to_search_page()
    search_page.search_product('unicorn')
    assert search_page.get_number_of_visible_products() >= 2

def test_search_results_above_10(main_page, search_page):
    # main_page = MainPage(page)
    # search_page = SearchPage(page)

    main_page.navigate_to_search_page()
    search_page.search_product('dress')
    assert search_page.get_number_of_visible_products() == 9

def test_search_results(page: Page):
    page.locator('a[href="/products"]').click()
    page.reload()
    page.locator('a[href="/products"]').click()
    page.locator('input#search_product').fill('unicorn')
    page.locator('button#submit_search').click()

    #1
    product_locator = page.locator(".single-products")
    products = product_locator.all()
    assert len(products) >= 2

    #2
    number_of_products = page.locator(".single-products").count()
    assert number_of_products >= 2







