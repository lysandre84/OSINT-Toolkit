#!/usr/bin/env python3
"""
screenshot_tool.py: Prendre des captures d'écran d'une page web.
Usage:
    python3 screenshot_tool.py https://example.com output.png
"""
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot(url, output):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    driver.save_screenshot(output)
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 screenshot_tool.py <url> <output_file>")
        sys.exit(1)
    take_screenshot(sys.argv[1], sys.argv[2])
