# Заява про зміну контрактних контрагентів


def test_17_lims_test_case_2_7(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')

    app.first_application.create_seventh_application()

    app.first_application.contract_contractors_seventh(edrpou='12345678',
                                               name_contractor='Тест5-1',
                                               adress='Тест5-1')

    app.first_application.notifications_and_license_terms_fourth(comment='Коментар тест')

    app.first_application.submit_application_fourth(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                                    password='111')

    app.session.logout()
