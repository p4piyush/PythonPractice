from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345@localhost/BC_DB'
db=SQLAlchemy(app)

class client_det(db.Model):
    __tablename__ = 'CLIENT_DETAILS'
    ID = db.Column('id',db.Integer, primary_key=True)
    f_name = db.Column('firstname', db.String(30))
    l_name = db.Column('lastname', db.String(30))
    mob_no = db.Column("mobile no", db.String(12))
    addr = db.Column('address', db.String(60))
    acc = db.Column('account', db.String(30))

    def __repr__(self) -> str:
        return f"{self.ID} - {self.acc}"


print('Tables are created..')
db.create_all()



@app.route('/')
@app.route('/client')
@app.route('/client/')
def client():
    return render_template('index.html')



@app.route("/client/add client",methods = ['GET','POST'])
def add_client():
    message =""
    if (request.method == 'POST'):
        f_name=request.form.get('cltfnm'),
        l_name=request.form.get('cltlnm'),
        mob_no=request.form.get('cltmob'),
        addr=request.form.get("cltaddr"),
        acc=request.form.get("cltacc")
        entry=client_det(f_name=f_name,l_name=l_name,mob_no=mob_no,addr=addr,acc=acc)
        db.session.add(entry)
        db.session.commit()
        message = "Employee Saved Successfully...!"
    #allClient = client.query.all()
    return render_template('add_client.html', result=message)





if__name__ = "__main__"
app.run(debug=True)

