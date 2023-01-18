# import the flask class

from flask import Flask, render_template, request, redirect, url_for, session

from flask_mysqldb import MySQL
import mysql.connector
import MySQLdb.cursors
# import re

  
  
app = Flask(__name__)
  
  
app.secret_key="caircocoders-ednalan"
  
  
app.config['MYSQL_HOST'] = 'p3nlmysql85plsk.secureserver.net'
app.config['MYSQL_USER'] = 'sms22'
app.config['MYSQL_PASSWORD'] = '4%lh12Io'
app.config['MYSQL_DB'] = 'schoolmngsms'


  
mysql = MySQL(app)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        print("Its in get")
        print("1")
        return render_template("index.html")
    else:
        print("2")
        return render_template('Dashboard.html')
    





@app.route('/UI/Accountant/listofstudent') 

def index(): 
    #create a cursor
    cur = mysql.connection.cursor() 
    #execute select statement to fetch data to be displayed in combo/dropdown
    cur.execute('SELECT add_session FROM add_session') 
    #fetch all rows ans store as a set of tuples 
    add_session = cur.fetchall() 
    #render template and send the set of tuples to the HTML file for displaying
    return render_template("/UI/Accountant/Dashboard",add_session=add_session ) 


if __name__ == "__main__":
    app.run(debug=True)
   