<a id="anchor"></a>
# Веб-сайт 
#### Ссылка на сайт: http://vicoding.pythonanywhere.com


Web Development with Flask - Build a Personal Website

Создание веб-сайта при помощи _html_, _css_ (frontend ) и _python_ (backend).

___
Содержание:

* [1. Создание виртуальной среды](#virtual)
* [2. Начало работы](#work)
* [3. HTML-шаблон страницы](#html)
* [4. Навигационное меню](#navigation)
* [5. CSS внешний вид страницы](#css)
* [6. Изображения](#images)
* [7. Развертывание сайта](#deploy)
___

## Процесс создания:


<a id="virtual"></a>
### 1. Создание виртуальной среды:

Виртуальная среда создается в начале, чтобы иметь доступ к версии _Python_ без библиотек, модулей и всего того, что не понадобится в работе над данным проектом.
> pip install virtualenv

> python3 -m venv virtual

Установка _Flask_ в виртуальной среде:
> virtual/bin/pip3 install flask  (для mac)

Запуск веб-сайта в виртуальной среде:
> virtual/bin/python3 Website_on_Flask/script1.py

<a id="work"></a>

### 2. Начало работы:
Импортируем класс _Flask_ фреймфорка _Flask_ в файле script1.py:
> from flask import Flask

Создаем переменную app для хранения экземляра объекта:
```
app = Flask(__name__)
```
\### name - специальная переменная, в качестве значения принимающая название _Python_ скрипта/файла.

Используем декоратор @app.route('/') для создания Домашней страницы.

URL по которому наш вебсайт будет виден (/ - Домашняя страница)

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

\### При запуске _Python_ файла, _Python_ присваивает файлу имя \__main__. При импорте данного скрипта в другой файл, данному файлу будет присвоено имя _script1.py_ и файл запускаться не будет. С помощью кода выше, мы получаем контроль над файлом, так как приложение запускается только из данного файла. 

<a id="html"></a>

### 3. Подготовка HTML-шаблона:

Для того чтобы функция возвращала не просто строку, а html-шаблон (return render_template("home.html")),
нужно импортировать метод _render_template_ библиотеки _Flask_.
> from flask import Flask, render_template

\### _render_template_ обращается к html-файлу, хранящемуся в папке приложения, и показывает данный html-файл по заданному URL.

\### Все html-файлы должны хранится в папке, названной '_templates_'.

Создадим файл _home.html_ в папке _templates_. Важно чтобы имя файла совпадало с именем файла, который
мы возвращаем в методе _render_template_ в функции.


Простой html-файл выглядит следующим образом:
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

_layout.html_ - базовый шаблон, соответственно, _home.html_ и _about.html_ - child шаблоны. 
(_стр.20 - 23_)
```
<div class="container">
    {%block content%}
    {%endblock%}
</div>
```

_block content_ - место куда будут определены child шаблоны _home.html_ и _about.html_.

На примере файла _home.html_ (см. выше):
Так как _home.html_ это child шаблон, \<!DOCTYPE html> не нужен, равно как и \<body> тег.

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

будет направлен в _{%block content%}_ файла _layout.html_ и файл _layout.html_ будет показан по URL домашней страницы.


<a id="css"></a>

### 5. Улучшение внешнего вида страниц при помощи CSS

Создадим файл _main.css_, который должен находиться в папке _static_.

Далее свяжем _main.css_ c _layout.html_ файлом.

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

В HTML-файле, который находится в папке _templates_ вставим строку:
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

_Pythonanywhere_ как и _Heroku_ позволяет бесплатно развертывать flask-приложения. Но _pythonanywhere_, на мой взгляд, удобней для пользователей. Поэтому я выбрал _pythonanywhere_.

Важно:
```
if __name__ == "__main__":
    app.run(debug=True)
```

При развертывании сайта, в файле _script1.py_, __True__ заменим на __False__, чтобы не показывать посетителям ошибки _Python_, так как это может привести к уязвимости сайта.

[Вверх](#anchor)
