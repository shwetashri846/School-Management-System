from flask import Flask, render_template, request, redirect, url_for, session,flash

from flask_mysqldb import MySQL,MySQLdb
import mysql.connector
import MySQLdb.cursors
# import re
 
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request
from datetime import datetime
 

  
  
app = Flask(__name__)
  
  
app.secret_key="caircocoders-ednalan"
  
  
app.config['MYSQL_HOST'] = 'p3nlmysql85plsk.secureserver.net'
app.config['MYSQL_USER'] = 'sms22'
app.config['MYSQL_PASSWORD'] = '4%lh12Io'
app.config['MYSQL_DB'] = 'schoolmngsms'
app.config['MYSQL_CURSORCLASS'] ='DictCursor'

  
mysql = MySQL(app)


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
  
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/', methods = ['GET', 'POST'])
def index():
   
        return render_template("index.html")
    
    
    
 ###########about page########################   
    
@app.route('/about', methods = ['GET', 'POST'])
def about():
    print("page open")
    return render_template('about.html')

#############terms&condition###############

@app.route('/termscondition', methods = ['GET', 'POST'])
def termscondition():
    print("page open")
    return render_template('terms&condition.html')

@app.route('/returnpolicy', methods = ['GET', 'POST'])
def returnpolicy():
    print("page open")
    return render_template('returnpolicy.html')

#############privacypolicy##################
@app.route('/privacypolicy', methods = ['GET', 'POST'])
def privacypolicy():
    print("page open")
    return render_template('Privacy&policy.html')

################courses page################

@app.route('/courses', methods = ['GET', 'POST'])
def courses():
    print("page open")
    return render_template('Courses.html')




    




@app.route('/contact',methods=['GET','POST'])
def contact1():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        mobileno=request.form['mobileno']
        subject=request.form['subject']
        message=request.form['message']
        cursor=mysql.connection.cursor()
        cursor.execute("INSERT INTO contact (name,email,mobileno,subject,message) VALUES(%s,%s,%s,%s,%s)",[name,email,mobileno,subject,message])
        mysql.connection.commit()
        msg="successfully send data"
        return render_template("Contact.html",msg=msg)
    else:
        return render_template("index.html")

 


if __name__ == "__main__":
    app.run(debug=True)
  