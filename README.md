## Тестовое задание для компании "Фабрика решений"

### Разворачивание
Скопируйте себе репозиторий с помощью команды `git clone https://github.com/warkb/SolutionFactoryTest.git`
В папке с проектом создайте виртуальное окружение с версией Python не ниже, чем 3.7 и установите зависимости
```
# SolutionFactoryTest\
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
```
Далее выполните команду и после запуска сервера перейдите по ссылке http://127.0.0.1:8000/
```
# SolutionFactoryTest\testFR
python manage.py runserver
```

### Документация по API

В системе сохранены два пользователя - admin с паролем admin и user с паролем user.

#### Функционал администратора
Авторизация в системе происходит через веб интерфейс DRF
Добавление/изменение/удаление опросов происходит через эндпоинт polls/
Добавление/изменение/удаление вопросов в опросе происходит через эндпоинт questions/
Добавление/изменение/удаление вариантов ответа через эндпоинт answer-options/

#### Функционал пользователя
Получение списка активных опросов происходи через эндпоинт polls/. Пользователи видят только те опросы, срок которых ещё не истек. Все опросы видит только админ
Прохождение опроса происходи путём создания объекта answer, через эндпоинт answers/
Получить данные о всех ответах на вопросы можно посмотрев объект пользователя, через эндпоинт users/. В поле answers сериализуются все ответы на вопросы
