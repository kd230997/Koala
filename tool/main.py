def main():
    from web_automation.browser import Browser
    from selenium import webdriver
    from web_automation.actions import click_element, input_text, get_element_text

    # Initialize the browser
    browser = Browser()
    browser.open_url("https://example.com")

    # Perform actions
    input_text("#search", "Python automation")
    click_element("#submit")

    # Get and print the current URL
    current_url = browser.get_current_url()
    print(f"Current URL: {current_url}")

    # Close the browser
    browser.close_browser()

if __name__ == "__main__":
    main()