from playwright.sync_api import Page, expect

user = 'Pajton'
login = 'playwrightpython@gmail.com'
password = 'test123'

def test_login_positive(page: Page):
    page.goto('https://automationexercise.com/')
    page.locator('a[href="/login"]').click()
    page.locator('[data-qa="login-email"]').fill(login)
    page.locator('[data-qa="login-password"]').fill(password)
    page.locator('[data-qa="login-button"]').click()

    user_locator = page.locator('.fa-user')

    assert user_locator.is_visible()
    expect(user_locator).to_be_visible()
