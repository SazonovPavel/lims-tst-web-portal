import time

class FirstApplicationHelper:

    def __init__(self, app):
        self.app = app

    def create_first_application(self, pib, email, phone_number, fax_number, city, flat, street, index,
                                 number_national_account, requisits_number_national_account, number_foreign_account,
                                 requisits_number_forein_account, duns_number):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про отримання ліцензії на провадження діяльності з виробництва лікарських засобів (промислового)» (додаток 2)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a").click()

        # Заповнюємо форму: Організаційно-правова форма* «460 Громадська організація»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div/div/div/ul/li[2]/span").click()

        # Заповнюємо форму: Форма власності «40 Власність інших держав»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div[2]/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div[2]/div/div/ul/li[2]/span").click()

        # Заповнюємо форму: Прізвищеб ім'я по батькові керівника юридичної особи  «Ступка Богдан Сильвестрович»
        wd.find_element_by_xpath("//input[@id='OrgDirector']").send_keys(pib)

        # Заповнюємо форму: E-mail* «test@test.ua»
        wd.find_element_by_xpath("//input[@id='EMail']").send_keys(email)

        # Заповнюємо форму: Номер телефону* «+380123456789»
        wd.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys(phone_number)

        # Заповнюємо форму: Номер факсу «+380123456789»
        wd.find_element_by_xpath("//input[@id='FaxNumber']").send_keys(fax_number)

        # Заповнюємо форму: Населений пункт* «Дніпропетровська область, Тернівка»
        wd.find_element_by_xpath("//input[@id='CityName']").send_keys(city)
        wd.find_element_by_xpath("//div[contains(.,'Дніпро')]").click()

        # Заповнюємо форму: Номер будинку, корпус або будівля, номер квартири або офісу* «13»
        wd.find_element_by_xpath("//input[@id='Building']").send_keys(flat)

        # Заповнюємо форму: Вулиця* (натискаємо синій квадрат з білим хрестиком посередині, зявляеться вікно додавання, у полі тип вулиці обераємо – проспект, у полі Назва вулиці пишемо «Тест» натискаємо кнопку СТВОРИТИ)
#        wd.find_element_by_xpath("//button[@id='btn-street']").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/div").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/ul/li[2]/span").click()
#        wd.find_element_by_xpath("//input[@id='Name']").send_keys(street)
#        time.sleep(1)
#        wd.find_element_by_xpath("//input[@value='Створити']").click()

        wd.find_element_by_xpath("//input[@id='StreetName']").send_keys("Тестова")
        time.sleep(2)
        wd.find_element_by_xpath("//div[contains(.,'вул. Тестова Вулиця')]").click()

        # Заповнюємо форму: Поштовий індекс* «12345»
        wd.find_element_by_xpath("//input[@id='PostIndex']").send_keys(index)

        # Заповнюємо форму: Номер рахунку в національній валюті «12345»
        wd.find_element_by_xpath("//input[@id='NationalAccount']").send_keys(number_national_account)

        # Заповнюємо форму: Реквизити банку з рахунком в національній валюті «23456»
        wd.find_element_by_xpath("//input[@id='NationalBankRequisites']").send_keys(requisits_number_national_account)

        # Заповнюємо форму: Номер рахунку в іноземній валюті «34567»
        wd.find_element_by_xpath("//input[@id='InternationalAccount']").send_keys(number_foreign_account)

        # Заповнюємо форму: Реквизити банку з рахунком в іноземній валюті «45678»
        wd.find_element_by_xpath("//input[@id='InternationalBankRequisites']").send_keys(
            requisits_number_forein_account)

        # Заповнюємо форму: D-U-N-S номер (за наявності) «56789»
        wd.find_element_by_xpath("//input[@id='Duns']").send_keys(duns_number)
        time.sleep(3)
        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def create_mpd(self, company_name, phone_number, email, fax_number, city, index, street, adress, building):
        wd = self.app.wd
        # Натискаємо кнопку «Місця проваждження діяльності»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Натискаємо кнопку «Додати МПД» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення провадження діяльності: Найменування структурного підрозділу (або найменування юридичної особи):* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(company_name)

        # Заповнюємо форми Створення провадження діяльності: Номер телефону* «+380123456789»
        wd.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys(phone_number)

        # Заповнюємо форми Створення провадження діяльності: E-mail* «test@test.ua»
        wd.find_element_by_xpath("//input[@id='EMail']").send_keys(email)

        # Заповнюємо форми Створення провадження діяльності: Номер факсу* «+380123456789»
        wd.find_element_by_xpath("//input[@id='FaxNumber']").send_keys(fax_number)

        # Заповнюємо форми Створення провадження діяльності: Населений пункт* «Дніпропетровська область, Дніпро»
        wd.find_element_by_xpath("//input[@id='CityName']").send_keys(city)
        wd.find_element_by_xpath("//div[contains(.,'Дніпро')]").click()

        # Заповнюємо форми Створення провадження діяльності: Поштовий індекс* «12345»
        wd.find_element_by_xpath("//input[@id='PostIndex']").send_keys(index)

        # Заповнюємо форми Створення провадження діяльності: Вулиця* (натискаємо синій квадрат з білим хрестиком посередині, зявляеться вікно додавання вулиці, у полі тип вулиці обераємо – проспект, у полі Назва вулиці пишемо «Тест» натискаємо кнопку СТВОРИТИ)
#        wd.find_element_by_xpath("//button[@id='btn-street']").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/div").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/ul/li[2]/span").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[3]/input").send_keys(street)
#        time.sleep(2)
#        wd.find_element_by_xpath("//input[@value='Створити']").click()

        wd.find_element_by_xpath("//input[@id='StreetName']").send_keys("Тестова")
        time.sleep(2)
        wd.find_element_by_xpath("//div[contains(.,'вул. Тестова Вулиця')]").click()

        # Заповнюємо форми Створення провадження діяльності: Адреса місця провадження діяльності (англійською)* «Test»
