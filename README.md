# Задание по курсу "Основы автоматизации тестирования на Python с помощью Selenium"
### Шаги, по которым был написан код:
* Home: добавление комментария
> 1. Откройте http://practice.automationtesting.in/
> 2. Проскролльте страницу вниз на 600 пикселей
> 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
> 4. Нажмите на вкладку "REVIEWS"
> 5. Поставьте 5 звёзд
> 6. Заполните поле "Review" сообщением : "Nice book!"
> 7. Заполните поле "Name"
> 8. Заполните "Email"
> 9. Нажмите на кнопку "SUBMIT"

* Registration_login: регистрация аккаунта
> 1.	Откройте http://practice.automationtesting.in/
> 2.	Нажмите на вкладку "My Account Menu"
> 3.	В разделе "Register", введите email для регистрации
> 4.	В разделе "Register", введите пароль для регистрации
>     •	составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
>     •	почту и пароль сохраните, потребуюутся в дальнейшем
> 5.	Нажмите на кнопку "Register"

* Registration_login: логин в систему
> 1.	Откройте http://practice.automationtesting.in/
> 2.	Нажмите на вкладку "My Account Menu"
> 3.	В разделе "Login", введите email для логина #данные можно взять из предыдущего теста
> 4.	В разделе "Login", введите пароль для логина	#данные можно взять из предыдущего теста
> 5.	Нажмите на кнопку "Login"
> 6.	Добавьте проверку, что на странице есть элемент "Logout"

* Shop: отображение страницы товара 
> 1.	Откройте http://practice.automationtesting.in/
> 2.	Залогиньтесь
> 3.	Нажмите на вкладку "Shop"
> 4.	Откройте книгу "HTML 5 Forms"
> 5.	Добавьте тест, что заголовок книги назвается: "HTML5 Forms"

* Shop: количество товаров в категории
> 1.	Откройте http://practice.automationtesting.in/
> 2.	Залогиньтесь
> 3.	Нажмите на вкладку "Shop"
> 4.	Откройте категорию "HTML"
> 5.	Добавьте тест, что отображается три товара

* Shop: сортировка товаров
> 1.	Откройте http://practice.automationtesting.in/
> 2.	Залогиньтесь
> 3.	Нажмите на вкладку "Shop"
> 4.	Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
>> •	Используйте проверку по value
> 5.	Отсортируйте товары от большего к меньшему
>> •	в селекторах используйте класс Select
> 6.	Снова объявите переменную с локатором основного селектора сортировки #т.к после сортировки страница обновится
> 7.	Добавьте тест, что в селекторе выбран вариант сортировки от большего к меньшему
>> •	Используйте проверку по value


