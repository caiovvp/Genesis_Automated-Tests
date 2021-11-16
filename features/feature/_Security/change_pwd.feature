Feature: Change user password being logged in to Genesis

  Background:
    Given user is logged in Genesis
    When wait for <1>
    And user moves mouse cursor over <gerenciar>
    And click on <alterar-senha>

    Scenario: Empty inputs
      When wait <2> and click on <alterar>
      Then show message <O campo Senha Atual é obrigatório> on <jquery-message error>
      Then show message <O campo Nova Senha é obrigatório> on <jquery-message error>
      Then show message <O campo Confirmar Senha é obrigatório> on <jquery-message error>

    Scenario: Invalid old password
      When clear and type <SenhaAtual>: <senha_errada>
      And clear and type <NovaSenha>: <genesis>
      And clear and type <ConfirmarSenha>: <genesis>
      Then show message <O campo Confirmar Senha é obrigatório> on <jquery-message error>

    Scenario: Old and new passwords are the same
      When clear and type <SenhaAtual>: <g3n3sis>
      And clear and type <NovaSenha>: <g3n3sis>
      And clear and type <ConfirmarSenha>: <g3n3sis>
      Then show message <O campo Confirmar Senha é obrigatório> on <jquery-message error>


    Scenario: Change password sucessfully
      When clear and type <SenhaAtual>: <g3n3sis>
      And clear and type <NovaSenha>: <SenhaNova>
      And clear and type <ConfirmarSenha>: <SenhaNova>
      Then dont find <Senha Atual>


  Scenario: Log with new password
    When click on <sair>
    Then log with new password: <SenhaNova>


  Scenario: Reset password to original
    When clear and type <SenhaAtual>: <SenhaNova>
    And clear and type <NovaSenha>: <g3n3sis>
    And clear and type <ConfirmarSenha>: <g3n3sis>


