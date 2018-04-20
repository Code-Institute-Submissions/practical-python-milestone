import os
from datetime import datetime
import json
import csv
from flask import Flask, redirect, render_template, request, flash

app = Flask(__name__)
user_answer=""
data= []
score_dictinary = {}
counter_dictinary = {}

with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)
        
def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)
        
    


@app.route('/', methods=["GET", "POST"])
def index():
    global data
    global score_dictinary
    global counter_dictinary
    """Main page with instructions"""
    # Handle POST request
    if request.method == "POST":
        username = request.form["username"]
        score_dictinary[username] = 0
        counter_dictinary[username] = 0
        return redirect("/riddles/" + username)
    return render_template("index.html")
    
@app.route('/riddles/<username>', methods=["GET", "POST"])
def next_riddle(username):
    global data
    global user_answer
    global score_dictinary
    global counter_dictinary
    
    if len(data) == counter_dictinary[username] + 1:
        return redirect("/congratulations/" + username)
    else:
        if request.method == "POST":
            if data[counter_dictinary[username]]["answer"] == request.form["answer"]:
                score_dictinary[username] += 1
                counter_dictinary[username] += 1
                user_answer = ""
                
            else:
                user_answer = request.form["answer"] + " is incorrect!"
                if score_dictinary[username] > 0:
                    score_dictinary[username] -= 1
                    
            
    return render_template("riddles.html", data=data, i=counter_dictinary[username], user_answer=user_answer, score = score_dictinary[username])  
    
@app.route('/congratulations/<username>', methods=["GET", "POST"])
def congratulations(username):
    """Main page with instructions"""
    global score_dictinary
    global counter_dictinary
    # Handle POST request
    if request.method == "POST":
        write_to_file("data/winners.csv", username + "," + str(score_dictinary[username]) + "\n")
        counter_dictinary[username] = 0
        score_dictinary[username] = 0
        return redirect("/")
    return render_template("win.html", username=username)
    
@app.route('/leaderboard')
def leaderboard():
    global score_dictinary
    data = []
    fields = []
    scores = []
    names = []
    users = []
    
    ifile = open("data/winners.csv", "rU")
    reader = csv.reader(ifile, delimiter=",")
    
    for row in reader:
        names.append(row[0])
        scores.append(row[1])
    
    ifile.close()
    quicksort(scores, names, 0, len(scores) - 1)
    
    i=0
    while i < len(scores):
        users.append(names[i] + " " + scores[i])
        i += 1
    
    return render_template("leaderboard.html", users=users)



    
    

    
def swap_values(lst, val1, val2):
    lst[val1], lst[val2] = lst[val2], lst[val1]

def quicksort(array, array2, start, end):

    if start < end:

        partition_index = partition(array, array2, start, end) #
        quicksort(array, array2, start, partition_index - 1)
        quicksort(array, array2, partition_index + 1, end)

def partition(array, array2, start, end):

    pivot = end
    partition_index = start

    for i in range(start, end):

        if array[i] < array[pivot]:
            swap_values(array, partition_index, i)
            swap_values(array2, partition_index, i)
            partition_index += 1

    array[pivot], array[partition_index] = array[partition_index], array[pivot]
    array2[pivot], array2[partition_index] = array2[partition_index], array2[pivot]
    return partition_index

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)