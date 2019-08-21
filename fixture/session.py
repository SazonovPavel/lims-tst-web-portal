import time


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, password, path_to_key):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 3 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 4 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 5 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            path_to_key)
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(10)
        # 9 Нажимаю кнопку ПОГОДИТИСЬ
        wd.find_element_by_xpath("//div[@id='contentSignJSModal']/button").click()
        time.sleep(5)
        # 10 Проверяю наличие элемента (заголовок Портал Держликслужбы)
        wd.find_element_by_xpath("//div[@class='header-inner']/h1").click()

    def login_second(self):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 3 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 4 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 5 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(3)

#        if (wd.find_element_by_xpath("//*[text()[contains(.,'No Sales Found')]")).Enabled)
#        {
#        wd.switch_to_alert().accept()
#        }

        alert = wd.switch_to.alert
        assert "Виникла помилка при зчитуванні особистого ключа. Опис помилки: файл з особистим ключем не обрано" in alert.text
        alert.accept()

#        wd.switch_to_alert().accept()

    def login_third(self, password, path_to_key):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 3 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 4 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 5 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            path_to_key)
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(3)

        alert = wd.switch_to.alert
        assert "Виникла помилка при зчитуванні особистого ключа. Опис помилки: не вказано пароль доступу до особистого ключа" in alert.text
        alert.accept()

#        wd.switch_to_alert().accept()

    def login_fourth(self, password):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        time.sleep(10)
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(3)

        alert = wd.switch_to.alert
        assert "Виникла помилка при зчитуванні особистого ключа. Опис помилки: файл з особистим ключем не обрано" in alert.text
        alert.accept()

#        wd.switch_to_alert().accept()

    def login_fifth(self, password, path_to_key):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        time.sleep(10)
        # 5 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            path_to_key)
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(3)

        alert = wd.switch_to.alert
        assert "Сертифікат не знайдено(51)" in alert.text
        alert.accept()

#        wd.switch_to_alert().accept()

    def login_sixth(self, password, path_to_key):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 3 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 4 выбираем вариант "МВС України"
        wd.find_element_by_xpath("//option[contains(.,'МВС України')]").click()
        # 5 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            path_to_key)
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(3)

        alert = wd.switch_to.alert
        assert "Сертифікат не знайдено(51)" in alert.text
        alert.accept()

#        wd.switch_to_alert().accept()

    def login_seventh(self, password, path_to_key):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 3 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 4 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 5 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            path_to_key)
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(3)

        alert = wd.switch_to.alert
        assert "Виникла помилка при відкритті особистого ключа (невірний пароль чи ключ пошкоджений)(24)" in alert.text
        alert.accept()

#        wd.switch_to_alert().accept()


    def login_eighth(self, password):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 3 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 4 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(3)

        alert = wd.switch_to.alert
        assert "Виникла помилка при зчитуванні особистого ключа. Опис помилки: файл з особистим ключем не обрано" in alert.text
        alert.accept()

#        wd.switch_to_alert().accept()

    def login_tenth(self, password, path_to_key):
        wd = self.app.wd
        self.app.open_home_page()
        # 1 нажимаем кнопку "Войти на портал"
        wd.find_element_by_xpath("//div[@id='content-wrapper']/div/a/div").click()
        # 2 выбираем вариант файловый носитель
        wd.find_element_by_xpath("//a[contains(.,'Файловий носій')]").click()
        # 3 открываем выпадающий список Центр сертификации ключей
        time.sleep(10)
        wd.find_element_by_xpath("//select[@id='CAsServersSelect']").click()
        # 4 выбираем вариант "Центр сертифікації ключів "Україна" "
        wd.find_element_by_xpath("//option[contains(.,'Україна')]").click()
        # 5 прописываем путь к ключу
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[2]/div/input").send_keys(
            path_to_key)
        # 6 Активирую поле ПАРОЛЬ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").click()
        # 7 Ввожу пароль
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div/div/input").send_keys(
            password)
        # 8 нажимаю кнопку ВОЙТИ
        wd.find_element_by_xpath("//form[@id='formAuthJSRequest']/fieldset/div[3]/div/div[2]/div/button").click()
        time.sleep(10)
        # 9 Нажимаю кнопку ПОГОДИТИСЬ
        wd.find_element_by_xpath("//div[@id='contentSignJSModal']/button").click()
        time.sleep(5)
        # 10 Проверяю наличие элемента (заголовок Портал Держликслужбы)
        wd.find_element_by_xpath("//div[@class='header-inner']/h1").click()










    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/div/div/span").click()
        wd.find_element_by_xpath("//ul[@id='header-account-menu']/li/div/ul/li[3]/div/a/div/span").click()
        time.sleep(3)
        # Проверяю наличие эленмента (Заголовок)
        wd.find_element_by_xpath("//h1[contains(.,'Онлайн-подача та відслідковування')]")
