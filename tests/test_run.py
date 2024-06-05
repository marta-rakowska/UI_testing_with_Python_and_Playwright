from playwright.sync_api import sync_playwright, expect

browser = sync_playwright().start().chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()

#logo
assert page.locator('//img[@alt="Website for automation practice"]').is_visible()

#cart
assert page.locator('div.header-middle div.container div.row div.col-sm-8 div.shop-menu.pull-right ul.nav.navbar-nav li:nth-child(3) > a:nth-child(1)').is_visible()

#email subscription
assert page.locator('//input[@id="susbscribe_email"]').is_visible()

#banner switch right
assert page.locator('(//i[@class="fa fa-angle-right"])[1]').is_visible()

#brands header
assert page.locator('//h2[contains(text(),"Brands")]').is_visible()

#footer
assert page.locator('//footer[@id="footer"]').is_visible()

#scroll-up
assert page.locator('//body/a[@id="scrollUp"]/i[1]').is_visible()

user = 'Pajton'
login = 'playwrightpython@gmail.com'
password = 'test123'

page.goto('https://automationexercise.com/')
page.locator('a[href="/login"]').click()
page.locator('[data-qa="login-email"]').fill(login)
page.locator('[data-qa="login-password"]').fill(password)
page.locator('[data-qa="login-button"]').click()

expect(page.get_by_text(f"Logged in as {user}")).to_be_visible()
assert page.get_by_text(f"Logged in as {user}").is_visible()





