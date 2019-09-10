# ЗАЯВА ПРО ЗАМІНУ ПЕРЕЛІКУ ЛІКАРСЬКИХ ЗАСОБІВ, ЩО ІМПОРТУЄ ЛІЦЕНЗІАТ (ІМПОРТ)

def test_23_lims_test_case_3_5(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.second_application.create_import_fifth_application()
    app.second_application.information_about_medicines_import_third()
    app.second_application.completeness_check_import_fifth()
    app.second_application.notifications_and_license_terms_import_fifth(comment='Коментар тест')
    app.second_application.submit_application_import_fifth(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
