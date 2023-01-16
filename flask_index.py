#Importing flask module in the project
from flask import Flask,render_template


#Create an object of the Flask class
app1 = Flask(__name__)

#The route() function of the Flask class 
#‘/’ URL is bound with first_flask function.
@app1.route("/index")
def first_webpage():
    name = 'flask'
    return render_template('index.html',index_variable = name)

#run the application on local server
app1.run(debug = True)
