# Login and logout  Авторизування в системі через АЦСК “Центр сертифікації ключів “Україна” (Відсутні данні про пароль)

def test_3_lims_test_case_1_3(app):
    app.session.login_third(password='', path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')

