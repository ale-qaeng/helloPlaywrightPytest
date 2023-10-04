from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.thereformation.com/")
    page.get_by_role("link", name="Clothing", exact=True).click()
    page.get_by_role("link", name="Dresses", exact=True).click()
    page.get_by_role("link", name="Tops", exact=True).click()
    page.get_by_role("link", name="Jeans", exact=True).click()
    page.get_by_role("link", name="Sweaters", exact=True).click()
    page.get_by_role("link", name="Weddings", exact=True).click()
    page.get_by_role("link", name="Shoes", exact=True).click()
    page.get_by_role("link", name="Bags", exact=True).click()
    page.get_by_role("link", name="Edits", exact=True).click()
    page.get_by_role("link", name="Sustainability", exact=True).click()
    page.get_by_label("Ref Bags", exact=True).click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
