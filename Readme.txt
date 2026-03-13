1) устанавливается python 3.14.3
2) по пути C:\ProgrammDjango4 создано виртуальное окружение: py -m venv my_env
3) виртуальное окружение активировано: .\my_env\Scripts\activate
4) установлен Django в виртуальном окружении: pip install Django~=4.1.0
5) создана файловая структура проекта: django-admin startproject mysite
6) по пути C:\ProgrammDjango4\mysite создан проект: python manage.py startapp diploma
7) в файле mysite/settings.py, diploma/models.py и прочих файлах проекта проводились различные надстройки
8) применялись миграции для корректной работы: python manage.py makemigrations; python manage.py migrate;
9) после всех настроек файлов запускается сервер: python manage.py runserver
10) происходит переход по ссылке: http://127.0.0.1:8000/diploma/add/