#        wd.find_element_by_xpath("//input[@id='AdressEng']").send_keys(adress)

        # Заповнюємо форми Створення провадження діяльності: Номер будинку, корпус або будівля, номер квартири або офісу* «13»
        wd.find_element_by_xpath("//input[@id='Building']").send_keys(building)

        time.sleep(2)
        # Обераємо чекбокс «Виробничі дільниці з переліком лікарських форм*»
        wd.find_element_by_xpath("//form[@id='editBranch']/div[3]/div/label").click()

        # Обераємо чекбокс «1. ВИРОБНИЧІ ОПЕРАЦІЇ - ЛІКАРСЬКІ ФОРМИ»
        wd.find_element_by_xpath("//div[@id='content-tree']/ul/li/div/label").click()
        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@id='submitBranch']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def contract_contractors(self, edrpou, name_contractor, adress):
        wd = self.app.wd
        # Натискаємо кнопку «Контрактні контрагенти»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[3]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати Контрактного контрагента» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення Контрактного контрагента: Тип контрагента* обираемо вариант «Контрактна лабораторія»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/ul/li[2]/span").click()

        # Заповнюємо форми Створення Контрактного контрагента: ЄДРПОУ/ІПН* «12345678»(мінімальна кількість знаків 8 шт.)
        wd.find_element_by_xpath("//input[@id='Edrpou']").send_keys(edrpou)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування суб'єкта господарювання «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(name_contractor)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування, місце провадження діяльності* «Тест»
        wd.find_element_by_xpath("//input[@id='Address']").send_keys(adress)

        # Заповнюємо форми Створення Контрактного контрагента: Оберіть МПД «Тест1»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест1')]").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def contract_contractors_2(self, edrpou, name_contractor, adress):
        wd = self.app.wd
        # Натискаємо кнопку «Контрактні контрагенти»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[3]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати Контрактного контрагента» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення Контрактного контрагента: Тип контрагента* обираемо вариант «Контрактна лабораторія»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/ul/li[2]/span").click()

        # Заповнюємо форми Створення Контрактного контрагента: ЄДРПОУ/ІПН* «12345678»(мінімальна кількість знаків 8 шт.)
        wd.find_element_by_xpath("//input[@id='Edrpou']").send_keys(edrpou)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування суб'єкта господарювання «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(name_contractor)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування, місце провадження діяльності* «Тест»
        wd.find_element_by_xpath("//input[@id='Address']").send_keys(adress)

        # Заповнюємо форми Створення Контрактного контрагента: Оберіть МПД «Тест2»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест2')]").click()


        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def contract_contractors_3(self, edrpou, name_contractor, adress):
        wd = self.app.wd
        # Натискаємо кнопку «Контрактні контрагенти»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[3]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати Контрактного контрагента» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення Контрактного контрагента: Тип контрагента* обираемо вариант «Контрактна лабораторія»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/ul/li[2]/span").click()

        # Заповнюємо форми Створення Контрактного контрагента: ЄДРПОУ/ІПН* «12345678»(мінімальна кількість знаків 8 шт.)
        wd.find_element_by_xpath("//input[@id='Edrpou']").send_keys(edrpou)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування суб'єкта господарювання «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(name_contractor)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування, місце провадження діяльності* «Тест»
        wd.find_element_by_xpath("//input[@id='Address']").send_keys(adress)

        # Заповнюємо форми Створення Контрактного контрагента: Оберіть МПД «Тест3»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест3')]").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")



    def authorized_persons(self, person_name, person_middle_name, person_last_name, person_ipn, person_birthday,
                           education, graduation_year, diplom_number, graduation_date, speciality, work_expirience,
                           contract_number, order_number, date_contract, date_appointment, position,
                           contact_information, comment):
        wd = self.app.wd

        # Натискаємо кнопку «Уповноважені особи»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[4]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати уповноважену особу» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення уповноваженної особи: Ім'я* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(person_name)

        # Заповнюємо форми Створення уповноваженної особи: По батькові* «Тестович»
        wd.find_element_by_xpath("//input[@id='MiddleName']").send_keys(person_middle_name)

        # Заповнюємо форми Створення уповноваженної особи: Прізвище* «Тестов»
        wd.find_element_by_xpath("//input[@id='LastName']").send_keys(person_last_name)

        # Заповнюємо форми Створення уповноваженної особи: ІПН «» (10 цифр)
        wd.find_element_by_xpath("//input[@id='IPN']").send_keys(person_ipn)

        # Заповнюємо форми Створення уповноваженної особи: Дата народження* «13.12.1986»
        wd.find_element_by_xpath("//input[@id='Birthday']").send_keys(person_birthday)

        # Заповнюємо форми Створення уповноваженної особи: Найменування навчального закладу «»
        wd.find_element_by_xpath("//input[@id='EducationInstitution']").send_keys(education)

        # Заповнюємо форми Створення уповноваженної особи: Рік закінчення навчального закладу «2004»
        wd.find_element_by_xpath("//input[@id='YearOfGraduation']").send_keys(graduation_year)

        # Заповнюємо форми Створення уповноваженної особи: Серія і номер диплому* «АП1312»
        wd.find_element_by_xpath("//input[@id='NumberOfDiploma']").send_keys(diplom_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата видачі диплому* «13.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfGraduation']").send_keys(graduation_date)

        # Заповнюємо форми Створення уповноваженної особи: Спеціальність «Тест»
        wd.find_element_by_xpath("//input[@id='Speciality']").send_keys(speciality)

        # Заповнюємо форми Створення уповноваженної особи: Стаж роботи за фахом(місяців) «95»
        wd.find_element_by_xpath("//input[@id='WorkExperience']").send_keys(work_expirience)

        # Заповнюємо форми Створення уповноваженної особи: Номер трудового договору «12345»
        wd.find_element_by_xpath("//input[@id='NumberOfContract']").send_keys(contract_number)

        # Заповнюємо форми Створення уповноваженної особи: Номер наказу про покладання обов'язків 23456
        wd.find_element_by_xpath("//input[@id='OrderNumber']").send_keys(order_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата трудового договору «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfContract']").send_keys(date_contract)

        # Заповнюємо форми Створення уповноваженної особи: Дата наказу про покладання обовєязків «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfAppointment']").send_keys(date_appointment)

        # Заповнюємо форми Створення уповноваженної особи: Посада «Тест директор»
        wd.find_element_by_xpath("//input[@id='NameOfPosition']").send_keys(position)

        # Заповнюємо форми Створення уповноваженної особи: Контактна інформація «12345»
        wd.find_element_by_xpath("//input[@id='ContactInformation']").send_keys(contact_information)

        # Заповнюємо форми Створення уповноваженної особи: Оберіть МПД «Тест1»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест1')] ").click()

        # Заповнюємо форми Створення уповноваженної особи: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Клік
        wd.find_element_by_xpath("//div[@id='header-wrapper']").click()

        time.sleep(3)

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        # wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def authorized_persons_2(self, person_name, person_middle_name, person_last_name, person_ipn, person_birthday,
                           education, graduation_year, diplom_number, graduation_date, speciality, work_expirience,
                           contract_number, order_number, date_contract, date_appointment, position,
                           contact_information, comment):
        wd = self.app.wd

        time.sleep(2)

        # Натискаємо кнопку «Уповноважені особи»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[4]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати уповноважену особу» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']").click()

        # Заповнюємо форми Створення уповноваженної особи: Ім'я* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(person_name)

        # Заповнюємо форми Створення уповноваженної особи: По батькові* «Тестович»
        wd.find_element_by_xpath("//input[@id='MiddleName']").send_keys(person_middle_name)

        # Заповнюємо форми Створення уповноваженної особи: Прізвище* «Тестов»
        wd.find_element_by_xpath("//input[@id='LastName']").send_keys(person_last_name)

        # Заповнюємо форми Створення уповноваженної особи: ІПН «» (10 цифр)
        wd.find_element_by_xpath("//input[@id='IPN']").send_keys(person_ipn)

        # Заповнюємо форми Створення уповноваженної особи: Дата народження* «13.12.1986»
        wd.find_element_by_xpath("//input[@id='Birthday']").send_keys(person_birthday)

        # Заповнюємо форми Створення уповноваженної особи: Найменування навчального закладу «»
        wd.find_element_by_xpath("//input[@id='EducationInstitution']").send_keys(education)

        # Заповнюємо форми Створення уповноваженної особи: Рік закінчення навчального закладу «2004»
        wd.find_element_by_xpath("//input[@id='YearOfGraduation']").send_keys(graduation_year)

        # Заповнюємо форми Створення уповноваженної особи: Серія і номер диплому* «АП1312»
        wd.find_element_by_xpath("//input[@id='NumberOfDiploma']").send_keys(diplom_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата видачі диплому* «13.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfGraduation']").send_keys(graduation_date)

        # Заповнюємо форми Створення уповноваженної особи: Спеціальність «Тест»
        wd.find_element_by_xpath("//input[@id='Speciality']").send_keys(speciality)

        # Заповнюємо форми Створення уповноваженної особи: Стаж роботи за фахом(місяців) «95»
        wd.find_element_by_xpath("//input[@id='WorkExperience']").send_keys(work_expirience)

        # Заповнюємо форми Створення уповноваженної особи: Номер трудового договору «12345»
        wd.find_element_by_xpath("//input[@id='NumberOfContract']").send_keys(contract_number)

        # Заповнюємо форми Створення уповноваженної особи: Номер наказу про покладання обов'язків 23456
        wd.find_element_by_xpath("//input[@id='OrderNumber']").send_keys(order_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата трудового договору «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfContract']").send_keys(date_contract)

        # Заповнюємо форми Створення уповноваженної особи: Дата наказу про покладання обовєязків «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfAppointment']").send_keys(date_appointment)

        # Заповнюємо форми Створення уповноваженної особи: Посада «Тест директор»
        wd.find_element_by_xpath("//input[@id='NameOfPosition']").send_keys(position)

        # Заповнюємо форми Створення уповноваженної особи: Контактна інформація «12345»
        wd.find_element_by_xpath("//input[@id='ContactInformation']").send_keys(contact_information)

        # Заповнюємо форми Створення уповноваженної особи: Оберіть МПД «Тест2»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест2')] ").click()

        # Заповнюємо форми Створення уповноваженної особи: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Клік
        wd.find_element_by_xpath("//div[@id='header-wrapper']").click()

        time.sleep(3)

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        # wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def authorized_persons_3(self, person_name, person_middle_name, person_last_name, person_ipn, person_birthday,
                           education, graduation_year, diplom_number, graduation_date, speciality, work_expirience,
                           contract_number, order_number, date_contract, date_appointment, position,
                           contact_information, comment):
        wd = self.app.wd

        # Натискаємо кнопку «Уповноважені особи»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[4]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати уповноважену особу» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']").click()

        # Заповнюємо форми Створення уповноваженної особи: Ім'я* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(person_name)

        # Заповнюємо форми Створення уповноваженної особи: По батькові* «Тестович»
        wd.find_element_by_xpath("//input[@id='MiddleName']").send_keys(person_middle_name)

        # Заповнюємо форми Створення уповноваженної особи: Прізвище* «Тестов»
        wd.find_element_by_xpath("//input[@id='LastName']").send_keys(person_last_name)

        # Заповнюємо форми Створення уповноваженної особи: ІПН «» (10 цифр)
        wd.find_element_by_xpath("//input[@id='IPN']").send_keys(person_ipn)

        # Заповнюємо форми Створення уповноваженної особи: Дата народження* «13.12.1986»
        wd.find_element_by_xpath("//input[@id='Birthday']").send_keys(person_birthday)

        # Заповнюємо форми Створення уповноваженної особи: Найменування навчального закладу «»
        wd.find_element_by_xpath("//input[@id='EducationInstitution']").send_keys(education)

        # Заповнюємо форми Створення уповноваженної особи: Рік закінчення навчального закладу «2004»
        wd.find_element_by_xpath("//input[@id='YearOfGraduation']").send_keys(graduation_year)

        # Заповнюємо форми Створення уповноваженної особи: Серія і номер диплому* «АП1312»
        wd.find_element_by_xpath("//input[@id='NumberOfDiploma']").send_keys(diplom_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата видачі диплому* «13.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfGraduation']").send_keys(graduation_date)

        # Заповнюємо форми Створення уповноваженної особи: Спеціальність «Тест»
        wd.find_element_by_xpath("//input[@id='Speciality']").send_keys(speciality)

        # Заповнюємо форми Створення уповноваженної особи: Стаж роботи за фахом(місяців) «95»
        wd.find_element_by_xpath("//input[@id='WorkExperience']").send_keys(work_expirience)

        # Заповнюємо форми Створення уповноваженної особи: Номер трудового договору «12345»
        wd.find_element_by_xpath("//input[@id='NumberOfContract']").send_keys(contract_number)

        # Заповнюємо форми Створення уповноваженної особи: Номер наказу про покладання обов'язків 23456
        wd.find_element_by_xpath("//input[@id='OrderNumber']").send_keys(order_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата трудового договору «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfContract']").send_keys(date_contract)

        # Заповнюємо форми Створення уповноваженної особи: Дата наказу про покладання обовєязків «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfAppointment']").send_keys(date_appointment)

        # Заповнюємо форми Створення уповноваженної особи: Посада «Тест директор»
        wd.find_element_by_xpath("//input[@id='NameOfPosition']").send_keys(position)

        # Заповнюємо форми Створення уповноваженної особи: Контактна інформація «12345»
        wd.find_element_by_xpath("//input[@id='ContactInformation']").send_keys(contact_information)

        # Заповнюємо форми Створення уповноваженної особи: Оберіть МПД «Тест3»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест3')] ").click()

        # Заповнюємо форми Створення уповноваженної особи: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Клік
        wd.find_element_by_xpath("//div[@id='header-wrapper']").click()

        time.sleep(3)

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        # wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")



    def dossier_file(self, version, comment, date_to, path_to_file):
        wd = self.app.wd

        # Натискаємо кнопку «Досьє»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[5]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати досьє» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']").click()

        # Заповнюємо форми Редагування досьє: Назва/Версія «Тест досьє»
        wd.find_element_by_xpath("//input[@id='Version']").send_keys(version)

        # Заповнюємо форми Редагування досьє: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Заповнюємо форми Редагування досьє: Дата з «01.01.2019»
        # wd.find_element_by_xpath("//input[@id='DateFrom']").send_keys('01.01.2019')

        # Заповнюємо форми Редагування досьє: Дата до «19.04.2025»
        wd.find_element_by_xpath("//input[@id='DateTo']").send_keys(date_to)

        # Заповнюємо форми Редагування досьє: Оберіть МПД «Тест1»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест1')]").click()
        wd.find_element_by_xpath("//button[@type='button']").click()

        # Заповнюємо форми Редагування досьє: На формі «Додайте файли до картки досьє» натисувємо кнопку прикріпити файл (з ліва синій квадрат з білою скріпкою)
        # потім натискаємо кнопку збереження файлу (з права синій квадрат з зображенням дискети білого кольору)
        wd.find_element_by_xpath("//input[@id='files']").send_keys(path_to_file)
        wd.find_element_by_xpath("//div[@id='uploadForm']/form/div[3]/button/i").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        time.sleep(2)

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def dossier_file_2(self, version, comment, date_to, path_to_file):
        wd = self.app.wd

        # Натискаємо кнопку «Досьє»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[5]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати досьє» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Редагування досьє: Назва/Версія «Тест досьє»
        wd.find_element_by_xpath("//input[@id='Version']").send_keys(version)

        # Заповнюємо форми Редагування досьє: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Заповнюємо форми Редагування досьє: Дата з «01.01.2019»
        # wd.find_element_by_xpath("//input[@id='DateFrom']").send_keys('01.01.2019')

        # Заповнюємо форми Редагування досьє: Дата до «19.04.2025»
        wd.find_element_by_xpath("//input[@id='DateTo']").send_keys(date_to)

        # Заповнюємо форми Редагування досьє: Оберіть МПД «Тест2»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест2')]").click()
        wd.find_element_by_xpath("//button[@type='button']").click()

        # Заповнюємо форми Редагування досьє: На формі «Додайте файли до картки досьє» натисувємо кнопку прикріпити файл (з ліва синій квадрат з білою скріпкою)
        # потім натискаємо кнопку збереження файлу (з права синій квадрат з зображенням дискети білого кольору)
        wd.find_element_by_xpath("//input[@id='files']").send_keys(path_to_file)
        wd.find_element_by_xpath("//div[@id='uploadForm']/form/div[3]/button/i").click()

        time.sleep(1)

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        time.sleep(2)

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def dossier_file_3(self, version, comment, date_to, path_to_file):
        wd = self.app.wd

        # Натискаємо кнопку «Досьє»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[5]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати досьє» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Редагування досьє: Назва/Версія «Тест досьє»
        wd.find_element_by_xpath("//input[@id='Version']").send_keys(version)

        # Заповнюємо форми Редагування досьє: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Заповнюємо форми Редагування досьє: Дата з «01.01.2019»
        # wd.find_element_by_xpath("//input[@id='DateFrom']").send_keys('01.01.2019')

        # Заповнюємо форми Редагування досьє: Дата до «19.04.2025»
        wd.find_element_by_xpath("//input[@id='DateTo']").send_keys(date_to)

        # Заповнюємо форми Редагування досьє: Оберіть МПД «Тест3»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест3')]").click()
        wd.find_element_by_xpath("//button[@type='button']").click()

        # Заповнюємо форми Редагування досьє: На формі «Додайте файли до картки досьє» натисувємо кнопку прикріпити файл (з ліва синій квадрат з білою скріпкою)
        # потім натискаємо кнопку збереження файлу (з права синій квадрат з зображенням дискети білого кольору)
        wd.find_element_by_xpath("//input[@id='files']").send_keys(path_to_file)
        wd.find_element_by_xpath("//div[@id='uploadForm']/form/div[3]/button/i").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        time.sleep(2)

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def completeness_check(self):
        wd = self.app.wd

        # Натискаємо кнопку «Досьє»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[6]/i").click()

        # Перевірка комплектності поданих документів не виявила ніяких помилок
        wd.find_element_by_xpath(
            "//p[contains(.,'Перевірка комплектності поданих документів не виявила ніяких помилок')]")

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[1]/i").click()

        time.sleep(2)

    def notifications_and_license_terms(self, comment):
        wd = self.app.wd
        # Натискаємо кнопку «Досьє»

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[7]/i").click()

        # wd.find_element_by_css_selector(".icon-msg-envelope").click()
        # Обераємо наступні чекбокси: «Прошу за місцем/місцями провадження господарської діяльності провести перевірку матеріально-технічної бази,
        # кваліфікованого персоналу, а також умов щодо контролю якості лікарських засобів, що вироблятимуться»
        # Додатково до електронної форми бажаю отримати ліцензію на паперовому носії: «Нарочно»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[2]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[3]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[4]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[4]/div[3]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[4]/div[4]/label").click()
        wd.find_element_by_xpath("//textarea[@id='Comment']").send_keys(comment)

        wd.find_element_by_xpath("//button[@id='scroll-top']").click()

        time.sleep(2)

    def submit_application(self, path_to_key, password):
        wd = self.app.wd
        # Натискаємо кнопку «Подання заяви»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[8]/i").click()

        # Натискаємо кнопку «Підписати і відправити заяву»
        wd.find_element_by_xpath("//a[@id='signButton']/span[2]").click()

        time.sleep(3)



#        alert = driver.switch_to_alert()
#        alert.accept()

#        alert = wd.switch_to_alert()
#        alert.accept()
##############################################################        wd.switch_to_alert().accept()
#        wd.switch_to_alert().accept()

        time.sleep(7)


        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): Оберіть ЦСК «АЦСК ПАТ КБ «ПРИВАТБАНК
#        wd.find_element_by_xpath("//div[@id='MainPageMenuPKeyPage']/div[2]/div[2]/div/div").click()
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()

        # wd.find_element_by_xpath("//span[contains(.,'Україна')]").click()
        # //li[@class='select-item'][14]

        # wd.find_element_by_xpath("//li[@class='select-item'][14]").click()

        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()

        # element = wd.find_element_by_xpath("//span[contains(.,'Україна')]").click
        # hover = ActionChains(wd).move_to_element(element)

        # hover.perform()

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): ОБЕРІТЬ ФАЙЛ З ОСОБИСТИМ КЛЮЧЕМ (ЗАЗВИЧАЙ З ІМ'ЯМ KEY-6.DAT) ТА ВКАЖІТЬ ПАРОЛЬ ЗАХИСТУ
        # Path
        wd.find_element_by_xpath("//input[@id='PKeyFileInput']").send_keys(path_to_key)
        # Пароль захисту ключа: «password»
        wd.find_element_by_xpath("//input[@id='PKeyPassword']").send_keys(password)
        # Натискаємо кнопку «Зчитати»
        wd.find_element_by_xpath("//button[@id='PKeyReadButton']").click()
        time.sleep(10)
        # ЩОБ ПІДПИСАТИ ТА ВІДПРАВИТИ ЗАЯВУ, ДАЙТЕ ЗГОДУ НА ПІДПИСАННЯ НАСТУПНИХ ФАЙЛІВ:
        # Обераємо Чекбокс  «Вибрати всі файли»
        # wd.find_element_by_xpath("//div[@id='MainPageMenuPKeyPage']/div[4]/div[2]/label").click()

        # Натискаємо кнопку «Підписати»
        wd.find_element_by_xpath("//button[@id='SignDataButton']").click()

        time.sleep(5)

################################################################################################################################################################################## 2

    def create_second_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про отримання ліцензії на провадження діяльності з виробництва лікарських засобів (промислового)» (додаток 2)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a[2]").click()

    def create_mpd_second(self, company_name, phone_number, email, fax_number, city, index, street, adress, building):
        wd = self.app.wd
        # Натискаємо кнопку «Місця проваждження діяльності»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Натискаємо кнопку «Додати МПД» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a").click()

        # Заповнюємо форми Створення провадження діяльності: Найменування структурного підрозділу (або найменування юридичної особи):* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(company_name)

        # Заповнюємо форми Створення провадження діяльності: Номер телефону* «+380123456789»
        wd.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys(phone_number)

        # Заповнюємо форми Створення провадження діяльності: E-mail* «test@test.ua»
        wd.find_element_by_xpath("//input[@id='EMail']").send_keys(email)

        # Заповнюємо форми Створення провадження діяльності: Номер факсу* «+380123456789»
        wd.find_element_by_xpath("//input[@id='FaxNumber']").send_keys(fax_number)

        # Заповнюємо форми Створення провадження діяльності: Населений пункт* «Дніпропетровська область, Дніпро»
        wd.find_element_by_xpath("//input[@id='CityName']").send_keys(city)
        wd.find_element_by_xpath("//div[contains(.,'Дніпро')]").click()

        # Заповнюємо форми Створення провадження діяльності: Поштовий індекс* «12345»
        wd.find_element_by_xpath("//input[@id='PostIndex']").send_keys(index)

        # Заповнюємо форми Створення провадження діяльності: Вулиця* (натискаємо синій квадрат з білим хрестиком посередині, зявляеться вікно додавання вулиці, у полі тип вулиці обераємо – проспект, у полі Назва вулиці пишемо «Тест» натискаємо кнопку СТВОРИТИ)
#        wd.find_element_by_xpath("//button[@id='btn-street']").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/div").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[2]/div/ul/li[2]/span").click()
#        wd.find_element_by_xpath("//div[@id='modal']/div/div[2]/form/div[3]/input").send_keys(street)
#        time.sleep(2)
#        wd.find_element_by_xpath("//input[@value='Створити']").click()

        wd.find_element_by_xpath("//input[@id='StreetName']").send_keys("Тестова вулиця")
        time.sleep(2)
        wd.find_element_by_xpath("//div[contains(.,'Тестова Вулиця')]").click()

        # Заповнюємо форми Створення провадження діяльності: Адреса місця провадження діяльності (англійською)* «Test»
#        wd.find_element_by_xpath("//input[@id='AdressEng']").send_keys(adress)

        # Заповнюємо форми Створення провадження діяльності: Номер будинку, корпус або будівля, номер квартири або офісу* «13»
        wd.find_element_by_xpath("//input[@id='Building']").send_keys(building)

        time.sleep(2)
        # Обераємо чекбокс «Виробничі дільниці з переліком лікарських форм*»
        wd.find_element_by_xpath("//form[@id='editBranch']/div[3]/div/label").click()

        # Обераємо чекбокс «1. ВИРОБНИЧІ ОПЕРАЦІЇ - ЛІКАРСЬКІ ФОРМИ»
        wd.find_element_by_xpath("//div[@id='content-tree']/ul/li/div/label").click()
        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@id='submitBranch']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        # wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def authorized_persons_second(self, person_name, person_middle_name, person_last_name, person_ipn, person_birthday,
                           education, graduation_year, diplom_number, graduation_date, speciality, work_expirience,
                           contract_number, order_number, date_contract, date_appointment, position,
                           contact_information, comment):
        wd = self.app.wd

        # Натискаємо кнопку «Уповноважені особи»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[4]/i").click()

        time.sleep(1)

        # Натискаємо кнопку «Додати уповноважену особу» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a").click()

        # Заповнюємо форми Створення уповноваженної особи: Ім'я* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(person_name)

        # Заповнюємо форми Створення уповноваженної особи: По батькові* «Тестович»
        wd.find_element_by_xpath("//input[@id='MiddleName']").send_keys(person_middle_name)

        # Заповнюємо форми Створення уповноваженної особи: Прізвище* «Тестов»
        wd.find_element_by_xpath("//input[@id='LastName']").send_keys(person_last_name)

        # Заповнюємо форми Створення уповноваженної особи: ІПН «» (10 цифр)
        wd.find_element_by_xpath("//input[@id='IPN']").send_keys(person_ipn)

        # Заповнюємо форми Створення уповноваженної особи: Дата народження* «13.12.1986»
        wd.find_element_by_xpath("//input[@id='Birthday']").send_keys(person_birthday)

        # Заповнюємо форми Створення уповноваженної особи: Найменування навчального закладу «»
        wd.find_element_by_xpath("//input[@id='EducationInstitution']").send_keys(education)

        # Заповнюємо форми Створення уповноваженної особи: Рік закінчення навчального закладу «2004»
        wd.find_element_by_xpath("//input[@id='YearOfGraduation']").send_keys(graduation_year)

        # Заповнюємо форми Створення уповноваженної особи: Серія і номер диплому* «АП1312»
        wd.find_element_by_xpath("//input[@id='NumberOfDiploma']").send_keys(diplom_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата видачі диплому* «13.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfGraduation']").send_keys(graduation_date)

        # Заповнюємо форми Створення уповноваженної особи: Спеціальність «Тест»
        wd.find_element_by_xpath("//input[@id='Speciality']").send_keys(speciality)

        # Заповнюємо форми Створення уповноваженної особи: Стаж роботи за фахом(місяців) «95»
        wd.find_element_by_xpath("//input[@id='WorkExperience']").send_keys(work_expirience)

        # Заповнюємо форми Створення уповноваженної особи: Номер трудового договору «12345»
        wd.find_element_by_xpath("//input[@id='NumberOfContract']").send_keys(contract_number)

        # Заповнюємо форми Створення уповноваженної особи: Номер наказу про покладання обов'язків 23456
        wd.find_element_by_xpath("//input[@id='OrderNumber']").send_keys(order_number)

        # Заповнюємо форми Створення уповноваженної особи: Дата трудового договору «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfContract']").send_keys(date_contract)

        # Заповнюємо форми Створення уповноваженної особи: Дата наказу про покладання обовєязків «14.12.2004»
        wd.find_element_by_xpath("//input[@id='DateOfAppointment']").send_keys(date_appointment)

        # Заповнюємо форми Створення уповноваженної особи: Посада «Тест директор»
        wd.find_element_by_xpath("//input[@id='NameOfPosition']").send_keys(position)

        # Заповнюємо форми Створення уповноваженної особи: Контактна інформація «12345»
        wd.find_element_by_xpath("//input[@id='ContactInformation']").send_keys(contact_information)

        # Заповнюємо форми Створення уповноваженної особи: Оберіть МПД «Тест»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label").click()

        # Заповнюємо форми Створення уповноваженної особи: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Клік
        wd.find_element_by_xpath("//div[@id='header-wrapper']").click()

        time.sleep(3)

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Додавання МПД')]")


    def dossier_file_second(self, version, comment, date_to, path_to_file):
        wd = self.app.wd

        # Натискаємо кнопку «Досьє»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[5]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати досьє» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a").click()

        # Заповнюємо форми Редагування досьє: Назва/Версія «Тест досьє»
        wd.find_element_by_xpath("//input[@id='Version']").send_keys(version)

        # Заповнюємо форми Редагування досьє: Коментар «Тест коментар»
        wd.find_element_by_xpath("//input[@id='Comment']").send_keys(comment)

        # Заповнюємо форми Редагування досьє: Дата з «01.01.2019»
        # wd.find_element_by_xpath("//input[@id='DateFrom']").send_keys('01.01.2019')

        # Заповнюємо форми Редагування досьє: Дата до «19.04.2025»
        wd.find_element_by_xpath("//input[@id='DateTo']").send_keys(date_to)

        # Заповнюємо форми Редагування досьє: Оберіть МПД «Тест»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label").click()

        # Заповнюємо форми Редагування досьє: На формі «Додайте файли до картки досьє» натисувємо кнопку прикріпити файл (з ліва синій квадрат з білою скріпкою)
        # потім натискаємо кнопку збереження файлу (з права синій квадрат з зображенням дискети білого кольору)
        wd.find_element_by_xpath("//input[@id='files']").send_keys(path_to_file)
        wd.find_element_by_xpath("//div[@id='uploadForm']/form/div[3]/button/i").click()

        time.sleep(2)

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        time.sleep(2)

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Додавання МПД')]")

    def notifications_and_license_terms_second(self, comment):
        wd = self.app.wd
        # Натискаємо кнопку «Досьє»

        time.sleep(2)

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[7]/i").click()

        # wd.find_element_by_css_selector(".icon-msg-envelope").click()
        # Обераємо наступні чекбокси: «Прошу за місцем/місцями провадження господарської діяльності провести перевірку матеріально-технічної бази,
        # кваліфікованого персоналу, а також умов щодо контролю якості лікарських засобів, що вироблятимуться»
        # Додатково до електронної форми бажаю отримати ліцензію на паперовому носії: «Нарочно»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[2]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[3]/div[2]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[3]/div[3]/label").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[3]/div[4]/label").click()
        # wd.find_element_by_xpath("//div[@id='content']/div[2]/div[7]/div[3]/div/div[4]/div[4]/label").click()
        wd.find_element_by_xpath("//textarea[@id='Comment']").send_keys(comment)

        wd.find_element_by_xpath("//button[@id='scroll-top']").click()

        time.sleep(2)

################################################################################################################################################################################## 3

    def create_third_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про отримання ліцензії на провадження діяльності з виробництва лікарських засобів (промислового)» (додаток 2)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a[3]").click()

    def change_mpd_third(self):
        wd = self.app.wd
        # Натискаємо кнопку «Місця проваждження діяльності»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Обираємо перший «МПД»
        wd.find_element_by_xpath("//div[@class='content-list'][1]").click()

        # Обираємо перший «МПД»
        wd.find_element_by_xpath("//*[text()='2. ВИРОБНИЧІ ОПЕРАЦІЇ - АКТИВНІ ФАРМАЦЕВТИЧНІ ІНГРЕДІЄНТИ']").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@id='submitBranch2']").click()

        time.sleep(1)

    def notifications_and_license_terms_third(self, comment):
        wd = self.app.wd

        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[5]/i").click()

        # wd.find_element_by_css_selector(".icon-msg-envelope").click()
        # Обераємо наступні чекбокси: «Прошу за місцем/місцями провадження господарської діяльності провести перевірку матеріально-технічної бази,
        # кваліфікованого персоналу, а також умов щодо контролю якості лікарських засобів, що вироблятимуться»
        # Додатково до електронної форми бажаю отримати ліцензію на паперовому носії: «Нарочно»
        wd.find_element_by_xpath("//*[contains(text(), 'провести перевірку матеріально-технічної бази')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'за місцезнаходженням/місцем ')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'З порядком отримання ліцензії ознайомлений.')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'Згоден на обробку персональних даних')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'На виконання вимог Закону України')]").click()
        wd.find_element_by_xpath("//textarea[@id='Comment']").send_keys(comment)

        wd.find_element_by_xpath("//button[@id='scroll-top']").click()

        time.sleep(1)

    def submit_application_third(self, path_to_key, password):
        wd = self.app.wd
        # Натискаємо кнопку «Подання заяви»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[6]/i").click()

        # Натискаємо кнопку «Підписати і відправити заяву»
        wd.find_element_by_xpath("//a[@id='signButton']/span[2]").click()

        time.sleep(2)

#        wd.switch_to_alert().accept()

        time.sleep(5)

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): Оберіть ЦСК «АЦСК ТОВ "Центр сертифікації ключів "Україна"
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()

        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): ОБЕРІТЬ ФАЙЛ З ОСОБИСТИМ КЛЮЧЕМ (ЗАЗВИЧАЙ З ІМ'ЯМ KEY-6.DAT) ТА ВКАЖІТЬ ПАРОЛЬ ЗАХИСТУ
        # Path
        wd.find_element_by_xpath("//input[@id='PKeyFileInput']").send_keys(path_to_key)
        # Пароль захисту ключа: «password»
        wd.find_element_by_xpath("//input[@id='PKeyPassword']").send_keys(password)
        # Натискаємо кнопку «Зчитати»
        wd.find_element_by_xpath("//button[@id='PKeyReadButton']").click()
        time.sleep(10)
        # ЩОБ ПІДПИСАТИ ТА ВІДПРАВИТИ ЗАЯВУ, ДАЙТЕ ЗГОДУ НА ПІДПИСАННЯ НАСТУПНИХ ФАЙЛІВ:
        # Обераємо Чекбокс  «Вибрати всі файли»
        # wd.find_element_by_xpath("//div[@id='MainPageMenuPKeyPage']/div[4]/div[2]/label").click()

        # Натискаємо кнопку «Підписати»
        wd.find_element_by_xpath("//button[@id='SignDataButton']").click()

        time.sleep(5)

################################################################################################################################################################################## 4

    def create_fourth_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про звуження переліку МПД» (додаток 16)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a[4]").click()

    def delete_mpd_fourth(self):
        wd = self.app.wd
        # Натискаємо кнопку «Місця проваждження діяльності»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Обираємо перший «МПД» (Помітка на видалення)
        wd.find_element_by_xpath("//label[@class='control-label']").click()

        time.sleep(1)

    def notifications_and_license_terms_fourth(self, comment):
        wd = self.app.wd

        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[4]/i").click()

        # Обераємо наступні чекбокси: «Про рішення, прийняте за результатами розгляду цієї заяви, прошу повідомити:»
        # «Нарочно»
        wd.find_element_by_xpath("//*[contains(text(), 'Поштовим відправленням')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'З порядком отримання ліцензії ознайомлений.')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'Згоден на обробку персональних даних')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'На виконання вимог Закону України')]").click()
        wd.find_element_by_xpath("//textarea[@id='Comment']").send_keys(comment)

        wd.find_element_by_xpath("//button[@id='scroll-top']").click()

        time.sleep(1)

    def submit_application_fourth(self, path_to_key, password):
        wd = self.app.wd
        # Натискаємо кнопку «Подання заяви»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[5]/i").click()

        # Натискаємо кнопку «Підписати і відправити заяву»
        wd.find_element_by_xpath("//a[@id='signButton']/span[2]").click()

        time.sleep(2)

#        wd.switch_to_alert().accept()

        time.sleep(5)

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): Оберіть ЦСК «АЦСК ТОВ "Центр сертифікації ключів "Україна"
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()

        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): ОБЕРІТЬ ФАЙЛ З ОСОБИСТИМ КЛЮЧЕМ (ЗАЗВИЧАЙ З ІМ'ЯМ KEY-6.DAT) ТА ВКАЖІТЬ ПАРОЛЬ ЗАХИСТУ
        # Path
        wd.find_element_by_xpath("//input[@id='PKeyFileInput']").send_keys(path_to_key)
        # Пароль захисту ключа: «password»
        wd.find_element_by_xpath("//input[@id='PKeyPassword']").send_keys(password)
        # Натискаємо кнопку «Зчитати»
        wd.find_element_by_xpath("//button[@id='PKeyReadButton']").click()
        time.sleep(10)

        # Натискаємо кнопку «Підписати»
        wd.find_element_by_xpath("//button[@id='SignDataButton']").click()

        time.sleep(5)

################################################################################################################################################################################## 5


    def create_fifth_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про звуження переліку лікарських форм» (додаток 16)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a[5]").click()

    def change_mpd_fifth(self):
        wd = self.app.wd
        # Натискаємо кнопку «Місця проваждження діяльності»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Обираємо перший «МПД»
        wd.find_element_by_xpath("//div[@class='content-list'][1]").click()

        # Обираємо пункт на видалення
        wd.find_element_by_xpath("//*[text()='1.4.2. Стерилізація активних речовин/допоміжних речовин/готової продукції']").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@id='submitBranch2']").click()

        time.sleep(1)

