# ЗАЯВА ПРО розширення переліку МПД (Імпорт)

def test_20_lims_test_case_3_2(app):
    app.session.login(password='111',
                      path_to_key='C:/98745612_7878789898_DU180323123055.ZS2')
    app.second_application.create_import_second_application()

    app.second_application.create_mpd_import_second(company_name='Тест4',
                           phone_number='+380123456789',
                           email='test@test.ua',
                           fax_number='+380123456789',
                           city="Дніпро",
                           index='12345',
                           street='Тестова вулиця',
                           adress='Test',
                           building='13')

    app.second_application.authorized_persons_import_second(person_name='Тест',
                                   person_middle_name='Тестович',
                                   person_last_name='4 - Тестов',
                                   person_ipn='1234567890',
                                   person_birthday='13.12.1986',
                                   education='Тест універ',
                                   graduation_year='2004',
                                   diplom_number='АП1312',
                                   graduation_date='13.12.2004',
                                   speciality='Тест',
                                   work_expirience='95', contract_number='12345',
                                   order_number='23456',
                                   date_contract='14.12.2004',
                                   date_appointment='14.12.2004',
                                   position='Тест директор',
                                   contact_information='12345',
                                   comment='Тест коментар')

    app.second_application.dossier_file_import_second(version='4 - Тест досьє',
                             comment='Тест коментар',
                             date_to='19.04.2025',
                             path_to_file='C:/masloy.png')
    app.second_application.completeness_check_import_second()
    app.second_application.add_files_import_second(path_to_file='C:/masloy.png')
    app.second_application.notifications_and_license_terms_import_second(comment='Коментар тест')
    app.second_application.submit_application_import_second(path_to_key='C:/98745612_7878789898_DU180323123055.ZS2',
                                   password='111')
    app.session.logout()
