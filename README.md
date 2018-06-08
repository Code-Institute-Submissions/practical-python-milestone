<h6>Ben Hasselgren</h6>
<h1> User Practical Python Milestone Project  </h1>

<a href="https://practical-python-milestone.herokuapp.com/" target="_blank"> Click here to view website</a>
<h3>Quick Tutorial</h3>
<ol>
    <li>Enter your username and press start</li>
    <li>You will be redirected to the riddles. <strong>Let the games begin!</strong></li>
    <li>The game is simple. You only get to the next question by guessing right</li>
    <ul>
        <h5>Answers (Here are the answers to the game)</h5>
        <li>envelope</li>
        <li>bed</li>
        <li>stamp</li>
        <li>candle</li>
        <li>clock</li>
        <li>teapot</li>
        <li>towel</li>
        <li>sponge</li>
        <li>seven</li>
        <li>envelope</li>
    </ul>
    <li>Play as much as you want and try guessing wrongly to see what happens</li>
    <li>Now click on the leaderboard</li>
    <ul>
        <h5>Leaderboard</h5>
        <li>This leaderbaord shows all users with the highest score at the top</li>
        <li>Did you manage to make it to the top? The highest score you can achieve is ten in this game.</li>
    </ul>
</ol>
<h3>Purpose</h3>
<p>
    The purpose of this project is to create a riddle me game on a website. The user can enter their username and then go through
    every riddle and answer it correctly in order to get their name on the leaderboard. Multiple users can play an instance of the same game
    and all users who have passed all questions will be added to the leaderboard.
</p>

<h3>Functionality/Technologies</h3>
<p>
    This website has lots of functionality. One functioniality is that it's resposnive. It has responsive elements
    that adapt to the screen size. The user can enter in their username and then this username is used in the routes to allow that user to have
    thir own unique instance of a game. This functionality allows multiple people to play a game. Each riddle has functionality to tell the user
    if their guess is wrong. It won't move to the next riddle until they guess correctly and it tells the user is they have guessed wrongly also.
</p>
    One thing I struggled to make my mind up on was the score. I wasn't too sure how to score the users as if they passed all the questions the score would always
    be equal to the number of riddles in the game meaning anyone who completed the game would have the same score. To try and fix this I made it that if the user
    guessed incorrcetly, the score would decrease by 1 point. This helped add variation to the scores.
</p>

<p>   
    This website used the Flask Framework. This technology allowed lots of functionality. Mainly to create url routes to guide users around the website 
    with their own unique username and allow them to navigate uniquely through the riddles. 
<p>
<p>
    Another technology used was bootsrap. It was referenced in my head section and made it easy to make my website responsive and look pretty using bootrap's vast css library. 
</p>
<p>
    PyMongo was alsed used alongside a mongodb server. This was used to save the scores of users. I originally had a csv file but after deploying it to heroku I discovered that you can't write to csv files. To fix this I decided to use
    an external storage facility. This allowed my to save my winners in a collection and access them to display them in the leaderboard.
</p>

<h3>Testing</h3>
<p>
    This website was tested using Chrome development tools. The website was created on a design made
    by wireframe diagrams using Balsamiq. It was important to make sure the final version looked like the designs so
    Chrome development tools were used to test out all the features and see if they responded correctly and looked 
    right. Once mistakes/changes were made with Chrome, the code was copied to the actual code to fix the issue permanently.
</p>
<p>
    I also had some automatic tests by using the testcase package. I didn't have many part to test as it was a very simple game but the automatic
    tests made it easy to see if my quicksort worked.
</p>
<p>
    I also did some manual tests. Here are a couple examples
</p>
<table>
    <tr>
        <th>Test</th>
        <th>Input</th>
        <th>Expected output</th>
        <th>Output</th>
        <th>Pass?</th>
    </tr>
    <tr>
        <td>Testing to see if the first riddle was working</td>
        <td>envelope</td>
        <td>correct</td>
        <td>correct</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Testing to see if the second riddle was correct</td>
        <td>wronganswer</td>
        <td>incorrect</td>
        <td>incorrect</td>
        <td>Yes</td>
    </tr>
</table>
<h3>Deployment</h3>
<p>
    This website was deployed to heroku. I created a heroku app and then pushed my code to it. To ensure it worked I had to add some config variables
    on the heroku dashboard. I then had to add a procfile and a reuiqrments.txt file so heroku would know how to set up my app. As my winners where stored extrenally
    and I didn't rely on heroku's local postgres database, I didn't have to worry about migrating my database over. I also had to add my local mondobb config variables to heroku configs variables.
</p>
