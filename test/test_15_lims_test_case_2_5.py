# Заява про звуження переліку лікарських форм (Додаток 16)

def test_15_lims_test_case_2_5(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')

    app.first_application.create_fifth_application()

    app.first_application.change_mpd_fifth()

    app.first_application.notifications_and_license_terms_fourth(comment='Коментар тест')

    app.first_application.submit_application_fourth(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                             password='111')

    app.session.logout()
