import imp
from urllib import request
from flask import Flask, render_template, request
import create_account

app = Flask(__name__)
app.template_folder = "html_pages/"

@app.route("/") # Main or Home page
def home():
    return render_template("home.html") # Home page file name
    
@app.route("/about/") # URL for about page
def about():
    return render_template("about.html") #About page file name

app.add_url_rule('/create_account/', view_func=create_account.create_acc, methods=['GET', 'POST']) #This method is used to access another python modeule 


@app.route("/login/",methods=['GET','POST'])
def login():
    msg=""
    if request.method=="POST":
        formdata=request.form
        usernm=formdata.get("email")
        passwrd=formdata.get("userpassword")
        if len(usernm)>=1 and passwrd=="admin123":
            msg="Successful login.."
        else:
            msg="Please enter correct credantials.."
        

    return render_template("/login.html",result=msg)




    
if __name__ == "__main__":
    app.run(debug=True)