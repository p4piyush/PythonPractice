from config import db as ORM


class Create_my_table(ORM.Model):
    __tablename__ = 'user_data'   #EMPLOYEE_MASTER
    id = ORM.Column('id',ORM.Integer,primary_key=True)
    name= ORM.Column('Name', ORM.String(30))
    emailid= ORM.Column('myemail', ORM.String(30))
    address= ORM.Column('address', ORM.String(30))








print('Tables are created..')
ORM.create_all()

