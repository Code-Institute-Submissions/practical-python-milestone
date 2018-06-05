<h6>Ben Hasselgren</h6>
<h1> User Centric Frontend Development Milestone Project  </h1>

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
    
    One thing I struggled to make my mind up on was the score. I wasn't too sure how to score the users as if they passed all the questions the score would always
    be equal to the number of riddles in the game meaning anyone the completed the game would have the same score. To try and fix this I made it that if the user
    guessed incorrcetly, this would decrease their score by 1 point. This helped add variation to the scores.
</p>

<p>   
    This website used the Flask Framework. This technology allowed lots of functionality. Mainly to create url routes to guide users around the website 
    with their own unique username and allow them to navigate uniquely through the riddles. Another technology used was bootsrap. It was referenced in my head
    section and made it easy to make my website responsive and look pretty using bootraps vast css library. PyMongo was alsed used alongside a mongodb server. This was
    used to save the scores of users. I originally had a csv file but after deploying it to heroku I discovered that you can't write to csv files. To fix this I decided to use
    an external storage facility. This allowed my to save my winners in a collection and access them to display them in the leaderboard.
</p>

<h3>Testing/Deployment</h3>
<p>
    This website was tested using Chrome development tools. The website was created on a design made
    by wireframe diagrams using Balsamiq. It was important to make sure the final version looked like the designs so
    Chrome development tools were used to test out all the features and see if they responded correctly and looked 
    right. Once mistakes/changes were made with Chrome, the code was copied to the actual code to fix the issue permanently.
</p>
<p>
    This website was deployed to heroku. I created a heroku app and then pushed my code to it. To ensure it worked I had to add some config variables
    on the heroku dashboard. I then had to add a procfile and a reuiqrments.txt file so heroku would know how to set up my app. As my winners where stored extrenally
    and I didn't rely on heroku's local postgres database, I didn't have to worry about migrating my database over.
</p>

<h1>ANSWERS</h1>
<ul>
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