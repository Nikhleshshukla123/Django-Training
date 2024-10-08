from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def testpaper(request):
    t = '''
<style>
body {
font-family: Arial, sans-serif;
background-color: #da8b15;
margin: 0;
padding: 0;
text-align: center;
}
section {
margin: 20px;
padding: 20px;
background-color: rgb(191, 240, 196);
border-radius: 10px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
header {
background-color: #333;
color: white;
padding: 1em;
}
button {
padding: 10px 20px;
font-size: 16px;
background-color: #333;
color: white;
border: none;
border-radius: 5px;
cursor: pointer;
}
</style>
</head>
<body>
<header>
<h1>Personality Quiz 1</h1>
</header>
<section>
<h2>Question 1</h2>
<p>What is your favorite color?</p>
<input type="radio" name="q1" value="red"> Red
<input type="radio" name="q1" value="blue"> Blue
<input type="radio" name="q1" value="green"> Green
</section>
<section>
<h2>Question 2</h2>
<p>What is your favorite animal?</p>
<input type="radio" name="q2" value="dog"> Dog
<input type="radio" name="q2" value="cat"> Cat
<input type="radio" name="q2" value="bird"> Bird
</section>
<section>
<h2>Question 3</h2>
<p>What is your preferred season?</p>
<input type="radio" name="q3" value="summer"> Summer
<input type="radio" name="q3" value="winter"> Winter
<input type="radio" name="q3" value="fall"> Fall
</section>
<section>
<h2>Question 4</h2>
<p>Do you prefer indoor or outdoor activities?</p>
<input type="radio" name="q4" value="indoor"> Indoor
<input type="radio" name="q4" value="outdoor"> Outdoor
<input type="radio" name="q4" value="both"> Both
</section>
<section>
<h2>Question 5</h2>
<p>What is your favorite type of music?</p>
<input type="radio" name="q5" value="rock"> Rock
<input type="radio" name="q5" value="pop"> Pop
<input type="radio" name="q5" value="hip-hop"> Hip-hop
</section>
<section>
<h2>Question 6</h2>
<p>You regularly make new friend</p>
<input type="radio" name="q6" value="Yes"> Yes
<input type="radio" name="q6" value="Sometimes"> Sometimes
<input type="radio" name="q6" value="No"> No
</section>
<section>
<h2>Question 7</h2>
<p>You usually stay claim even under a lot of pressure</p>
<input type="radio" name="q7" value="Yes"> Yes
<input type="radio" name="q7" value="Sometimes"> Sometimes
<input type="radio" name="q7" value="No"> No
</section>
<section>
<h2>Question 8</h2>
<p>You enjoy participating in group activities</p>
<input type="radio" name="q8" value="Yes"> Yes
<input type="radio" name="q8" value="Sometimes"> Sometimes
<input type="radio" name="q8" value="No"> No
</section>
<section>
<h2>Question 9</h2>
<p>How would you describe your personality</p>
<input type="radio" name="q9" value="Yes"> Yes
<input type="radio" name="q9" value="Sometimes"> Sometimes
<input type="radio" name="q9" value="No"> No
</section>
<section>
<h2>Question 10</h2>
<p>What are your parents like</p>
<input type="radio" name="q10" value="Honest"> Honest
<input type="radio" name="q10" value="always happy"> always happy
<input type="radio" name="q10" value="Study">Study
</section>
<section>
<h2>
<a href="personality4.html" target="_blank">Next </a>
</h2>
</section>
'''
    return HttpResponse(t)

def result(request):
    r = '<h1>This is a result page</h1>'
    return HttpResponse(r)