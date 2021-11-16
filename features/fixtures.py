import datetime
import random
import time

from ipython_genutils.py3compat import xrange
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# FUNCTION THAT INSTANCES THAT THE BROWSER IS CHROME AND THAT IT QUITS ONCE THE TEST IS OVER
def browser_firefox(context):
    # -- BEHAVE-FIXTURE: Similar to @contextlib.contextmanager
    # -- IF WANT TO RUN ON CONNECT REMOTE SERVER
    # capability = DesiredCapabilities.FIREFOX
    # context.browser = Remote('http://srv01.connect.com.vc:4444/wd/hub', capability)
    # -- IF WANT TO RUN ON LOCAL MACHINE FIREFOX
    context.browser = Firefox(executable_path='C:\Selenium WebDriver\geckodriver.exe')
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    # context.browser.quit()


# FUNCTION TO TIMEOUT THE TEST IF NECESSARY
def timeout_for_page_load(context):
    context.browser.set_page_load_timeout(5)


# -- NOTE: Change False for True if you want ipdb debugger running when an error happens
BEHAVE_DEBUG_ON_ERROR = False
def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


# CONFIRMS IF MESSAGE BOX IS SHOWN AND ASSERT MESSAGE IN BOX.TEXT
def show_message(context, message, element):
    WebDriverWait(context.browser, 3).until(EC.text_to_be_present_in_element((By.CLASS_NAME, element), message))
    web_ele = find_input(context.browser, element)
    assert message in web_ele.text


# RETURNS A WEB ELEMENT THAT CONTAINS THE HREF "LINK" IN ITS PROPERTIES
def find_by_link(context, link):
    anchors_list = context.browser.find_elements_by_tag_name('a')
    for element in anchors_list:
        if link in element.get_attribute('href'):
            element_parent = element.find_element_by_xpath('..')
            return element_parent


# CALCULATES A RANDOM CPF AND RETURNS IT (NOT FORMATTED, ONLY NUMBERS)
def cpf():
    def calculate_cpf(digs):
        s = 0
        qtd = len(digs)
        for i in xrange(qtd):
            s += n[i] * (1 + qtd - i)
        res = 11 - s % 11
        if res >= 10:
            return 0
        return res

    n = [random.randrange(10) for i in xrange(9)]
    n.append(calculate_cpf(n))
    n.append(calculate_cpf(n))
    return "%d%d%d%d%d%d%d%d%d%d%d" % tuple(n)


# CALCULATES A RANDOM INDEX FOR AN ITEM ON A LIST
def random_option(options_list):
    if len(options_list) == 1:
        random_num = 0
    else:
        random_num = random.randint(0, (len(options_list) - 1))
    return random_num


# GENERATE RANDOM DATE TIME AND RETURNS IT
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_datetime = start_date + datetime.timedelta(days=random_number_of_days)
    return random_datetime.strftime('%d\%m\%Y')


# SAVE THE INPUT VALUE AND CLEAR IT LATER
def save_and_clear(input):
    input_value = input.get_attribute('value')
    input.clear()
    return input_value


# FIND AN INPUT ON THE PAGE AND CLEAR IT
def find_and_clear_input(context, id):
    input = context.browser.find_element_by_id(id)
    input.clear()
    return input


# GENERATES RANDOM INTEGERS ACCORDING TO THE RANGE GIVEN
def random_numbers(web_ele, num_quantity):
    for num in range(num_quantity):
        web_ele.send_keys(f'{random.randint(0, 9)}')


# FIND INPUT BY XPATH OR ID OR CLASS NAME
def find_input(general_context, input):
    try:
        input = general_context.find_element_by_xpath(input)
        return input
    except NoSuchElementException:
        try:
            input = general_context.find_element_by_id(input)
            return input
        except NoSuchElementException:
            try:
                input = general_context.find_element_by_class_name(input)
                return input
            except NoSuchElementException:
                try:
                    input = general_context.find_element_by_name(input)
                    return input
                except NoSuchElementException:
                    try:
                        input = general_context.find_element_by_tag_name(input)
                        return input
                    except NoSuchElementException as e:
                        raise e


# STOPS THE PROCESS THREAD FROM EXECUTING CODE FOR "X" AMOUNT OF SECONDS
def sleep_thread(time_in_secs):
    time.sleep(time_in_secs)


def mouse_over_element(context, web_ele):
    element = find_input(context.browser, web_ele)
    ActionChains(context.browser).move_to_element(element).perform()

def go_to_tab(context, tab_id):
    tabs_div = find_input(context.browser, 'ui-tabs-nav')
    tab = find_input(tabs_div, tab_id)
    if 'ui-tabs-selected' not in tab.get_attr('class'):
        tab.click()

