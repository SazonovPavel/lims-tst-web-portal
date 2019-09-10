# ЗАЯВА ПРО звуження переліку МПД

def test_22_lims_test_case_3_4(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.second_application.create_import_fourth_application()
    app.second_application.delete_mpd_import_fourth()
    app.second_application.completeness_check_import_fourth()
    app.second_application.notifications_and_license_terms_import_fourth(comment='Коментар тест')
    app.second_application.submit_application_import_fourth(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
