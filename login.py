
from flask import Flask, render_template,redirect, url_for, request,jsonify,session,flash

from flask_mysqldb import MySQL,MySQLdb
# from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import MySQLdb.cursors
from werkzeug.utils import secure_filename
import os
import header
import header1

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
# db = SQLAlchemy(app)
  
mysql = MySQL(app)


UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif','pdf'])
  
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 



  
#######index page#######


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        print("Its in get")
        print("1")
        return render_template("index.html")
    else:
        print("2")
        return render_template('Dashboard.html')


################## index page ##############


@app.route("/index")
def ind():

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


#################loginMaster################

@app.route('/loginMaster', methods = ['GET', 'POST'])
def loginMaster():
    print("page open")
    return render_template('UI/Login/loginMaster.html')


################sreport#################

@app.route('/sreport', methods = ['GET', 'POST'])
def sreport():
    if request.method==['GET']:
        # cur=mysql.connection.cursor()
        # return request. args. get("param")
        # cur.execute("SELECT * FROM  addstudentdetail  WHERE id='params'")
        # mysql.connection.commit()
        # data=cur.fetchall()
        
        args=request.args
        if param in args:
            param=args.get("param")
            print("param")
    
        # return render_template("sreport.html",addstudentdetail=data)
    

################courses page################

@app.route('/courses', methods = ['GET', 'POST'])
def courses():
    print("page open")
    return render_template('Courses.html')


################contact page##############


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    print("page open")
    return render_template('Contact.html')


#######dashboard#####

@app.route('/Dashboard', methods = ['GET', 'POST'])
def dashboard():
    if request.method=='POST':
        username=request.method['username']
        cursor=mysql.connection.cursor()
        cursor.execute("select * From loginmaster where username=%s",(username))
        if session.loggedin:
            return render_template("Dashboard.html",username=username)
    return render_template('Dashboard.html')
###########master dashboard###############

@app.route('/UI/Master/dashboard', methods = ['GET', 'POST'])
def masterdashboard():
    if request.method=='POST':
        username=request.method['username']
        cursor=mysql.connection.cursor()
        cursor.execute("select * From masteloginr where username=%s",(username))
        if session.loggedin:
            return render_template("UI/Master/dashboard.html",username=username)
    return render_template('UI/Master/dashboard.html')



#############feetitle##############


@app.route('/UI/Master/feetitle',methods=['GET','POST'])
def fee():
    if request.method == 'POST':
        feetitle=request.form['feetitle']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  addfeetitle(feetitle) VALUES (%s)",[feetitle])
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeetitle")
        
        data = cur.fetchall()
        mysql.connection.commit()
        flash('You were successfully submitted')
        return render_template("UI/Master/addfeetitle.html",addfeetitle= data)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeetitle")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("UI/Master/addfeetitle.html" ,addfeetitle= data)
    
    
    
    
###################Add_Class_Update#############


# @app.route('/UI/Report/addclassreport',methods=['GET','POST'])
# def update():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
#         add_class=request.form['class']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE add_class
#                SET class=%s
#                WHERE id=%s
#             """, ( add_class, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("UI/Report/addclassreport.html" ,msg=msg)

############# Fee Amount Report ##################

@app.route('/UI/Report/addfeereport',methods=['GET','POST'])
def addfeereport():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addfeeamount')
        c=cur.fetchall()
        
        return render_template("UI/Report/addfeereport.html",addfeeamount=c)
    else:
        id_data = request.form['id']
        feetitle=request.form['feetitle']
        add_class = request.form['class']      
        feeamount=request.form['feeamount']
        rollno=request.form['rollno']
        add_section=request.form['add_section']
        add_session=request.form['add_session']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
                UPDATE addfeeamount 
                SET feetitle=%s,class=%s,feeamount=%s,rollno=%s,add_section=%s,add_session=%s
                WHERE id=%s
             """, ( feetitle,add_class,feeamount,rollno,add_section,add_session,id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addfeeamount')
        c=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/addfeereport.html",addfeeamount=c,msg=msg)



    
    
    
##############add_Class_Delete########################


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM add_class WHERE id=%s", (id_data,))
    cur.execute("SELECT * FROM add_class")
    a=cur.fetchall()

    
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("UI/Report/addclassreport.html" , msg=msg,add_class=a)

###################  Search Date in admin panel ################

# @app.route('/searchdata/<string:id_data>', methods = ['GET'])
# def searchdata(id_data):
    
   
#     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cur.execute("SELECT id,name,rollno,class,add_section,add_session,date,feetitle,category,actualfee,discount,total FROM practice WHERE id=%s", (id_data,))
    
#     c=cur.fetchone()

    
#     mysql.connection.commit()
#     msg=("Search Successfully")
#     return render_template("UI/Accountant/monthlyfeebill.html" , msg=msg,practice=c)


    


##################add class##################




# @app.route('/UI/Admin/addclass',methods=['GET','POST'])
# def addclass():
    
#     cur = mysql.connection.cursor()
#     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     now = datetime.now()
#     if request.method == 'POST':
#         files1 = request.files.getlist('files1[]')
#         add_class=request.form['class']
#         #print(files)
#         for file in files1:
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 cur.execute("INSERT INTO add_class (file_name, uploaded_on,add_class) VALUES (%s, %s,%s)",[filename, now,add_class])
#                 mysql.connection.commit()
#             print(file)
#         cur.close()   
#         flash('File(s) successfully uploaded')    
#     return render_template('UI/Admin/Add Class.html')
#     # else:
#     #     cur = mysql.connection.cursor()
#     #     cur.execute("SELECT * FROM add_class")
#     #     data = cur.fetchall()
#     #     print("gridview")
#     #     return render_template("UI/Admin/Add Class.html" ,add_class= data)

        

@app.route('/UI/Master/addclass',methods=['GET','POST'])
def addclass():
    if request.method == 'POST':
        add_class=request.form['class']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO add_class (class) VALUES (%s)",[add_class])
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM add_class")
        data = cur.fetchall()
        mysql.connection.commit()
        msg="successfully addclass"
        return render_template("UI/Master/Add Class.html" ,msg=msg,add_class=data)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM add_class")
        data = cur.fetchall()
        print("gridview")
        return render_template("UI/Master/Add Class.html",add_class=data)
    
    
    
####################UPDATE STUDeNT REGISTRATION REPORT####################




# @app.route('/updatedemo',methods=['GET','POST'])
# def updatedemo():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
#         name=request.form['name']
#         add_section=request.form['add_section']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE student_registration
#                SET name=%s,add_section
#                WHERE id=%s
#             """, ( name,add_section, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)



# @app.route('/updatestudentregistrationreport',methods=['GET','POST'])
# def updatestudentregistrationreport():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
#         name=request.form['name']
        
#         add_class=request.form['class']
#         add_section=request.form['add_section']
#         rollno=request.form['rollno']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addstudentdetail
#                SET name=%s,class=%s,add_section=%s,rollno=%s
#                WHERE id=%s
#             """, ( add_class, id_data,name,add_section,rollno))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
        
        
#############datashow#############



# @app.route('/datashow',methods=['GET','POST'])

# def test():
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * FROM add_class")
        
#         data = cur.fetchall()
#         print("demo")
        
#         return render_template("datashow.html" ,add_class= data)





################Update Section###############



# @app.route('/updatesection',methods=['GET','POST'])
# def updatesection():
#     if request.method == 'POST':
#         id_data = request.form['id']
#         add_section=request.form['add_section']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE new_section
#                SET add_section=%s
#                WHERE id=%s
#             """, (add_section,id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
##############delete section########################


