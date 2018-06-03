import os
import json
import csv
from flask import Flask, redirect, render_template, request, flash

app = Flask(__name__)
user_answer=""
data= []
score_dictinary = {}
counter_dictinary = {}

#Opens the riddles file 
with open("data/riddles.json", "r") as json_data:
        data = json.load(json_data)

"""--------------------Routes--------------------"""  

@app.route('/', methods=["GET", "POST"])
def index():
    
    """Main page with instructions"""
    global data
    global score_dictinary
    global counter_dictinary
    
    # Handle POST request
    if request.method == "POST":
        username = request.form["username"]
        score_dictinary[username] = 0
        counter_dictinary[username] = 0
        return redirect("/riddles/" + username)
    return render_template("index.html")
    
@app.route('/riddles/<username>', methods=["GET", "POST"])
def next_riddle(username):
    
    """ This page shows each riddle at a time """
    global data
    global counter_dictinary
    global user_answer
    
    if len(data) == counter_dictinary[username] + 1:
        # Redirects to winning page is user completes all riddles
        return redirect("/congratulations/" + username)
    else:
        if request.method == "POST":
                # Updates score and counter dictionaries if the user guesses correctly
            if data[counter_dictinary[username]]["answer"] == (request.form["answer"]).upper():
                correct(request, username)
                
            else:
                user_answer = request.form["answer"] + " is incorrect!"
                incorrect(request, username)
    
    
    return render_template("riddles.html", data=data, i=counter_dictinary[username], user_answer=user_answer)  
    
@app.route('/congratulations/<username>', methods=["GET", "POST"])
def congratulations(username):
    
    """ This page will appear once the user has completd all riddles"""
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
    """ Displays all the winners of the riddle game in a leaderboard """
    
    global score_dictinary
    data = []
    fields = []
    scores = []
    names = []
    users = []
    i=0
    
    #Reads the winners.csv file using import csv
    write_to_csv_file("data/winners.csv", scores, names)
    
    #Sorts the list in descending order
    quicksort(scores, names, 0, len(scores) - 1)
    
    #Joins the names and scores arrays together
    while i < len(scores):
        users.append(names[i] + " " + scores[i])
        i += 1
    
    users = (reversed(users))
    
    return render_template("leaderboard.html", users=users)
    
    
"""--------------------Methods for quicksort--------------------"""
def swap_values(lst, val1, val2):
    lst[val1], lst[val2] = lst[val2], lst[val1]

def quicksort(array, array2, start, end):

    if start < end:

        partition_index = partition(array, array2, start, end) #
        quicksort(array, array2, start, partition_index - 1)
        quicksort(array, array2, partition_index + 1, end)
    return array

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
    
"""--------------------Functions for routes--------------------"""
    
"""Riddles Route"""

def correct(request, username):
    global user_answer
    global score_dictinary
    global counter_dictinary
    
    score_dictinary[username] += 1
    counter_dictinary[username] += 1
    user_answer = ""
    
def incorrect(request, username):
    global user_answer
    global score_dictinary
    global counter_dictinary
    
    # Updates score and counter dictionaries if the user guesses incorrectly
    if score_dictinary[username] > 0:
        score_dictinary[username] -= 1
        
"""--------------------Functions for file handling--------------------"""
#Function used to write data to files       
def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)

#Function used to write data to csv files  
def write_to_csv_file(filename, scores, names):
    
    ifile = open(filename, "a")
    reader = csv.reader(ifile, delimiter=",")
        
    for row in reader:
        names.append(row[0])
        scores.append(row[1])
        
    ifile.close()
    return True

    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)