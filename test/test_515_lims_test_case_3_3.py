# ЗАЯВА ПРО розширення перелыку лікарських форм

def test_15_lims_test_case_3_3(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.first_application.create_import_third_application()

    app.first_application.information_about_medicines_import_third()

    app.first_application.completeness_check_import_second()

    app.first_application.notifications_and_license_terms_import_third(comment='Коментар тест')

    app.first_application.submit_application_import_second(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
