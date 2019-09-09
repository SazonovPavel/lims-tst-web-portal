# ЗАЯВА ПРО АНУЛЮВАННЯ ЛІЦЕНЗІЇ(ІМПОРТ)

def test_25_lims_test_case_3_7(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.first_application.create_import_seventh_application()
    app.first_application.add_files_import_seventh(path_to_file='C:/masloy.png')
    app.first_application.notifications_and_license_terms_import_seventh(comment='Коментар тест')
    app.first_application.submit_application_import_seventh(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
