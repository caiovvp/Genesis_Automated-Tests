from behave import *

from features.fixtures import *



@given('go to {page_name}: <{link}>')
@when('go to {page_name}: <{link}>')
def step_impl(context, page_name, link):
    context.browser.get(link)
    WebDriverWait(context.browser, 8).until(EC.url_to_be(link))

@given('try go to {page_name}: <{link}>')
def step_impl(context, page_name, link):
    context.browser.get(link)

@when('type {input}: <{value}>')
def type_input(context, input, value):
    find_input(context.browser, input).send_keys(value)

@given('click on <{input}>')
@when('click on <{input}>')
@then('click on <{input}>')
def click_on_btn(context, input):
    try:
        web_ele = context.browser.find_element_by_xpath(input)
        WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.XPATH, input)))
        web_ele.click()
    except NoSuchElementException:
        try:
            web_ele = context.browser.find_element_by_id(input)
            WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.ID, input)))
            web_ele.click()
        except NoSuchElementException:
            try:
                web_ele = context.browser.find_element_by_class_name(input)
                WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, input)))
                web_ele.click()
            except NoSuchElementException:
                try:
                    web_ele = context.browser.find_element_by_link_text(input)
                    WebDriverWait(context.browser, 3).until(EC.element_to_be_clickable((By.LINK_TEXT, input)))
                    web_ele.click()
                except NoSuchElementException:
                    try:
                        link_button = find_by_link(context, input)
                        if link_button is not None:
                            link_button.click()
                    except NoSuchElementException as e:
                        raise e

@when('choose <{item_text}> from <{input}>')
def step_impl(context, item_text, input):
    list_ele = find_input(context.browser, input)
    list_itens = list_ele.find_elements_by_tag_name('option')
    for item in list_itens:
        if item.text == item_text:
            item.click()
            break

@then('redirect to {page_name}: <{link}> on window <{window_handle_number}>')
def step_impl(context, page_name, link, window_handle_number):
    window = context.browser.window_handles[int(window_handle_number) - 1]
    context.browser.switch_to_window(window)
    WebDriverWait(context.browser, 5).until(EC.url_to_be(link))

@given('user is logged in {system_name}')
def step_impl(context, system_name):
    try:
        context.execute_steps(u'''
            Given try go to Dashboard Page: <http://192.168.201.13/Genesis_ap/>
        ''')
        find_input(context.browser, 'sair')
    except NoSuchElementException:
        context.execute_steps(u'''
            When clear and type <LoginOrCPF>: <suporte.connect>
            And clear and type <Senha>: <g3n3sis>
            And click on <btn-submit>
            Then redirect to Dashboard Page: <http://192.168.201.13/Genesis_ap/> on window <1>
        '''.format(system_name, system_name))

@when('find <{text}> [type: <{input_type}>, name: <{input_name}>] in <{web_ele}>')
def step_impl(context, text, input_type, input_name, web_ele):
    web_ele = find_input(context.browser, web_ele)
    if input_type == 'tag':
        item_list = web_ele.find_elements_by_tag_name(input_name)
    if input_type == 'class':
        item_list = web_ele.find_elements_by_class_name(input_name)
    for item in item_list:
        if 'btn' in input_name:
            item.click()
            break
        else:
            if item.text == text:
                find_input(item, 'a').click()
                break

@when('find <{text}> [type: <{input_type}>, name: <{input_name}>] in <{web_ele}> (FOR LISTS)')
def step_impl(context, text, input_type, input_name, web_ele):
    web_ele = find_input(context.browser, web_ele)
    trs_list = web_ele.find_elements_by_tag_name('tr')
    for tr in trs_list:
        if text in tr.text:
            correct_tr = tr
    if input_type == 'tag':
        item_list = web_ele.find_elements_by_tag_name(input_name)
    if input_type == 'class':
        item_list = correct_tr.find_elements_by_class_name(input_name)
    for item in item_list:
        if 'btn' in input_name:
            item.click()
        else:
            if item.text == text:
                find_input(item, 'a').click()
                break
            if len(context.browser.window_handles) < 2:
                raise NoSuchElementException

@then('close browser window <{number}>')
def step_impl(context, number):
    context.browser.close()
    context.browser.switch_to_window(context.browser.window_handles[(len(number) - 2)])

@when('clear <{input_name}>')
def clear_input(context, input_name):
    find_input(context.browser, input_name).clear()

@when('clear and type <{input_name}>: <{value}>')
def step_impl(context, input_name, value):
    input = find_input(context.browser, input_name)
    WebDriverWait(context.browser, 3).until(EC.visibility_of(input))
    input.clear()
    input.send_keys(value)

@when('set <{input_id}> value to <{value}>')
def step_impl(context, input_id, value):
    context.browser.execute_script(f"document.getElementById('{input_id}').value = '{value}';")

@then('find <{web_ele}> on page')
def step_impl(context, web_ele):
    find_input(context.browser, web_ele)

@when('wait for <{time_in_sec}>')
@then('wait for <{time_in_sec}>')
def step_impl(context, time_in_sec):
    sleep_thread(float(time_in_sec))

@then('show message <{message}> on <{web_ele}>')
def step_impl(context, message, web_ele):
    show_message(context, message, web_ele)

@when('wait <{seconds}> and click on <{web_ele}>')
@then('wait <{seconds}> and click on <{web_ele}>')
def step_impl(context, seconds, web_ele):
    time.sleep(float(seconds))
    web_ele = find_input(context.browser, web_ele)
    web_ele.click()

@then('log out of {system}')
def step_impl(context, system):
    context.execute_steps(u'''
        Then wait <1> and click on <sair>
        And redirect to Login Page: <http://192.168.201.13/Genesis_ap/Security/Login> on window <1>
        And wait for <0.5>
    ''')

@when('user moves mouse cursor over <{web_ele}>')
def step_impl(context, web_ele):
    mouse_over_element(context, web_ele)

@when('go to tab <{tab_id}>')
def step_impl(context, tab_id):
    go_to_tab(context, tab_id)

