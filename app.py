import re
from flask import Flask, flash, render_template, request, redirect,url_for
from flask_mysqldb import MySQL


app = Flask(__name__)
#MySQL connection 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

#Secion, datos que guarda nuestra aplicacion del servidor para volver a utilizarlos
#Settings
app.secret_key = 'mysecretekey'

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact',methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname =  request.form['fullname']
        phone =  request.form['phone']
        email =  request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts(fullname,phone,email) VALUES(%s,%s,%s)',(fullname,phone,email))
        mysql.connection.commit()
        flash('contact Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit contact'
@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(port = 3000, debug= True)

