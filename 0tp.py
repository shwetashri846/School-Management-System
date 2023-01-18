from flask import *  
from flask_mail import Mail,Message
from flask import Flask

from random import *
  
app = Flask(__name__) 
mail = Mail(app)  
  
#Flask mail configuration  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'shweta.infoera@gmail.com'  
app.config['MAIL_PASSWORD'] = 'info2022'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
#instantiate the Mail class  
mail = Mail(app) 
otp = randint(000000,999999)   
  
#configure the Message class object and send the mail from a URL  
@app.route('/')  
def index():  
    msg = Message('subject', sender = 'shweta.infoera@gmail.com', recipients=['username@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    # return "Mail Sent, Please check the mail id"
    return render_template("index1.html") 


@app.route('/verify',methods = ["POST"])  
def verify():  
    email = request.form["email"]  
      
    msg = Message('OTP',sender = 'username@gmail.com', recipients = [email])  
    msg.body = str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  
 
@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3>Email verified successfully</h3>"  
    return "<h3>failure</h3>"     
  
if __name__ == '__main__':  
    app.run(debug = True)  