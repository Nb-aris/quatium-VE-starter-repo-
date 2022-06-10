import dash
from dash import html
from task4 import dashAPP

from selenium.webdriver.chrome.options import Options

def pytest_setup_options():
    options = Options()
    options.add_argument('--disable-gpu')
    return options


def test_header_exists(dash_duo):
    dash_duo.start_server(dashAPP)
    dash_duo.wait_for_element("#header", timeout=20)


def test_visualization_exists(dash_duo):
    dash_duo.start_server(dashAPP)
    dash_duo.wait_for_element("#visualization", timeout=20)


def test_region_picker_exists(dash_duo):
    dash_duo.start_server(dashAPP)
    dash_duo.wait_for_element("#region_picker", timeout=20)