################################################################################################################################################################################## 6

# ЗМІНА УПОВНОВАЖЕНИХ ОСІБ

    def create_sixth_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про звуження переліку лікарських форм» (додаток 16)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a[6]").click()

    def authorized_persons_sixth(self):
        wd = self.app.wd

        # Натискаємо кнопку «Уповноважені особи»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[3]/i").click()

        time.sleep(2)

        # обираємо першу УО редагування
        wd.find_element_by_xpath("//div[@class='content-list'][1]").click()

        # Змінюємо Ім'я на "Тест зміна"
        wd.find_element_by_xpath("//input[@id='Name']").send_keys("Тест зміна")


        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()


        time.sleep(1)

    ################################################################################################################################################################################## 7

    # ЗМІНА ЗМІНА КОНТРАКТНИХ КОНТРАГЕНТІВ

    def create_seventh_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про звуження переліку лікарських форм» (додаток 16)
#        wd.find_element_by_xpath("//*[text()='Заява на зміну контрактних виробників і контрактних лабораторій']").click()
        wd.find_element_by_xpath("//*[contains(text(), 'на зміну контрактних виробників і контрактних')]").click()

    def contract_contractors_seventh(self, edrpou, name_contractor, adress):
        wd = self.app.wd
        # Натискаємо кнопку «Контрактні контрагенти»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[3]/i").click()

        time.sleep(2)

        # Натискаємо кнопку «Додати Контрактного контрагента» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a").click()

        # Заповнюємо форми Створення Контрактного контрагента: Тип контрагента* обираемо вариант «Контрактна лабораторія»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div/div/div/div/ul/li[3]").click()

        # Заповнюємо форми Створення Контрактного контрагента: ЄДРПОУ/ІПН* «12345678»(мінімальна кількість знаків 8 шт.)
        wd.find_element_by_xpath("//input[@id='Edrpou']").send_keys(edrpou)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування суб'єкта господарювання «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(name_contractor)

        # Заповнюємо форми Створення Контрактного контрагента: Найменування, місце провадження діяльності* «Тест»
        wd.find_element_by_xpath("//input[@id='Address']").send_keys(adress)

        # Заповнюємо форми Створення Контрактного контрагента: Оберіть МПД «Тест1»
        wd.find_element_by_xpath("//button[@type='button']").click()
        wd.find_element_by_xpath("//div[@id='ms-list-1']/div/ul/li/label[contains(text(), 'Тест1')]").click()

        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()
        time.sleep(1)













































