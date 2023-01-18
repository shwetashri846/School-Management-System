from flask import Flask, render_template, request, redirect, url_for, session,flash

from flask_mysqldb import MySQL,MySQLdb
import mysql.connector
import MySQLdb.cursors
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
# app.config['MYSQL_CURSORCLASS'] ='DictCursor'

  
mysql = MySQL(app)


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
  
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS





 ################### header#################
@app.route("/",methods=['GET','POST'])
def header():
    if request.method=='POST':
        username=request.method['username']
        add_class=request.form['class']
        cursor=mysql.connection.cursor()
        cursor.execute("select * From studentreport where username=%s AND class=%s",(username,add_class))
        if session.loggedin:
            return render_template("UI/student/header.html",username=username,add_class=add_class)
    return render_template('UI/student/StudentDashboard.html')


               
 





  