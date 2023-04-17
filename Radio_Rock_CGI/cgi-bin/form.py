#!/usr/bin/env python3
import cgi
import html
from base.base import DataBase
from base.models import people
from werkzeug.security import generate_password_hash, check_password_hash
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages

form = cgi.FieldStorage()


sign_up_email = generate_password_hash(html.escape(form.getfirst('sign_up_email',' ')))
sign_up_password = generate_password_hash(html.escape(form.getfirst('sign_up_password', ' ')))
sign_up_login = generate_password_hash(html.escape(form.getfirst('sign_up_username',' ')))
sign_in_login = html.escape(form.getfirst('sign_in_username',' '))
sign_in_password = html.escape(form.getfirst('sign_in_password',' '))
bd=DataBase()

people(bd,'PEOPLE_LIST',sign_up_login,sign_up_password,sign_up_email)
print("Content-type: text/html")
print()
print('''<body>
Регистрация прошла успешно. Возвращаем вас на домашнюю страницу через 3...2....1...
</body>''')
print('<title>Переадресация</title>')
print('<meta http-equiv="refresh" content="3; URL=../RadioRock">')



     