################################################################################################################################################################################## 10


    def create_tenth_application(self):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заява щодо провадження діяльності з виробництва лікарських засобів (промислового)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про звуження переліку лікарських форм» (додаток 16)
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div/div[2]/a[10]").click()

    def notifications_and_license_terms_tenth(self, comment):
        wd = self.app.wd

        time.sleep(1)

        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Обераємо наступні чекбокси: «Про рішення, прийняте за результатами розгляду цієї заяви, прошу повідомити:»
        # «Нарочно»
        wd.find_element_by_xpath("//*[contains(text(), 'Поштовим відправленням')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'З порядком отримання ліцензії ознайомлений.')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'Згоден на обробку персональних даних')]").click()
        wd.find_element_by_xpath("//*[contains(text(), 'На виконання вимог Закону України')]").click()
        wd.find_element_by_xpath("//textarea[@id='Comment']").send_keys(comment)

        wd.find_element_by_xpath("//button[@id='scroll-top']").click()

        time.sleep(1)

    def submit_application_tenth(self, path_to_key, password):
        wd = self.app.wd
        # Натискаємо кнопку «Подання заяви»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[3]/i").click()

        # Натискаємо кнопку «Підписати і відправити заяву»
        wd.find_element_by_xpath("//a[@id='signButton']/span[2]").click()

        time.sleep(2)

        #        wd.switch_to_alert().accept()

        time.sleep(5)

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): Оберіть ЦСК «АЦСК ТОВ "Центр сертифікації ключів "Україна"
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()

        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()

        # Заповнюємо форми Ідентифікація за електронним підписом: Встановлення особистого ключа (ще раз): ОБЕРІТЬ ФАЙЛ З ОСОБИСТИМ КЛЮЧЕМ (ЗАЗВИЧАЙ З ІМ'ЯМ KEY-6.DAT) ТА ВКАЖІТЬ ПАРОЛЬ ЗАХИСТУ
        # Path
        wd.find_element_by_xpath("//input[@id='PKeyFileInput']").send_keys(path_to_key)
        # Пароль захисту ключа: «password»
        wd.find_element_by_xpath("//input[@id='PKeyPassword']").send_keys(password)
        # Натискаємо кнопку «Зчитати»
        wd.find_element_by_xpath("//button[@id='PKeyReadButton']").click()
        time.sleep(10)

        # Натискаємо кнопку «Підписати»
        wd.find_element_by_xpath("//button[@id='SignDataButton']").click()

        time.sleep(5)

