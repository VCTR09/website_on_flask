<a id="anchor"></a>
# Веб-сайт 

[ссылка на сайт: ![link1](https://user-images.githubusercontent.com/97599612/173779440-88b4b491-3bde-4dac-a54a-e3afa5b3ffcb.png)](http://vicoding.pythonanywhere.com)



** Web Development with Flask - Build a Personal Website.

** Фронтенд сайта - _HTML_, _CSS_; Бэкенд - _Python_.

___
Содержание:

* [1. Создание виртуального окружения](#virtual)
* [2. Начало разработки](#work)
* [3. HTML-шаблон страницы](#html)
* [4. Навигационное меню](#navigation)
* [5. CSS внешний вид страницы](#css)
* [6. Изображения](#images)
* [7. Развертывание сайта](#deploy)
___

## Процесс создания:


<a id="virtual"></a>
### 1. Создание виртуального окружения:

Виртуальное окружение создается в начале, чтобы иметь доступ к версии _Python_ без библиотек, модулей - всего, что не понадобится в работе над проектом.

> pip install virtualenv

> python3 -m venv virtual

** Установка _Flask_ в виртуальном окружении.
> virtual/bin/pip3 install flask  (для mac)

** Запуск веб-сайта в виртуальном окружении.
> virtual/bin/python3 Website_on_Flask/script1.py

<a id="work"></a>

### 2. Начало разработки:
Импорт класса _Flask_ фреймфорка _Flask_ в файле script1.py:

> from flask import Flask

Создание переменной _app_ для хранения экземляра класса:
```
app = Flask(__name__)
```
** _name_ - специальная переменная, в качестве значения принимающая название _Python_ скрипта.

Используем декоратор _@app.route('/')_ для создания Домашней страницы.

_URL_ по которому вебсайт будет виден (/ - Домашняя страница)

Создадим функцию, определяющую функционал веб-страницы:
```
@app.route('/')
def home():
    return render_template("home.html")
```

Используем новый декоратор и новую функцию, для создания страницы 'about':
```
@app.route('/about/')
def about():
    return render_template("about.html")
```

Далее:
```
if __name__ == "__main__":
    app.run(debug=True)
```

** При запуске _Python_ файла, _Python_ присваивает файлу имя \__main__. При импорте данного скрипта в другой файл, данному файлу будет присвоено имя _script1.py_. Соответсвенно, приложение запускается только из данного файла. 

<a id="html"></a>

### 3. Подготовка HTML-шаблона:

Для того чтобы функция возвращала не просто строку, а _html_-шаблон __(return render_template("home.html"))__, импортируем метод _render_template_ библиотеки _Flask_.

> from flask import Flask, render_template

** _render_template_ имеет доступ к _html_-файлу, хранящемуся в папке _templates__, и отображает данный _html_-файл по заданному _URL_.

** Все _html_-файлы должны хранится в папке '_templates_'.

Создадим файл _home.html_ в папке _templates_. Важно чтобы имя файла совпадало с именем файла, который мы возвращаем в методе _render_template_ в функции.


Пример базового _html_-файла:
```
<!DOCTYPE html>
<html>
<body>
    <h1>Домашняя страница</h1>
    <p>Какой-то текст</p>
</body>
</html>
```

<a id="navigation"></a>

### 4. Создание навигационного меню сайта:

На примере файла _layout.html_

_layout.html_ - базовый шаблон, соответственно, _home.html_ и _about.html_ -  шаблоны-наследники.

```
<div class="container">
    {%block content%}
    {%endblock%}
</div>
```

_block content_ - место куда будут определены  шаблоны-наследники _home.html_ и _about.html_.

На примере файла _home.html_ (см. выше):
Так как _home.html_ - шаблон-наследник, \<!DOCTYPE html> не нужен, равно как и \<body> тег.

Заменим \<body> тег на \<div class="home">.

Добавим в начале:
```
{%extends "layout.html"%}
{%block content%}
```

Таким образом, данный код из файла _home.html_
```
<div class="home">
    <h1>Домашняя страница</h1>
    <p>Какой-то текст</p>
</div>
```

будет направлен в _{%block content%}_ файла _layout.html_ и файл _layout.html_ будет отображаться по _URL_ домашней страницы.


<a id="css"></a>

### 5. Работа над внешним видом страниц при помощи CSS

Создадим файл _main.css_, который находится в папке _static_.

Привяжем _main.css_ к _layout.html_.

Чтобы получить доступ к файлу _main.css_, в файле _layout.html_ надо добавить в начале данный код:
```
<head>
      <title>Flask App</title>
      <link rel="stylesheet" href="{{url_for('static',filename='css/main.css')}}">
  </head>
``` 
<a id="images"></a>

### 6. Прикрепление изображений:

Поместим изображение в _static/images_.

В _HTML_-файле папки _templates_ вставим строку:
> <img src="{‌{url_for('static', filename='images/a.jpg')}}"

Файл _home.html_ теперь выглядит так:
```
{%extends "layout.html"%}
{%block content%}
<div class="home">
    <h1>My homepage</h1>
    <p>Enjoying ourselves!</p>
    <img src="{{url_for('static', filename='images/IMG_1349.jpeg')}}" align="middle" width="390" height="280" />
</div>
{%endblock%}
```

<a id="deploy"></a>

### 7. Развертывание сайта на pythonanywhere:

_Pythonanywhere_ как и _Heroku_ позволяет бесплатно развертывать flask-приложения.

Важно:
```
if __name__ == "__main__":
    app.run(debug=True)
```

При развертывании сайта, в файле _script1.py_, __True__ заменим на __False__, чтобы не показывать посетителям ошибки _Python_, так как это может привести к уязвимости сайта.

[Вверх](#anchor)
