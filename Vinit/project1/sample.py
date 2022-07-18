from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/vinit' #PLEASE CHANGE PASSWORD TO YOURS
db=SQLAlchemy(app)

class ab (db.Model):
    __tablename__ = 'CD_table'
    phone= db.Column('phone', db.String(12), primary_key=True) 
    name = db.Column('name',db.String(30))
    about = db.Column('about',db.String(30))

class ab2 (db.Model):
    __tablename__ = 'CD_table2'
    phone= db.Column('phone', db.String(12), primary_key=True) 
    name = db.Column('name',db.String(30))
    about = db.Column('about',db.String(30))

class ab3 (db.Model):
    __tablename__ = 'CD_table3'
    phone= db.Column('phone', db.String(12), primary_key=True) 
    name = db.Column('name',db.String(30))
    about = db.Column('about',db.String(30))
    
    print("Table created....")


db.create_all() #Hey Vinit YOU MISSED THIS 😉



    #def __repr__(self) -> str:
        #return f"{self.name} - {self.phone}"

    



@app.route("/", methods=['GET','POST'])
def ef():
    if (request.method =='POST'):
        entry= ab(name = request.form.get('name'),
                about = request.form.get('about'),
                phone=request.form.get('phone'))
        #entry =ab (name=name, about=about, phone=phone )
        entry2= ab2(name = request.form.get('name'),
                about = request.form.get('about'),
                phone=request.form.get('phone'))
            
        entry3= ab3(name = request.form.get('name'),
                about = request.form.get('about'),
                phone=request.form.get('phone'))

        db.session.add(entry)
        db.session.add(entry2)
        db.session.add(entry3)
        db.session.commit()



    return render_template('sample1.html')

if __name__ == "__main__":
    app.run (debug=True)
