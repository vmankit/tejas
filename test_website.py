import os
from playwright.sync_api import sync_playwright

WORKSPACE_DIR = r"C:\Users\rolln\OneDrive\Desktop\tejas"
HTML_PATH = os.path.join(WORKSPACE_DIR, "index.html")

def test_site():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()

        console_errors = []
        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        print(f"Opening: file:///{HTML_PATH.replace(os.sep, '/')}")
        page.goto(f"file:///{HTML_PATH.replace(os.sep, '/')}", wait_until="networkidle")

        print("Page title:", page.title())

        # Check vehicle cards count
        cards = page.locator(".v-card")
        card_count = cards.count()
        print(f"Total cards rendered: {card_count}")
        assert card_count > 0, "No vehicle cards rendered!"

        # Screenshot hero & top
        page.screenshot(path=os.path.join(WORKSPACE_DIR, "site_screenshot_desktop.png"), full_page=False)

        # Test Category Filter: Click 'suv'
        print("Testing SUV category filter...")
        page.locator('.cat-pill-card[data-cat="suv"]').first.click()
        page.wait_for_timeout(500)
        suv_count = page.locator(".v-card").count()
        print(f"SUV cards rendered: {suv_count}")
        assert suv_count == 8, f"Expected 8 SUVs, got {suv_count}"

        # Test Search Filter
        print("Testing search filter for 'Hayabusa'...")
        # Reset category to all
        page.locator('.cat-pill-card[data-cat="all"]').first.click()
        page.wait_for_timeout(300)
        page.locator('#searchInput').fill("Hayabusa")
        page.wait_for_timeout(500)
        busa_count = page.locator(".v-card").count()
        print(f"Search results for 'Hayabusa': {busa_count}")
        assert busa_count >= 1, "Hayabusa search failed"

        # Clear search
        page.locator('#searchInput').fill("")
        page.wait_for_timeout(500)

        # Screenshot Fleet
        fleet_sec = page.locator('#fleet')
        fleet_sec.screenshot(path=os.path.join(WORKSPACE_DIR, "site_screenshot_fleet.png"))


        # Test Calculator
        print("Testing Instant Rental Calculator...")
        page.locator('#calcVehicleSelect').select_option("thar-black")
        page.locator('#calcDurationSelect').select_option("24")
        page.wait_for_timeout(300)
        calc_total = page.locator('#calcTotalRent').inner_text()
        clean_calc_total = calc_total.replace('₹', 'Rs.')
        print(f"Calculator Total for Thar (24h): {clean_calc_total}")



        calc_sec = page.locator('#calculator')
        calc_sec.screenshot(path=os.path.join(WORKSPACE_DIR, "site_screenshot_calculator.png"))

        # Test Modal
        print("Testing Vehicle Modal...")
        page.locator('.btn-details-card').first.click()
        page.wait_for_timeout(500)
        modal_visible = page.locator('#vehicleModal').is_visible()
        print(f"Modal opened: {modal_visible}")
        page.screenshot(path=os.path.join(WORKSPACE_DIR, "site_screenshot_modal.png"))
        page.locator('#modalCloseBtn').click()
        page.wait_for_timeout(300)

        # Mobile Viewport Test
        print("Testing mobile viewport 390x844...")
        context_mobile = browser.new_context(viewport={"width": 390, "height": 844})
        page_mobile = context_mobile.new_page()
        page_mobile.goto(f"file:///{HTML_PATH.replace(os.sep, '/')}", wait_until="networkidle")
        page_mobile.screenshot(path=os.path.join(WORKSPACE_DIR, "site_screenshot_mobile.png"))

        browser.close()

        if console_errors:
            print("Console Errors:", console_errors)
        else:
            print("Zero console errors! Everything passed perfectly.")

if __name__ == "__main__":
    test_site()
