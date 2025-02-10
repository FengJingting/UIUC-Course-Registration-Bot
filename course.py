from playwright.sync_api import sync_playwright
import time

def main():
    with sync_playwright() as p:
        # Replace with the actual WebSocket debugging URL
        ws_url = "ws://127.0.0.1:9222/devtools/browser/334787d1-3f8e-4277-bfe4-9c490e454e45"  # Replace with the URL obtained from JSON
        browser = p.chromium.connect_over_cdp(ws_url)

        # Get the context and page
        context = browser.contexts[0]  # Get the first context
        page = context.pages[0]  # Get the first page

        # Ensure the page is open and navigate to the target page
        page.goto("https://banner.apps.uillinois.edu/StudentRegistrationSSB/ssb/classRegistration/classRegistration")

        # Click the outer container to activate the dropdown options
        page.wait_for_selector("div#s2id_txt_subject")  # Wait for the container to load
        page.click("div#s2id_txt_subject")  # Click the container to activate the input box

        # Enter department name in the input box
        subject_input = page.locator("input#s2id_autogen7")  # Locate the input box
        subject_input.fill("CS")  # Fill in your department name

        # Wait for the dropdown options to load and select Computer Science
        page.wait_for_selector("div#CS")  # Wait for the target option to load(Fill in your department name)
        page.click("div#CS")  # Click to select Computer Science(Fill in your department name)

        # Enter the course number "525"
        page.fill("input#txt_courseNumber", "525")  # Fill in your course number

        # Click the search button
        page.click("button#search-go")

        # Check course status
        page.wait_for_selector("span.status-bold")  # Wait for the status element to load
        status_element = page.locator("span.status-bold")
        status_text = status_element.text_content().strip()  # Get the status text

        while True:
            try:
                # Check course status
                page.wait_for_selector("span.status-bold")
                status_element = page.locator("span.status-bold")
                status_text = status_element.text_content().strip()

                if status_text == "FULL":
                    print("Seats are full, clicking 'Search Again' button...")
                    time.sleep(7) # be polite!
                    # Click the Search Again button
                    page.click("button#search-again-button")
                    page.wait_for_selector("button#search-go")  # Wait for the search button to reload
                    page.click("button#search-go")  # Execute the search again
                else:
                    print("Seats available, clicking 'Add' button...")
                    # Click the Add button
                    add_button = page.locator("button#addSection12025146186")  # Replace with the actual button ID or selector
                    add_button.click()

                    # Click the Submit button
                    submit_button = page.locator("button#saveButton")
                    submit_button.click()

                    print("Course successfully added and submitted.")
                    break  # Exit the loop
            except Exception as e:
                print(f"An error occurred: {e}")
                continue  # If an error occurs, continue the loop

        # Keep the browser open to review the result
        input("Press Enter to close the browser...")
        browser.close()

if __name__ == "__main__":
    main()
