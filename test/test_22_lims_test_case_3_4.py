# ЗАЯВА ПРО звуження переліку МПД

# Ошибка на строке 1819 (Хуй поймешь почему падает !!!)

def test_22_lims_test_case_3_4(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.first_application.create_import_fourth_application()
    app.first_application.delete_mpd_import_fourth()
    app.first_application.completeness_check_import_fourth()
    app.first_application.notifications_and_license_terms_import_fourth(comment='Коментар тест')
    app.first_application.submit_application_import_fourth(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
