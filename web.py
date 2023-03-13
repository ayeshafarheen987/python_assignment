# step 1
from flask import Flask,request
# step 2
app = Flask(__name__)

#step 3
@app.route('/')
def home():
    return "<h1 style='background-color:pink;'>Hello Fellow Innomatics Interns</h1><br></br><h1 style='color:green;'>My self Ayesha Farheen.</h1>"

@app.route('/search')
def search_page():
    return 'Hii ayesha'

@app.route('/add')
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    
    return str(int(a)+int(b))

@app.route('/to_upper')
def upperCase():
    name = request.args.get('name')
    if name:
        name = name.upper()

        return f'<div><h1>Flask Backend Assignment</h1></br><h3>Your Username in uppercase is {name}</h3>'
    else:
        return '<div><h1>Flask Backend Assignment</h1></br><h3>Kindly input your username </h3></div>'
        


@app.route('/innomatics')
def quiz():
    if 3*0.1 == 0.3 and 4*0.1 == 0.4:
        return "INNOMATICS"
    elif 3*0.1 == 0.3 and 4*0.1 != 0.4:
        return "INNOMATICS RESEARCH"

    elif 3*0.1 != 0.3 and 4*0.1 == 0.4:
        return "INNOMATICS RESEARCH LAB"




# step 4
if __name__ == "__main__":
    app.run(debug=True)

