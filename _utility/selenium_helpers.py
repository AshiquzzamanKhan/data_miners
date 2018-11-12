# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import os

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

from _utility.configure import timer

def get_driver(proxy_server=None, popups=False, headless=False):

    _executable_path = os.path.abspath('../_selenium/_webdrivers/chromedriver.exe')  # the location of the binary file
    _options = webdriver.ChromeOptions()                            # initializing chrome options
    if headless:
        _options.add_argument('headless')                           # headless mode of the browser
    if popups:
        _options.add_argument("--disable-popup-blocking")           # popups disabled
    if proxy_server:
        _options.add_argument(f'--proxy-server={proxy_server}')     # proxy server added

    _capabilities = DesiredCapabilities.CHROME.copy()               # copying all capabilities of original chrome
    _capabilities['acceptSslCerts'] = True                          # accepting ssl certificates
    _capabilities['acceptInsecureCerts'] = True                     # accepting non valid certificates

    return webdriver.Chrome(chrome_options=_options,
                            executable_path=_executable_path,
                            desired_capabilities=_capabilities)


def close(driver):
    """
    functions for closing the web driver
    :param driver: the web driver object
    :return:
    """
    driver.close()                                                  # closing the driver


def fast_scroll(driver, timeout, element="document.body"):
    """
    functions for scrolling the page fast
    :param driver: web driver object
    :param timeout: one decimal point value
    :param element: the element which needs to be scrolled in html
    :return:
    """
    last_height = driver.execute_script(f"return {element}.scrollHeight")     # Get scroll height
    while True:
        driver.execute_script(f"window.scrollTo(0, {element}.scrollHeight);")  # Scroll down to bottom
        timer(timeout)  # Wait to load page
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script(f"return {element}.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    timer(timeout)


def slow_scroll():
    pass


def login(driver, timeout, username, password, login_url):
    """
    functions for login to facebook
    :param _driver: the web driver object
    :param _username: a string provided by the flask input
    :param _password: a string provided by the flask input
    :return:
    """
    driver.get(login_url)                                  # get the login page
    timer(timeout)                                         # wait for the page to load
    _username = driver.find_element_by_id("m_login_email")  # find the username input
    _username.send_keys(username)                           # pass the username
    _password = driver.find_element_by_name("pass")
    # password = _driver.find_element_by_id("m_login_password")# find the password input
    _password.send_keys(password)                           # pass the password
    _password.send_keys(Keys.RETURN)                         # simulate enter / return key of keyboard
    timer(timeout)                                         # wait for the next page to load