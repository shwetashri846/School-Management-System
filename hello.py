
from flask import Flask,render_template,request, redirect, url_for, session,flash
from flask_mysqldb import MySQL

import mysql.connector

app=Flask(__name__)
app.secret_key="caircocoders-ednalan"
# app.secret_key = 'your secret key'

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "admin12345"
app.config['MYSQL_DB']= "student1"
app.config['MYSQL_CURSORCLASS'] ='DictCursor'

mysql = MySQL(app)

  
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
    
    
 ###########about page########################   
    
@app.route('/about', methods = ['GET', 'POST'])
def about():
    print("page open")
    return render_template('about.html')


#################loginMaster################


@app.route('/loginMaster', methods = ['GET', 'POST'])
def loginMaster():
    print("page open")
    return render_template('loginMaster.html')









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
    print("page open")
    return render_template('Dashboard.html')



#############feetitle##############





@app.route('/feetitle',methods=['GET','POST'])
def fee():
    if request.method == 'POST':
        feetitle=request.form['feetitle']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO  addfeetitle(feetitle) VALUES (%s)",[feetitle])
        mysql.connection.commit()
        msg="successfully addfeetitle"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeetitle")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("addfeetitle.html" ,feetitle= data)
    
    
    
    
###################Add_Class_Update#############


