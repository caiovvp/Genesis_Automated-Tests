from behave import *

from features.fixtures import *


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
        ''')

@then('log out of {system}')
def step_impl(context, system):
    context.execute_steps(u'''
        Then wait <1> and click on <sair>
        And redirect to Login Page: <http://192.168.201.13/Genesis_ap/Security/Login> on window <1>
        And wait for <0.5>
    ''')

@then('log with new password: <{new_pwd}>')
def step_impl(context, new_pwd):
    try:
        context.execute_steps(u'''
            Given try go to Dashboard Page: <http://192.168.201.13/Genesis_ap/>
        ''')
        find_input(context.browser, 'sair')
    except NoSuchElementException:
        context.execute_steps(u'''
            When clear and type <LoginOrCPF>: <suporte.connect>
            And clear and type <Senha>: <{}>
            And click on <btn-submit>
            Then redirect to Dashboard Page: <http://192.168.201.13/Genesis_ap/> on window <1>
        '''.format(new_pwd))