##################################################################################################################################################################################  Import
    def create_import_first_application(self, pib, email, phone_number, fax_number, city, flat, street, index,
                                 number_national_account, requisits_number_national_account, number_foreign_account,
                                 requisits_number_forein_account, duns_number):
        wd = self.app.wd
        # У меню з ліва натискаємо пункт «Подання заяв»
        wd.find_element_by_xpath("//ul[@id='aside-menu']/li[2]/div/a/div/span").click()

        #        time.sleep(3)
        # Натискаємо кнопку створити заяву (У правому верхньому куті Синій кружочок з білим хрестиком у центрі)
        wd.find_element_by_xpath("//a[contains(@ href,'/App/AppTypes')]").click()

        # На сторінці Створення нової заяви, на переліку заяв натискаємо «Заяви щодо провадження діяльності з імпорту лікарських засобів (крім активних фармацевтичних інгредієнтів)»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/div[2]").click()

        # У вище вказанному переліку заяв обираємо пункт «Заява про отримання ліцензії на провадження діяльності з виробництва лікарських засобів (промислового)» (додаток 2)
        wd.find_element_by_xpath("//*[contains(text(), 'Заява про отримання ліцензії на провадження діяльності з імпорту лікарських засобів')]").click()

        # Заповнюємо форму: Організаційно-правова форма* «460 Громадська організація»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div/div/div/ul/li[2]/span").click()

        # Заповнюємо форму: Форма власності «40 Власність інших держав»
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div[2]/div/div/div").click()
        wd.find_element_by_xpath("//div[@id='content']/div[2]/div/form/div[2]/div[2]/div/div/ul/li[2]/span").click()

        # Заповнюємо форму: Прізвищеб ім'я по батькові керівника юридичної особи  «Ступка Богдан Сильвестрович»
        wd.find_element_by_xpath("//input[@id='OrgDirector']").send_keys(pib)

        # Заповнюємо форму: E-mail* «test@test.ua»
        wd.find_element_by_xpath("//input[@id='EMail']").send_keys(email)

        # Заповнюємо форму: Номер телефону* «+380123456789»
        wd.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys(phone_number)

        # Заповнюємо форму: Номер факсу «+380123456789»
        wd.find_element_by_xpath("//input[@id='FaxNumber']").send_keys(fax_number)

        # Заповнюємо форму: Населений пункт* «Дніпропетровська область, Тернівка»
        wd.find_element_by_xpath("//input[@id='CityName']").send_keys(city)
        wd.find_element_by_xpath("//div[contains(.,'Дніпро')]").click()

        # Заповнюємо форму: Номер будинку, корпус або будівля, номер квартири або офісу* «13»
        wd.find_element_by_xpath("//input[@id='Building']").send_keys(flat)

        wd.find_element_by_xpath("//input[@id='StreetName']").send_keys("Тестова")
        time.sleep(2)
        wd.find_element_by_xpath("//div[contains(.,'вул. Тестова Вулиця')]").click()

        # Заповнюємо форму: Поштовий індекс* «12345»
        wd.find_element_by_xpath("//input[@id='PostIndex']").send_keys(index)

        # Заповнюємо форму: Номер рахунку в національній валюті «12345»
        wd.find_element_by_xpath("//input[@id='NationalAccount']").send_keys(number_national_account)

        # Заповнюємо форму: Реквизити банку з рахунком в національній валюті «23456»
        wd.find_element_by_xpath("//input[@id='NationalBankRequisites']").send_keys(
            requisits_number_national_account)

        # Заповнюємо форму: Номер рахунку в іноземній валюті «34567»
        wd.find_element_by_xpath("//input[@id='InternationalAccount']").send_keys(number_foreign_account)

        # Заповнюємо форму: Реквизити банку з рахунком в іноземній валюті «45678»
        wd.find_element_by_xpath("//input[@id='InternationalBankRequisites']").send_keys(
            requisits_number_forein_account)

        # Заповнюємо форму: D-U-N-S номер (за наявності) «56789»
        wd.find_element_by_xpath("//input[@id='Duns']").send_keys(duns_number)
        time.sleep(3)
        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@value='Зберегти']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")

    def create_mpd_import(self, company_name, phone_number, email, fax_number, city, index, street, adress, building):
        wd = self.app.wd
        # Натискаємо кнопку «Місця проваждження діяльності»
        wd.find_element_by_xpath("//div[@id='content-switcher']/a[2]/i").click()

        # Натискаємо кнопку «Додати МПД» (з верху з права білий хрестик)
        wd.find_element_by_xpath("//div[@id='content-btn']/a[2]").click()

        # Заповнюємо форми Створення провадження діяльності: Найменування структурного підрозділу (або найменування юридичної особи):* «Тест»
        wd.find_element_by_xpath("//input[@id='Name']").send_keys(company_name)

        # Заповнюємо форми Створення провадження діяльності: Номер телефону* «+380123456789»
        wd.find_element_by_xpath("//input[@id='PhoneNumber']").send_keys(phone_number)

        # Заповнюємо форми Створення провадження діяльності: E-mail* «test@test.ua»
        wd.find_element_by_xpath("//input[@id='EMail']").send_keys(email)

        # Заповнюємо форми Створення провадження діяльності: Номер факсу* «+380123456789»
        wd.find_element_by_xpath("//input[@id='FaxNumber']").send_keys(fax_number)

        # Заповнюємо форми Створення провадження діяльності: Населений пункт* «Дніпропетровська область, Дніпро»
        wd.find_element_by_xpath("//input[@id='CityName']").send_keys(city)
        wd.find_element_by_xpath("//div[contains(.,'Дніпро')]").click()

        # Заповнюємо форми Створення провадження діяльності: Поштовий індекс* «12345»
        wd.find_element_by_xpath("//input[@id='PostIndex']").send_keys(index)

        wd.find_element_by_xpath("//input[@id='StreetName']").send_keys("Тестова")
        time.sleep(2)
        wd.find_element_by_xpath("//div[contains(.,'вул. Тестова Вулиця')]").click()

        # Заповнюємо форми Створення провадження діяльності: Адреса місця провадження діяльності (англійською)* «Test»
        wd.find_element_by_xpath("//input[@id='AdressEng']").send_keys(adress)

        # Заповнюємо форми Створення провадження діяльності: Номер будинку, корпус або будівля, номер квартири або офісу* «13»
        wd.find_element_by_xpath("//input[@id='Building']").send_keys(building)

        time.sleep(2)






        # Обераємо чекбокс «Складські зони (приміщення для зберігання)»
        wd.find_element_by_xpath("//label[contains(text(), 'Складські зони (приміщення для зберігання)')]").click()
        wd.find_element_by_xpath("//label[contains(text(), 'Умови щодо контролю якості')]").click()
        wd.find_element_by_xpath("//label[contains(text(), 'Імпорт зареєстрованих лікарських засобів у формі “in bulk” (продукції “in bulk”)')]").click()
        wd.find_element_by_xpath("//label[contains(text(), 'Зони здійснення видачі дозволу на випуск (реалізацію) серії лікарського засобу')]").click()
        wd.find_element_by_xpath("//label[contains(text(), 'Імпорт зареєстрованих готових лікарських засобів')]").click()



        # Натискаємо кнопку «ЗБЕРЕГТИ»
        wd.find_element_by_xpath("//input[@id='submitBranch']").click()

        # Перевірка переходу на сторінку "Заява про отримання ліцензії на провадження діяльності"
        wd.find_element_by_xpath("//h1[contains(.,'Заява про отримання ліцензії на провадження діяльності')]")