@app.route('/update',methods=['GET','POST'])
def update():
    
    if request.method == 'POST':
        id_data = request.form['id']
        add_class=request.form['class']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE add_class
               SET class=%s
               WHERE id=%s
            """, ( add_class, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    
    
  ##############update sr#######################  
    
@app.route('/update',methods=['GET','POST'])
def update():
    
    if request.method == 'POST':
        id_data = request.form['id']
        add_class=request.form['class']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE add_class
               SET class=%s
               WHERE id=%s
            """, ( add_class, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    
    
##############add_Class_Delete########################


@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM add_class WHERE id=%s", (id_data,))
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("Dashboard.html" , msg=msg)


    


##################add class##################

@app.route('/addclass',methods=['GET','POST'])
def addclass():
    if request.method == 'POST':
        add_class=request.form['class']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO add_class (class) VALUES (%s)",[add_class])
        mysql.connection.commit()
        msg="successfully addclass"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM add_class")
        data = cur.fetchall()
        print("gridview")
        return render_template("Add Class.html" ,add_class= data)
    
    
    
####################UPDATE STUDeNT REGISTRATION REPORT####################



@app.route('/updatestudentregistrationreport',methods=['GET','POST'])
def updatestudentregistrationreport():
    
    if request.method == 'POST':
        id_data = request.form['id']
        name=request.form['name']
        
        add_class=request.form['class']
        add_section=request.form['add_section']
        rollno=request.form['rollno']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addstudentdetail
               SET name=%s,class=%s,add_section=%s,rollno=%s
               WHERE id=%s
            """, ( add_class, id_data,name,add_section,rollno))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
        
        
#############datashow#############



# @app.route('/datashow',methods=['GET','POST'])

# def test():
#         cur = mysql.connection.cursor()
#         cur.execute("SELECT * FROM add_class")
        
#         data = cur.fetchall()
#         print("demo")
        
#         return render_template("datashow.html" ,add_class= data)





################Update Section###############



@app.route('/updatesection',methods=['GET','POST'])
def updatesection():
    if request.method == 'POST':
        id_data = request.form['id']
        add_section=request.form['add_section']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE new_section
               SET add_section=%s
               WHERE id=%s
            """, ( add_section, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    
    
##############delete section########################


@app.route('/deletesection/<string:id_data>', methods = ['GET'])
def deletesection(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM new_section WHERE id=%s", (id_data,))
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("Dashboard.html" , msg=msg)




################Update Session###############



@app.route('/updatesession',methods=['GET','POST'])
def updatesession():
    if request.method == 'POST':
        id_data = request.form['id']
        add_session=request.form['add_session']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE add_session
               SET add_session=%s
               WHERE id=%s
            """, ( add_session, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    
    
#################delete Session###################


@app.route('/deletesession/<string:id_data>', methods = ['GET'])
def deletesession(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM add_session WHERE id=%s", (id_data,))
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("Dashboard.html" , msg=msg)

    
    

        


##################add Session#################    
    
@app.route('/addsession',methods=['GET','POST'])
def addsession():
    if request.method == 'POST':
        add_session=request.form['add_session']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO add_session (add_session) VALUES (%s)",[add_session])
        mysql.connection.commit()
        msg="successfully addsession"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM add_session")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("Add Session.html" ,add_session= data)
    
    
    
    
    
################add Section######################3   
    
    
@app.route('/addsection',methods=['GET','POST'])
def addsection():
    if request.method == 'POST':
        add_section=request.form['add_section']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO new_section (add_section) VALUES (%s)",[add_section])
        mysql.connection.commit()
        msg="successfully addsection"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM new_section")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("Add Section.html" ,new_section= data)
    
    
    
###################Update Nonfaculty#######################



@app.route('/updatenonfaculty',methods=['GET','POST'])
def updatenonfaculty():
    if request.method == 'POST':
        id_data = request.form['id']
        name=request.form['name']
        email=request.form['email']
        mobileno=request.form['mobileno']
        gender=request.form['gender']
        dateofbirth=request.form['dateofbirth']
        qualification=request.form['qualification']
        yearofexperience=request.form['yearofexperience']
        aadharno=request.form['aadharno']
        address=request.form['address']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE nonfaculty
               SET name=%s, email=%s, mobileno=%s,gender=%s,dateofbirth=%s,qualification=%s,yearofexperience=%s,aadharno=%s,address=%s
               WHERE id=%s
            """, ( name,email,mobileno,gender,dateofbirth,qualification,yearofexperience,aadharno,address, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
######################Delete Nonfaculty###############



@app.route('/deletenonfaculty/<string:id_data>', methods = ['GET'])
def deletenonfaculty(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM nonfaculty WHERE id=%s", (id_data,))
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("Dashboard.html" , msg=msg)

        
        
###################Add NonFaculty#################    
    
@app.route('/addnonfaculty',methods=['GET','POST'])
def addnonfaculty(): 
    if request.method=='POST':
        print("6")
        schoolname=request.form['schoolname']
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
        photo=request.form['photo']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO nonfaculty (schoolname,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[schoolname,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo])
        mysql.connection.commit()
        msg="successfully addnonfaculty"
        return render_template('Dashboard.html',msg=msg)
    else: 
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM nonfaculty")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("Add NonFaculty.html" ,nonfaculty= data)
    
#################Update Teacher##############




@app.route('/updateteacher',methods=['GET','POST'])
def updateteacher():
    if request.method == 'POST':
        id_data = request.form['id']
        schoolname=request.form['schoolname']
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
        photo=request.form['photo']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE addteacher
               SET schoolname=%s, name=%s, nationalid=%s,phone=%s,gender=%s,birthdate=%s,joiningdate=%s,fathername=%s,aadharno=%s,presentaddress=%s,permanentaddress=%s,qualification=%s,email=%s,username=%s,password=%s,designation=%s,photo=%s
               WHERE id=%s
            """, ( schoolname,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    
    
    
######################Delete Teacher###############



@app.route('/deleteteacher/<string:id_data>', methods = ['GET'])
def deleteteacher(id_data):
   
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM teacher WHERE id=%s", (id_data,))
    mysql.connection.commit()
    msg=("Record Has Been Deleted Successfully")
    return render_template("Dashboard.html" , msg=msg)


#########################Teacher Report################



@app.route('/teacherreport',methods=['GET','POST'])
def teacherreport ():
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM addteacher')
        data=cur.fetchall()
        return render_template('teacherReport.html',addteacher=data)
    



###################### Manage Section Report#################



@app.route('/managesectionreport',methods=['GET','POST'])
def managesectionreport ():
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM managesection')
        data=cur.fetchall()
        return render_template('manageSectionReport.html',managesection=data)
    
    
    
    
    
    
    
###################Manage Class Report###############



@app.route('/manageclassreport',methods=['GET','POST'])
def manageclassreport ():
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM manageclass')
        data=cur.fetchall()
        return render_template('manageclassreport.html',manageclass=data)
    
    
 ################Update Manage Class Report##########   
    
@app.route('/updatemanageclass',methods=['GET','POST'])
def updatemanageclass():
    if request.method == 'POST':
        id_data = request.form['id']
        numericname=request.form['numericname']
        
        note=request.form['note']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE manageclass
               SET numericname=%s, note=%s
               WHERE id=%s
            """, ( numericname,note, id_data))
        mysql.connection.commit()
        msg="successfully updated"
        return render_template("Dashboard.html" ,msg=msg)
    
    


       
    
#####################Add Teacher####################    
    
@app.route('/addteacher',methods=['GET','POST'])
def addteacher():
    if request.method == 'POST':
        print("6")
        schoolname=request.form['schoolname']
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
        photo=request.form['photo']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO addteacher (schoolname,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[schoolname,name,nationalid,phone,gender,birthdate,joiningdate,fathername,aadharno,presentaddress,permanentaddress,qualification,email,username,password,designation,photo])
        mysql.connection.commit()
        msg="successfully addteacher"
        return render_template('Dashboard.html',msg=msg)
    else: 
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM addteacher")
        
        data = cur.fetchall()
        print("demo")
        
        return render_template("Add Teacher.html" ,teacher= data)




##################feecategory#######################

@app.route('/feecategory',methods=['GET','POST'])
def feecategory():
    if request.method=="POST":
         
        feetitle=request.form['feetitle']
        category=request.form['category']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO category (feetitle,category)VALUES(%s,%s)" ,[feetitle,category])
        mysql.connection.commit()
        msg="Successfully addcategory"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM addfeetitle ORDER BY id")
        data=cur.fetchall()
        return render_template('feecategory.html',feetitle=data)
    
    
    
    
    
 ####################Manage Class###############   


@app.route('/manageclass',methods=['GET','POST'])
def manageclass():
    if request.method=="POST":
         
        schoolname=request.form['schoolname']
        add_class=request.form['class']
        numericname=request.form['numericname']
        classteacher=request.form['classteacher']
        note=request.form['note']
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO manageclass (schoolname,class,numericname,classteacher,note)VALUES(%s,%s,%s,%s,%s)" ,[schoolname,add_class,numericname,classteacher,note])
        mysql.connection.commit()
        msg="Successfully manageclass"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur=mysql.connection.cursor()
        cur.execute("SELECT name FROM addteacher ORDER BY id")
        f=cur.fetchall()
        cur.execute("SELECT class FROM add_class ORDER BY id")
        h=cur.fetchall()
        return render_template('manageClass.html',addteacher=f,add_class=h)
    
    
    
########################## Manage Section##################



@app.route('/managesection',methods=['GET','POST'])
def managesection():
    if request.method=="POST":
         
        schoolname=request.form['schoolname']
        name=request.form['name']
        add_class=request.form['class']
        
        classteacher=request.form['classteacher']
        note=request.form['note']
        
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO managesection (schoolname,name ,class,classteacher,note)VALUES(%s,%s,%s,%s,%s)" ,[schoolname,add_class,name,classteacher,note])
        mysql.connection.commit()
        msg="Successfully manageclass"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur=mysql.connection.cursor()
        cur.execute("SELECT name FROM addteacher ORDER BY id")
        j=cur.fetchall()
        cur.execute("SELECT class FROM add_class ORDER BY id")
        k=cur.fetchall()
        return render_template('manageSection.html',addteacher=j,add_class=k)
    
    
    
    
    
################addFeeClass##############
@app.route('/feeclass',methods=['GET','POST'])
def addfeeclass():
    if request.method=="GET":
        cur=mysql.connection.cursor()

        cur.execute("SELECT feetitle,category FROM category ")
        enroll = cur.fetchall()
        
        cur.execute("SELECT class FROM add_class ")
        abc = cur.fetchall()
        return render_template("addFeeClass.html",category=enroll,add_class=abc)
    else:
        feetitle=request.form['feetitle']
        category=request.form['category']
        add_class=request.form['class']
        feeamount=request.form['feeamount']
        cur=mysql.connection.cursor()
        
        cur.execute("INSERT INTO addfeeclass (feetitle,category,class,feeamount)VALUES(%s,%s,%s,%s)" ,[feetitle,category,add_class,feeamount])
        mysql.connection.commit()
        msg="Successfully "
        return render_template("Dashboard.html" ,msg=msg)
    
    
##################student report#####################


# @app.route('/studentreport',methods=['GET','POST'])
# def studentreport ():
#         cur=mysql.connection.cursor()
#         cur.execute('SELECT id,studentname,email,mobileno,gender,class,address FROM sregistration')
#         data=cur.fetchall()
#         return render_template('studentReport.html',sregistration=data)
    
    
    
    
##################Student Registration###############


@app.route('/registration',methods=['GET','POST'])
def studentregistration ():
    if request.method == 'POST':
        print("4")
        studentname=request.form['studentname']
        class1=request.form['class']
        email=request.form['email']
        mobileno=request.form['mobileno']
        gender=request.form['gender']
        dateofbirth=request.form['dateofbirth']
        fileinput=request.form['fileinput']
        fathername=request.form['fathername']
        fqualification=request.form['fqualification']
        fmobileno=request.form['fmobileno']
        mothername=request.form['mothername']
        mqualification=request.form['mqualification']
        mmobileno=request.form['mmobileno']
        address=request.form['address']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sregistration (studentname,class,email,mobileno,gender,dateofbirth,fileinput,fathername,fqualification,fmobileno,mothername,mqualification,mmobileno,address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[studentname,class1,email,mobileno,gender,dateofbirth,fileinput,fathername,fqualification,fmobileno,mothername,mqualification,mmobileno,address])
        mysql.connection.commit()
        msg="Successfully Registered"
        return render_template("Dashboard.html" ,msg=msg)
    else:
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM sregistration')
        data=cur.fetchall()
        return render_template('sregistration.html',sregistration=data)
    
    
    
###############Qualification###########################    


@app.route('/qualification',methods=['GET','POST'])
def stream():
    if request.method == 'POST':
        
        stream=request.form['stream']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO stream (stream) VALUES (%s)",[stream])
        mysql.connection.commit()
        print("test1")
        msg="successfully addstream"
        print("test")
        return render_template("Dashboard.html" ,msg=msg)
    else:
        return render_template("stream.html")
  
    
    

################Designation####################   



@app.route('/designation',methods=['GET','POST'])
def designation():
    if request.method == 'POST':
        
        designation=request.form['designation']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO designation (designation) VALUES (%s)",[designation])
        mysql.connection.commit()
        print("test1")
        msg="successfully adddesignation"
        print("test")
        return render_template("Dashboard.html" ,msg=msg)
    else:
        return render_template("designation.html")
    
    
    
    
################### add Student details####################


@app.route('/studentdetails',methods=['GET','POST'])
def studentdetail():
    if request.method == 'POST':
        
        schoolname=request.form['schoolname']
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
        presentaddress=request.form['presentaddress']
        permanentaddress=request.form['permanentaddress']
        username=request.form['username']
        password=request.form['password']
        file=request.form['file']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO addstudentdetail (schoolname,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[schoolname,name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,add_class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,file])
        mysql.connection.commit()
        print("test1")
        msg="successfully addstudentdetail"
        print("test")
        return render_template("Dashboard.html" ,msg=msg)
    
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT class FROM add_class")
        a=cur.fetchall()
        cur.execute("SELECT add_section FROM new_section")
        b=cur.fetchall()
        cur.execute("SELECT stream FROM stream")
        e=cur.fetchall()
        return render_template("addStudentDetail.html",add_class=a,new_section=b,stream=e)
    
    
    
    
    
##################AddStudentRegistrationReport#########################




@app.route('/studentregistrationreport',methods=['GET','POST'])
def studentregistrationreport ():
    
        cur=mysql.connection.cursor()
        cur.execute('SELECT  id,name,class,add_section,rollno FROM addstudentdetail')
        data=cur.fetchall()
        return render_template('studentRegistrationReport.html',addstudentdetail=data)
    
    
    
#########################fetching Report#################
    
@app.route('/studentdetails',methods=['GET','POST'])
def studentreport ():  
     
    if request.method=='POST':
        studentreport=request.form
        name=studentreport['name']
        cur=mysql.connection.cursor()
        cur.execute("SELECT  id,schoolname, name,fathername,mothername,addmission,admissiondate,birthdate,gender,aadharno,religion,caste,housename,phone,email,class,add_section,stream,rollno,feeexcused,presentaddress,permanentaddress,username,password,photo FROM addstudentdetail where name='"+name+"'")
        r=cur.fetchone()
        mysql.connction.commit()
        return render_template("addStudentDetail.html",r=r)
    
    
###########################addnonfacultyreport#############################


@app.route('/nonfacultyreport',methods=['GET','POST'])
def nonfacultyreport ():
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM nonfaculty')
        data=cur.fetchall()
        return render_template('nonFacultyReport.html',nonfaculty=data)
    
    
    
    
    

    
    
    
    
################### Admin login#########################

@app.route('/login',methods=['GET','GET'])
def adminlogin():
    
    msg = ''
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM loginmaster WHERE username = % s AND password = % s', (username, password, ))
        loginmaster = cur.fetchone()
        if loginmaster:
            session['loggedin'] = True
            session['id'] = loginmaster['id']
            session['username'] = loginmaster['username']
            msg = 'Logged in successfully !'
            return render_template('Dashboard.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)






    
    
    
    
    
######################Student Login#########################


@app.route('/studentlogin',methods=['GET','POST'])
def studentlogin():
    if request.method == 'GET':
        print("3")
        print("Its in get")
        return render_template("studentlogin.html")
    
        
    else:
        print("4")
        #studentDetails=request.form
        email=request.form['email']
        password=request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO studentlogin (email,password) VALUES (%s,%s)",(email,password))
        mysql.connection.commit()
        # msg="successfully student login"
        
        
        return render_template("addStudentDetail.html" )
    
    
    
    
########################Teacher Login#################



@app.route('/teacherlogin',methods=['GET','POST'])
def teacherlogin():
    if request.method == 'GET':
        print("3")
        print("Its in get")
        return render_template("teacherlogin.html")
    
        
    else:
        print("4")
        #studentDetails=request.form
        email=request.form['email']
        password=request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO teacherlogin (email,password) VALUES (%s,%s)",(email,password))
        mysql.connection.commit()
        # msg="successfully student login"
        
        
        return render_template("Add Teacher.html" )
    
    
    
    
    
    
#######################NonFaculty login############



@app.route('/nonfacultylogin' ,methods=['GET','POST'])
def nonfacultylogin ():
    if request.method == 'GET':
        print("3")
        print("Its in get")
        return render_template("nonFacultyLogin.html")
    
        
    else:
        print("4")
        #studentDetails=request.form
        email=request.form['email']
        password=request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO nonfacultylogin (email,password) VALUES (%s,%s)",(email,password))
        mysql.connection.commit()
        # msg="successfully nonfacultylogin"
        
        
        return render_template("Add NonFaculty.html" )
    
    
    
    



    
    
    
    
    
    
    


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
    
    




    

        

if __name__ == "__main__":


    app.run(debug=True)









