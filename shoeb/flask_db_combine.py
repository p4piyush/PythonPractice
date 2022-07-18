from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
#######################################################################################
app = Flask(__name__) #THIS IS FOR CONFIGURATION LIKE DB CONNECTION AND HTML PAGES
app.template_folder = "templates/"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/pydbshoeb'
db = SQLAlchemy(app)

#######################################################################################
class ShoebTable(db.Model):#THIS IS FOR DATABASE CONNECTION WE WIRTE THIS CODE IN MODELS.PY
    __tablename__ = 'shoebdb'   #student record
    id = db.Column('id',db.Integer,primary_key=True)
    name = db.Column('name', db.String(20))
    mobileno= db.Column('mobileno', db.String(13))
db.create_all()


#######################################################################################

@app.route('/')
def welcome_page():
    return render_template('home.html')


@app.route('/register/', methods=['GET','POST']) 
def register_user():
    #THIS METHOD IS USED TO VALIDATE AND INSERT DATA INTO DATABSE
    msg=''
    try:
        if request.method == 'POST':
            #if len(formdata.get('fname'))==0 or len(formdata.get('mobileno'))>10 or len(formdata.get('mobileno'))==0:
              #  msg='Please enter valid details..'
           # else:
                formdata=request.form
                data=ShoebTable(name=formdata.get('fname'), mobileno=formdata.get('mobileno'))
                db.session.add(data)
                db.session.commit()
                msg='Record added to db'
    except:
        msg='Something is wrong....'
        
    return render_template("/register.html",result=msg)






if __name__ == '__main__':
    app.run(debug=True)