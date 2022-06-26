import email
from flask import Flask, render_template, request

app = Flask(__name__)
app.template_folder = "html_pages/"

def create_acc():
    msg=''
    if request.method=="POST":
        formdata=request.form
        eml=formdata.get("email")
        usrnm=formdata.get("username")
        pswd=formdata.get("password")
        msg=eml
        
    

        #THIS IS FOR EMAIL ADDRESS VALIDATION
        if eml.count('@')==0:   #This will check for absense of  @ symbol
                msg="Enter valid email ID '@' symbol missing"

        elif eml.count('@')>=2: #This will check for multiple occurances of @ symbol
                msg="Enter valid email ID \nMultiple '@' symbol used in email ID"

        elif eml.index('@')==0: #This will check for @ syambol at the begining of the ID
                msg="Invalid Email ID plese enter valid ID..."
        
        elif eml.index('@')>eml.rindex('.'): #This will compare occurance of @ and . 
                msg="Invalid Email ID plese enter valid ID..."

        elif (eml.__len__())<eml.rindex('.'):   #This will compare email length with last index of . (dot)
                msg="Invalid Email ID plese enter valid ID..."

        elif (eml.__len__()-1)==eml.rindex('.'):  #This will nake shure email id not ending with . (dot)  
                msg="Invalid Email ID plese enter valid ID..."

        

        msg=msg+" "+str(usrnm)+" "+str(pswd)


    return render_template("/create_account.html",result=msg)
