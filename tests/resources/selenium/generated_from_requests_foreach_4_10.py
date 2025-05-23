# coding=utf-8

import logging
import random
import string
import sys
import unittest
from time import time, sleep

import apiritif

import os
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as econd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.options import ArgOptions
from bzt.resources.selenium_extras import waiter, get_elements, get_locator

class TestLocSc(unittest.TestCase):

    def setUp(self):
        self.vars = {'city_select_name': 'fromPort', 'input_name_id': 'inputName'}

        timeout = 3.5
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.set_capability('unhandledPromptBehavior', 'ignore')
        service = Service(service_args=['--log-path=/somewhere/webdriver.log'])
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(timeout)
        apiritif.put_into_thread_store(timeout=timeout, func_mode=False, driver=self.driver, windows={},
                                       scenario_name='loc_sc')


    def _1_Foreach_test(self):
        with apiritif.smart_transaction('Foreach test'):

            elements = get_elements([{'css': 'input'}, {'xpath': '/table/input/'}])
            for el in elements:
                self.assertEqual(el.get_attribute('innerText').strip(), 'text'.strip())

                var_loc_as = get_locator([{'css': 'style'}, {'xpath': '//tr'}], el)
                self.assertEqual(el.find_element(
                    var_loc_as[0],
                    var_loc_as[1]).get_attribute('innerText').strip(), 'text'.strip())
                self.assertEqual(el.get_attribute('value').strip(), 'value'.strip())
                self.assertEqual(el.get_attribute('value').strip(), 'value'.strip())

                if el.get_attribute('contenteditable'):
                    self.driver.execute_script(("arguments[0].innerHTML = '%s';" % 'new text'), el)
                else:
                    raise NoSuchElementException(("The element '%s' (tag name: '%s', text: '%s') is not a contenteditable element" % ('el', el.tag_name, el.text)))

                if el.get_attribute('contenteditable'):
                    self.driver.execute_script(("arguments[0].innerHTML = '%s';" % 'new text'), el)
                else:
                    raise NoSuchElementException(("The element '%s' (tag name: '%s', text: '%s') is not a contenteditable element" % ('el', el.tag_name, el.text)))
                el.click()
                waiter()

                var_loc_keys = get_locator([{'css': 'input-cls'}, {'xpath': '//input'}], el)
                el.find_element(
                    var_loc_keys[0],
                    var_loc_keys[1]).click()
                waiter()
                ActionChains(self.driver).double_click(el).perform()
                waiter()
                ActionChains(self.driver).double_click(el).perform()
                waiter()
                ActionChains(self.driver).context_click(el).perform()
                waiter()
                ActionChains(self.driver).context_click(el).perform()
                waiter()
                ActionChains(self.driver).click_and_hold(el).perform()
                ActionChains(self.driver).click_and_hold(el).perform()
                ActionChains(self.driver).release(el).perform()
                ActionChains(self.driver).release(el).perform()
                ActionChains(self.driver).move_to_element_with_offset(el, -10, -10).perform()
                ActionChains(self.driver).move_to_element_with_offset(el, -10, -10).perform()
                ActionChains(self.driver).move_to_element(el).perform()
                ActionChains(self.driver).move_to_element(el).perform()

                target = get_locator([{'id': 'id12'}])
                ActionChains(self.driver).drag_and_drop(el, self.driver.find_element(
                    target[0],
                    target[1])).perform()
                waiter()

                source = get_locator([{'id': 'id34'}])
                ActionChains(self.driver).drag_and_drop(self.driver.find_element(
                    source[0],
                    source[1]), el).perform()
                waiter()

                target = get_locator([{'id': 'id12'}])
                ActionChains(self.driver).drag_and_drop(el, self.driver.find_element(
                    target[0],
                    target[1])).perform()
                waiter()

                source = get_locator([{'id': 'id34'}])
                ActionChains(self.driver).drag_and_drop(self.driver.find_element(
                    source[0],
                    source[1]), el).perform()
                waiter()
                Select(el).select_by_visible_text('value')
                waiter()
                Select(el).select_by_visible_text('value')
                waiter()

                self.vars['my_var'] = el.get_attribute('innerText')

                self.vars['my_var'] = el.get_attribute('innerText')

                self.vars['my_var'] = el.get_attribute('value')

                self.vars['my_var'] = el.get_attribute('value')
                el.clear()
                el.send_keys('text')
                waiter()
                el.clear()
                el.send_keys('text')
                waiter()
                el.clear()
                el.send_keys('passwd')
                el.clear()
                el.send_keys('passwd')
                el.submit()
                el.submit()
                el.send_keys(Keys.ENTER)
                el.send_keys(Keys.ENTER)

    def test_locsc(self):
        self._1_Foreach_test()

    def tearDown(self):
        if self.driver:
            self.driver.quit()
