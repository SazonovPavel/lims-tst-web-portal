# ЗАЯВА ПРО ЗМІНУ ІНФОРМАЦІЇ У ДОДАТКУ ДО ЛІЦЕНЗІЇ ЩОДО ОСОБЛИВИХ УМОВ ПРОВАДЖЕННЯ ДІЯЛЬНОСТІ - ЗМІНА УПОВНОВАЖЕНИХ ОСІБ 6

# Не доделано !!!

def test_24_lims_test_case_3_6(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.second_application.create_import_sixth_application()







#    app.first_application.completeness_check_import_fifth()






    app.second_application.notifications_and_license_terms_import_sixth(comment='Коментар тест')
    app.second_application.submit_application_import_sixth(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
