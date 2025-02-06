from browser_use.browser.browser import Browser, BrowserConfig


main_browser = Browser(
  config=BrowserConfig(
    headless=False,
    chrome_instance_path='/opt/brave.com/brave/brave',
  )
)

def init_browser():
  return Browser(
    config=BrowserConfig(
      headless=False,
      chrome_instance_path='/opt/brave.com/brave/brave',
    )
  )