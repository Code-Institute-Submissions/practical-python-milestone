import os
from datetime import datetime
import json
from flask import Flask, redirect, render_template, request, flash

app = Flask(__name__)
counter = 0
username = ""
user_answer=""
score=0
data= []
with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
        
def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)


@app.route('/', methods=["GET", "POST"])
def index():
    global counter
    global data
    global username
    """Main page with instructions"""
    # Handle POST request
    if request.method == "POST":
        username = request.form["username"]
        write_to_file("data/users.txt", username + "\n")
        return redirect("/riddles")
    return render_template("index.html")
    
@app.route('/riddles', methods=["GET", "POST"])
def next_riddle():
    global counter
    global data
    global user_answer
    global score
    
    if len(data) == counter + 1:
        return redirect("/congratulations")
    else:
        if request.method == "POST":
            if data[counter]["answer"] == request.form["answer"]:
                counter += 1
                score += 1
                user_answer = ""
                
            else:
                user_answer = request.form["answer"] + " is incorrect!"
                if score > 0:
                    score -= 1
                    
            
    return render_template("riddles.html", data=data, i=counter, user_answer=user_answer)  
    
@app.route('/congratulations', methods=["GET", "POST"])
def congratulations():
    global username
    global counter
    global score
    """Main page with instructions"""
    write_to_file("data/winners.txt", username + "," + str(score) + "\n")
    # Handle POST request
    if request.method == "POST":
        counter = 0
        score=0
        return redirect("/")
    return render_template("win.html", username=username)
    
@app.route('/leaderboard')
def leaderboard():
    global username
    global score
    data = []
   
    with open("data/winners.txt", "r") as file:
        for line in file:
            data = line
    return render_template("leaderboard.html", data=data)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)