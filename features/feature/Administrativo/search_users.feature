@autoretry
Feature: Login into Genesis

  Background:
    Given go to Login Page: <http://192.168.201.13/Genesis_ap/Security/Login>

    Scenario: Try go to Dashboard without logging in
      Given try go to Dashboard Page: <http://192.168.201.13/Genesis_ap/>
      Then redirect to Login Page: <http://192.168.201.13/Genesis_ap/Security/Login> on window <1>

    Scenario: Valid credentials
      When clear and type <LoginOrCPF>: <suporte.connect>
      And clear and type <Senha>: <g3n3sis>
      And click on <btn-submit>
      Then redirect to Dashboard Page: <http://192.168.201.13/Genesis_ap/> on window <1>
      And log out of Genesis
      When clear and type <LoginOrCPF>: <654.743.182-78>
      And clear and type <Senha>: <g3n3sis>
      And click on <btn-submit>
      Then redirect to Dashboard Page: <http://192.168.201.13/Genesis_ap/> on window <1>
      And log out of Genesis

    Scenario: Invalid credentials
      When clear and type <LoginOrCPF>: <a@?:P!1234a@?:P!1234a@?:P!1234a@?:P!1234a@?:P!1234>
      And clear and type <Senha>: <a@?:P!1234a@?:P!1234a@?:P!1234a@?:P!1234a@?:P!1234>
      And click on <btn-submit>
      Then show message <Usuário ou Senha Incorretos> on <error>

    Scenario: Empty credentials
      When clear <LoginOrCPF>
      And clear <Senha>
      And click on <btn-submit>
      Then show message <Usuário ou Senha em Branco> on <error>
      When clear and type <LoginOrCPF>: <suporte.connect>
      Then show message <Usuário ou Senha em Branco> on <error>
      When clear <LoginOrCPF>
      And clear and type <Senha>: <wrong_pwd>
      Then show message <Usuário ou Senha em Branco> on <error>
