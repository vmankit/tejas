import os
from playwright.sync_api import sync_playwright

WORKSPACE_DIR = r"C:\Users\rolln\OneDrive\Desktop\tejas"
HTML_PATH = os.path.join(WORKSPACE_DIR, "index.html")

def capture_all():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        # Desktop
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        page.goto(f"file:///{HTML_PATH.replace(os.sep, '/')}", wait_until="networkidle")

        # 1. Desktop Top & Hero
        page.screenshot(path=os.path.join(WORKSPACE_DIR, "ui_hero_updated.png"))

        # 2. Events section
        page.locator("#events").scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.locator("#events").screenshot(path=os.path.join(WORKSPACE_DIR, "ui_events_updated.png"))

        # 3. Open Modal
        page.locator("#fleet").scroll_into_view_if_needed()
        page.wait_for_timeout(300)
        page.locator(".v-card .btn-details-card").first.click()
        page.wait_for_timeout(400)
        page.screenshot(path=os.path.join(WORKSPACE_DIR, "ui_modal_updated.png"))
        page.locator("#modalCloseBtn").click()
        page.wait_for_timeout(300)

        # 4. Mobile Viewport
        mobile_ctx = browser.new_context(viewport={"width": 390, "height": 844}, is_mobile=True)
        m_page = mobile_ctx.new_page()
        m_page.goto(f"file:///{HTML_PATH.replace(os.sep, '/')}", wait_until="networkidle")
        m_page.screenshot(path=os.path.join(WORKSPACE_DIR, "ui_mobile_updated.png"))

        browser.close()
    print("All updated screenshots captured!")

if __name__ == "__main__":
    capture_all()
