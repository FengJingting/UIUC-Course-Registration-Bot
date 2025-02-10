# UIUC Course Registration Robot

This script automates the process of checking course availability on the University of Illinois registration system and automatically adds the course when a seat becomes available.

## Prerequisites

Before running the script, ensure you have the following installed
(The tutorial is based on Mac system, you can use your owns! Just ask GPT how to edit lol):

- macOS
- Python 3.x
- Playwright library

## Installation

1. Install Python dependencies:

   ```sh
   pip install playwright
   ```

## Usage

1. Start a Chromium instance with debugging enabled. Open a terminal and run:

   ```sh
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
   ```

2. You should first log in to your account and go to the course registration page.
 
4. Obtain the WebSocket debugging URL by navigating to:

   ```
   http://127.0.0.1:9222/json
   ```
   Copy the `webSocketDebuggerUrl` value.

5. Update the script:
   - Replace the `ws_url` variable with the copied WebSocket URL.

6. Change the deparment name
   ```python
    subject_input.fill("CS")  # Fill in your department name
    page.wait_for_selector("div#CS")  # Fill in your department name
   ```
   Change the course name, you should inspect the webpage to see the id
   ```python
    page.fill("input#txt_courseNumber", "525")  # Fill in your course name
    add_button = page.locator("button#addSection12025146186")  # Replace with the actual button ID or selector(Inspect the web page to find)
   ```
7. Run the script:

   ```sh
   python script.py
   ```

8.  Follow on-screen prompts to monitor course availability.

## Notes

- Ensure that Playwright is correctly installed and the Chromium instance is running.
- Modify the course and subject parameters in the script if necessary.
- If the course is full, the script will automatically retry until a seat is available.
- Once a seat is available, it will attempt to add and submit the course registration.
- Be polite when web scraping!
- Before attempting to register for a course, test the script with a less popular course to ensure it runs correctly on your computer.
- This script saves you from manually refreshing the page repeatedly, but you can also use it just to refresh the page and check seat availability with your own eyes.
- While this script can successfully register for a course, it is not entirely stable. If you have a better solution, feel free to contribute.
- A more stable version will be released after testing in the next semester's course registration period.
- (The market value of course registration bots is $50, which surprised me!)


## License

This script is for personal use only. Modify it at your own risk.

