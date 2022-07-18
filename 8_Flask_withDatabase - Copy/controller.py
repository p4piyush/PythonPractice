from xml.etree.ElementTree import tostring
from config import app, db
from flask import request,render_template
from models import Create_my_table

@app.route('/')
def welcome_page():
    return render_template('home.html')

@app.route('/register/', methods=['GET','POST'])
def register_user():
    msg=''
    if request.method == 'POST':
        formdata=request.form
        data=Create_my_table(name=formdata.get("username"), emailid=formdata.get("useremail"), address=formdata.get("useraddress"))
        db.session.add(data)
        db.session.commit()
        msg="User Added:"
    return render_template("/register_user.html",result=msg)




@app.route('/listusers/')
def list_of_users():
    user_list = Create_my_table.query.all()

    return render_template('userlist.html',result_list = user_list)    

if __name__ == '__main__':
    app.run(debug=True)