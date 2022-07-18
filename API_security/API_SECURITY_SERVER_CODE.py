import json
import time

from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/novdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#security related
from datetime import timedelta

from flask_jwt_extended import get_jwt_identity,JWTManager,create_access_token,create_refresh_token,jwt_required
                                #server side la
app.config["JWT_SECRET_KEY"] = "!I&#*JKHSDYUI#YRUIKJSF$&^$&DH"      #token generate kar hoto
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=5)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=8)
jwt = JWTManager(app)

db = SQLAlchemy(app)


class Account(db.Model):
    id = db.Column('id',db.Integer, primary_key=True)
    balance = db.Column('acc_balace',db.Float)
    type = db.Column('acc_type',db.String(30))
    cust_id = db.Column('cust_id',db.ForeignKey('customer.id'),unique=False)
    #customer


class Customer(db.Model):   #customer.query.filter_by(id=101).first()  customer.accounts
    id = db.Column('id',db.Integer, primary_key=True)
    name = db.Column('name',db.String(30))
    username = db.Column('username',db.String(80), unique=True)
    password = db.Column('password',db.String(120))
    email = db.Column('email',db.String(80), unique=True)
    accounts = db.relationship(Account,lazy=False,backref='customer')
    #accounts = db.relationship(Account, lazy=False, backref='customer')

#whitebox testing --> unit/module --< khud --test --< collection handover --

@app.route("/customer/save",methods=['POST'])
@jwt_required()
def add_customer():
    reqData = request.get_json()
    print(reqData)
    if not reqData:
        return json.dumps({"ERROR" : "Customer Fields Cannot blank"})

    try:
        cust = Customer.query.filter_by(id=reqData.get('Id')).first()
        if cust:
            return json.dumps({"ERROR" : "Customer Id already Present "})

        cust = Customer.query.filter(Customer.email==reqData.get('Email')).first()
        if cust:
            return json.dumps({"ERROR": "Customer Email already Present "})

        cust = Customer(id=reqData.get('Id'),
                        name=reqData.get('Name'),
                        username=reqData.get('Username'),
                        password=reqData.get('Password'),
                        email=reqData.get('Email'))
        print('Customer Record',cust)
        db.session.add(cust)
        db.session.commit()
        return json.dumps({"SUCCESS" : "Customer Record added into databases "})
    except BaseException as e:
        print(e.args)
        return json.dumps({"ERROR": "Problem in customer Add"})


def application_req():
    print('initializing the system....')
    db.drop_all()
    time.sleep(3)
    db.create_all()

    cust1 = Customer(id=101,name='Yogesh1',username='yogymax1',password='yogy@123',email='yogesh1@gmail.com')
    cust2 = Customer(id=102,name='Yogesh2',username='yogymax2',password='yogy@123',email='yogesh2@gmail.com')
    cust3 = Customer(id=103,name='Yogesh3',username='yogymax3',password='yogy@123',email='yogesh3@gmail.com')
    db.session.add_all([cust1,cust2,cust3])
    db.session.commit()
    ac1 = Account(id=111111,balance=28693.34,type='saving',cust_id=cust1.id)
    ac2 = Account(id=111112,balance=25893.34,type='saving',cust_id=cust1.id)
    ac3 = Account(id=111113,balance=28933.34,type='saving',cust_id=cust2.id)
    ac4 = Account(id=111114,balance=28893.34,type='Current',cust_id=cust2.id)
    ac5 = Account(id=111115,balance=92893.34,type='saving',cust_id=cust3.id)
    db.session.add_all([ac1,ac2,ac3,ac4,ac5])
    db.session.commit()
    print('Objects created...')

#http://localhost:5000/api/customer/1212
@app.route('/api/customer/<int:cust_id>')
@jwt_required()
def get_customer_account_balance(cust_id):
    customer = Customer.query.filter_by(id=cust_id).first() #.all()
    if customer:
        customer_accounts = customer.accounts  #list -
        customer_account_serializer = [{'customer_id':customer.id,'customer_name':customer.name}]        #json format madhe
        for account in customer_accounts:
            account = {"ACCOUNT_NUMBER " : account.id,"ACCOUNT_TYPE":account.type,"ACCOUNT_BALANCE":account.balance}
                       #"CUSTOMER_NAME":account.customer.name}
            customer_account_serializer.append(account)
        return json.dumps(customer_account_serializer)
    return json.dumps({"ERROR" : "No Details found for given customer id {}".format(cust_id)})

#http://localhost:5000/api/token  {"username":"piyush","password":"piyush123"}
@app.route("/api/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    #record = Customer.query.filter(Customer.username==username,Customer.password==password).first()
    #if record:
    if username=='piyush' and password == 'piyush123':
        #identity = (record.username,record.password)
        identity = (username,password)
        accessToken = create_access_token(identity=identity)
        refreshToken = create_refresh_token(identity=identity)
        return jsonify({"ACCESS_TOKEN": accessToken, "REFRESH_TOKEN": refreshToken,
                        "USERNAME": username})
    else:
        return jsonify({"msg": "Bad username or password"}), 401

@app.route("/api/token/refresh", methods=["GET"])
@jwt_required(refresh=True)  # token --> refresh True -- refresh token
def get_refresh_token():
    current_user_id = get_jwt_identity()  #username,password
    accesstoken = create_access_token(identity=current_user_id) #
    return jsonify({"accesstoken": accesstoken})


@app.route('/api/customer/')
def get_customer_details():
    pass


@app.route('/api/customer/')
def get_customer_account_details():
    pass


@app.route('/api/customer/')
def search_customer_by_account():
    pass


@app.route('/api/customer/')
def search_customer_by_email():
    pass



if __name__ == '__main__':
    #application_req()
    app.run(debug=True)
