from playwright.sync_api import sync_playwright
import time

def fetch_case_details_delhi(case_type, case_number, filing_year, max_retries=3):
    attempt = 0
    last_error = None

    while attempt < max_retries:
        attempt += 1
        print(f"Attempt {attempt} of {max_retries}...")

        try:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True, slow_mo=200)  # slow_mo for stability
                page = browser.new_page()

                # Load the case search page
                page.goto("https://delhihighcourt.nic.in/case.asp", wait_until="domcontentloaded")

                # Wait for form to load
                page.wait_for_selector("#ddlCaseType", timeout=15000)
                page.select_option("#ddlCaseType", case_type)

                # Fill in case details
                page.fill("#txtCaseNo", case_number)
                page.fill("#txtCaseYear", filing_year)

                # Click Search
                page.click("#btnSearch")

                # Wait for results to appear
                try:
                    page.wait_for_selector("xpath=//*[contains(text(),'Petitioner')]", timeout=20000)
                except:
                    raise Exception("Results did not load — possible invalid case or site timeout.")

                html = page.content()
                data = {}

                # Extract details
                data['petitioner'] = page.locator(
                    "xpath=//*[contains(text(),'Petitioner')]//following::td[1]"
                ).inner_text(timeout=5000)

                data['respondent'] = page.locator(
                    "xpath=//*[contains(text(),'Respondent')]//following::td[1]"
                ).inner_text(timeout=5000)

                data['filing_date'] = page.locator(
                    "xpath=//*[contains(text(),'Filing Date')]//following::td[1]"
                ).inner_text(timeout=5000)

                data['next_date'] = page.locator(
                    "xpath=//*[contains(text(),'Next Date')]//following::td[1]"
                ).inner_text(timeout=5000)

                pdf_element = page.locator("a[href*='.pdf']").first
                data['pdf_link'] = pdf_element.get_attribute("href") if pdf_element.count() > 0 else None

                browser.close()
                return html, data

        except Exception as e:
            last_error = e
            print(f"Error: {e}")
            if attempt < max_retries:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries reached. Giving up.")

    raise last_error


