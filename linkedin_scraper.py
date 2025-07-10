from playwright.sync_api import sync_playwright

def scrape_linkedin_job(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)

        try:
            # This waits for the job description section to load
            page.wait_for_selector("div.description__text", timeout=10000)
            job_desc = page.locator("div.description__text").inner_text()
        except:
            job_desc = "❌ Failed to extract job description. Make sure you're using a direct job listing URL."

        browser.close()
        return job_desc
        