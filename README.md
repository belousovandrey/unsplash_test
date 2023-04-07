# unsplash_test

- base_page.py - тут мы храним методы, которые применяются по всему проекту вообще, всё завернуто в класс, чтобы было удобно импортировать.
- main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py
- locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать
- main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице. Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в base_page.py
- в test_main_page мы будем хранить сами тест-кейсы, которые будем запускать с помощью pytest, выполняем по префиксу "test_" это для PyTest.
- - Здесь мы будем создавать функции, которым:
- - - выдаём нужный для проверки линк
- - - создаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага №1
- - - следом говорим "page, откройся", но методом из base_page.py(класс BasePage)
- - - добавляем проверки, которые создавали методами в main_page.py
