# ЗАЯВА ПРО розширення переліку лікарських форм (Імпорт)

# Есть заминка одна
# Нужно в ручную выбирать список товаров, которые планируем импортировать
# Этот фаил тоже храниться на диске C

def test_21_lims_test_case_3_3(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.second_application.create_import_third_application()

    app.second_application.information_about_medicines_import_third()

    app.second_application.completeness_check_import_second()

    app.second_application.notifications_and_license_terms_import_third(comment='Коментар тест')

    app.second_application.submit_application_import_second(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
