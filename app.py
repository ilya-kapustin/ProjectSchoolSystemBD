from flask import Flask, render_template, request, redirect
import connectBD as contBD
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)
engine = create_engine(contBD.Database_Con)
con = engine.connect()

hed_menu = {
    'Главная': '/',
    'Студенты': '/student',
    'О нас': '/about',
}


@app.route('/')
def index():
    return render_template('index.html', menu=hed_menu, title='Главная')


@app.route('/about')
def about():
    return render_template('about.html', menu=hed_menu, title='О нас')


@app.route('/student')
def student():
    df_students = pd.read_sql_query("Select * from [School].[dbo].[Students]", con)
    return render_template('student.html', menu=hed_menu, students=df_students, title='Студенты')


@app.route('/add_student', methods=['POST', 'GET'])
def add_student():
    if request.method == 'POST':
        print('fff')
        name = str(request.form['name'])
        surname = str(request.form['surname'])
        gender = str(request.form['gender'])
        born = int(request.form['born'])
        engine.execute(
            f"INSERT INTO [School].[dbo].[Students] (Name, Surname, Gender, Born) VALUES ('{name}', '{surname}', '{gender}', '{born}')")
        return redirect('/')
    else:
        return render_template('add_student.html', menu=hed_menu, title='Добавление студента')


if __name__ == '__main__':
    app.run(debug=True)
