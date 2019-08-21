# Login Авторизування в системі через АЦСК “Центр сертифікації ключів “Україна” (Коректний ключ та невірний пароль)

def test_7_lims_test_case_1_7(app):
    app.session.login_seventh(password='222', path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')