@app.route('/deletesection/<string:id_data>', methods = ['GET'])
def deletesection(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM new_section WHERE id=%s",(id_data,))
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM new_section")
    c=cur.fetchall()

    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("UI/Report/addsectionreport.html" , msg=msg,new_section=c)




################Update Session###############



# @app.route('/UI/Report/addsessionreport',methods=['GET','POST'])
# def updatesession():
#     if request.method == 'POST':
#         id_data = request.form['id']
#         add_session=request.form['add_session']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE add_session
#                SET add_session=%s
#                WHERE id=%s
#             """, ( add_session, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("UI/Report/addsessionreport.html" ,msg=msg)

########### Update feetitle#############
# @app.route('/updatefeetitle',methods=['GET','POST'])
# def updatefeetitle():
#     if request.method == 'POST':
#         id_data = request.form['id']
#         feetitle=request.form['feetitle']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addfeetitle
#                SET feetitle=%s
#                WHERE id=%s
#             """, ( feetitle, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("UI/Report/feetitleeport.html" ,msg=msg)



################ delete Manage section ###############

@app.route('/deletemanagesection/<string:id_data>', methods = ['GET'])
def deletemanagesection(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM managesection WHERE id=%s",(id_data,))
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,name,class,classteacher,note FROM managesection")
        data=cur.fetchall()

        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/managesectionreport.html",managesection=data,msg=msg)






    
    
    
    
#################delete Session###################


@app.route('/deletesession/<string:id_data>', methods = ['GET'])
def deletesession(id_data):
    if request.method=='GET':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM add_session WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM add_session")
        c=cur.fetchall()


        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/addsessionreport.html" , msg=msg,add_session=c)

    
    

        


##################add Session#################    
    
@app.route('/UI/Master/addsession',methods=['GET','POST'])
def addsession():
    if request.method == 'POST':
        add_session=request.form['add_session']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO add_session (add_session) VALUES (%s)",[add_session])
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM add_session")
        
        data = cur.fetchall()
        mysql.connection.commit()
        msg="successfully addsession"
        return render_template("UI/Master/Add Session.html" ,msg=msg,add_session= data)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM add_session")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("UI/Master/Add Session.html" ,add_session= data)
    
    
    
    
    
################add Section######################3   
    
    
@app.route('/UI/Master/addsection',methods=['GET','POST'])
def addsection():
    if request.method == 'POST':
        add_section=request.form['add_section']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO new_section (add_section) VALUES (%s)",[add_section])
        cur = mysql.connection.cursor()
        cur.execute("SELECT id,add_section FROM new_section")
        
        data = cur.fetchall()
        mysql.connection.commit()
        msg="successfully addsection"
        return render_template("UI/Master/Add Section.html" ,msg=msg,new_section= data)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id,add_section FROM new_section")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("UI/Master/Add Section.html",new_section= data)
    
    
    
###################Update Nonfaculty#######################



# @app.route('/updatenonfaculty',methods=['GET','POST'])
# def updatenonfaculty():
#     if request.method == 'POST':
#         id_data = request.form['id']
#         name=request.form['name']
#         email=request.form['email']
#         mobileno=request.form['mobileno']
#         gender=request.form['gender']
#         dateofbirth=request.form['dateofbirth']
#         qualification=request.form['qualification']
#         yearofexperience=request.form['yearofexperience']
#         aadharno=request.form['aadharno']
#         address=request.form['address']
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE nonfaculty
#                SET name=%s, email=%s, mobileno=%s,gender=%s,dateofbirth=%s,qualification=%s,yearofexperience=%s,aadharno=%s,address=%s
#                WHERE id=%s
#             """, ( name,email,mobileno,gender,dateofbirth,qualification,yearofexperience,aadharno,address, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
######################Delete Nonfaculty###############



@app.route('/deletenonfaculty/<string:id_data>', methods = ['GET'])
def deletenonfaculty(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM nonfaculty WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor,file_name FROM nonfaculty')
        data=cur.fetchall()
       
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")

        return render_template('UI/Report/nonfacultyreport.html',nonfaculty=data,msg=msg)

        
        
###################Add NonFaculty################# 



@app.route('/UI/Accountant/addnonfaculty',methods=['GET','POST'])
def addnonfaculty():
    
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':
        
        name=request.form['name']
        nationalid=request.form['nationalid']
        phone=request.form['phone']
        gender=request.form['gender']
        birthdate=request.form['birthdate']
        joiningdate=request.form['joiningdate']
        fathername=request.form['fathername']
        aadharno=request.form['aadharno']
        presentaddress=request.form['presentaddress']
        permanentaddress=request.form['permanentaddress']
        qualification=request.form['qualification']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        designation=request.form['designation']
         
        applyfor=request.form['applyfor']
        files1 = request.files.getlist('files1[]')
        print("files")
        for file in files1:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cur.execute("INSERT INTO nonfaculty (name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor,file_name,uploaded_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor,filename, now])
                mysql.connection.commit()
            print(file)
           
        flash('File(s) successfully uploaded')    
    return render_template('UI/Accountant/Add NonFaculty.html')



# @app.route('/UI/NonFaculty/addnonfaculty',methods=['GET','POST'])
# def addnonfaculty(): 
    
#     cur = mysql.connection.cursor()
#     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     now = datetime.now()
#     if request.method == 'POST':
#         files1 = request.files.getlist('files1[]')
#         name=request.form['name']
#         nationalid=request.form['nationalid']
#         phone=request.form['phone']
#         gender=request.form['gender']
#         birthdate=request.form['birthdate']
#         joiningdate=request.form['joiningdate']
#         fathername=request.form['fathername']
#         aadharno=request.form['aadharno']
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         qualification=request.form['qualification']
#         email=request.form['email']
#         username=request.form['username']
#         password=request.form['password']
#         designation=request.form['designation']
#         applyfor=request.form['applyfor']
         
#         # yearofexperience=request.form['yearofexperience']
#         print("files")
#         for file in files1:
#             if file and allowed_file(file.filename):
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#                 cur.execute("INSERT INTO nonfaculty (file_name, uploaded_on,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[filename,now,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor])
#                 mysql.connection.commit()
#             print(file)
           
#         flash('File(s) successfully uploaded')    
#     return render_template('UI/NonFaculty/Add Nonfaculty.html')

   
    
# @app.route('/UI/NonFaculty/addnonfaculty',methods=['GET','POST'])
# def addnonfaculty(): 
#     if request.method=='POST':
#         print("6")
        
#         name=request.form['name']
#         nationalid=request.form['nationalid']
#         phone=request.form['phone']
#         gender=request.form['gender']
#         birthdate=request.form['birthdate']
#         joiningdate=request.form['joiningdate']
#         fathername=request.form['fathername']
#         aadharno=request.form['aadharno']
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         qualification=request.form['qualification']
#         email=request.form['email']
#         username=request.form['username']
#         password=request.form['password']
#         designation=request.form['designation']
#         photo=request.form['photo']
#         applyfor=request.form['applyfor']
#         cur=mysql.connection.cursor()
    #     cur.execute("INSERT INTO nonfaculty (name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo,applyfor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo,applyfor])
    #     mysql.connection.commit()
    #     msg="successfully addnonfaculty"
    #     return render_template('Dashboard.html',msg=msg)
    # else: 
        
        
    #     return render_template("UI/NonFaculty/Add Nonfaculty.html" )
    
#################Update Teacher##############



# @app.route('/updateteacher',methods=['GET','POST'])
# def updateteacher():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
        
#         name=request.form['name']
#         nationalid=request.form['nationalid']
#         phone=request.form['phone']
#         gender=request.form['gender']
#         birthdate=request.form['birthdate']
#         joiningdate=request.form['joiningdate']
#         fathername=request.form['fathername']
#         aadharno=request.form['aadharno']
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         qualification=request.form['qualification']
#         email=request.form['email']
#         username=request.form['username']
#         password=request.form['password']
#         designation=request.form['designation']
#         # photo=request.form['photo']
#         yearofexperience=request.form['yearofexperience']
#         add_class=request.form['class']
#         subject=request.form['subject']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addteacher
#                SET name=%s,nationalid=%s,phone=%s,gender=%s,birthdate=%s,joiningdate=%s,fathername=%s,aadharno=%s,presentaddress=%s,permanentaddress=%s,qualification=%s,email=%s,username=%s,password=%s,designation=%s,yearofexperience=%s,class=%s,subject=%s
#                WHERE id=%s
#             """, (name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,yearofexperience,add_class,subject,id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    





    
################ Update student gridview#####################




# @app.route('/updatestudentgridview',methods=['GET','POST'])
# def updatetgridview():
#     if request.method == 'POST':
#         id_data = request.form['id']
        
#         name=request.form['name']
#         fathername=request.form['fathername']
#         mothername=request.form['mothername']
#         addmission=request.form['addmission']
#         admissiondate=request.form['admissiondate']
#         birthdate=request.form['birthdate']
#         gender=request.form['gender']
#         aadharno=request.form['aadharno']
#         religion=request.form['religion']
#         caste=request.form['caste']
#         housename=request.form['housename']
#         phone=request.form['phone']
#         email=request.form['email']
#         add_class=request.form['class']
#         add_section=request.form['add_section']
#         stream=request.form['stream']
#         rollno=request.form['rollno']
#         feeexcused=request.form['feeexcused']
#         add_session=request.form['add_session']
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         username=request.form['username']
#         password=request.form['password']
            
#         cur = mysql.connection.cursor()
#         cur.execute('UPDATE studentreport SET  name=%s,fathername=%s,mothername=%s,addmission=%s,admissiondate=%s,birthdate=%s,gender=%s, aadharno=%s,religion=%s,caste=%s,housename=%s,phone=%s,email=%s,class=%s,add_section=%s,stream=%s,rollno=%s,feeexcused=%s,add_section=%s,presentaddress=%s,permanentaddress=%s,username=%s,password=%s WHERE id =% s', (name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,add_class,add_section,stream,rollno,feeexcused,add_session,presentaddress,permanentaddress,username,password ,id_data ))
                
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("UI/student/StudentDashboard.html" ,msg=msg)
        
    
    
######################Delete Teacher###############



@app.route('/deleteteacher/<string:id_data>', methods = ['GET'])
def deleteteacher(id_data):
    if request.method=='GET':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addteacher WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,yearofexperience,file_name,class,subject FROM addteacher')
        data=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/teacherreport.html" ,msg=msg,addteacher=data)


#########################Teacher Report################



@app.route('/UI/Report/teacherreport',methods=['GET','POST'])
def teacherreport ():
    if request.method=="GET":
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,yearofexperience,file_name,class,subject FROM addteacher')
        data=cur.fetchall()
        return render_template('UI/Report/teacherreport.html',addteacher=data)
    else:
            
        
        id_data = request.form['id']
        
        name=request.form['name']
        nationalid=request.form['nationalid']
        phone=request.form['phone']
        gender=request.form['gender']
        birthdate=request.form['birthdate']
        joiningdate=request.form['joiningdate']
        fathername=request.form['fathername']
        aadharno=request.form['aadharno']
        presentaddress=request.form['presentaddress']
        permanentaddress=request.form['permanentaddress']
        qualification=request.form['qualification']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        designation=request.form['designation']
        # files1 = request.files.getlist('files1[]')

        yearofexperience=request.form['yearofexperience']
        add_class=request.form['class']
        subject=request.form['subject']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addteacher
               SET name=%s,nationalid=%s,phone=%s,gender=%s,birthdate=%s,joiningdate=%s,fathername=%s,aadharno=%s,presentaddress=%s,permanentaddress=%s,qualification=%s,email=%s,username=%s,password=%s,designation=%s,yearofexperience=%s,class=%s,subject=%s
               WHERE id=%s
            """, (name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,yearofexperience,add_class,subject,id_data))
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,yearofexperience,file_name,class,subject FROM addteacher")
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template('UI/Report/teacherreport.html',addteacher=data,msg=msg)







    


    
    
    
    
########################## student Report##############



@app.route('/UI/Report/studentreport',methods=['GET','POST'])
def studentrep ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        # cur.execute('SELECT id,add_session,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file_name, FROM studentreport')
        # data=cur.fetchall()
        cur.execute('SELECT * FROM studentreport')
        data=cur.fetchall()
        return render_template('UI/Report/studentgridview.html',studentreport=data)
    else:
        id_data = request.form['id']
        
        name=request.form['name']
        fathername=request.form['fathername']
        mothername=request.form['mothername']
        addmission=request.form['addmission']
        admissiondate=request.form['admissiondate']
        birthdate=request.form['birthdate']
        gender=request.form['gender']
        aadharno=request.form['aadharno']
        religion=request.form['religion']
        caste=request.form['caste']
        housename=request.form['housename']
        phone=request.form['phone']
        email=request.form['email']
        add_class=request.form['class']
        add_section=request.form['add_section']
        stream=request.form['stream']
        rollno=request.form['rollno']
        feeexcused=request.form['feeexcused']
        add_session=request.form['add_session']
        presentaddress=request.form['presentaddress']
        permanentaddress=request.form['permanentaddress']
        username=request.form['username']
        password=request.form['password']
            
        cur = mysql.connection.cursor()
        cur.execute('UPDATE studentreport SET  name=%s,fathername=%s,mothername=%s,addmission=%s,admissiondate=%s,birthdate=%s,gender=%s, aadharno=%s,religion=%s,caste=%s,housename=%s,phone=%s,email=%s,class=%s,add_section=%s,stream=%s,rollno=%s,feeexcused=%s,add_session=%s,presentaddress=%s,permanentaddress=%s,username=%s,password=%s WHERE id =% s', (name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,add_class,add_section,stream,rollno,feeexcused,add_session,presentaddress,permanentaddress,username,password ,id_data ))
        cur=mysql.connection.cursor()
        # cur.execute('SELECT id,add_session,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file_name, FROM studentreport')
        # data=cur.fetchall()
        cur.execute('SELECT * FROM studentreport')
        data=cur.fetchall()        
        mysql.connection.commit()
        msg="successfully updated"
        return render_template('UI/Report/studentgridview.html',studentreport=data,msg=msg)
    
    



###################### Manage Section Report#################



@app.route('/UI/Report/managesectionreport',methods=['GET','POST'])
def managesectionreport ():
    if request.method=='GET':

        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,class,classteacher,note FROM managesection')
        data=cur.fetchall()
        return render_template('UI/Report/manageSectionReport.html',managesection=data)
    else:
        id_data = request.form['id']
        name=request.form['name']
        add_class=request.form['class']
        
        classteacher=request.form['classteacher']
        note=request.form['note']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE managesection
               SET name=%s,class=%s,classteacher=%s,note=%s
               WHERE id=%s
            """, (name,add_class,classteacher,note, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,class,classteacher,note FROM managesection')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/managesectionreport.html",managesection=data,msg=msg)

    
    
    
    
    
    
    
###################Manage Class Report###############



@app.route('/UI/Report/manageclassreport',methods=['GET','POST'])
def manageclassreport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,class,numericname,classteacher,note FROM manageclass')
        data=cur.fetchall()
        return render_template('UI/Report/manageclassreport.html',manageclass=data)
    else:
        id_data = request.form['id']
        add_class=request.form['class']

        numericname=request.form['numericname']
        classteacher=request.form['classteacher']
        
        note=request.form['note']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE manageclass
               SET class=%s,numericname=%s,classteacher=%s, note=%s
               WHERE id=%s
            """, ( add_class,numericname,classteacher,note, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,class,numericname,classteacher,note FROM manageclass')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("/UI/Report/manageclassreport.html" ,msg=msg,manageclass=data)
    
    


    
    
 ################Update Manage Class Report##########   
    
# @app.route('/UI/Report/manageclassreport',methods=['GET','POST'])
# def updatemanageclass():
#     if request.method == 'POST':
#         id_data = request.form['id']
#         add_class=request.form['class']

#         numericname=request.form['numericname']
#         classteacher=request.form['classteacher']
        
#         note=request.form['note']
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE manageclass
#                SET class=%s,numericname=%s,classteacher=%s, note=%s
#                WHERE id=%s
#             """, ( add_class,numericname,classteacher,note, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("/UI/Report/manageclassreport.html" ,msg=msg)
    
    


       
    
#####################Add Teacher####################    
    
# @app.route('/UI/Faculty/addteacher',methods=['GET','POST'])
# def addteacher():
#     if request.method == 'POST':
#         print("6")
        
#         name=request.form['name']
#         nationalid=request.form['nationalid']
#         phone=request.form['phone']
#         gender=request.form['gender']
#         birthdate=request.form['birthdate']
#         joiningdate=request.form['joiningdate']
#         fathername=request.form['fathername']
#         aadharno=request.form['aadharno']
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         qualification=request.form['qualification']
#         email=request.form['email']
#         username=request.form['username']
#         password=request.form['password']
#         designation=request.form['designation']
#         photo=request.form['photo']
#         yearofexperience=request.form['yearofexperience']
#         cur=mysql.connection.cursor()
#         cur.execute("INSERT INTO addteacher (yearofexperience,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[yearofexperience,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo])
#         mysql.connection.commit()
#         msg="successfully addteacher"
#         return render_template('Dashboard.html',msg=msg)
#     else: 
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * FROM addteacher")
        
#         data = cur.fetchall()
#         print("demo")
        
#         return render_template("UI/Faculty/Add Teacher.html" ,teacher= data)

########### Addstudentfee############### 
@app.route('/UI/Accountant/insert',methods=['GET','POST'])
def insdemo():
    if request.method=='GET':
        name=request.form.get['name']
        rollno=request.form.get['rollno']
        add_class=request.form.get['class']
        add_section=request.form.get['add_section']
        add_session=request.form.get['add_session']
        admissiondate=request.form.get['admissiondate']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT name,rollno,add_session,add_section,class,admissiondate FROM studentreport WHERE add_session=%s AND add_section=%s AND class=%s AND rollno=%s AND admissiondate=%s",(add_session,add_section,add_class,rollno,admissiondate))
        s=cursor.fetchone() 
        cursor=mysql.connection.cursor()
        cursor.execute("SELECT id,feetitle,category,class,feeamount FROM addfeeamount WHERE  class=%s",(add_class))  
        addfeeamount=cursor.fetchall()
        return render_template("UI/Accountant/insertdemomas.html",studentreport=s,addfeeamount=addfeeamount)
    else:
        
        
        cursor = mysql.connection.cursor()
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        now = datetime.now()
        if request.method=='POST':
            name=request.form['name']
            feetitle=request.form['feetitle']
            category=request.form['category']
            actualfee=request.form['actualfee']
            discount=request.form['discount']
            total=request.form['total']
            rollno=request.form['rollno']
            add_class=request.form['class']
            add_section=request.form['add_section']
            add_session=request.form['add_session']
            admissiondate=request.form['admissiondate']
            
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT name,rollno,add_session,add_section,class,admissiondate FROM studentreport WHERE add_session=%s AND add_section=%s AND class=%s AND rollno=%s AND admissiondate=%s",(add_session,add_section,add_class,rollno,admissiondate))
            s=cursor.fetchone()
            cursor = mysql.connection.cursor()
            
            cursor.execute('INSERT INTO practice  (name,feetitle,category,actualfee,discount,total,rollno,class,add_section,add_session,admissiondate,date) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', [name,feetitle,category,actualfee,discount,total,rollno,add_class,add_section,add_session,admissiondate,now])
            cursor=mysql.connection.cursor()
            cursor.execute("SELECT id,feetitle,category,class,feeamount FROM addfeeamount WHERE  class=%s",(add_class))  
            addfeeamount=cursor.fetchall()
            mysql.connection.commit()
            msg="successfully inserted"
            return render_template("UI/Accountant/insertdemomas.html" ,msg=msg,studentreport=s,addfeeamount=addfeeamount)

    
    

    


@app.route('/UI/Accountant/addteacher',methods=['GET','POST'])
def addteacher():
    if request.method=='GET':
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT * FROM add_class ')
        add_class=cur.fetchall()
        cur.execute('SELECT * FROM addsubject ')
        addsubject=cur.fetchall()
        return render_template("UI/Accountant/Add Teacher.html",add_class=add_class,addsubject=addsubject)

    else:
        cur = mysql.connection.cursor()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        now = datetime.now()
        if request.method == 'POST':
            files1 = request.files.getlist('files1[]')
            name=request.form['name']
            nationalid=request.form['nationalid']
            phone=request.form['phone']
            gender=request.form['gender']
            birthdate=request.form['birthdate']
            joiningdate=request.form['joiningdate']
            fathername=request.form['fathername']
            aadharno=request.form['aadharno']
            presentaddress=request.form['presentaddress']
            permanentaddress=request.form['permanentaddress']
            qualification=request.form['qualification']
            add_class=request.form['class']
            subject=request.form["subject"]
            email=request.form['email']
            username=request.form['username']
            password=request.form['password']
            designation=request.form['designation']
         
            yearofexperience=request.form['yearofexperience']
            print("files")
            for file in files1:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    cur.execute("INSERT INTO addteacher (file_name, uploaded_on,yearofexperience,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,class,subject,email,username,password,designation) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,)",[filename, now,yearofexperience,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,add_class,subject,email,username,password,designation])
                    mysql.connection.commit()
                print(file)
           
            flash('File(s) successfully uploaded')    
        return render_template('UI/Accountant/Add Teacher.html')




##################feecategory#######################
# @app.route('/UI/Admin/addsyllabus',methods=['GET','POST'])
# def addsyllabus():
#     if request.method=="POST":
         
        
#         topic=request.form['topic']
#         subject=request.form['subject']
#         complete=request.form["complete"]
#         add_class=request.form["class"]
        
#         cur=mysql.connection.cursor()
#         cur.execute("INSERT INTO addsyllabus (topic,subject,complete,class)VALUES(%s,%s,%s,%s)" ,[topic,subject,complete,add_class])
#         mysql.connection.commit()
#         msg="Successfully addsyllabus"
#         return render_template("Dashboard.html" ,msg=msg)
#     else:
#         cur=mysql.connection.cursor()
        
#         cur.execute("SELECT * FROM addsyllabus")
#         h=cur.fetchall()
#         cur.execute("SELECT class FROM add_class")
#         o=cur.fetchall()
#         cur.execute("SELECT subject FROM addsubject")
#         i=cur.fetchall()
#         return render_template('UI/Admin/addsyllabus.html',addsylabus=h,addsubject=i,add_class=o)

@app.route('/UI/Master/addfeecategory',methods=['GET','POST'])
def addfeecategory():
    if request.method=="GET":
        
        feetitle=request.form['feetitle']
        category=request.form['category']
        c_id=request.form['c_id']
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM addfeetitle")
        v=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeecategory")
        b=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO addfeecategory (feetitle,category,c_id)VALUES(%s,%s,%s)",[feetitle,category,c_id])
        msg="successfully insert"
        return render_template('UI/Master/addfeecategory.html',addfeetitle=v,addfeecategory=b,msg=msg)
   
        
        
        
        
        
    else:    
        
        
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT id FROM addfeetitle WHERE feetitle=%s",(feetitle) )
        a=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("SELECT feetitle FROM addfeecategory")
        v=cur.fetchall()
        mysql.connection.commit()
        msg="Successfully addcategory"
        return render_template("UI/Master/addfeecategory.html" ,msg=msg,addfeetitle=a,addfeecategory=v)
        
    
    
        
    
    
    
    
    
 ####################Manage Class###############   


@app.route('/UI/Admin/manageclass',methods=['GET','POST'])
def manageclass():
    if request.method=="POST":
         
        
        add_class=request.form['class']
        numericname=request.form['numericname']
        classteacher=request.form['classteacher']
        note=request.form['note']
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO manageclass (class,numericname,classteacher,note)VALUES(%s,%s,%s,%s)" ,[add_class,numericname,classteacher,note])
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,class,numericname,classteacher,note FROM manageclass')
        data=cur.fetchall()
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT name FROM addteacher ORDER BY id")
        f=cur.fetchall()
        cur.execute("SELECT class FROM add_class ORDER BY id")
        h=cur.fetchall()
        mysql.connection.commit()
        msg="Successfully manageclass"
        return render_template('UI/Admin/manageClass.html',addteacher=f,add_class=h,manageclass=data,msg=msg)
    else:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT name FROM addteacher ORDER BY id")
        f=cur.fetchall()
        cur.execute("SELECT class FROM add_class ORDER BY id")
        h=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,class,numericname,classteacher,note FROM manageclass')
        data=cur.fetchall()
        return render_template('UI/Admin/manageClass.html',addteacher=f,add_class=h,manageclass=data)
    
    
    
########################## Manage Section##################



@app.route('/UI/Admin/managesection',methods=['GET','POST'])
def managesection():
    if request.method=="POST":
         
        
        name=request.form['name']
        add_class=request.form['class']
        
        classteacher=request.form['classteacher']
        note=request.form['note']
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO managesection (name ,class,classteacher,note)VALUES(%s,%s,%s,%s)" ,[add_class,name,classteacher,note])
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,class,classteacher,note FROM managesection')
        data=cur.fetchall()
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT name FROM addteacher ORDER BY id")
        j=cur.fetchall()
        cur.execute("SELECT class FROM add_class ORDER BY id")
        k=cur.fetchall()
       
        mysql.connection.commit()
        msg="Successfully manageclass"
        return render_template('UI/Admin/manageSection.html',addteacher=j,add_class=k,managesection=data,msg=msg)
    
    else:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT name FROM addteacher ORDER BY id")
        j=cur.fetchall()
        cur.execute("SELECT class FROM add_class ORDER BY id")
        k=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,class,classteacher,note FROM managesection')
        data=cur.fetchall()
        return render_template('UI/Admin/manageSection.html',addteacher=j,add_class=k,managesection=data)
    
    
    
    
    
################addFeeClass   using dependent dropdown  ##############

@app.route('/UI/Master/feeclass',methods=['GET','POST'])
def addfeeclass():
    if request.method=="GET":
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cur.execute("SELECT * FROM addfeetitle ORDER BY feetitle_id")
        addfeetitle = cur.fetchall()
        
        cur.execute("SELECT class FROM add_class ")
        abc = cur.fetchall()
        cur=mysql.connection.cursor()

        cur.execute("SELECT * FROM addfeeclass ")
        a = cur.fetchall()
        return render_template("UI/Master/addFeeClass.html",addfeetitle=addfeetitle,add_class=abc,addfeeclass=a)
    else:
        feetitle=request.form['feetitle']
        category=request.form['category']
        add_class=request.form['class']
        feeamount=request.form['feeamount']
        cur=mysql.connection.cursor()
        
        cur.execute("INSERT INTO addfeeclass (feetitle,category,class,feeamount)VALUES(%s,%s,%s,%s)" ,[feetitle,category,add_class,feeamount])
        
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cur.execute("SELECT feetitle,category FROM category ")
        enroll = cur.fetchall()
        
        cur.execute("SELECT class FROM add_class ")
        abc = cur.fetchall()
        cur=mysql.connection.cursor()

        cur.execute("SELECT * FROM addfeeclass ")
        a = cur.fetchall()
        mysql.connection.commit()
        msg="Successfully addfee "
        return render_template("UI/Master/addFeeClass.html" ,msg=msg,category=enroll,add_class=abc,addfeeclass=a)
    
 #########  code of  dependent dropdown in addfeeclass####################

# @app.route("/addfeetitle",methods=["POST","GET"])
# def abc():  
#     cur = mysql.connection.cursor()
#     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     if request.method == 'POST':
#         category_id = request.form['category_id'] 
#         print(category_id) 
#         cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
#         cur.execute("SELECT * FROM category WHERE feetitle_id = %s ORDER BY category ASC", [category_id] )
#         category = cur.fetchall()  
#         OutputArray = []
#         for row in category:
#             outputObj = {
#                 'id': row['feetitle_id'],
#                 'name': row['category']}
#             OutputArray.append(outputObj)
#     return jsonify(OutputArray)

    


     
    
##################student report#####################


# @app.route('/studentreport',methods=['GET','POST'])
# def studentreport ():
#         cur=mysql.connection.cursor()
#         cur.execute('SELECT id,studentname,email,mobileno,gender,class,address FROM sregistration')
#         data=cur.fetchall()
#         return render_template('studentReport.html',sregistration=data)
    
    
    
    
##################Student Registration###############


# @app.route('/registration',methods=['GET','POST'])
# def studentregistration ():
#     if request.method == 'POST':
#         print("4")
#         studentname=request.form['studentname']
#         class1=request.form['class']
#         email=request.form['email']
#         mobileno=request.form['mobileno']
#         gender=request.form['gender']
#         dateofbirth=request.form['dateofbirth']
#         fileinput=request.form['fileinput']
#         fathername=request.form['fathername']
#         fqualification=request.form['fqualification']
#         fmobileno=request.form['fmobileno']
#         mothername=request.form['mothername']
#         mqualification=request.form['mqualification']
#         mmobileno=request.form['mmobileno']
#         address=request.form['address']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO sregistration (studentname,class,email,mobileno,gender,dateofbirth,fileinput,fathername,fqualification,fmobileno,mothername,mqualification,mmobileno,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[studentname,class1,email,mobileno,gender,dateofbirth,fileinput,fathername,fqualification,fmobileno,mothername,mqualification,mmobileno,address])
#         mysql.connection.commit()
#         msg="Successfully Registered"
#         return render_template("Dashboard.html" ,msg=msg)
#     else:
#         cur=mysql.connection.cursor()
#         cur.execute('SELECT * FROM sregistration')
#         data=cur.fetchall()
#         return render_template('sregistration.html',sregistration=data)
    
    
    
###############Stream###########################    


@app.route('/UI/Admin/stream',methods=['GET','POST'])
def stream():
    if request.method =='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM stream")
        abc=cur.fetchall()
        return render_template("UI/Admin/stream.html",stream=abc)
    else:
        
        stream=request.form['stream']
        cur = mysql.connection.cursor()
        
        cur.execute("INSERT INTO stream (stream) VALUES (%s)",[stream])
        cur.execute("SELECT * FROM stream")
        abc=cur.fetchall()
        mysql.connection.commit()
        print("test1")
        msg="successfully addstream"
        print("test")
        return render_template("UI/Admin/stream.html",msg=msg,stream=abc)



@app.route('/UI/Report/streamreport',methods=['GET','POST'])
def streamreport():
    if request.method =='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM stream")
        c=cur.fetchall()
        return render_template("UI/Report/streamreport.html",stream=c)
    else:
        id_data = request.form['id']
        
        
        stream=request.form['stream']
        
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE stream
               SET stream=%s
               WHERE id=%s
            """, ( stream, id_data))
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM stream")
        c=cur.fetchall()
        
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/streamreport.html",stream=c,msg=msg)
    
    
    

################Designation####################   



@app.route('/UI/Admin/designation',methods=['GET','POST'])
def designation():
    if request.method == 'POST':
        
        designation=request.form['designation']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO designation (designation) VALUES (%s)",[designation])
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM designation")
        abc=cur.fetchall()

        mysql.connection.commit()
        print("test1")
        msg="successfully adddesignation"
        print("test")
        return render_template("UI/Admin/designation.html" ,msg=msg,designation=abc)
    else:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM designation")
        abc=cur.fetchall()

        return render_template("UI/Admin/designation.html",designation=abc)
    
    
    
    
################### add Student details####################
@app.route('/UI/Accountant/studentdetails',methods=['GET','POST'])
def studentdetail():
    if request.method=="GET":
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT class FROM add_class")
        a=cur.fetchall()
        cur.execute("SELECT add_section FROM new_section")
        b=cur.fetchall()
        cur.execute("SELECT add_session FROM add_session")
        f=cur.fetchall()
        cur.execute("SELECT stream FROM stream")
        e=cur.fetchall()
        
        return render_template("UI/Accountant/addStudentDetail.html",add_class=a,new_section=b,stream=e,add_session=f)
    else:    
    
    
        cur = mysql.connection.cursor()
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        now = datetime.now()
        if request.method == 'POST':
            name=request.form['name']
            fathername=request.form['fathername']
            mothername=request.form['mothername']
            addmission=request.form['addmission']
            admissiondate=request.form['admissiondate']
            birthdate=request.form['birthdate']
            gender=request.form['gender']
            aadharno=request.form['aadharno']
            religion=request.form['religion']
            caste=request.form['caste']
            housename=request.form['housename']
            phone=request.form['phone']
            email=request.form['email']
            add_class=request.form['class']
            add_section=request.form['add_section']
            stream=request.form['stream']
            rollno=request.form['rollno']
            feeexcused=request.form['feeexcused']
            add_session=request.form['add_session']
            presentaddress=request.form['presentaddress']
            permanentaddress=request.form['permanentaddress']
            username=request.form['username']
            password=request.form['password']
            files1 = request.files.getlist('files1[]')
            print("files")
            for file in files1:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                    print('upload_image filename:' + filename)
                    cur.execute("INSERT INTO studentreport (add_session,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file_name,uploaded_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[add_session,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,add_class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,filename,now])
                    mysql.connection.commit()
                print(file)
           
            flash('File(s) successfully uploaded')
             
        return render_template('UI/Accountant/addStudentDetail.html')

# @app.route('/display/<filename>')
# def display_image(filename):
#     #print('display_image filename: ' + filename)
#     return redirect(url_for('static', filename='uploads/' + filename), code=301)
 







# @app.route('/UI/student/studentdetails',methods=['GET','POST'])
# def studentdetail():
#     if request.method == 'POST':
        
        
#         name=request.form['name']
#         fathername=request.form['fathername']
#         mothername=request.form['mothername']
#         addmission=request.form['addmission']
#         admissiondate=request.form['admissiondate']
#         birthdate=request.form['birthdate']
#         gender=request.form['gender']
#         aadharno=request.form['aadharno']
#         religion=request.form['religion']
#         caste=request.form['caste']
#         housename=request.form['housename']
#         phone=request.form['phone']
#         email=request.form['email']
#         add_class=request.form['class']
#         add_section=request.form['add_section']
#         stream=request.form['stream']
#         rollno=request.form['rollno']
#         feeexcused=request.form['feeexcused']
#         add_session=request.form['add_session']
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         username=request.form['username']
#         password=request.form['password']
#         file=request.form['file']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO studentreport (add_session,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[add_session,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,add_class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file])
#         mysql.connection.commit()
#         print("test1")
#         msg="successfully addstudentdetail"
#         print("test")
#         return render_template("Dashboard.html" ,msg=msg)
    
    # else:
        # cur = mysql.connection.cursor()
        # cur.execute("SELECT class FROM add_class")
        # a=cur.fetchall()
        # cur.execute("SELECT add_section FROM new_section")
        # b=cur.fetchall()
        # cur.execute("SELECT add_session FROM add_session")
        # f=cur.fetchall()
        # cur.execute("SELECT stream FROM stream")
        # e=cur.fetchall()
        
        # return render_template("UI/student/addStudentDetail.html",add_class=a,new_section=b,stream=e,add_session=f)
    
    
    
    
    
##################AddStudentRegistrationReport#########################




@app.route('/studentregistrationreport',methods=['GET','POST'])
def check ():
    
        cur=mysql.connection.cursor()
        cur.execute("SELECT id, name  FROM student_registration" )
        data=cur.fetchall
        return render_template('studentRegistrationReport.html',student_registration=data)
    
    
    
#########################fetching Report#################
    
# @app.route('/studentdetails',methods=['GET','POST'])
# def studentreport ():  
     
#     if request.method=='POST':
#         studentreport=request.form
#         name=studentreport['name']
#         cur=mysql.connection.cursor()
#         cur.execute("SELECT  id,schoolname, name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,photo FROM addstudentdetail where name='"+name+"'")
#         r=cur.fetchone()
#         mysql.connction.commit()
#         return render_template("addStudentDetail.html",r=r)
    
    
###########################addnonfacultyreport#############################


@app.route('/UI/Report/nonfacultyreport',methods=['GET','POST'])
def nonfacultyreport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor,file_name FROM nonfaculty')
        data=cur.fetchall()
        return render_template('UI/Report/nonfacultyreport.html',nonfaculty=data)
    else:
        id_data = request.form['id']
        
        name=request.form['name']
        nationalid=request.form['nationalid']
        phone=request.form['phone']
        gender=request.form['gender']
        birthdate=request.form['birthdate']
        joiningdate=request.form['joiningdate']
        fathername=request.form['fathername']
        aadharno=request.form['aadharno']
        presentaddress=request.form['presentaddress']
        permanentaddress=request.form['permanentaddress']
        qualification=request.form['qualification']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        designation=request.form['designation']
        applyfor=request.form['applyfor']
        # yearofexperience=request.form['yearofexperience']
        # add_class=request.form['class']
        # subject=request.form['subject']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE nonfaculty
               SET name=%s,nationalid=%s,phone=%s,gender=%s,birthdate=%s,joiningdate=%s,fathername=%s,aadharno=%s,presentaddress=%s,permanentaddress=%s,qualification=%s,email=%s,username=%s,password=%s,designation=%s,applyfor=%s
               WHERE id=%s
            """, (name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor,id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,applyfor,file_name FROM nonfaculty')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template('UI/Report/nonfacultyreport.html',nonfaculty=data,msg=msg)
    

        

    
    
    
    
    

    
    
    
    
################### Admin login#########################

# @app.route('/login',methods=['GET','GET'])
# def adminlogin():
    
#     msg = ''
#     if request.method == 'POST': 
#         username = request.form['username']
#         password = request.form['password']
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT * FROM loginmaster WHERE username = % s AND password = % s', (username, password, ))
#         loginmaster = cur.fetchone()
#         if loginmaster:
#             session['loggedin'] = True
#             session['id'] = loginmaster['id']
#             session['username'] = loginmaster['username']
#             msg = 'Logged in successfully !'
#             return render_template('Dashboard.html', msg = msg)
#         else:
#             msg = 'Incorrect username / password !'
#     return render_template('login.html', msg = msg)






    
    
    
    
    
######################Student Login#########################


# @app.route('/studentlogin',methods=['GET','POST'])
# def studentlogin():
#     if request.method == 'GET':
#         print("3")
#         print("Its in get")
#         return render_template("studentlogin.html")
    
        
#     else:
#         print("4")
#         #studentDetails=request.form
#         email=request.form['email']
#         password=request.form['password']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO studentlogin (email,password) VALUES (%s,%s)",(email,password))
#         mysql.connection.commit()
#         # msg="successfully student login"
        
        
#         return render_template("addStudentDetail.html" )
    
    
    
    
########################Teacher Login#################



# @app.route('/teacherlogin',methods=['GET','POST'])
# def teacherlogin():
#     if request.method == 'GET':
#         print("3")
#         print("Its in get")
#         return render_template("teacherlogin.html")
    
        
#     else:
#         print("4")
#         #studentDetails=request.form
#         email=request.form['email']
#         password=request.form['password']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO teacherlogin (email,password) VALUES (%s,%s)",(email,password))
#         mysql.connection.commit()
#         # msg="successfully student login"
        
        
#         return render_template("Add Teacher.html" )
    
    
    
    
    
    
#######################NonFaculty login############



# @app.route('/nonfacultylogin' ,methods=['GET','POST'])
# def nonfacultylogin ():
#     if request.method == 'GET':
#         print("3")
#         print("Its in get")
#         return render_template("nonFacultyLogin.html")
    
        
#     else:
#         print("4")
#         #studentDetails=request.form
#         email=request.form['email']
#         password=request.form['password']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO nonfacultylogin (email,password) VALUES (%s,%s)",(email,password))
#         mysql.connection.commit()
#         # msg="successfully nonfacultylogin"
        
        
#         return render_template("Add NonFaculty.html" )
    
    
    
    



    
    
    
    
    
    
    


########################signupupdate#############################
    
@app.route('/signupupdate',methods=['GET','POST'])
def signupupdate():
    if request.method == 'GET':
        print("5")
        print("Its in get")
        return render_template("signup.html")
    else:
        print("6")
        id_data=request.form[id]
        
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        password=request.form['password']
        address=request.form['address']
        
        cur=mysql.connection.cursor()
        cur.execute("""UPDATE signupupdate SET name=%s,email=%s,mobile=%s,password=%s,address=%s WHERE id=%s""",(name,email,mobile,password,address,id_data))
        msg="successfully updated"
        mysql.connection.commit()
        
        
        return render_template('signupupdated.html',msg=msg)
    
    
######################signup##################
    
@app.route('/signup',methods=['GET','POST'])
def signup(): 
    if request.method == 'GET':
        print("5")
        print("Its in get")
        return render_template("signup.html")
    else:
        print("6")
        name=request.form['name']
        email=request.form['email']
        mobile=request.form['mobile']
        password=request.form['password']
        address=request.form['address']
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO signup (name,email,mobile,password,address) VALUES(%s,%s,%s,%s,%s)",(name,email,mobile,password,address))
        mysql.connection.commit()
        msg="successfully signup"
        
        return render_template('signup.html',msg=msg)
    
    

























# @app.route('/', methods =['GET', 'POST'])
# def test():
#     return render_template("index.html")


# @app.route('/loginMaster', methods = ['GET', 'POST'])
# def loginMaster():
#     print("page open")
#     return render_template('loginMaster.html')

  
  ##################admin login#############

@app.route('/UI/Admin/login', methods =['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM loginmaster WHERE username = % s AND password = % s', (username, password, ))
        loginmaster = cursor.fetchone()
        if loginmaster:
            session['loggedin'] = True
            session['id'] = loginmaster['id']
            session['username'] = loginmaster['username']
            msg = 'Logged in successfully !'
            return render_template('Dashboard.html', msg = msg)
        else:
            msg = 'Wrong Credential !'
            return render_template('UI/Admin/login.html', msg = msg)
    else:
        return render_template("UI/Admin/login.html")
    
################  nonfacuty login #############

    
@app.route('/UI/Login/nonfacultylogin',methods=['GET','POST'])
def nonfaculty():
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM nonfaculty WHERE username = % s AND password = % s', (username, password, ))
        nonfaclog = cursor.fetchone()
        if nonfaclog:
            session['loggedin'] = True
            session['id'] = nonfaclog['id']
            session['username'] = nonfaclog['username']
            msg = 'Logged in successfully !'
            return render_template('UI/NonFaculty/NonfacultyDashboard.html', msg = msg)
        else:
            msg = 'Wrong Credential !'
            return render_template('UI/Login/nonfacultylogin.html', msg = msg)
    else:
        return render_template("/UI/Login/nonfacultylogin.html")
    
################## faculty login################    
    
@app.route('/UI/Login/teacherlogin',methods=['GET','POST'])
def teacherlogin():
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM addteacher WHERE username = % s AND password = % s', (username, password, ))
        teacherlogin = cursor.fetchone()
        if teacherlogin:
            session['loggedin'] = True
            session['id'] = teacherlogin['id']
            session['username'] = teacherlogin['username']
            
            
            msg = 'Logged in successfully !'
            return render_template('UI/Faculty/FacultyDashboard.html', msg = msg)
        else:
            msg = 'Wrong Credential !'
            return render_template('UI/Login/teacherlogin.html', msg = msg)
    else:
        return render_template("UI/Login/teacherlogin.html")
    
####################student login#################### 
 
 
    
@app.route('/UI/Login/studentlogin',methods=['GET','POST'])
def studentlogin():
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM studentreport WHERE username = % s AND password = % s', (username, password, ))
        signup = cursor.fetchone()
        if signup:
            session['loggedin'] = True
            session['id'] = signup['id']
            session['username'] = signup['username']
            session['class']=signup['class']
            
            msg = 'Logged in successfully !'
            return render_template('UI/student/StudentDashboard.html', msg = msg)
        else:
            msg = 'Wrong Credential !'
            return render_template('UI/Login/studentlogin.html', msg = msg)
    else:
        return render_template("UI/Login/studentlogin.html")
    
    




    
    
    
 #############student registration report###############   
    
# @app.route('/studentregistrationreport',methods=['GET','POST'])
# def studentregistrationreport ():
    
#         cur=mysql.connection.cursor()
#         cur.execute("SELECT  id, name FROM addstudentdetail")
#         data=cur.fetchall()
#         return render_template('studentRegistrationReport.html',addstudentdetail=data)
    
    
####################UPDATE STUDeNT REGISTRATION REPORT####################



@app.route('/updateregistration',methods=['GET','POST'])
def updatestudentregistrationreport():
    
    if request.method == 'POST':
        id_data = request.form['id']
        
        rollno=request.form['rollno']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addstudentdetail
               SET rollno=%s
               WHERE id=1
            """, (  id_data,rollno))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    
###########################Delete Ustudent registration####################    
    
@app.route('/deletestudentregistrationreport/<string:id_data>', methods = ['GET'])
def deletestudentregistrationreport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM studentreport WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        # cur.execute('SELECT id,add_session,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file_name, FROM studentreport')
        # data=cur.fetchall()
        cur.execute('SELECT * FROM studentreport')
        data=cur.fetchall()
        
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template('UI/Report/studentgridview.html',studentreport=data,msg=msg)






#############################   add subject#######################




@app.route('/UI/Master/addsubject',methods=['GET','POST'])
def addsubject():
    if request.method=="POST":
         
        
        add_class=request.form['class']
        subject=request.form['subject']
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO addsubject (class,subject)VALUES(%s,%s)" ,[add_class,subject])
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        cur.execute("SELECT class FROM add_class ORDER BY id")
        h=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,class,subject FROM addsubject")
        i=cur.fetchall()
        mysql.connection.commit()
        msg="Successfully addsubject"
        return render_template("UI/Master/addsubject.html" ,msg=msg,add_class=h,addsubject=i)
    else:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        cur.execute("SELECT class FROM add_class ORDER BY id")
        h=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,class,subject FROM addsubject")
        i=cur.fetchall()
        return render_template('UI/Master/addsubject.html',add_class=h,addsubject=i)
    
    
##############################addsyllabus#########################
    
    
@app.route('/UI/Master/addsyllabus',methods=['GET','POST'])
def addsyllabus():
    if request.method=="POST":
         
        
        topic=request.form['topic']
        subject=request.form['subject']
        complete=request.form["complete"]
        add_class=request.form["class"]
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO addsyllabus (topic,subject,complete,class)VALUES(%s,%s,%s,%s)" ,[topic,subject,complete,add_class])
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        
        cur.execute("SELECT class FROM add_class")
        o=cur.fetchall()
        cur.execute("SELECT subject FROM addsubject")
        i=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,class,subject,topic,complete FROM addsyllabus")
        abc=cur.fetchall()
        mysql.connection.commit()
        msg="Successfully addsyllabus"
        return render_template("UI/Master/addsyllabus.html" ,msg=msg,addsyllabus=abc,addsubject=i,add_class=o)
    else:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        
        cur.execute("SELECT class FROM add_class")
        o=cur.fetchall()
        cur.execute("SELECT subject FROM addsubject")
        i=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,class,subject,topic,complete FROM addsyllabus")
        abc=cur.fetchall()
        return render_template('UI/Master/addsyllabus.html',addsyllabus=abc,addsubject=i,add_class=o)
    
    
##########################classlecture############################
    
    
@app.route('/UI/Admin/classlecture',methods=['GET','POST'])
def classlecture():
    if request.method=="POST":
         
        
        topic=request.form['topic']
        subject=request.form['subject']
        name=request.form["name"]
        description=request.form['description']
        date=request.form['date']
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO classlecture (topic,subject,name,description,date)VALUES(%s,%s,%s,%s,%s)" ,[topic,subject,name,description,date])
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM classlecture')
        data=cur.fetchall()
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        
        cur.execute("SELECT subject FROM addsubject")
        h=cur.fetchall()
        cur.execute("SELECT topic FROM addsyllabus")
        i=cur.fetchall()
        cur.execute("SELECT name FROM addteacher")
        k=cur.fetchall()
        
    
        mysql.connection.commit()
        msg="Successfully addclasslecture"
        return render_template('UI/Admin/classlecture.html',addsyllabus=i,addsubject=h,addteacher=k,classlecture=data,msg=msg)
    
    
    else:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        
        cur.execute("SELECT subject FROM addsubject")
        h=cur.fetchall()
        cur.execute("SELECT topic FROM addsyllabus")
        i=cur.fetchall()
        cur.execute("SELECT name FROM addteacher")
        k=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM classlecture')
        data=cur.fetchall()
        return render_template('UI/Admin/classlecture.html',addsyllabus=i,addsubject=h,addteacher=k,classlecture=data)
    
    
    
##########################adsyllabusreport###############


@app.route('/UI/Report/addsyllabusreport',methods=['GET','POST'])
def addsyllabusreport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addsyllabus')
        data=cur.fetchall()
        return render_template('UI/Report/addsyllabusreport.html',addsyllabus=data)
    else:
       
        id_data = request.form['id']
        
        topic=request.form['topic']
        subject=request.form['subject']
        complete=request.form["complete"]
        add_class=request.form["class"]
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addsyllabus
               SET topic=%s,subject=%s,complete=%s,class=%s
               WHERE id=%s
            """, (topic,subject,complete,add_class, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addsyllabus')
        data=cur.fetchall()
        
        mysql.connection.commit()
        msg="successfully updated"
        return render_template('UI/Report/addsyllabusreport.html',addsyllabus=data,msg=msg)
    
 ###########################addsubjectreport#################
 
    
@app.route('/UI/Report/addsubjectsreport',methods=['GET','POST'])
def addsubjectsreport ():
    if request.method=='GET':

        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addsubject')
        data=cur.fetchall()
        return render_template('UI/Report/addsubjectreport.html',addsubject=data)
    else:
        id_data = request.form['id']
        
        add_class=request.form['class']
        subject=request.form['subject']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addsubject
               SET subject=%s,class=%s
               WHERE id=%s
            """, ( subject,add_class, id_data))
        cur.execute("SELECT * FROM addsubject")
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/addsubjectreport.html" ,msg=msg,addsubject=data)
    
    
    
    
#################classlecturereport#############################
    
@app.route('/UI/Report/classlecturereport',methods=['GET','POST'])
def classlecturereport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM classlecture')
        data=cur.fetchall()
        return render_template('UI/Report/classlecturereport.html',classlecture=data)
    else:
        id_data = request.form['id']
        
        topic=request.form['topic']
        subject=request.form['subject']
        name=request.form["name"]
        description=request.form['description']
        date=request.form['date']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE classlecture
               SET topic=%s,subject=%s,name=%s,description=%s,date=%s
               WHERE id=%s
            """, ( topic,subject,name,description,date, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM classlecture')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template('UI/Report/classlecturereport.html',classlecture=data,msg=msg)
    
    
    
    
    
    
############################Update Classlecture Report########################



# @app.route('/updateclasslecturereport',methods=['GET','POST'])
# def updateclasslecturereport():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
        
#         topic=request.form['topic']
#         subject=request.form['subject']
#         name=request.form["name"]
#         description=request.form['description']
#         date=request.form['date']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE classlecture
#                SET topic=%s,subject=%s,name=%s,description=%s,date=%s
#                WHERE id=%s
#             """, ( topic,subject,name,description,date, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
    
    
@app.route('/deleteclasslecturereport/<string:id_data>', methods = ['GET'])
def deleteclasslecturereport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM classlecture WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM classlecture')
        data=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/classlecturereport.html",msg=msg,classlecture=data)

    
    
    
############Update Subject Report###################
    
    
    
# @app.route('/updatesubjectreport',methods=['GET','POST'])
# def updatesubjectreport():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
        
#         add_class=request.form['class']
#         subject=request.form['subject']
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addsubject
#                SET subject=%s,class=%s
#                WHERE id=%s
#             """, ( subject,add_class, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
@app.route('/deletesubjectreport/<string:id_data>', methods = ['GET'])
def deletesubjectreport(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM addsubject WHERE id=%s", (id_data,))
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM addsubject")
    data=cur.fetchall()
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("UI/Report/addsubjectreport.html" , msg=msg,addsubject=data)





#####################update Syllabus#####################



# @app.route('/updatesyllabusreport',methods=['GET','POST'])
# def updatesyllabusreport():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
        
#         topic=request.form['topic']
#         subject=request.form['subject']
#         complete=request.form["complete"]
#         add_class=request.form["class"]
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addsyllabus
#                SET subject=%s,class=%s,complete=%s,topic=%s
#                WHERE id=%s
#             """, ( subject,add_class,topic,complete, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
@app.route('/deletesyllabusreport/<string:id_data>', methods = ['GET'])
def deletesyllabusreport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addsyllabus WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addsyllabus')
        data=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/addsyllabusreport.html" ,msg=msg,addsyllabus=data)



##################Update Stream##################

# @app.route('/updatestream',methods=['GET','POST'])
# def updatestream():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
        
        
#         stream=request.form['stream']
        
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE stream
#                SET stream=%s
#                WHERE id=%s
#             """, ( stream, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
@app.route('/deletestream/<string:id_data>', methods = ['GET'])
def deletestream(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM stream WHERE id=%s", (id_data,))
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM stream")
    c=cur.fetchall()
       
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM stream")
    c=cur.fetchall()
    return render_template("UI/Report/streamreport.html",stream=c,msg=msg)



# @app.route('/classlecturereport',methods=['GET','POST'])
# def classlecturereport ():
#         cur=mysql.connection.cursor()
#         cur.execute('SELECT * FROM classlecture')
#         data=cur.fetchall()
#         return render_template('classlecturereport.html',classlecture=data)




###################Add Hostel Fee###################################
    
    
    
    
    

    
    
    
 ############ time insert ##############   
    
@app.route('/UI/Admin/time',methods=['GET','POST'])
def time():
    if request.method=="POST":
        time=request.form['time']
        time1=request.form['time1']

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM time")
        abc=cur.fetchall()

        cur.execute("INSERT INTO time (time,time1)VALUES(%s,%s)" ,[time,time1])

        mysql.connection.commit()
        msg="Successfully addedtime"
        return render_template("UI/Admin/time.html",msg=msg,time=abc)
    else:
       
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM time")
        abc=cur.fetchall()
        return render_template("UI/Admin/time.html",time=abc)

#################  Routine Test##################### 
# @app.route('/UI/Admin/routinetest',methods=['GET','POST'])
# def routine():
#     if request.method == 'POST': 
#         name=request.form['name']
#         # add_section=request.form["add_section"]
       
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT nationalid FROM addteacher WHERE name = % s', [name])
#         abc = cursor.fetchall()
#         if abc:
#             add_class=request.form['class']
#             subject=request.form['subject']
#             add_section=request.form['add_section']
        
#             name=request.form['name']
#             nationalid=request.form['nationalid']
        
#             time=request.form['time']
#             time1=request.form['time1']
#             periodname=request.form['periodname']
#             day=request.form['day']
        
#             cur = mysql.connection.cursor()
#             cur.execute("INSERT INTO routine (class,subject,add_section,name,nationalid,time,time1,periodname,day)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,[add_class,subject,add_section,name,nationalid,time,time1,periodname,day])
#             mysql.connection.commit()
#             msg="Successfully addroutine "
#         return render_template("Dashboard.html" ,msg=msg)
#     else:
#         cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute("SELECT class FROM add_class ")
#         h=cur.fetchall()
#         cur.execute("SELECT subject FROM addsubject")
#         i=cur.fetchall()
#         cur.execute("SELECT add_section FROM new_section")
#         o=cur.fetchall()
#         cur.execute('SELECT name FROM addteacher ' )
#         l=cur.fetchall()
#         # cur.execute("SELECT nationalid FROM addteacher ")
#         # abc=cur.fetchall()

#         cur.execute("SELECT time FROM time ")
#         m=cur.fetchall()
#         cur.execute("SELECT time1 FROM time ")
#         n=cur.fetchall()
#         return render_template('UI/Admin/Routine1.html',add_class=h,addsubject=i,addteacher=l,time=m,time1=n,new_section=o)
    
        
        
        
        
        

          
    
@app.route('/UI/Admin/routinetest',methods=['GET','POST'])
def routine():
    if request.method=='GET':
        
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT class FROM add_class")
        h=cur.fetchall()
        cur.execute("SELECT subject FROM addsubject")
        i=cur.fetchall()
        cur.execute("SELECT add_section FROM new_section")
        o=cur.fetchall()
        
        cur.execute("SELECT name FROM addteacher ORDER BY id")
        addteacher = cur.fetchall()
    
 
        

        cur.execute("SELECT time FROM time ")
        m=cur.fetchall()
        cur.execute("SELECT time1 FROM time ")
        n=cur.fetchall()
        return render_template('UI/Admin/Routine1.html',add_class=h,addsubject=i,addteacher=addteacher,time=m,time1=n,new_section=o)
    else:
        add_class=request.form['class']
        subject=request.form['subject']
        add_section=request.form['add_section']
        name=request.form['name']
        nationalid=request.form['nationalid']
        time=request.form['time']
        time1=request.form['time1']
        periodname=request.form['periodname']
        day=request.form['day']
        

        cur.execute("INSERT INTO routine (class,subject,add_section,name,nationalid,time,time1,periodname,day)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" ,[add_class,subject,add_section,name,nationalid,time,time1,periodname,day])
        mysql.connection.commit()
        msg="Successfully addroutine "
        return render_template('UI/Admin/Routine1.html'"Dashboard.html" ,msg=msg)

    


@app.route("/addteacher",methods=["POST","GET"])
def addteacher1():  
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        category_id = request.form['category_id'] 
        print(category_id)  
        cur.execute("SELECT * FROM nationalid WHERE id = %s ORDER BY nationalid ASC", [category_id] )
        nationalid = cur.fetchall()  
        OutputArray = []
        for row in nationalid:
            outputObj = {
                'id': row['id'],
                'name': row['nationalid']}
            OutputArray.append(outputObj)
    return jsonify(OutputArray)




    
            
            
       
    



#################    Time Report##########################      
  
@app.route('/UI/Report/timereport',methods=['GET','POST'])
def timereport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM time')
        data=cur.fetchall()
        return render_template('UI/Report/timereport.html',time=data)
    else:
        id_data = request.form['id']
        time=request.form['time']
        time1=request.form['time1']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE time
               SET time=%s,time1=%s
               WHERE id=%s
            """, ( time,time1, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM time')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/timereport.html",msg=msg,time=data)
    
    
    
    
    
# @app.route('/updatetimereport',methods=['GET','POST'])
# def updatetimereport():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
        
        
#         time=request.form['time']
#         time1=request.form['time1']
        
        
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE time
#                SET time=%s,time1=%s
#                WHERE id=%s
#             """, ( time,time1, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
@app.route('/deletetimereport/<string:id_data>', methods = ['GET'])
def deletetimereport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM time WHERE id=%s", (id_data,))
        cur.execute("SELECT * FROM time")
        data=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/timereport.html" ,msg=msg,time=data)








    
    



    
###########################Add Hostel##############################



@app.route('/UI/Master/addhostel',methods=['GET','POST'])
def addhostel():
    if request.method == 'POST':
        roomno=request.form['roomno']
        noofseat=request.form['noofseat']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO addhostel (roomno,noofseat) VALUES (%s,%s)",[roomno,noofseat])
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addhostel")
        abc=cur.fetchall()
     
        mysql.connection.commit()
        msg="successfully addhostel"
        return render_template("UI/Master/addhostel.html" ,msg=msg,addhostel=abc)
    else:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addhostel")
        abc=cur.fetchall()
     
        return render_template("UI/Master/addhostel.html" ,addhostel=abc)
    
    
    
    
    
@app.route('/UI/Admin/addhostelfee',methods=['GET','POST'])
def addhostelfee():
    if request.method == 'POST':
        roomno=request.form['roomno']
        perbedcharge=request.form['perbedcharge']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO addhostelfee (roomno,perbedcharge) VALUES (%s,%s)",[roomno,perbedcharge])
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT roomno FROM addhostel")
        data=cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("SELECT id,roomno,perbedcharge FROM addhostelfee")
        a=cur.fetchall()
        mysql.connection.commit()
        msg="successfully addhostelfee"
        return render_template("UI/Admin/addhostelfee.html",msg=msg ,addhostel=data,addhostelfee=a)

    
    else:
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT roomno FROM addhostel")
        data=cur.fetchall()
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, roomno,perbedcharge FROM addhostelfee")
        a=cur.fetchall()
        
     
        
        
        return render_template("UI/Admin/addhostelfee.html" ,addhostel=data,addhostelfee=a)

    
    
    
###################Teacher Subject Report#########################
    
@app.route('/UI/Report/teachersubjectreport',methods=['GET','POST'])
def teachersubjectreport ():
    if request.method=='GET':

            cur=mysql.connection.cursor()
            cur.execute('SELECT id, name,subject,nationalid,phone,gender FROM teachersub')
            data=cur.fetchall()
            return render_template('UI/Report/teachersubjectreport.html',teachersub=data)
    else:
            id_data = request.form['id']
            name=request.form['name']
            subject=request.form['subject']
            empid=request.form['nationalid']
            phone=request.form['phone']
            gender=request.form['gender']
            cur = mysql.connection.cursor()
            cur.execute("""
               UPDATE teachersub
               SET name=%s,subject=%s,nationalid=%s,phone=%s,gender=%s
               WHERE id=%s
            """, ( name,subject,empid,phone,gender, id_data))
            cur=mysql.connection.cursor()
            cur.execute('SELECT id, name,subject,nationalid,phone,gender FROM teachersub')
            data=cur.fetchall()
            mysql.connection.commit()
            msg="successfully updated"
            return render_template('UI/Report/teachersubjectreport.html',teachersub=data,msg=msg)
    
    
       
    
    
    
    
# @app.route('/updateteachersubjectreport',methods=['GET','POST'])
# def updateteachersubject():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
        
        
#         name=request.form['name']
#         subject=request.form['subject']
#         empid=request.form['nationalid']
#         phone=request.form['phone']
#         gender=request.form['gender']
        
        
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE teachersub
#                SET name=%s,subject=%s,nationalid=%s,phone=%s,gender=%s
#                WHERE id=%s
#             """, ( name,subject,empid,phone,gender, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
    
@app.route('/deleteteachersubjectreport/<string:id_data>', methods = ['GET'])
def deleteteachersubjectreport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM teachersub WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, name,subject,nationalid,phone,gender FROM teachersub')
        data=cur.fetchall()
        
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template('UI/Report/teachersubjectreport.html',teachersub=data,msg=msg)

    
  ##################hostel report######################  
    
@app.route('/UI/Report/addhostelreport',methods=['GET','POST'])
def addhostelreport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, roomno,noofseat FROM addhostel')
        data=cur.fetchall()
        return render_template('UI/Report/addhostelreport.html',addhostel=data)
    else:
        id_data = request.form['id']
        roomno=request.form['roomno']
        noofseat=request.form['noofseat']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addhostel
               SET roomno=%s,noofseat=%s
               WHERE id=%s
            """, ( roomno,noofseat, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, roomno,noofseat FROM addhostel')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/addhostelreport.html" ,msg=msg,addhostel=data)
    
    
    
    
# @app.route('/updateaddhostelreport',methods=['GET','POST'])
# def updateaddhostelreport():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
#         roomno=request.form['roomno']
#         noofseat=request.form['noofseat']
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addhostel
#                SET roomno=%s,noofseat=%s
#                WHERE id=%s
#             """, ( roomno,noofseat, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
    
@app.route('/deleteaddhostelreport/<string:id_data>', methods = ['GET'])
def deleteaddhostelreport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addhostel WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, roomno,noofseat FROM addhostel')
        data=cur.fetchall()
       
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template('UI/Report/addhostelreport.html',addhostel=data,msg=msg)




##################hostel Fee report######################  
    
@app.route('/UI/Report/addhostelfeereport',methods=['GET','POST'])
def addhostelfeereport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, roomno,perbedcharge FROM addhostelfee')
        data=cur.fetchall()
        return render_template('UI/Report/addhostelfeereport.html',addhostelfee=data)
    else:
        id_data = request.form['id']
        roomno=request.form['roomno']
        perbedcharge=request.form['perbedcharge']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addhostelfee
               SET roomno=%s,perbedcharge=%s
               WHERE id=%s
            """, ( roomno,perbedcharge, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, roomno,perbedcharge FROM addhostelfee')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        
        
        return render_template('UI/Report/addhostelfeereport.html',addhostelfee=data,msg=msg)
    
    

    
    
    
# @app.route('/updateaddhostelfeereport',methods=['GET','POST'])
# def updateaddhostelfeereport():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
#         roomno=request.form['roomno']
#         perbedcharge=request.form['perbedcharge']
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addhostelfee
#                SET roomno=%s,perbedcharge=%s
#                WHERE id=%s
#             """, ( roomno,perbedcharge, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
    
@app.route('/deleteaddhostelfeereport/<string:id_data>', methods = ['GET'])
def deleteaddhostelfeereport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addhostelfee WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, roomno,perbedcharge FROM addhostelfee')
        data=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template('UI/Report/addhostelfeereport.html',addhostelfee=data,msg=msg)




@app.route('/UI/Admin/teachersubject',methods=['GET','POST'])
def teachersubject():
    if request.method=="POST":
        name=request.form["name"]
        subject=request.form["subject"]
        nationalid=request.form["nationalid"]
        phone=request.form["phone"]
        gender=request.form["gender"]
       
        cur=mysql.connection.cursor()
        
        cur.execute("INSERT INTO teachersub (name,subject,nationalid,phone,gender)VALUES(%s,%s,%s,%s,%s)" ,[name,subject,nationalid,phone,gender])
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT name,nationalid,phone,gender FROM addteacher")
        k=cur.fetchall()
        cur.execute("SELECT subject FROM addsubject")
        h=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, name,subject,nationalid,phone,gender FROM teachersub')
        data=cur.fetchall()
        
        mysql.connection.commit()
        msg="Successfully addteachersubject"
        return render_template('UI/Admin/teachersubject.html' ,msg=msg,addteacher=k,addsubject=h,teachersub=data)
    else:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT name,nationalid,phone,gender FROM addteacher")
        k=cur.fetchall()
        cur.execute("SELECT subject FROM addsubject")
        h=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute('SELECT id, name,subject,nationalid,phone,gender FROM teachersub')
        data=cur.fetchall()
        
        return render_template('UI/Admin/teachersubject.html',addteacher=k,addsubject=h,teachersub=data)






############ routine report####################



@app.route('/UI/Report/routinereport',methods=['GET','POST'])
def routinereport ():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM routine ')
        data=cur.fetchall()
        return render_template('UI/Report/routinereport.html',routine=data)
    else:
        id_data = request.form['id']
        
        
        add_class=request.form['class']
        subject=request.form['subject']
        add_section=request.form['add_section']
        name=request.form['name']
        time=request.form['time']
        time1=request.form['time1']
        periodname=request.form['periodname']
        nationalid=request.form['nationalid']
        day=request.form['day']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE routine
               SET class=%s,subject=%s,add_section=%s,name=%s,time=%s,time1=%s,periodname=%s,nationalid=%s,day=%s
               WHERE id=%s
            """, (add_class,subject,add_section,name,time,time1,periodname,nationalid,day, id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM routine ')
        data=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        
        return render_template('UI/Report/routinereport.html',routine=data,msg=msg)
    
    
    
    
@app.route('/deleteroutinereport/<string:id_data>', methods = ['GET'])
def deleteroutinereport(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM routine WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM routine ')
        data=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/routinereport.html" , msg=msg,routine=data)





# @app.route('/UI/Admin/attendence', methods=['GET', 'POST'])
# def attendence():
#     if request.method == 'POST':
#         if 'email' in request.form and 'password' in request.form:
#             email = request.form['email']
#             password = request.form['password']
#             cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#             cur.execute("SELECT * FROM addteacher WHERE email=%s AND password =%s", (email,password))
#             info = cur.fetchone()
#             print(info)
#             if info is not None:
#                 if info['email'] == email and info['password'] == password:
#                     session['loginsuccess'] = True
#                     return redirect(url_for('UI/Admin/attendence'))
#             else:
#                return redirect(url_for('UI/Login/teacherlogin'))

#     return render_template("Dashboard.html")





############FacultyDashboard##################


@app.route('/UI/Faculty/FacultyDashboard', methods = ['GET', 'POST'])
def FacultyDashboard():
    if request.method=='POST':
        username=request.method['username']
        cursor=mysql.connection.cursor()
        cursor.execute("select * From addteacher where username=%s",(username))
        if session.loggedin:
            return render_template("UI/Faculty/FacultyDashboard.html",username=username)
    return render_template('UI/Faculty/FacultyDashboard.html')





#############FacultyLogout#############



@app.route('/UI/Faculty/Facultylogout')
def Facultylogout():
    session.pop('username')
    
    return render_template('UI/Login/teacherlogin.html')

############Change Password############




@app.route('/UI/Faculty/changepassword',methods=['GET','POST'])
def changepassword():
    if request.method == 'POST': 
        OldPassword = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM addteacher WHERE password = % s ', (OldPassword, ))
        abc = cursor.fetchone()
        if abc:
            id_data = request.form['id']
            OldPassword=request.form['password']
            newPassword=request.form['newpassword']
            
            cur = mysql.connection.cursor()
            cur.execute("""
               UPDATE addteacher
               SET password=%s
               WHERE id=%s
            """, (newPassword, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Faculty/FacultyDashboard.html" ,msg=msg)

    msg="Not Change"
    return render_template("UI/Faculty/changepassword.html" )
    










##############Student dashboard############
@app.route('/UI/student/StudentDashboard', methods = ['GET', 'POST'])
def StudentDashboard():
    if request.method=='POST':
        username=request.method['username']
        add_class=request.form['class']
        cursor=mysql.connection.cursor()
        cursor.execute("select * From studentreport where username=%s AND class=%s",(username,add_class))
        if session.loggedin:
            return render_template("UI/student/StudentDashboard.html",username=username,add_class=add_class)
    return render_template('UI/student/StudentDashboard.html')

##############Student logout#############

@app.route('/UI/student/studentlogout')
def Studentlogout():
    session.pop('username')
    return render_template('UI/Login/studentlogin.html')



##############Nonfaculty `dashboard###########

@app.route('/UI/NonFaculty/NonfacultyDashboard', methods = ['GET', 'POST'])
def facultydashboard():
    if 'loggedin' in session:
        username=request.form.get['username']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM nonfaculty WHERE username = % s',(username  ))
        
        # User is loggedin show them the home page
        return render_template('UI/NonFaculty/NonfacultyDashboard.html', username=session['username'])
    # User is not loggedin redirect to login page
   
    
    return render_template('UI/NonFaculty/NonfacultyDashboard.html')

    

        
    
    

##############Nonfaculty logout#############

@app.route('/UI/NonFaculty/Nonfacultylogout')
def Nonfacultylogout():
    session.pop('username')
    
    return render_template('/UI/Login/nonfacultylogin.html')

################Adminlogout####################
@app.route('/UI/Admin/Adminlogout')
def Adminlogout():
    session.pop('username')
    
    return render_template('/UI/Admin/login.html')


 ########  Master Logout###############

@app.route('/UI/Master/logout')
def Masterlogout():
    session.pop('username')
    
    return render_template('/UI/Login/masterlogin.html')





############Nonfaculty change password#############

@app.route('/UI/NonFaculty/changepassword',methods=['GET','POST'])
def NonFacultchangepassword():
    if request.method == 'POST': 
        OldPassword = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM nonfaculty WHERE password = % s ', (OldPassword, ))
        abc = cursor.fetchone()
        if abc:
            id_data = request.form['id']
            OldPassword=request.form['password']
            newPassword=request.form['newpassword']
            
            cur = mysql.connection.cursor()
            cur.execute("""
               UPDATE nonfaculty
               SET password=%s
               WHERE id=%s
            """, (newPassword, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/NonFaculty/NonfacultyDashboard.html" ,msg=msg)

    msg="Not Change"
    return render_template("UI/NonFaculty/changepassword.html" )




##################Student changepassword##################


@app.route('/UI/student/changepassword',methods=['GET','POST'])
def studentchangepassword():
    if request.method == 'POST': 
        OldPassword = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM studentreport WHERE password = % s ', (OldPassword, ))
        abc = cursor.fetchone()
        if abc:
            id_data = request.form['id']
            OldPassword=request.form['password']
            newPassword=request.form['newpassword']
            
            cur = mysql.connection.cursor()
            cur.execute("""
               UPDATE studentreport
               SET password=%s
               WHERE id=%s
            """, (newPassword, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/student/StudentDashboard.html" ,msg=msg)

    msg="Not Change"
    return render_template("UI/student/changepassword.html" )




#################Admin change password#################

@app.route('/UI/Admin/changepassword',methods=['GET','POST'])
def adminchangepassword():
    if request.method == 'POST': 
        OldPassword = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM loginmaster WHERE password = % s ', (OldPassword, ))
        abc = cursor.fetchone()
        if abc:
            id_data = request.form['id']
            OldPassword=request.form['password']
            newPassword=request.form['newpassword']
            
            cur = mysql.connection.cursor()
            cur.execute("""
               UPDATE loginmaster
               SET password=%s
               WHERE id=%s
            """, (newPassword, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)

    msg="Not Change"
    return render_template("UI/Admin/changepassword.html" )





############  Faculty Forgot Password###############

@app.route('/UI/Login/facultyforgotpassword',methods=['GET','POST'])
def facultyforgotpassword():
    return render_template("UI/Login/facultyforgotpassword.html")


############# stuedent Forgot Password#############
@app.route('/UI/Login/studentforgotpassword',methods=['GET','POST'])
def studentforgotpassword():
    return render_template("UI/Login/studentforgotpassword.html")
    

############Nonfaculty Forgot Password####################

@app.route('/UI/Login/nonfacultyforgotpassword',methods=['GET','POST'])
def NonFacultyforgotpassword():
    return render_template("UI/Login/nonfacultyforgotpassword.html")


############Admin Forgot Password#######################

@app.route('/UI/Login/forgotpassword',methods=['GET','POST'])
def Adminforgotpassword():
    return render_template("UI/Login/forgotpassword.html")


############## Reception Register#############
@app.route('/UI/Reception/addreceptionist',methods=['GET','POST'])
def feeee():

    
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':
        name=request.form['name']
        birthdate=request.form['birthdate']
        joiningdate=request.form['joiningdate']
        gender=request.form['gender']
        phone=request.form['phone']
        email=request.form['email']
        aadharno=request.form['aadharno']
        presentaddress=request.form['presentaddress']
        permanentaddress=request.form['permanentaddress']
        username=request.form['username']
        password=request.form['password']
        files1 = request.files.getlist('files1[]')
        
        #print(files)
        for file in files1:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cur.execute("INSERT INTO addreception (name,birthdate,joiningdate,gender,phone,email,aadharno,presentaddress,permanentaddress,username,password,file_name,uploaded_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[name,birthdate,joiningdate,gender,phone,email,aadharno,presentaddress,permanentaddress,username,password,filename,now])
                mysql.connection.commit()
            print(file)
        cur.close()   
        flash('File(s) successfully uploaded')    
    return render_template("UI/Reception/addreception.html")
        


# @app.route('/UI/Reception/addreceptionist',methods=['GET','POST'])
# def feeee():

#     if request.method == 'POST':
        
       
#         name=request.form['name']
#         birthdate=request.form['birthdate']
#         joiningdate=request.form['joiningdate']
        
       
#         gender=request.form['gender']
#         phone=request.form['phone']
#         email=request.form['email']
#         aadharno=request.form['aadharno']
        
       
        
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         username=request.form['username']
#         password=request.form['password']
#         photo=request.form['photo']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO addreception (name,birthdate,joiningdate,gender,aadharno,phone,email,presentaddress,permanentaddress,username,password,photo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[name,birthdate,joiningdate,gender,aadharno,phone,email,presentaddress,permanentaddress,username,password,photo])
#         mysql.connection.commit()
#         print("test1")
#         msg="successfully addReception"
#         print("test")
#         return render_template("UI/Reception/Dashboard.html" ,msg=msg)
    
#     else:
#         return render_template("UI/Reception/addreception.html")

############Reception Login###################
    


@app.route('/UI/Login/receptionlogin',methods=['GET','POST'])
def reception():
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM addreception WHERE username = % s AND password = % s', (username, password, ))
        nonfaclog = cursor.fetchone()
        if nonfaclog:
            session['loggedin'] = True
            session['id'] = nonfaclog['id']
            session['username'] = nonfaclog['username']
            msg = 'Logged in successfully !'
            return render_template('UI/Reception/Dashboard.html', msg = msg)
        else:
            msg = 'Wrong Credential !'
            return render_template('UI/Login/receptionlogin.html', msg = msg)
    else:
        return render_template("/UI/Login/receptionlogin.html")
    



###############Reception Dashboard##############



@app.route('/UI/Reception/receptionDashboard', methods = ['GET', 'POST'])
def receptiondashboard():
    if request.method=='POST':
        username=request.method['username']
        cursor=mysql.connection.cursor()
        cursor.execute("select * From addrecepton where username=%s",(username))
        if session.loggedin:
            return render_template("UI/Reception/Dashboard.html",username=username)
        return render_template('UI/Login/receptionlogin.html')


###############Recepton Forgot Password#################



@app.route('/UI/Login/receptionforgotpassword',methods=['GET','POST'])
def receptionforgotpassword():
    return render_template("UI/Login/receptionforgotpassword.html")



###############Change npassword##############

@app.route('/UI/Reception/changepassword',methods=['GET','POST'])
def receptionchangepassword():
    
    if request.method == 'POST': 
        OldPassword = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM addreception WHERE password = % s ', (OldPassword, ))
        abc = cursor.fetchone()
        if abc:
            id_data = request.form['id']
            OldPassword=request.form['password']
            newPassword=request.form['newpassword']
            
            cur = mysql.connection.cursor()
            cur.execute("""
               UPDATE addreception
               SET password=%s
               WHERE id=%s
            """, (newPassword, id_data))
        mysql.connection.commit()
        msg="successfully updated"
       



        return render_template("UI/Reception/Dashboard.ht`ml" ,msg=msg)

    msg="Not Change"
    return render_template("UI/Reception/changepassword.html" )

   
##########Reception Logout############

@app.route('/UI/Reception/logout')
def receptionlogout():
    session.pop('username')
    
    return render_template('UI/Login/receptionlogin.html')



################ Accountant Register####################
@app.route('/UI/Accountant/addaccountant',methods=['GET','POST'])
def accountant():
    
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':
        name=request.form['name']
        birthdate=request.form['birthdate']
        joiningdate=request.form['joiningdate']
        gender=request.form['gender']
        phone=request.form['phone']
        email=request.form['email']
        aadharno=request.form['aadharno']
        presentaddress=request.form['presentaddress']
        permanentaddress=request.form['permanentaddress']
        username=request.form['username']
        password=request.form['password']
        files1 = request.files.getlist('files1[]')
        
        #print(files)
        for file in files1:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cur.execute("INSERT INTO addaccountant (name,birthdate,joiningdate,gender,phone,email,aadharno,presentaddress,permanentaddress,username,password,file_name,uploaded_on) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[name,birthdate,joiningdate,gender,phone,email,aadharno,presentaddress,permanentaddress,username,password,filename,now])
                mysql.connection.commit()
            print(file)
        cur.close()   
        flash('File(s) successfully uploaded')    
    return render_template('UI/Accountant/addaccountant.html')
        
    

        
            
    
              


    



# @app.route('/UI/Accountant/addaccountant',methods=['GET','POST'])
# def accountant():

#     if request.method == 'POST':
        
       
#         name=request.form['name']
#         birthdate=request.form['birthdate']
#         joiningdate=request.form['joiningdate']
        
       
#         gender=request.form['gender']
#         phone=request.form['phone']
#         email=request.form['email']
#         aadharno=request.form['aadharno']
        
       
        
#         presentaddress=request.form['presentaddress']
#         permanentaddress=request.form['permanentaddress']
#         username=request.form['username']
#         password=request.form['password']
#         photo=request.form['photo']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO addaccountant (name,birthdate,joiningdate,gender,aadharno,phone,email,presentaddress,permanentaddress,username,password,photo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[name,birthdate,joiningdate,gender,aadharno,phone,email,presentaddress,permanentaddress,username,password,photo])
#         mysql.connection.commit()
#         print("test1")
#         msg="successfully addAccountant"
#         print("test")
#         return render_template("UI/Accountant/Dashboard.html" ,msg=msg)
    
#     else:
#         return render_template("UI/NonFaculty/addaccountant.html")



###############Accountant Login########################



@app.route('/UI/Login/accountantlogin',methods=['GET','POST'])
def accountantlogin():
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM addaccountant WHERE username = % s AND password = % s', (username, password, ))
        nonfaclog = cursor.fetchone()
        if nonfaclog:
            session['loggedin'] = True
            session['id'] = nonfaclog['id']
            session['username'] = nonfaclog['username']
            msg = 'Logged in successfully !'
            return render_template('UI/Accountant/Dashboard.html', msg = msg)
        else:
            msg = 'Wrong Credential !'
            return render_template('UI/Login/accountantlogin.html', msg = msg)
    else:
        return render_template("/UI/Login/accountantlogin.html")


    


    



###############Accountant Dashboard##############



@app.route('/UI/Accountant/Dashboard', methods = ['GET', 'POST'])
def accountantdashboard():
    if request.method=='POST':
        username=request.method['username']
        cursor=mysql.connection.cursor()
        cursor.execute("select * From addaccountant where username=%s",(username))
        if session.loggedin:
            return render_template("UI/Accountant/Dashboard.html",username=username)
        return render_template('UI/Accountant/Dashboard.html')


###############Accountant Forgot Password#################



@app.route('/UI/Accountant/forgotpassword',methods=['GET','POST'])
def accountantforgotpassword():
    return render_template("UI/Accountant/forgotpassword.html")


@app.route('/UI/Accountant/logout')
def accountantlogout():
    session.pop('username')
    
    return render_template('UI/Login/accountantlogin.html')



###########Accountant Changepassword#####################



@app.route('/UI/Accountant/changepassword',methods=['GET','POST'])
def accountantchangepassword():
    if request.method == 'POST': 
        OldPassword = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM addaccountant WHERE password = % s ', (OldPassword, ))
        abc = cursor.fetchone()
        if abc:
            id_data = request.form['id']
            OldPassword=request.form['password']
            newPassword=request.form['newpassword']
            
            cur = mysql.connection.cursor()
            cur.execute("""
               UPDATE addaccountant
               SET password=%s
               WHERE id=%s
            """, (newPassword, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Accountant/changepassword.html" ,msg=msg)

    msg="Not Change"
    return render_template("UI/Accountant/changepassword.html" )








 
############### search code###############

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#     if request.method == "GET":
#         students = request.form['id']
#         cur = mysql.connection.cursor() 
#         cur.execute("SELECT name,email,phone from students where id=%s",(students))
#         mysql.connection.commit()
#         data = cur.fetchall()
#         return redirect(url_for('Index',data=data))
#     return redirect(url_for('Index'))

############## LIST OF STUDENT###############

@app.route('/UI/Accountant/listofstudent',methods=['GET','POST'])
def listofstudent():
    if request.method=='GET':
        print("i am a line no 2661")
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT add_session FROM add_session') 
        add_session = cursor.fetchall() 
        cursor.execute('SELECT class FROM add_class') 
        add_class = cursor.fetchall() 
        cursor.execute('SELECT add_section FROM new_section') 
        new_section = cursor.fetchall() 
       
        
        return render_template("UI/Accountant/listofstudent.html",add_session=add_session,add_class=add_class,new_section=new_section) 

    else:
        print("i am a line no 2663")
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT add_session FROM add_session') 
        add_session = cursor.fetchall() 
        cursor.execute('SELECT class FROM add_class') 
        add_class = cursor.fetchall() 
        cursor.execute('SELECT add_section FROM new_section') 
        new_section = cursor.fetchall() 
        print("i am line no2664 ")
        add_class=request.form['class']
        add_session=request.form['add_session']
        add_section=request.form['add_section']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id,rollno,name,fathername,addmission,phone,email,feeexcused,aadharno FROM studentreport WHERE add_session=%s AND class=%s AND add_section=%s ',(add_session,add_class,add_section ))
        abc=cursor.fetchall()
        print("line no 2681")
        
         
        return render_template("UI/Accountant/listofstudent.html",add_session=add_session,add_class=add_class,new_section=new_section,studentreport=abc)




@app.route("/imageupload",methods=["POST","GET"])
def upload():
    
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    now = datetime.now()
    if request.method == 'POST':
        files1 = request.files.getlist('files1[]')
        name= request.form['name']
        #print(files)
        for file in files1:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cur.execute("INSERT INTO images (file_name, uploaded_on,name) VALUES (%s, %s,%s)",[filename, now,name])
                mysql.connection.commit()
            print(file)
        cur.close()   
        flash('File(s) successfully uploaded')    
    return render_template('imageupload.html')




# @app.route('/contact',methods=['GET','POST'])
# def contact1():
#     if request.method=='POST':
#         name=request.form['name']
#         email=request.form['email']
#         mobileno=request.form['mobileno']
#         subject=request.form['subject']
#         message=request.form['message']
#         cur=mysql.connection.cursor()
#         cur.execute("INSERT INTO contact (name,email,mobileno,subject,message) VALUES(%s,%s,%s,%s,%s)",[name,email,mobileno,subject,message])
#         mysql.connection.commit()
#         msg="successfully send data"
#         return render_template("contact.html",msg=msg)






############ master login#####################

@app.route('/UI/Login/masterlogin',methods=['GET','POST'])
def masterlogin():
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM masterlogin WHERE username = % s AND password = % s', (username, password, ))
        masterlogin = cursor.fetchone()
        if masterlogin:
            session['loggedin'] = True
            session['id'] = masterlogin['id']
            session['username'] = masterlogin['username']
            msg = 'Logged in successfully !'
            return render_template('UI/Master/dashboard.html', msg = msg)
        else:
            msg = 'Wrong Credential !'
            return render_template('UI/Login/masterlogin.html', msg = msg)
    else:
        return render_template("/UI/Login/masterlogin.html")


############# Add Class Report##############
@app.route("/UI/Report/addclassreport",methods=['GET','POST'])
def addclassreport():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM add_class")
        c=cur.fetchall()
        return render_template("UI/Report/addclassreport.html",add_class=c)
    else:
         
        id_data = request.form['id']
        add_class=request.form['class']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE add_class
               SET class=%s
               WHERE id=%s
            """, ( add_class, id_data))
        
        cur.execute("SELECT * FROM add_class")
        c=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/addclassreport.html" ,msg=msg,add_class=c)



################# Add Section Report#############

@app.route("/UI/Report/addsectionreport",methods=['GET','POST'])
def addsectionreport():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM new_section")
        c=cur.fetchall()
        return render_template("UI/Report/addsectionreport.html",new_section=c)
    else:
        id_data = request.form['id']
        add_section=request.form['add_section']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE new_section
               SET add_section=%s
               WHERE id=%s
            """, (add_section,id_data))
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM new_section")
        c=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/addsectionreport.html",new_section=c,msg=msg)




############ Add Session Report############

@app.route("/UI/Report/addsessionreport",methods=['GET','POST'])
def addsessionreport():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM add_session")
        c=cur.fetchall()
        return render_template("UI/Report/addsessionreport.html",add_session=c)
    else:
        
        id_data = request.form['id']
        add_session=request.form['add_session']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE add_session
               SET add_session=%s
               WHERE id=%s
            """, ( add_session, id_data))

        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM add_session")
        c=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/addsessionreport.html",msg=msg,add_session=c)


###########Feetile report######################
@app.route("/UI/Report/feetitleeport",methods=['GET','POST'])
def feetitlereport():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeetitle")
        c=cur.fetchall()
        return render_template("UI/Report/feetitlereport.html",addfeetitle=c)
    else:
        id_data = request.form['id']
        feetitle=request.form['feetitle']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addfeetitle
               SET feetitle=%s
               WHERE id=%s
            """, ( feetitle, id_data))
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeetitle")
        c=cur.fetchall()
        
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/feetitlereport.html",addfeetitle=c,msg=msg)





########### DElete feetitle#########

@app.route("/deletefeetitle/<string:id_data>",methods=['GET'])
def deletefeetitle(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addfeetitle WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeetitle")
        c=cur.fetchall()
       
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/feetitlereport.html",addfeetitle=c,msg=msg)
    

############### update fee###########    
@app.route('/updateaddfeeclass',methods=['GET','POST'])
def updateaddfeeclass():
    if request.method == 'POST':
        id_data = request.form['id']
        feetitle=request.form['feetitle']
        category=request.form['category']
        add_class=request.form['class']
        feeamount=request.form['feeamount']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addfeeamount
               SET feetitle=%s,category=%s,class=%s,feeamount=%s
               WHERE id=%s
            """, ( feetitle,category,add_class,feeamount, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/addfeereport.html" ,msg=msg)


############### delete fee############
@app.route("/deleteaddfeeclass/<string:id_data>",methods=['GET'])
def deleteaddfeeclass(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addfeeamount WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addfeeamount')
        c=cur.fetchall()
        
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/addfeereport.html",msg=msg,addfeeamount=c)




###########Feecategory report######################
@app.route("/UI/Report/feecategoryreport",methods=['GET','POST'])
def feecategoryreport():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,feetitle,category FROM addfeecategory")
        c=cur.fetchall()
        return render_template("UI/Report/feecategoryreport.html",addfeecategory=c)
    else:
        id_data = request.form['id']
        feetitle=request.form['feetitle']
        category=request.form['category']
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addfeecategory
               SET feetitle=%s,category=%s
               WHERE id=%s
            """, (feetitle,category,id_data))
        cur=mysql.connection.cursor()
        cur.execute("SELECT id,feetitle,category FROM addfeecategory")
        c=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/feecategoryreport.html",addfeecategory=c,msg=msg)






############### Update feecategory #################

# @app.route('/updatefeecategory',methods=['GET','POST'])
# def updatefeecategory():
#     if request.method == 'POST':
#         id_data = request.form['id']
#         feetitle=request.form['feetitle']
#         category=request.form['category']
        
        
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addfeecategory
#                SET feetitle=%s,category=%s,
#                WHERE id=%s
#             """, ( feetitle,category, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("UI/Report/feecategoryreport.html" ,msg=msg)



############# delete fee category#################


@app.route("/deletefeecategory/<string:id_data>",methods=['GET'])
def deletefeecategory(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addfeecategory WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeecategory")
        c=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/feecategoryreport.html",msg=msg,addfeecategory=c)





#########   Student  Profile ################




# @app.route('/UI/student/myprofile',methods=['GET','POST'])
# def myprofile():
#     if request.method=='GET':
#         print("i am a line no 2661")
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT username FROM studentreport') 
#         studentreport = cursor.fetchone(size=5) 
        
       
        
#         return render_template("/UI/student/myprofile.html",studentreport=studentreport) 

#     else:
#         print("i am a line no 2663")
        
        
#         print("i am line no2664 ")
#         username=request.form['username']
        
#         cursor = mysql.connection.cursor()

#         cursor.execute("SELECT id,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,add_session,presentaddress,permanentaddress FROM studentreport WHERE username LIKE %s",[username ])
#         studentreport=cursor.fetchall()
#         print("line no 2681")
        
         
#         return render_template("/UI/student/myprofile1.html",studentreport=studentreport)


# @app.route('/UI/student/myprofile1',methods=['GET','POST'])
# def myprofile1():
#     return render_template("UI/student/myprofile1.html")



# @app.route('/updatemyprofile',methods=['GET','POST'])
# def updatemyprofile():
    
#     if request.method == 'POST':
#             id_data=request.form['id']
#             name=request.form['name']
#             fathername=request.form['fathername']
#             mothername=request.form['mothername']
#             addmission=request.form['addmission']
#             admissiondate=request.form['admissiondate']
#             birthdate=request.form['birthdate']
#             gender=request.form['gender']
#             aadharno=request.form['aadharno']
#             religion=request.form['religion']
#             caste=request.form['caste']
#             housename=request.form['housename']
#             phone=request.form['phone']
#             email=request.form['email']
#             add_class=request.form['class']
#             add_section=request.form['add_section']
#             stream=request.form['stream']
#             rollno=request.form['rollno']
#             feeexcused=request.form['feeexcused']
#             add_session=request.form['add_session']
#             presentaddress=request.form['presentaddress']
#             permanentaddress=request.form['permanentaddress']
#             cursor = mysql.connection.cursor()
#             cursor.execute("""
#                UPDATE studentreport
#                SET name=%s,fathername=%s,mothername=%s,addmission=%s,admissiondate=%s,birthdate=%s,gender=%s,aadharno=%s,religion=%s,caste=%s,housename=%s,phone=%s,email=%s,class=%s,add_section=%s,stream=%s,rollno=%s,feeexcused=%s,add_section=%s,presentaddress=%s,permanentaddress=%s
#                WHERE id=%s
#             """, (name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,add_class,add_section,stream,rollno,feeexcused,add_session,presentaddress,permanentaddress,id_data))
#             mysql.connection.commit()
#             msg="successfully updated"
#             return render_template("UI/student/myprofile1.html" ,msg=msg)



# @app.route('/UI/student/mypro',methods=['GET','POST'])
# def mypro():
    
#     msg = ''
#     if 'loggedin' in session:
#         if request.method == 'POST':  
#             name=request.form.get['name']
#             fathername=request.form.get['fathername']
#             mothername=request.form.get['mothername']
#             addmission=request.form.get['addmission']
#             admissiondate=request.form.get['admissiondate']
#             birthdate=request.form.get['birthdate']
#             gender=request.form.get['gender']
#             aadharno=request.form.get['aadharno']
#             religion=request.form.get['religion']
#             caste=request.form.get['caste']
#             housename=request.form.get['housename']
#             phone=request.form.get['phone']
#             email=request.form.get['email']
#             # add_class=request.form['class']
#             # add_section=request.form['add_section']
#             # stream=request.form['stream']
#             rollno=request.form.get['rollno']
#             feeexcused=request.form.get['feeexcused']
#             # add_session=request.form['add_session']
#             presentaddress=request.form.get['presentaddress']
#             permanentaddress=request.form.get['permanentaddress']
#             username=request.form.get['username']
#             password=request.form.get['password']
#             cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#             cursor.execute('SELECT * FROM studentreport WHERE username = % s',(username, ))
#             studentreport = cursor.fetchone()
#             if studentreport:
#             #     msg = 'Account already exists !'
#             # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
#             #     msg = 'Invalid email address !'
#             # elif not re.match(r'[A-Za-z0-9]+', username):
#             #     msg = 'name must contain only characters and numbers !'
#             # else:
#                 cursor.execute('UPDATE studentreport SET  name=%s,fathername=%s,mothername=%s,addmission=%s,admissiondate=%s,birthdate=%s,gender=%s,aadharno=%s,religion=%s,caste=%s,housename=%s,phone=%s,email=%s,rollno=%s,feeexcused=%s,presentaddress=%s,permanentaddress=%s,username=%s,password=%s WHERE id =% s', (name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,rollno,feeexcused,presentaddress,permanentaddress,username,password (session['id'], ), ))
#                 mysql.connection.commit()
#                 msg = 'You have successfully updated !'
#         # elif request.method == 'POST':
#         #     msg = 'Please fill out the form !'
#         return render_template("UI/student/mypro.html", msg = msg)
#     return render_template("UI/student/mypro.html")



@app.route('/UI/student/mypro',methods=['GET','POST'])
def mypro():

    if 'loggedin' in session:
        if request.method=='GET':
        
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,add_session,presentaddress,permanentaddress,username,file_name FROM studentreport WHERE id = % s', (session['id'], ))
            studentreport = cursor.fetchone()   
            return render_template("UI/student/mypro.html", studentreport = studentreport)
        else:
                
                    name=request.form['name']
                    fathername=request.form['fathername']
                    mothername=request.form['mothername']
                    addmission=request.form['addmission']
                    admissiondate=request.form['admissiondate']
                    birthdate=request.form['birthdate']
                    gender=request.form['gender']
                    aadharno=request.form['aadharno']
                    religion=request.form['religion']
                    caste=request.form['caste']
                    housename=request.form['housename']
                    phone=request.form['phone']
                    email=request.form['email']
                    add_class=request.form['class']
                    add_section=request.form['add_section']
                    stream=request.form['stream']
                    rollno=request.form['rollno']
                    feeexcused=request.form['feeexcused']
                    add_session=request.form['add_session']
                    presentaddress=request.form['presentaddress']
                    permanentaddress=request.form['permanentaddress']
                    username=request.form['username']
            
                    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

                    cursor.execute('UPDATE studentreport SET  name=%s,fathername=%s,mothername=%s,addmission=%s,admissiondate=%s,birthdate=%s,gender=%s, aadharno=%s,religion=%s,caste=%s,housename=%s,phone=%s,email=%s,class=%s,add_section=%s,stream=%s,rollno=%s,feeexcused=%s,add_session=%s,presentaddress=%s,permanentaddress=%s,username=%s WHERE id =% s', (name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,add_class,add_section,stream,rollno,feeexcused,add_session,presentaddress,permanentaddress,username, (session['id'], ), ))
                
                    mysql.connection.commit()
                    msg="successfully updated"
                    return render_template("UI/student/StudentDashboard.html" ,msg=msg)



# if request.method=='POST':
#         username=request.method['username']
#         add_class=request.form['class']
#         cursor=mysql.connection.cursor()
#         cursor.execute("select * From studentreport where username=%s AND class=%s",(username,add_class))
#         if session.loggedin:
#             return render_template("UI/student/StudentDashboard.html",username=username,add_class=add_class)
#     return render_template('UI/Login/studentlogin.html')




    

############# updateprofilepic######################

@app.route('/UI/student/updateprofilepic',methods=['GET','POST'])
def updateprofilepic():
    
    
        if request.method=='GET':
            # cursor=mysql.connection.cursor()
            # cursor.execute('SELECT id,subject,name FROM routine WHERE class = % s', (session['class'], ))
            # abc=cursor.fetchall()
            
     
            return render_template("UI/student/updateprofilepic.html")
        else:
            
            
            return render_template("UI/student/updateprofilepic.html")


    # if request.method=='POST':
    #     username=request.method['username']
    #     add_class=request.form['class']
    #     cursor=mysql.connection.cursor()
    #     cursor.execute("select * From studentreport where username=%s AND class=%s",(username,add_class))
    #     if session.loggedin: 

    




############# homework######################

@app.route('/UI/student/homework',methods=['GET','POST'])
def homework():
    if request.method=='GET':
     
        return render_template("UI/student/homework.html")


############# Attendance ######################

@app.route('/UI/student/attendance',methods=['GET','POST'])
def attendance(): 
    if request.method=='GET':
     
        return render_template("UI/student/attendance.html")  


############# onlineclass ######################

@app.route('/UI/student/onlineclass',methods=['GET','POST'])
def onlineclass():
    if request.method=='GET': 
     
        return render_template("UI/student/onlineclass.html") 


############# fee ######################

@app.route('/UI/student/fee',methods=['GET','POST'])
def fee1():
    if request.method=='GET':
   
        return render_template("UI/student/fee.html")  

############## Routine.html#######################
@app.route('/UI/student/routine',methods=['GET','POST'])
def studentroutine():
    
        if request.method=='GET':
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT id,periodname,time,time1,class,subject,name FROM routine WHERE class = % s', (session['class'], ))
            abc=cursor.fetchall()
            
     
            return render_template("UI/student/routine.html",routine=abc)
        else:
            # username=request.method['username']
            # add_class=request.form['class']
            # cursor=mysql.connection.cursor()
            # cursor.execute("select * From studentreport where username=%s AND class=%s",(username,add_class))
            # if session.loggedin:
                return render_template("UI/student/routine.html",(header))
    

################# Teacher Profile########################

@app.route('/UI/student/teacherprofile',methods=['GET','POST'])
def teacherprofile():
    
        if request.method=='GET':
            cursor=mysql.connection.cursor()
            cursor.execute('SELECT id,subject,name FROM routine WHERE class = % s', (session['class'], ))
            abc=cursor.fetchall()
            
     
            return render_template("UI/student/teacherprofile.html",routine=abc)
        else:
            
            
            return render_template("UI/student/teacherprofile.html",(header))






################# Teachers Profile###################
@app.route("/UI/Faculty/teacherprofile1",methods=['GET','POST'])
def teacherpro():
    if 'loggedin' in session:
        if request.method=='GET':
            cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute('SELECT * FROM addteacher WHERE id = %s',(session['id'],))
            addteacher=cur.fetchone()
            return render_template("UI/Faculty/teacherprofile1.html",addteacher=addteacher)
        else:
            name=request.form['name']
            nationalid=request.form['nationalid']
            phone=request.form['phone']
            gender=request.form['gender']
            birthdate=request.form['birthdate']
            joiningdate=request.form['joiningdate']
            fathername=request.form['fathername']
            aadharno=request.form['aadharno']
            presentaddress=request.form['presentaddress']
            permanentaddress=request.form['permanentaddress']
            qualification=request.form['qualification']
            email=request.form['email']
            username=request.form['username']
       
            designation=request.form['designation']
         
            yearofexperience=request.form['yearofexperience']
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            

            cur.execute('UPDATE addteacher SET  name=%s,nationalid=%s,phone=%s,gender=%s,birthdate=%s,joiningdate=%s,fathername=%s,aadharno=%s,presentaddress=%s,permanentaddress=%s,qualification=%s,email=%s,username=%s,designation=%s,yearofexperience=%s WHERE id =% s', (name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,designation,yearofexperience, (session['id'], ) ,))
                
            mysql.connection.commit()
            msg="successfully updated"
           
            
            return render_template('UI/Faculty/FacultyDashboard.html',msg=msg)



# @app.route("/UI/Faculty/routineclasswise",methods=['GET','POST'])
# def routineclasswise():
#     if 'loggedin' in session:
#         if request.method=='GET':
#             cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#             cur.execute('SELECT nationalid FROM addteacher WHERE username = %s',(session['username'],))
#             addteacher=cur.fetchone()
#             return render_template("UI/Faculty/routineclasswise.html",addteacher=addteacher)
#         else:
        

            

#             cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#             cur.execute('SELECT subject,name FROM routine') 
#             routine=cur.fetchall()
#             mysql.connection.commit()
#             return render_template("UI/Faculty/routineclasswise.html",routine=routine)




@app.route("/UI/Faculty/routineclasswise",methods=['GET','POST'])
def routineclasswise():
    
        if request.method=='GET':
            cur=mysql.connection.cursor()
            cur.execute("SELECT day,subject,name FROM routine ")
            add=cur.fetchall()
            mysql.connection.commit()
            return render_template("UI/Faculty/routineclasswise.html",routine=add)

    
        # if request.method=='POST':
        #         nationalid=request.form['nationalid']
        #         print("i am a line no 2661")
        #         print("i am a line no 2663")
        #         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #         cursor.execute('SELECT nationalid FROM routine') 
        #         abc = cursor.fetchall() 
        
        #         print("i am line no2664 ")
                
        
        #         cursor = mysql.connection.cursor()
        #         cursor.execute('SELECT nationalid,subject,name FROM routine WHERE nationalid=%s',[nationalid])
                 
        #         abc = cursor.fetchall()
             
        
       
        
        #         return render_template("UI/Faculty/routineclasswise.html",routine=abc) 
        # else:
            
        #         # print("i am a line no 2663")
        #         # cursor = mysql.connection.cursor()
        #         # cursor.execute('SELECT nationalid FROM routine') 
        #         # abc = cursor.fetchall() 
        
        #         # print("i am line no2664 ")
        #         # nationalid=request.form['nationalid']
        
        #         # cursor = mysql.connection.cursor()
        #         # cursor.execute('SELECT subject,name FROM routine WHERE nationalid=%s',[nationalid ])
        #         # abc=cursor.fetchall()
        #         # print("line no 2681")
        
         
        #         return render_template("UI/Faculty/routineclasswise.html")


####################### Add homework ################

@app.route("/UI/Faculty/addhomework",methods=['GET','POST'])
def addhomework():
    if request.method=="GET":
        
        
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       
        
        
        cur.execute('SELECT class,add_section,subject FROM routine ')
        routine=cur.fetchall()
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addhomework")
        abc=cur.fetchall()
       
        
        return render_template("UI/Faculty/addhomework.html",routine=routine,addhomework=abc)
    else:
            cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
       
        
        
            cur.execute('SELECT class,add_section,subject FROM routine ')
            routine=cur.fetchall()
            cur=mysql.connection.cursor()
            cur.execute("SELECT * FROM addhomework")
            abc=cur.fetchall()
            cur=mysql.connection.cursor()
            
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            now = datetime.now()
            if request.method == 'POST':
                files1 = request.files.getlist('files1[]')
                add_class=request.form['class']
                add_section=request.form['add_section']
                subject=request.form['subject']
                title=request.form['title']
                description=request.form['description']
                
                print("files")
                for file in files1:
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                        cur.execute("INSERT INTO addhomework (file_name, uploaded_on,class,add_section,subject,title,description) VALUES (%s, %s,%s,%s,%s,%s,%s)",[filename, now,add_class,add_section,subject,title,description])
                        mysql.connection.commit()
                    print(file)
           
                flash('File(s) successfully uploaded')    
            return render_template("UI/Faculty/addhomework.html",routine=routine,addhomework=abc)




#####################   Assign Subject To Teacher #############



# @app.route("/UI/Admin/assignsubjecttoteacher",methods=['GET','POST'])
# def assignsubjecttoteacher():
#     if request.method=='GET':
        
        

#         cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute("SELECT class,add_section,subject,name FROM routine")
#         routine=cur.fetchall()
#         # cur=mysql.connection.cursor()
        
        
#         return render_template("UI/Admin/assignsubjecttoteacher.html",routine=routine)
#     else:
#         add_class=request.form['class']
#         add_section=request.form["add_section"]
#         subject=request.form["subject"]
#         teachername=request.form["name"]
#         cur=mysql.connection.cursor()
#         cur.execute("SELECT id,class,add_section,subject,name FROM assignsubject WHERE class=%s AND add_section=%s ",(add_class,add_section))
#         assignsubject=cur.fetchall()
#         cur.execute("INSERT INTO assignsubject (class,add_section,subject,name)VALUES(%s,%s,%s,%s)",(add_class,add_section,subject,teachername))
#         mysql.connection.commit()
#         return render_template("UI/Admin/assignsubjecttoteacher.html",assignsubject=assignsubject)


        



@app.route("/UI/Admin/assignsubjecttoteacher",methods=['GET','POST'])
def assignsubjecttoteacher():
    if request.method == 'POST': 
        add_class=request.form['class']
        add_section=request.form["add_section"]
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT class,add_section,subject,name FROM routine")
        ab=cur.fetchall()
       
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id,class,add_section,subject,name FROM assignsubject WHERE class = % s AND add_section=%s ', (add_class,add_section ))
        abc = cursor.fetchall()
        if abc:
            add_class=request.form['class']
            add_section=request.form["add_section"]
            subject=request.form["subject"]
            teachername=request.form["name"]
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO assignsubject (class,add_section,subject,name)VALUES(%s,%s,%s,%s)",(add_class,add_section,subject,teachername))
            mysql.connection.commit()
        return render_template("UI/Admin/assignsubjecttoteacher.html",assignsubject=abc,routine=ab)
    else:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT class,add_section,subject,name FROM routine")
        routine=cur.fetchall()
        
        
        
        return render_template("UI/Admin/assignsubjecttoteacher.html",routine=routine)
    

        





#################### View Student  ##############



        
      
@app.route("/UI/Faculty/viewstudent",methods=['GET','POST'])
def viewstudent():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT add_session FROM studentreport ')
        studentreport=cur.fetchall()
       
        return render_template("UI/Faculty/viewstudent.html",studentreport=studentreport)
    else:
        add_session=request.form['add_session']
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM studentreport WHERE add_session=%s',(add_session,))
        studentreport=cur.fetchall()
        return render_template("UI/Faculty/viewstudent1.html",studentreport=studentreport)


    
# @app.route('/UI/Accountant/listofstudent',methods=['GET','POST'])
# def listofstudent():
#     if request.method=='GET':
#         print("i am a line no 2661")
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT add_session FROM add_session') 
#         add_session = cursor.fetchall() 
#         cursor.execute('SELECT class FROM add_class') 
#         add_class = cursor.fetchall() 
#         cursor.execute('SELECT add_section FROM new_section') 
#         new_section = cursor.fetchall() 
       
        
#         return render_template("UI/Accountant/listofstudent.html",add_session=add_session,add_class=add_class,new_section=new_section) 

#     else:
#         print("i am a line no 2663")
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT add_session FROM add_session') 
#         add_session = cursor.fetchall() 
#         cursor.execute('SELECT class FROM add_class') 
#         add_class = cursor.fetchall() 
#         cursor.execute('SELECT add_section FROM new_section') 
#         new_section = cursor.fetchall() 
#         print("i am line no2664 ")
#         add_class=request.form['class']
#         add_session=request.form['add_session']
#         add_section=request.form['add_section']
#         cursor = mysql.connection.cursor()
#         cursor.execute('SELECT id,rollno,name,fathername,addmission,phone,email,feeexcused,aadharno FROM studentreport WHERE add_session=%s AND class=%s AND add_section=%s ',(add_session,add_class,add_section ))
#         abc=cursor.fetchall()
#         print("line no 2681")
        
         
#         return render_template("UI/Accountant/listofstudent.html",add_session=add_session,add_class=add_class,new_section=new_section,studentreport=abc)




             












##########insert carbrand##############

@app.route('/carinsert', methods=['GET','POST'])
def carinsert():
    if request.method=='GET':
        return render_template("carinsert.html")
    else:
        # brand_id=request.form['brand_id']
        brand_name=request.form['brand_name']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO cartest (brand_name) VALUES (%s)",[brand_name])
        return render_template("Dashboard.html")





#################  Dependent Dropdoen Code Demo ######################
@app.route('/UI/Master/dependent')
def main():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM addfeetitle ORDER BY id")
    carbrands = cur.fetchall()
    return render_template('UI/Master/dependentdropdown.html', addfeetitle=carbrands)
 
@app.route("/carbrand",methods=["POST","GET"])
def carbrand():  
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        category_id = request.form['category_id'] 
        print(category_id)  
        cur.execute("SELECT * FROM addfeecategory WHERE id = %s ORDER BY category ASC", [category_id] )
        addfeecategory = cur.fetchall()  
        OutputArray = []
        for row in addfeecategory:
            outputObj = {
                'id': row['id'],
                'name': row['category']}
            OutputArray.append(outputObj)
    return jsonify(OutputArray)


     
    

        
# @app.route('/dependentdropdown')
# def main():
#     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cur.execute("SELECT * FROM cartest ORDER BY brand_id")
#     carbrands = cur.fetchall()
#     return render_template('dependentdropdown.html', cartest=carbrands)
 
# @app.route("/carbrand",methods=["POST","GET"])
# def carbrand():  
#     cur = mysql.connection.cursor()
#     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     if request.method == 'POST':
#         category_id = request.form['category_id'] 
#         print(category_id)  
#         cur.execute("SELECT * FROM carmodtest WHERE brand_name = %s ORDER BY car_models ASC", [category_id] )
#         carmodtest = cur.fetchall()  
#         OutputArray = []
#         for row in carmodtest:
#             outputObj = {
#                 'id': row['brand_name'],
#                 'name': row['car_models']}
#             OutputArray.append(outputObj)
#     return jsonify(OutputArray)




########## Add Nationalid ##################



@app.route('/UI/Acccountant/nationalid',methods=['GET','POST'])
def nationalid():
    if request.method=="GET":
        return render_template("UI/Accountant/nationalid.html")
    else:
        id=request.form['id']
        nationalid=request.form['nationalid']

        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO nationalid (id,nationalid)VALUES(%s,%s)" ,[id,nationalid])
        mysql.connection.commit()
        msg="Successfully addedtime"
        return render_template("UI/Accountant/Dashboard.html" ,msg=msg)
    
##############  generatefee####################

@app.route('/UI/Accountant/generatefee',methods=['GET','POST'])
def generatefee():

    if request.method=="GET":
       
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT feetitle FROM addfeeamount")
        ghi=cur.execute()

        cur.execute("SELECT * FROM add_session")
        abc=cur.fetchall()
        cur.execute("SELECT * FROM  new_section")
        data=cur.fetchall()
        cur.execute("SELECT * FROM add_class")
        ad=cur.fetchall()
        cur.execute("SELECT rollno,admissiondate from studentreport")
        add=cur.fetchall()
        
            
        

        return render_template("UI/Accountant/generatefee.html",add_session=abc,new_section=data,add_class=ad,studentreport=add,addfeeamount=ghi)
    else:
            rollno=request.form['rollno']
            admissiondate=request.form['admissiondate']
            add_session=request.form['add_session']
            add_section=request.form['add_section']
            add_class=request.form['class']
            cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT name,rollno,add_session,add_section,class,admissiondate FROM studentreport WHERE add_session=%s AND add_section=%s AND class=%s AND rollno=%s AND admissiondate=%s",(add_session,add_section,add_class,rollno,admissiondate))
            s=cur.fetchone()
            # cur=mysql.connection.cursor()
            # cur.execute("INSERT INTO generatefee (add_session,add_section,class,rollno,admissiondate) VALUES(%s,%s,%s,%s,%s)",(add_session,add_section,add_class,rollno,admissiondate))
            cur=mysql.connection.cursor()
            cur.execute("SELECT id,feetitle,category,class,feeamount FROM addfeeamount WHERE class=%s",[add_class])
            c=cur.fetchall()
            cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            # cur.execute("SELECT feetitle FROM addfeeamount")
            # ghi=cur.execute()
            

            
            
            return render_template("UI/Accountant/insertdemomas.html",studentreport=s,addfeeamount=c)
            
            
                
            
            
                
   
            



@app.route('/UI/Acccountant/nationalid',methods=['GET','POST'])
def national():
    if request.method=="GET":
        
        return render_template("UI/Accountant/nationalid.html")
    else:
        id=request.form['id']
        nationalid=request.form['nationalid']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO nationalid(id,nationalid) VALUES (%s,%s)",(id,nationalid))
        mysql.connection.commit() 
        return render_template("UI/Accountant/Dashboard.html")

     

         
    
              



############  Dependent dropdown demo apply in project ####################
   
@app.route('/depdrpdemo2')
def kjl():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM addfeetitle ORDER BY id")
    abc = cur.fetchall()
    return render_template('depdrpdemo.html', addfeetitle=abc)


 
@app.route("/addfeetitle",methods=["POST","GET"])
def kvt():  
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        category_id = request.form['category_id'] 
        print(category_id)  
        cur.execute("SELECT category FROM addfeecategory WHERE feetitle = %s ORDER BY category ASC", [category_id] )
        addfeecategory = cur.fetchall()  
        OutputArray = []
        for row in addfeecategory:
            outputObj = {
                'id': row['feetitle'],
                'name': row['category']}
            OutputArray.append(outputObj)
    return jsonify(OutputArray)


#################   ADD FEE AMOUNT #####################


@app.route("/UI/Master/addfeeamount",methods=['GET','POST'])
def testing():
    if request.method=='GET':
        feetitle=request.form.get['feetitle']
        
    
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM addfeetitle")
        a=cur.fetchall()
        cur.execute("SELECT * FROM add_class")
        c=cur.fetchall()
        
        
        # category=request.form['category']
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT category FROM addfeecategory WHERE feetitle=%s",(feetitle))
        b=cur.fetchall()
        # cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cur.execute("SELECT * FROM addfeetitle")
        # a=cur.fetchall()
        # cur.execute("SELECT * FROM add_class")
        # c=cur.fetchall()
        return render_template("/UI/Master/addfeeamount.html",addfeetitle=a,addfeecategory=b,add_class=c)




# @app.route('/UI/Master/addfeeamount',methods=['POST','GET'])
# def stockk():
#     cur=mysql.connection.cursor()
#     cur.execute("SELECT feetitle FROM addfeetitle")
#     addfeetitle=cur.fetchall()
#     '''
#     result=[]
#     for row in addfeetitle:
#         result.append("|".join(row))
#     '''
#     cur.close()

#     return render_template('UI/Master/addfeeamount.html', addfeetitle=addfeetitle)

# @app.route('/category/get_feetitle>',methods=['POST','GET'])
# def year(get_feetitle):
#     cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

#     cur.execute("SELECT * FROM addfeecategory WHERE feetitle = %s", [get_feetitle])
    

#     addfeecategory = cur.fetchall()
#     print(addfeecategory)
#     categoryArray=[]
#     for row in addfeecategory:
#         categoryobj={
#             'category':row['category']}
        
        
#         categoryArray.append(categoryobj)
#     print(categoryArray)

#     return jsonify({'categorylist':categoryArray})






# @app.route('/UI/Master/addfeeamount',methods=['GET','POST'])
# def addfeemount():
#     if request.method=="GET":
        
        
#         cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute("SELECT * FROM addfeetitle WHERE feetitle=%s",(feetitle))
#         addfeet = cur.fetchall()
#         cur.execute("SELECT class FROM add_class ")
#         ghi = cur.fetchall()
        
#         # cur.execute('SELECT category FROM addfeecategory ORDER BY feetitle ')
        
#         cur.execute('SELECT category FROM addfeecategory')
#         feecat = cur.fetchall()
        
#         cur=mysql.connection.cursor()
#         cur.execute("SELECT * FROM addfeeamount ")
#         a = cur.fetchall()
        
#         return render_template("UI/Master/addfeeamount.html",addfeecategory=feecat,addfeetitle=addfeet,add_class=ghi,addfeeamount=a)
#     else:
#         feetitle=request.form['feetitle']
#         category=request.form['category']
#         add_class=request.form['class']
#         feeamount=request.form['feeamount']

#         cur=mysql.connection.cursor()
        
        
        
#         cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)

#         cur.execute("SELECT * FROM addfeetitle")
#         addfeet = cur.fetchall()
#         cur.execute("SELECT class FROM add_class ")
#         ghi = cur.fetchall()
        
#         cur.execute('SELECT category FROM addfeecategory')
#         feecat = cur.fetchall()
#         cur.execute("INSERT INTO addfeeamount (feetitle,category,class,feeamount)VALUES(%s,%s,%s,%s)" ,[feetitle,category,add_class,feeamount])
        
#         cur=mysql.connection.cursor()
#         cur.execute("SELECT * FROM addfeeamount ")
#         a = cur.fetchall()
#         mysql.connection.commit()
#         msg="Successfully addfee"
#         return render_template("UI/Master/addfeeamount.html",addfeecategory=feecat,addfeetitle=addfeet,add_class=ghi,addfeeamount=a,msg=msg)
    
        
##################    Add fee amount demo again ########################




# @app.route('/UI/Master/addfeeamount',methods=['GET','POST'])
# def addfeemount():
#     if request.method == 'POST': 
#         feetitle=request.form['feetitle']
        
#         cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute("SELECT feetitle FROM addfeetitle")
#         ab=cur.fetchall()
#         cur.execute('SELECT category FROM addfeecategory WHERE feetitle= %s',(feetitle))
#         b=cur.fetchall()
#         cur.execute("SELECT class FROM add_class")
#         e=cur.fetchall()
       
        
#         if b:
            
#             feetitle=request.form["feetitle"]
#             category=request.form["category"]
#             add_class=request.form['class']
#             feeamount=request.form["feeamount"]
#             cur = mysql.connection.cursor()
#             cur.execute("INSERT INTO addfeeamount (feetitle,category,class,feeamount)VALUES(%s,%s,%s,%s)",(add_class,feetitle,category,feeamount))
#             mysql.connection.commit()
#         return render_template("UI/Master/addfeeamount.html",addfeetitle=ab,addfeecategory=b,add_class=e)
#     else:
        
        


#         feetitle=request.form.get('feetitle')
        
#         cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute("SELECT feetitle FROM addfeetitle")
#         ab=cur.fetchall()
#         cur.execute('SELECT category FROM addfeecategory WHERE feetitle= %s',[feetitle])
#         b=cur.fetchall()
#         cur.execute("SELECT class FROM add_class")
#         e=cur.fetchall()
       
        
        
#         return render_template("UI/Master/addfeeamount.html",addfeetitle=ab,addfeecategory=b,add_class=e)
    
        
    

##################  Report Designation ###############
@app.route("/UI/Report/designation",methods=['GET','POST'])
def reportdesignation():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM designation")
        abc=cur.fetchall()
        return render_template("/UI/Report/designation.html",designation=abc)

    else:
    
        id_data=request.form['id']
        designation=request.form['designation']
        cur=mysql.connection.cursor()
        cur.execute("""
               UPDATE designation
               SET designation=%s
               WHERE id=%s
            """, ( designation, id_data))
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM designation")
        abc=cur.fetchall()

        mysql.connection.commit()
        msg="successfully updated"
        return render_template("/UI/Report/designation.html",designation=abc,msg=msg)



################ Update Designation Report##################


# @app.route("/updatedesignation",methods=['GET','POST'])
# def updatedesignation():
#     if request.method=='POST':
#         id_data=request.form['id']
#         designation=request.form['designation']
#         cur=mysql.connection.cursor()
#         cur.execute("""
#                UPDATE designation
#                SET designation=%s
#                WHERE id=%s
#             """, ( designation, id_data))

#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("/UI/Report/designation.html" ,msg=msg)


############# addhomework Report#####################


@app.route("/UI/Report/addhomeworkreport",methods=['GET','POST'])
def addhomeworkreport():
    if request.method=="GET":
        cur=mysql.connection.cursor()
        
        cur.execute("SELECT * FROM addhomework")
        abc=cur.fetchall()
       
        
        return render_template("/UI/Report/addhomeworkreport.html",addhomework=abc)
    else:
        id_data = request.form['id']
        add_class=request.form['class']
        add_section=request.form['add_section']
        subject=request.form['subject']
        title=request.form['title']
        description=request.form['description']
        
                
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addhomework
               SET class=%s,add_section=%s,subject=%s,title=%s,description=%s
               WHERE id=%s
            """, ( add_class,add_section,subject,title,description, id_data))
        cur=mysql.connection.cursor()
        
        cur.execute("SELECT * FROM addhomework")
        abc=cur.fetchall()
       
        
        
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("/UI/Report/addhomeworkreport.html",addhomework=abc,msg=msg)




############# addhomework report###############

# @app.route('/updateaddhomework',methods=['GET','POST'])
# def updateaddhomework():
    
#     if request.method == 'POST':
#         id_data = request.form['id']
#         add_class=request.form['class']
#         add_section=request.form['add_section']
#         subject=request.form['subject']
#         title=request.form['title']
#         description=request.form['description']
        
                
        
#         cur = mysql.connection.cursor()
#         cur.execute("""
#                UPDATE addhomework
#                SET class=%s,add_section=%s,subject=%s,title=%s,decription=%s
#                WHERE id=%s
#             """, ( add_class,add_section,subject,title,description, id_data))
#         mysql.connection.commit()
#         msg="successfully updated"
#         return render_template("UI/Report/addhomeworkreport.html" ,msg=msg)




##############  delete Add homework###############


@app.route('/deleteaddhomework/<string:id_data>', methods = ['GET'])
def deleteaddhomework(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM addhomework WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        
        cur.execute("SELECT * FROM addhomework")
        abc=cur.fetchall()
       
        
       
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("/UI/Report/addhomeworkreport.html",addhomework=abc,msg=msg)


###################  delete designation  #######################  

@app.route('/deletedesignation/<string:id_data>', methods = ['GET'])
def deletedesignation(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM designation WHERE id=%s", (id_data,))
        
        cur.execute("SELECT * FROM designation")
        a=cur.fetchall()
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template("UI/Report/designation.html",msg=msg,designation=a)


############ delete manage class#####################

@app.route('/deletemanageclass/<string:id_data>', methods = ['GET'])
def deletemanageclass(id_data):
    if request.method=='GET':
   
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM manageclass WHERE id=%s", (id_data,))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,class,numericname,classteacher,note FROM manageclass')
        data=cur.fetchall()
        
        mysql.connection.commit()
        msg=("Record Has Been Deleted Successfully")
        return render_template('UI/Report/manageclassreport.html',manageclass=data,msg=msg)


 ############### student fee report#####################

@app.route('/UI/Report/studentfeereport',methods=['GET','POST'])
def studentfeereport():
    if request.method=='GET':
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,rollno,class,add_section,add_session,admissiondate,date,feetitle,category,actualfee,discount,total FROM practice')
        c=cur.fetchall()
        
        return render_template("UI/Report/studentfeereport.html",practice=c)
    else:
        id_data = request.form['id']
        name=request.form['name']
        rollno=request.form['rollno']
        add_class=request.form['class']
        add_section=request.form['add_section']
        add_session=request.form['add_session']
        admissiondate=request.form['admissiondate']
        feetitle=request.form['feetitle']
        category=request.form['category']
        actualfee=request.form['actualfee']
        discount=request.form['discount']
        total=request.form['total']
            
            
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
                UPDATE practice 
                SET name=%s,rollno=%s,class=%s,add_section=%s,add_section=%s,admissiondate=%s,feetitle=%s,category=%s,actualfee=%s,discount=%s,total=%s
                WHERE id=%s
             """, (name,rollno,add_class,add_section,add_session,admissiondate,feetitle,category,actualfee,discount,total,id_data))
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,rollno,class,add_section,add_session,admissiondate,date,feetitle,category,actualfee,discount,total FROM practice')
        c=cur.fetchall()
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("UI/Report/studentfeereport.html",practice=c,msg=msg)


############## Delete Student Fee Report ##############

@app.route('/deletestudentfeereport/<string:id_data>', methods = ['GET'])
def deletestudentfeereport(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM practice WHERE id=%s", (id_data,))
    cur.execute('SELECT id,name,rollno,class,add_section,add_session,admissiondate,feetitle,category,actualfee,discount,total FROM practice')
    c=cur.fetchall()
    

    
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("UI/Report/studentfeereport.html" , msg=msg,practice=c)


    
################  Monthly Fee Bill########################


@app.route("/UI/Accountant/monthlyfeebill",methods=['GET','POST'])
def monthlyfeebill():
    return render_template("UI/Accountant/monthlyfeebill.html")

########### Student Monthly fee report##################
@app.route('/UI/Accountant/monthlyfee',methods=['GET','POST'])
def month():
    if request.method=='GET':
        
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT rollno FROM practice")
        d=cur.fetchall()
        cur.execute("SELECT class FROM add_class")
        e=cur.fetchall()
        cur.execute("SELECT add_section FROM new_section")
        f=cur.fetchall()
        
        
        return render_template("UI/Accountant/Monthlyfee.html",practice=d,add_class=e,new_section=f)
    else:
        rollno=request.form["rollno"]
        add_class=request.form["class"]
        add_section=request.form["add_section"]
        cur=mysql.connection.cursor()
        cur.execute('SELECT id,name,rollno,class,add_section,add_session,date,feetitle,category,actualfee,discount,total FROM practice WHERE rollno=%s AND class=%s AND add_section=%s',(rollno,add_class,add_section))
        c=cur.fetchall()
        
        
        
        
        return render_template("UI/Accountant/Monthlyfee1.html",practice=c)





    




#################   demo dropdown  ################
@app.route("/UI/Master/dpdemo/<string:feetitle>",methods=['GET','POST'])
def dpdemo(feetitle):
    if request.method==['GET']:
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        
        cur.execute("SELECT id FROM addfeetitle WHERE feetitle=%s",(feetitle))
        a=cur.fetchone()
        cur.execute("SELECT category FROM addfeecategory")
        b=cur.fetchall()
        return render_template("UI/Master/dpdemo.html",addfeetitle=a,addfeecategory=b)
    else:
        
        cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("SELECT * FROM addfeetitle")
        a=cur.fetchall()
            
        cur.execute("SELECT category FROM addfeecategory")
        b=cur.fetchall()
        return render_template("UI/Master/dpdemo.html",addfeecategory=b,addfeetitle=a)
        
            
        
# def dpdemotest():
#     if request.method==['GET']:
#         cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#         cur.execute("SELECT * FFROM addfeetitle WHERE feetitle='feetitle'")
#         c=cur.fetchone()
#         # cur.execute("SELECT * FROM addfeetitle")
#         # a=cur.fetchall()
#         return render_template("UI/Master/dpdemo.html",addfeetitle=c)
#     else:
#             cur=mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#             cur.execute("SELECT * FROM addfeetitle where feetitle='feetitle'")
#             a=cur.fetchall()
#             # cur.execute("SELECT category FROM addfeecategory")
#             # b=cur.fetchall()
#             return render_template("UI/Master/dpdemo.html",addfeetitle=a)


@app.route("/getfee",methods=['GET'])
def getfee():
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'GET':
        category_id = request.form['category_id'] 
        print(category_id)  
         
        
        
        cur.execute("SELECT * FROM addfeetitle WHERE id=[category_id]")
        abc=cur.fetchone()
        print(abc)
    else:
        print("failed")
           
        








	






    
    
    
    
    
    
    


 
    


 
    
    



    




    
    
    
    

    
    
    
    
    
    
    
















    
    
    
    
    

    
    
    
    
    


    
    
    


















        
        
        
        
    
    
        












if __name__ == "__main__":
    app.run(debug=True)
  