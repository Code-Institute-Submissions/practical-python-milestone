import os
from datetime import datetime
import json
from flask import Flask, redirect, render_template, request, flash

app = Flask(__name__)


counter = 0
user_answer=""
data= []
with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
        
def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)


@app.route('/', methods=["GET", "POST"])
def index():
    """Main page with instructions"""
    
    # Handle POST request
    if request.method == "POST":
        write_to_file("data/users.txt", request.form["username"] + "\n")
    return render_template("index.html")


@app.route('/riddles', methods=["GET", "POST"])
def riddles():
    global counter
    global data
    global user_answer
    """Page with riddles"""
    return render_template("riddles.html", data=data, i=counter, user_answer=user_answer)
    
@app.route('/next-riddle/', methods=["GET", "POST"])
def next_riddle():
    global counter
    global data
    global user_answer
    
    if request.method == "POST":
        if data[counter]["answer"] == request.form["answer"]:
            counter += 1
            user_answer = ""
        else:
            user_answer = request.form["answer"] + " is incorrect!"
            
    return render_template("riddles.html", data=data, i=counter, user_answer=user_answer)  


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)