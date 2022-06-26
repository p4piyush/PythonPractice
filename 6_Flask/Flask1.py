from flask import Flask, render_template

app = Flask(__name__)
app.template_folder = "html_pages/"

@app.route("/") # Main or Home page
def home():
    return render_template("home.html") # Home page file name
    
@app.route("/about/") # URL for about page
def about():
    return render_template("about.html") #About page file name
 










    
if __name__ == "__main__":
    app.run(debug=True)