# -*- coding:  utf-8 -*-
from flask import render_template, flash, redirect
from app import app
from forms import DnevnikForm, TrenForm
from myStorage import myStorage

STORAGE = myStorage('C:\Users\Григорий\Google Диск\Python\RPGWorld\data.txt')
STORAGE_TREN = myStorage('C:\Users\Григорий\Google Диск\Python\RPGWorld\Trendata.txt')
STORAGE_RABOT = myStorage('C:\Users\Григорий\Google Диск\Python\RPGWorld\Rabotdata.txt')


@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'mrgrigorii' } # выдуманный пользователь
    posts = STORAGE.loadLast(10)
    posts2 = STORAGE_TREN.loadLast(5)
    posts3 = STORAGE_RABOT.loadLast(5)
    #old_posts = [ # список выдуманных постов
        #{ 
            #'author': { 'nickname': 'John' }, 
            #'body': 'Beautiful day in Portland!' 
        #},
        #{ 
            #'author': { 'nickname': 'Susan' }, 
            #'body': 'The Avengers movie was so cool!' 
        #}
    #]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts,
        posts2 = posts2,
        posts3 = posts3)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = DnevnikForm()
    if form.validate_on_submit():
        print form.openid.data
        STORAGE.addOne(form.openid.data)##.encode('utf-8')) ## Важно, позволяет работать с русским текстом!!
        flash('Login requested for OpenID="' + form.openid.data + '"') # + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    Hame = 'Dnecnick'#.decode('ascii').encode('utf-8')
    return render_template('login.html', 
        title = 'Add',
        form = form,
        Hame = Hame,
        posts2 = STORAGE.loadLast(10))

@app.route('/tren', methods = ['GET', 'POST'])
def tren():
    form = TrenForm()
    if form.validate_on_submit():
        print form.openid.data
        STORAGE_TREN.addOne(form.openid.data)##.encode('utf-8')) ## Важно, позволяет работать с русским текстом!!
        flash('Login requested for OpenID="' + form.openid.data + '"') # + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Add',
        form = form,
        Hame = 'Dnevnick Tren',
        posts2 = STORAGE_TREN.loadLast(5))
        
@app.route('/rabot', methods = ['GET', 'POST'])
def rabot():
    form = TrenForm()
    if form.validate_on_submit():
        print form.openid.data
        STORAGE_RABOT.addOne(form.openid.data)##.encode('utf-8')) ## Важно, позволяет работать с русским текстом!!
        flash('Login requested for OpenID="' + form.openid.data + '"') # + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', 
        title = 'Add',
        form = form,
        Hame = 'Dnevnick Rabot',
        posts2 = STORAGE_RABOT.loadLast(5))
